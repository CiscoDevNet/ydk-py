""" Cisco_IOS_XE_environment_oper 

This module contains a collection of YANG definitions
for monitoring Environment of a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SensorUnitsType(Enum):
    """
    SensorUnitsType (Enum Class)

    Units used by various sensors

    .. data:: watts = 0

    .. data:: celsius = 1

    .. data:: millivolts = 2

    .. data:: amperes = 3

    .. data:: volts_dc = 4

    .. data:: volts_ac = 5

    .. data:: milliamperes = 6

    .. data:: unknown = 7

    .. data:: revolutions_per_minute = 8

    """

    watts = Enum.YLeaf(0, "watts")

    celsius = Enum.YLeaf(1, "celsius")

    millivolts = Enum.YLeaf(2, "millivolts")

    amperes = Enum.YLeaf(3, "amperes")

    volts_dc = Enum.YLeaf(4, "volts-dc")

    volts_ac = Enum.YLeaf(5, "volts-ac")

    milliamperes = Enum.YLeaf(6, "milliamperes")

    unknown = Enum.YLeaf(7, "unknown")

    revolutions_per_minute = Enum.YLeaf(8, "revolutions-per-minute")



class EnvironmentSensors(Entity):
    """
    Data nodes for Environmental Monitoring
    
    .. attribute:: environment_sensor
    
    	The list of components on the device chasis
    	**type**\: list of  		 :py:class:`EnvironmentSensor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper.EnvironmentSensors.EnvironmentSensor>`
    
    

    """

    _prefix = 'environment-ios-xe-oper'
    _revision = '2017-11-27'

    def __init__(self):
        super(EnvironmentSensors, self).__init__()
        self._top_entity = None

        self.yang_name = "environment-sensors"
        self.yang_parent_name = "Cisco-IOS-XE-environment-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("environment-sensor", ("environment_sensor", EnvironmentSensors.EnvironmentSensor))])
        self._leafs = OrderedDict()

        self.environment_sensor = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-environment-oper:environment-sensors"

    def __setattr__(self, name, value):
        self._perform_setattr(EnvironmentSensors, [], name, value)


    class EnvironmentSensor(Entity):
        """
        The list of components on the device chasis
        
        .. attribute:: name  (key)
        
        	Name of the sensor component. This includes all physical components of the chasis \- both fixed and pluggable
        	**type**\: str
        
        .. attribute:: location  (key)
        
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
        
        .. attribute:: low_critical_threshold
        
        	Alarm threshold under which a critical alarm will be signaled
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: low_normal_threshold
        
        	No alarm above this threshold
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: high_normal_threshold
        
        	No alarm below this threshold
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: high_critical_threshold
        
        	Alarm threshold over which a critical  alarm will be signaled
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'environment-ios-xe-oper'
        _revision = '2017-11-27'

        def __init__(self):
            super(EnvironmentSensors.EnvironmentSensor, self).__init__()

            self.yang_name = "environment-sensor"
            self.yang_parent_name = "environment-sensors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name','location']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('location', YLeaf(YType.str, 'location')),
                ('state', YLeaf(YType.str, 'state')),
                ('current_reading', YLeaf(YType.uint32, 'current-reading')),
                ('sensor_units', YLeaf(YType.enumeration, 'sensor-units')),
                ('low_critical_threshold', YLeaf(YType.int32, 'low-critical-threshold')),
                ('low_normal_threshold', YLeaf(YType.int32, 'low-normal-threshold')),
                ('high_normal_threshold', YLeaf(YType.int32, 'high-normal-threshold')),
                ('high_critical_threshold', YLeaf(YType.int32, 'high-critical-threshold')),
            ])
            self.name = None
            self.location = None
            self.state = None
            self.current_reading = None
            self.sensor_units = None
            self.low_critical_threshold = None
            self.low_normal_threshold = None
            self.high_normal_threshold = None
            self.high_critical_threshold = None
            self._segment_path = lambda: "environment-sensor" + "[name='" + str(self.name) + "']" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-environment-oper:environment-sensors/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EnvironmentSensors.EnvironmentSensor, ['name', 'location', 'state', 'current_reading', 'sensor_units', 'low_critical_threshold', 'low_normal_threshold', 'high_normal_threshold', 'high_critical_threshold'], name, value)

    def clone_ptr(self):
        self._top_entity = EnvironmentSensors()
        return self._top_entity

