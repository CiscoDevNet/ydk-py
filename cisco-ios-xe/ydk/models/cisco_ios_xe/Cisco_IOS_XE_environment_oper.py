""" Cisco_IOS_XE_environment_oper 

This module contains a collection of YANG definitions
for monitoring Environment of a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    	**type**\: list of    :py:class:`EnvironmentSensor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper.EnvironmentSensors.EnvironmentSensor>`
    
    

    """

    _prefix = 'environment-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(EnvironmentSensors, self).__init__()
        self._top_entity = None

        self.yang_name = "environment-sensors"
        self.yang_parent_name = "Cisco-IOS-XE-environment-oper"

        self.environment_sensor = YList(self)

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
                    super(EnvironmentSensors, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(EnvironmentSensors, self).__setattr__(name, value)


    class EnvironmentSensor(Entity):
        """
        The list of components on the device chasis
        
        .. attribute:: name  <key>
        
        	Name of the sensor component. This includes all physical components of the chasis \- both fixed and pluggable
        	**type**\:  str
        
        .. attribute:: location  <key>
        
        	Sensor location
        	**type**\:  str
        
        .. attribute:: current_reading
        
        	Numerical value of the current sensor reading in sensor\-units
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: sensor_units
        
        	Units corresponding to the current\-reading value
        	**type**\:   :py:class:`SensorUnitsType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper.SensorUnitsType>`
        
        .. attribute:: state
        
        	A description of the current state of the sensor
        	**type**\:  str
        
        

        """

        _prefix = 'environment-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(EnvironmentSensors.EnvironmentSensor, self).__init__()

            self.yang_name = "environment-sensor"
            self.yang_parent_name = "environment-sensors"

            self.name = YLeaf(YType.str, "name")

            self.location = YLeaf(YType.str, "location")

            self.current_reading = YLeaf(YType.uint32, "current-reading")

            self.sensor_units = YLeaf(YType.enumeration, "sensor-units")

            self.state = YLeaf(YType.str, "state")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("name",
                            "location",
                            "current_reading",
                            "sensor_units",
                            "state") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EnvironmentSensors.EnvironmentSensor, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EnvironmentSensors.EnvironmentSensor, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.name.is_set or
                self.location.is_set or
                self.current_reading.is_set or
                self.sensor_units.is_set or
                self.state.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.location.yfilter != YFilter.not_set or
                self.current_reading.yfilter != YFilter.not_set or
                self.sensor_units.yfilter != YFilter.not_set or
                self.state.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "environment-sensor" + "[name='" + self.name.get() + "']" + "[location='" + self.location.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-environment-oper:environment-sensors/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                leaf_name_data.append(self.location.get_name_leafdata())
            if (self.current_reading.is_set or self.current_reading.yfilter != YFilter.not_set):
                leaf_name_data.append(self.current_reading.get_name_leafdata())
            if (self.sensor_units.is_set or self.sensor_units.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sensor_units.get_name_leafdata())
            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                leaf_name_data.append(self.state.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "name" or name == "location" or name == "current-reading" or name == "sensor-units" or name == "state"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "location"):
                self.location = value
                self.location.value_namespace = name_space
                self.location.value_namespace_prefix = name_space_prefix
            if(value_path == "current-reading"):
                self.current_reading = value
                self.current_reading.value_namespace = name_space
                self.current_reading.value_namespace_prefix = name_space_prefix
            if(value_path == "sensor-units"):
                self.sensor_units = value
                self.sensor_units.value_namespace = name_space
                self.sensor_units.value_namespace_prefix = name_space_prefix
            if(value_path == "state"):
                self.state = value
                self.state.value_namespace = name_space
                self.state.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.environment_sensor:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.environment_sensor:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-environment-oper:environment-sensors" + path_buffer

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

        if (child_yang_name == "environment-sensor"):
            for c in self.environment_sensor:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = EnvironmentSensors.EnvironmentSensor()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.environment_sensor.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "environment-sensor"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EnvironmentSensors()
        return self._top_entity

