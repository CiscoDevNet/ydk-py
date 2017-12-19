""" Cisco_IOS_XE_environment_oper 

This module contains a collection of YANG definitions
for monitoring Environment of a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SensorUnitsType(Enum):
    """
    SensorUnitsType

    Units used by various sensors

    .. data:: Watts = 0

    .. data:: Celsius = 1

    .. data:: milliVolts = 2

    .. data:: Amperes = 3

    .. data:: Volts_DC = 4

    .. data:: Volts_AC = 5

    .. data:: milliAmperes = 6

    """

    Watts = Enum.YLeaf(0, "Watts")

    Celsius = Enum.YLeaf(1, "Celsius")

    milliVolts = Enum.YLeaf(2, "milliVolts")

    Amperes = Enum.YLeaf(3, "Amperes")

    Volts_DC = Enum.YLeaf(4, "Volts-DC")

    Volts_AC = Enum.YLeaf(5, "Volts-AC")

    milliAmperes = Enum.YLeaf(6, "milliAmperes")



class EnvironmentSensors(Entity):
    """
    Data nodes for Environmental Monitoring
    
    .. attribute:: environment_sensor
    
    	The list of components on the device chasis
    	**type**\: list of  		 :py:class:`EnvironmentSensor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper.EnvironmentSensors.EnvironmentSensor>`
    
    

    """

    _prefix = 'environment-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(EnvironmentSensors, self).__init__()
        self._top_entity = None

        self.yang_name = "environment-sensors"
        self.yang_parent_name = "Cisco-IOS-XE-environment-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"environment-sensor" : ("environment_sensor", EnvironmentSensors.EnvironmentSensor)}

        self.environment_sensor = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-environment-oper:environment-sensors"

    def __setattr__(self, name, value):
        self._perform_setattr(EnvironmentSensors, [], name, value)


    class EnvironmentSensor(Entity):
        """
        The list of components on the device chasis
        
        .. attribute:: name  <key>
        
        	Name of the sensor component. This includes all physical components of the chasis \- both fixed and pluggable
        	**type**\: str
        
        .. attribute:: location  <key>
        
        	Sensor location
        	**type**\: str
        
        .. attribute:: state
        
        	A description of the current state of the sensor
        	**type**\: str
        
        .. attribute:: current_reading
        
        	Numerical value of the current sensor reading in sensor\-units
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sensor_units
        
        	Units corresponding to the current\-reading value
        	**type**\:  :py:class:`SensorUnitsType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper.SensorUnitsType>`
        
        

        """

        _prefix = 'environment-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(EnvironmentSensors.EnvironmentSensor, self).__init__()

            self.yang_name = "environment-sensor"
            self.yang_parent_name = "environment-sensors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.name = YLeaf(YType.str, "name")

            self.location = YLeaf(YType.str, "location")

            self.state = YLeaf(YType.str, "state")

            self.current_reading = YLeaf(YType.uint32, "current-reading")

            self.sensor_units = YLeaf(YType.enumeration, "sensor-units")
            self._segment_path = lambda: "environment-sensor" + "[name='" + self.name.get() + "']" + "[location='" + self.location.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-environment-oper:environment-sensors/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EnvironmentSensors.EnvironmentSensor, ['name', 'location', 'state', 'current_reading', 'sensor_units'], name, value)

    def clone_ptr(self):
        self._top_entity = EnvironmentSensors()
        return self._top_entity

