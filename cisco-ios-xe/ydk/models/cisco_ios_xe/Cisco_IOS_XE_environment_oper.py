""" Cisco_IOS_XE_environment_oper 

This module contains a collection of YANG definitions for
monitoring Environment of a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SensorUnitsTypeEnum(Enum):
    """
    SensorUnitsTypeEnum

    .. data:: Watts = 0

    .. data:: Celsius = 1

    .. data:: milliVolts = 2

    .. data:: Amperes = 3

    .. data:: Volts_DC = 4

    .. data:: Volts_AC = 5

    .. data:: milliAmperes = 6

    """

    Watts = 0

    Celsius = 1

    milliVolts = 2

    Amperes = 3

    Volts_DC = 4

    Volts_AC = 5

    milliAmperes = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_environment_oper as meta
        return meta._meta_table['SensorUnitsTypeEnum']



class EnvironmentSensors(object):
    """
    Data nodes for Environmental Monitoring.
    
    .. attribute:: environment_sensor
    
    	The list of components on the device chasis
    	**type**\: list of    :py:class:`EnvironmentSensor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper.EnvironmentSensors.EnvironmentSensor>`
    
    

    """

    _prefix = 'environment-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.environment_sensor = YList()
        self.environment_sensor.parent = self
        self.environment_sensor.name = 'environment_sensor'


    class EnvironmentSensor(object):
        """
        The list of components on the device chasis.
        
        .. attribute:: name  <key>
        
        	The name of the sensor component. This includes all physical components of the chasis \-  both fixed and pluggable
        	**type**\:  str
        
        .. attribute:: location  <key>
        
        	The name of the location where this slot is present
        	**type**\:  str
        
        .. attribute:: current_reading
        
        	Numerical value of current sensor reading in sensor\-units
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: sensor_units
        
        	Units corresponding to current\-reading value
        	**type**\:   :py:class:`SensorUnitsTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper.SensorUnitsTypeEnum>`
        
        .. attribute:: state
        
        	A description of current state of the sensor
        	**type**\:  str
        
        

        """

        _prefix = 'environment-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.name = None
            self.location = None
            self.current_reading = None
            self.sensor_units = None
            self.state = None

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')
            if self.location is None:
                raise YPYModelError('Key property location is None')

            return '/Cisco-IOS-XE-environment-oper:environment-sensors/Cisco-IOS-XE-environment-oper:environment-sensor[Cisco-IOS-XE-environment-oper:name = ' + str(self.name) + '][Cisco-IOS-XE-environment-oper:location = ' + str(self.location) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.name is not None:
                return True

            if self.location is not None:
                return True

            if self.current_reading is not None:
                return True

            if self.sensor_units is not None:
                return True

            if self.state is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_environment_oper as meta
            return meta._meta_table['EnvironmentSensors.EnvironmentSensor']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-environment-oper:environment-sensors'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.environment_sensor is not None:
            for child_ref in self.environment_sensor:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_environment_oper as meta
        return meta._meta_table['EnvironmentSensors']['meta_info']


