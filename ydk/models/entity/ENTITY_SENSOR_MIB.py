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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EntitySensorDataScale_Enum(Enum):
    """
    EntitySensorDataScale_Enum

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
        from ydk.models.entity._meta import _ENTITY_SENSOR_MIB as meta
        return meta._meta_table['EntitySensorDataScale_Enum']


class EntitySensorDataType_Enum(Enum):
    """
    EntitySensorDataType_Enum

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


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _ENTITY_SENSOR_MIB as meta
        return meta._meta_table['EntitySensorDataType_Enum']


class EntitySensorStatus_Enum(Enum):
    """
    EntitySensorStatus_Enum

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

    """

    OK = 1

    UNAVAILABLE = 2

    NONOPERATIONAL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _ENTITY_SENSOR_MIB as meta
        return meta._meta_table['EntitySensorStatus_Enum']



class ENTITYSENSORMIB(object):
    """
    
    
    .. attribute:: entphysensortable
    
    	This table contains one row per physical sensor represented by an associated row in the entPhysicalTable
    	**type**\: :py:class:`EntPhySensorTable <ydk.models.entity.ENTITY_SENSOR_MIB.ENTITYSENSORMIB.EntPhySensorTable>`
    
    

    """

    _prefix = 'entity-sensor'
    _revision = '2002-12-16'

    def __init__(self):
        self.entphysensortable = ENTITYSENSORMIB.EntPhySensorTable()
        self.entphysensortable.parent = self


    class EntPhySensorTable(object):
        """
        This table contains one row per physical sensor represented
        by an associated row in the entPhysicalTable.
        
        .. attribute:: entphysensorentry
        
        	Information about a particular physical sensor.  An entry in this table describes the present reading of a sensor, the measurement units and scale, and sensor operational status.  Entries are created in this table by the agent.  An entry for each physical sensor SHOULD be created at the same time as the associated entPhysicalEntry.  An entry SHOULD be destroyed if the associated entPhysicalEntry is destroyed
        	**type**\: list of :py:class:`EntPhySensorEntry <ydk.models.entity.ENTITY_SENSOR_MIB.ENTITYSENSORMIB.EntPhySensorTable.EntPhySensorEntry>`
        
        

        """

        _prefix = 'entity-sensor'
        _revision = '2002-12-16'

        def __init__(self):
            self.parent = None
            self.entphysensorentry = YList()
            self.entphysensorentry.parent = self
            self.entphysensorentry.name = 'entphysensorentry'


        class EntPhySensorEntry(object):
            """
            Information about a particular physical sensor.
            
            An entry in this table describes the present reading of a
            sensor, the measurement units and scale, and sensor
            operational status.
            
            Entries are created in this table by the agent.  An entry
            for each physical sensor SHOULD be created at the same time
            as the associated entPhysicalEntry.  An entry SHOULD be
            destroyed if the associated entPhysicalEntry is destroyed.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entphysensoroperstatus
            
            	The operational status of the sensor
            	**type**\: :py:class:`EntitySensorStatus_Enum <ydk.models.entity.ENTITY_SENSOR_MIB.EntitySensorStatus_Enum>`
            
            .. attribute:: entphysensorprecision
            
            	The number of decimal places of precision in fixed\-point sensor values returned by the associated entPhySensorValue object.  This object SHOULD be set to '0' when the associated entPhySensorType value is not a fixed\-point type\: e.g., 'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\: int
            
            	**range:** \-8..9
            
            .. attribute:: entphysensorscale
            
            	The exponent to apply to values returned by the associated entPhySensorValue object.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\: :py:class:`EntitySensorDataScale_Enum <ydk.models.entity.ENTITY_SENSOR_MIB.EntitySensorDataScale_Enum>`
            
            .. attribute:: entphysensortype
            
            	The type of data returned by the associated entPhySensorValue object.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\: :py:class:`EntitySensorDataType_Enum <ydk.models.entity.ENTITY_SENSOR_MIB.EntitySensorDataType_Enum>`
            
            .. attribute:: entphysensorunitsdisplay
            
            	A textual description of the data units that should be used in the display of entPhySensorValue
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: entphysensorvalue
            
            	The most recent measurement obtained by the agent for this sensor.  To correctly interpret the value of this object, the associated entPhySensorType, entPhySensorScale, and entPhySensorPrecision objects must also be examined
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: entphysensorvaluetimestamp
            
            	The value of sysUpTime at the time the status and/or value of this sensor was last obtained by the agent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: entphysensorvalueupdaterate
            
            	An indication of the frequency that the agent updates the associated entPhySensorValue object, representing in milliseconds.  The value zero indicates\:      \- the sensor value is updated on demand (e.g.,       when polled by the agent for a get\-request),     \- the sensor value is updated when the sensor       value changes (event\-driven),     \- the agent does not know the update rate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'entity-sensor'
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
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB/ENTITY-SENSOR-MIB:entPhySensorTable/ENTITY-SENSOR-MIB:entPhySensorEntry[ENTITY-SENSOR-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _ENTITY_SENSOR_MIB as meta
                return meta._meta_table['ENTITYSENSORMIB.EntPhySensorTable.EntPhySensorEntry']['meta_info']

        @property
        def _common_path(self):

            return '/ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB/ENTITY-SENSOR-MIB:entPhySensorTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.entphysensorentry is not None:
                for child_ref in self.entphysensorentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _ENTITY_SENSOR_MIB as meta
            return meta._meta_table['ENTITYSENSORMIB.EntPhySensorTable']['meta_info']

    @property
    def _common_path(self):

        return '/ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.entphysensortable is not None and self.entphysensortable._has_data():
            return True

        if self.entphysensortable is not None and self.entphysensortable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _ENTITY_SENSOR_MIB as meta
        return meta._meta_table['ENTITYSENSORMIB']['meta_info']


