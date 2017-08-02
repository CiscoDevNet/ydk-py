""" Cisco_IOS_XR_asr9k_sc_envmon_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-envmon package operational data.

This module contains definitions
for the following management objects\:
  environmental\-monitoring\: Environmental Monitoring Operational
    data space

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EnvironmentalMonitoring(Entity):
    """
    Environmental Monitoring Operational data space
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks>`
    
    

    """

    _prefix = 'asr9k-sc-envmon-oper'
    _revision = '2017-01-19'

    def __init__(self):
        super(EnvironmentalMonitoring, self).__init__()
        self._top_entity = None

        self.yang_name = "environmental-monitoring"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-sc-envmon-oper"

        self.racks = EnvironmentalMonitoring.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Number
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack>`
        
        

        """

        _prefix = 'asr9k-sc-envmon-oper'
        _revision = '2017-01-19'

        def __init__(self):
            super(EnvironmentalMonitoring.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "environmental-monitoring"

            self.rack = YList(self)

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
                        super(EnvironmentalMonitoring.Racks, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EnvironmentalMonitoring.Racks, self).__setattr__(name, value)


        class Rack(Entity):
            """
            Number
            
            .. attribute:: rack  <key>
            
            	Rack number
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'asr9k-sc-envmon-oper'
            _revision = '2017-01-19'

            def __init__(self):
                super(EnvironmentalMonitoring.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"

                self.rack = YLeaf(YType.int32, "rack")

                self.slots = EnvironmentalMonitoring.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._children_yang_names.add("slots")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rack") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EnvironmentalMonitoring.Racks.Rack, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EnvironmentalMonitoring.Racks.Rack, self).__setattr__(name, value)


            class Slots(Entity):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Name
                	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'asr9k-sc-envmon-oper'
                _revision = '2017-01-19'

                def __init__(self):
                    super(EnvironmentalMonitoring.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"

                    self.slot = YList(self)

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
                                super(EnvironmentalMonitoring.Racks.Rack.Slots, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EnvironmentalMonitoring.Racks.Rack.Slots, self).__setattr__(name, value)


                class Slot(Entity):
                    """
                    Name
                    
                    .. attribute:: slot  <key>
                    
                    	Slot name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: modules
                    
                    	Table of modules
                    	**type**\:   :py:class:`Modules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-envmon-oper'
                    _revision = '2017-01-19'

                    def __init__(self):
                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"

                        self.slot = YLeaf(YType.str, "slot")

                        self.modules = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules()
                        self.modules.parent = self
                        self._children_name_map["modules"] = "modules"
                        self._children_yang_names.add("modules")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("slot") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot, self).__setattr__(name, value)


                    class Modules(Entity):
                        """
                        Table of modules
                        
                        .. attribute:: module
                        
                        	Name
                        	**type**\: list of    :py:class:`Module <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-envmon-oper'
                        _revision = '2017-01-19'

                        def __init__(self):
                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules, self).__init__()

                            self.yang_name = "modules"
                            self.yang_parent_name = "slot"

                            self.module = YList(self)

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
                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules, self).__setattr__(name, value)


                        class Module(Entity):
                            """
                            Name
                            
                            .. attribute:: module  <key>
                            
                            	Module name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: power
                            
                            	Module Power Draw
                            	**type**\:   :py:class:`Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power>`
                            
                            .. attribute:: sensor_types
                            
                            	Table of sensor types
                            	**type**\:   :py:class:`SensorTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-envmon-oper'
                            _revision = '2017-01-19'

                            def __init__(self):
                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module, self).__init__()

                                self.yang_name = "module"
                                self.yang_parent_name = "modules"

                                self.module = YLeaf(YType.str, "module")

                                self.power = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power()
                                self.power.parent = self
                                self._children_name_map["power"] = "power"
                                self._children_yang_names.add("power")

                                self.sensor_types = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes()
                                self.sensor_types.parent = self
                                self._children_name_map["sensor_types"] = "sensor-types"
                                self._children_yang_names.add("sensor-types")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("module") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module, self).__setattr__(name, value)


                            class Power(Entity):
                                """
                                Module Power Draw
                                
                                .. attribute:: power_bag
                                
                                	Detailed power bag information
                                	**type**\:   :py:class:`PowerBag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-envmon-oper'
                                _revision = '2017-01-19'

                                def __init__(self):
                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power, self).__init__()

                                    self.yang_name = "power"
                                    self.yang_parent_name = "module"

                                    self.power_bag = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag()
                                    self.power_bag.parent = self
                                    self._children_name_map["power_bag"] = "power-bag"
                                    self._children_yang_names.add("power-bag")


                                class PowerBag(Entity):
                                    """
                                    Detailed power bag information
                                    
                                    .. attribute:: power_accuracy
                                    
                                    	Accuracy of the Power Value
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_admin_state
                                    
                                    	Admin Status of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_current_type
                                    
                                    	Current Type of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_max_value
                                    
                                    	Max Power Value of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: power_measure_caliber
                                    
                                    	Measure Caliber
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_oper_state
                                    
                                    	Oper Status of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_origin
                                    
                                    	The Power Origin of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_state_enter_reason
                                    
                                    	Enter Reason for the State
                                    	**type**\:  str
                                    
                                    	**length:** 0..50
                                    
                                    .. attribute:: power_unit_multiplier
                                    
                                    	Unit Multiplier of Power
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: power_value
                                    
                                    	Current Power Value of the Unit
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-envmon-oper'
                                    _revision = '2017-01-19'

                                    def __init__(self):
                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag, self).__init__()

                                        self.yang_name = "power-bag"
                                        self.yang_parent_name = "power"

                                        self.power_accuracy = YLeaf(YType.uint32, "power-accuracy")

                                        self.power_admin_state = YLeaf(YType.uint32, "power-admin-state")

                                        self.power_current_type = YLeaf(YType.uint32, "power-current-type")

                                        self.power_max_value = YLeaf(YType.int32, "power-max-value")

                                        self.power_measure_caliber = YLeaf(YType.uint32, "power-measure-caliber")

                                        self.power_oper_state = YLeaf(YType.uint32, "power-oper-state")

                                        self.power_origin = YLeaf(YType.uint32, "power-origin")

                                        self.power_state_enter_reason = YLeaf(YType.str, "power-state-enter-reason")

                                        self.power_unit_multiplier = YLeaf(YType.uint32, "power-unit-multiplier")

                                        self.power_value = YLeaf(YType.int32, "power-value")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("power_accuracy",
                                                        "power_admin_state",
                                                        "power_current_type",
                                                        "power_max_value",
                                                        "power_measure_caliber",
                                                        "power_oper_state",
                                                        "power_origin",
                                                        "power_state_enter_reason",
                                                        "power_unit_multiplier",
                                                        "power_value") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.power_accuracy.is_set or
                                            self.power_admin_state.is_set or
                                            self.power_current_type.is_set or
                                            self.power_max_value.is_set or
                                            self.power_measure_caliber.is_set or
                                            self.power_oper_state.is_set or
                                            self.power_origin.is_set or
                                            self.power_state_enter_reason.is_set or
                                            self.power_unit_multiplier.is_set or
                                            self.power_value.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.power_accuracy.yfilter != YFilter.not_set or
                                            self.power_admin_state.yfilter != YFilter.not_set or
                                            self.power_current_type.yfilter != YFilter.not_set or
                                            self.power_max_value.yfilter != YFilter.not_set or
                                            self.power_measure_caliber.yfilter != YFilter.not_set or
                                            self.power_oper_state.yfilter != YFilter.not_set or
                                            self.power_origin.yfilter != YFilter.not_set or
                                            self.power_state_enter_reason.yfilter != YFilter.not_set or
                                            self.power_unit_multiplier.yfilter != YFilter.not_set or
                                            self.power_value.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "power-bag" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.power_accuracy.is_set or self.power_accuracy.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_accuracy.get_name_leafdata())
                                        if (self.power_admin_state.is_set or self.power_admin_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_admin_state.get_name_leafdata())
                                        if (self.power_current_type.is_set or self.power_current_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_current_type.get_name_leafdata())
                                        if (self.power_max_value.is_set or self.power_max_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_max_value.get_name_leafdata())
                                        if (self.power_measure_caliber.is_set or self.power_measure_caliber.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_measure_caliber.get_name_leafdata())
                                        if (self.power_oper_state.is_set or self.power_oper_state.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_oper_state.get_name_leafdata())
                                        if (self.power_origin.is_set or self.power_origin.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_origin.get_name_leafdata())
                                        if (self.power_state_enter_reason.is_set or self.power_state_enter_reason.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_state_enter_reason.get_name_leafdata())
                                        if (self.power_unit_multiplier.is_set or self.power_unit_multiplier.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_unit_multiplier.get_name_leafdata())
                                        if (self.power_value.is_set or self.power_value.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_value.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "power-accuracy" or name == "power-admin-state" or name == "power-current-type" or name == "power-max-value" or name == "power-measure-caliber" or name == "power-oper-state" or name == "power-origin" or name == "power-state-enter-reason" or name == "power-unit-multiplier" or name == "power-value"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "power-accuracy"):
                                            self.power_accuracy = value
                                            self.power_accuracy.value_namespace = name_space
                                            self.power_accuracy.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-admin-state"):
                                            self.power_admin_state = value
                                            self.power_admin_state.value_namespace = name_space
                                            self.power_admin_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-current-type"):
                                            self.power_current_type = value
                                            self.power_current_type.value_namespace = name_space
                                            self.power_current_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-max-value"):
                                            self.power_max_value = value
                                            self.power_max_value.value_namespace = name_space
                                            self.power_max_value.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-measure-caliber"):
                                            self.power_measure_caliber = value
                                            self.power_measure_caliber.value_namespace = name_space
                                            self.power_measure_caliber.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-oper-state"):
                                            self.power_oper_state = value
                                            self.power_oper_state.value_namespace = name_space
                                            self.power_oper_state.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-origin"):
                                            self.power_origin = value
                                            self.power_origin.value_namespace = name_space
                                            self.power_origin.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-state-enter-reason"):
                                            self.power_state_enter_reason = value
                                            self.power_state_enter_reason.value_namespace = name_space
                                            self.power_state_enter_reason.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-unit-multiplier"):
                                            self.power_unit_multiplier = value
                                            self.power_unit_multiplier.value_namespace = name_space
                                            self.power_unit_multiplier.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-value"):
                                            self.power_value = value
                                            self.power_value.value_namespace = name_space
                                            self.power_value.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.power_bag is not None and self.power_bag.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.power_bag is not None and self.power_bag.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "power" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "power-bag"):
                                        if (self.power_bag is None):
                                            self.power_bag = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag()
                                            self.power_bag.parent = self
                                            self._children_name_map["power_bag"] = "power-bag"
                                        return self.power_bag

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "power-bag"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class SensorTypes(Entity):
                                """
                                Table of sensor types
                                
                                .. attribute:: sensor_type
                                
                                	Type of sensor
                                	**type**\: list of    :py:class:`SensorType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-envmon-oper'
                                _revision = '2017-01-19'

                                def __init__(self):
                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes, self).__init__()

                                    self.yang_name = "sensor-types"
                                    self.yang_parent_name = "module"

                                    self.sensor_type = YList(self)

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
                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes, self).__setattr__(name, value)


                                class SensorType(Entity):
                                    """
                                    Type of sensor
                                    
                                    .. attribute:: type  <key>
                                    
                                    	Sensor type
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: sensor_names
                                    
                                    	Table of sensors
                                    	**type**\:   :py:class:`SensorNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-envmon-oper'
                                    _revision = '2017-01-19'

                                    def __init__(self):
                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType, self).__init__()

                                        self.yang_name = "sensor-type"
                                        self.yang_parent_name = "sensor-types"

                                        self.type = YLeaf(YType.str, "type")

                                        self.sensor_names = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames()
                                        self.sensor_names.parent = self
                                        self._children_name_map["sensor_names"] = "sensor-names"
                                        self._children_yang_names.add("sensor-names")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("type") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType, self).__setattr__(name, value)


                                    class SensorNames(Entity):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor_name
                                        
                                        	Name of sensor
                                        	**type**\: list of    :py:class:`SensorName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-envmon-oper'
                                        _revision = '2017-01-19'

                                        def __init__(self):
                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames, self).__init__()

                                            self.yang_name = "sensor-names"
                                            self.yang_parent_name = "sensor-type"

                                            self.sensor_name = YList(self)

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
                                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames, self).__setattr__(name, value)


                                        class SensorName(Entity):
                                            """
                                            Name of sensor
                                            
                                            .. attribute:: name  <key>
                                            
                                            	Sensor name
                                            	**type**\:  str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            .. attribute:: thresholds
                                            
                                            	The threshold information
                                            	**type**\:   :py:class:`Thresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds>`
                                            
                                            .. attribute:: value_brief
                                            
                                            	The sensor value
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: value_detailed
                                            
                                            	Detailed sensor information including the sensor value
                                            	**type**\:   :py:class:`ValueDetailed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-envmon-oper'
                                            _revision = '2017-01-19'

                                            def __init__(self):
                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName, self).__init__()

                                                self.yang_name = "sensor-name"
                                                self.yang_parent_name = "sensor-names"

                                                self.name = YLeaf(YType.str, "name")

                                                self.value_brief = YLeaf(YType.int32, "value-brief")

                                                self.thresholds = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds()
                                                self.thresholds.parent = self
                                                self._children_name_map["thresholds"] = "thresholds"
                                                self._children_yang_names.add("thresholds")

                                                self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed()
                                                self.value_detailed.parent = self
                                                self._children_name_map["value_detailed"] = "value-detailed"
                                                self._children_yang_names.add("value-detailed")

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
                                                                "value_brief") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName, self).__setattr__(name, value)


                                            class Thresholds(Entity):
                                                """
                                                The threshold information
                                                
                                                .. attribute:: threshold
                                                
                                                	Types of thresholds
                                                	**type**\: list of    :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold>`
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-envmon-oper'
                                                _revision = '2017-01-19'

                                                def __init__(self):
                                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds, self).__init__()

                                                    self.yang_name = "thresholds"
                                                    self.yang_parent_name = "sensor-name"

                                                    self.threshold = YList(self)

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
                                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds, self).__setattr__(name, value)


                                                class Threshold(Entity):
                                                    """
                                                    Types of thresholds
                                                    
                                                    .. attribute:: type  <key>
                                                    
                                                    	Threshold type
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    .. attribute:: trap
                                                    
                                                    	Threshold trap enable flag true\-ENABLE, false\-DISABLE
                                                    	**type**\:  bool
                                                    
                                                    .. attribute:: value_brief
                                                    
                                                    	Threshold value for the sensor
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: value_detailed
                                                    
                                                    	Detailed sensor threshold information
                                                    	**type**\:   :py:class:`ValueDetailed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-envmon-oper'
                                                    _revision = '2017-01-19'

                                                    def __init__(self):
                                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold, self).__init__()

                                                        self.yang_name = "threshold"
                                                        self.yang_parent_name = "thresholds"

                                                        self.type = YLeaf(YType.str, "type")

                                                        self.trap = YLeaf(YType.boolean, "trap")

                                                        self.value_brief = YLeaf(YType.int32, "value-brief")

                                                        self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed()
                                                        self.value_detailed.parent = self
                                                        self._children_name_map["value_detailed"] = "value-detailed"
                                                        self._children_yang_names.add("value-detailed")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("type",
                                                                        "trap",
                                                                        "value_brief") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold, self).__setattr__(name, value)


                                                    class ValueDetailed(Entity):
                                                        """
                                                        Detailed sensor threshold
                                                        information
                                                        
                                                        .. attribute:: threshold_evaluation
                                                        
                                                        	Indicates the result of the most recent evaluation of the thresholD
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: threshold_notification_enabled
                                                        
                                                        	Indicates whether or not a notification should result, in case of threshold violation
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: threshold_relation
                                                        
                                                        	Indicates relation between sensor value and threshold
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: threshold_severity
                                                        
                                                        	Indicates minor, major, critical severities
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: threshold_value
                                                        
                                                        	Value of the configured threshold
                                                        	**type**\:  int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-envmon-oper'
                                                        _revision = '2017-01-19'

                                                        def __init__(self):
                                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed, self).__init__()

                                                            self.yang_name = "value-detailed"
                                                            self.yang_parent_name = "threshold"

                                                            self.threshold_evaluation = YLeaf(YType.boolean, "threshold-evaluation")

                                                            self.threshold_notification_enabled = YLeaf(YType.boolean, "threshold-notification-enabled")

                                                            self.threshold_relation = YLeaf(YType.uint32, "threshold-relation")

                                                            self.threshold_severity = YLeaf(YType.uint32, "threshold-severity")

                                                            self.threshold_value = YLeaf(YType.uint32, "threshold-value")

                                                        def __setattr__(self, name, value):
                                                            self._check_monkey_patching_error(name, value)
                                                            with _handle_type_error():
                                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                        "Please use list append or extend method."
                                                                                        .format(value))
                                                                if isinstance(value, Enum.YLeaf):
                                                                    value = value.name
                                                                if name in ("threshold_evaluation",
                                                                            "threshold_notification_enabled",
                                                                            "threshold_relation",
                                                                            "threshold_severity",
                                                                            "threshold_value") and name in self.__dict__:
                                                                    if isinstance(value, YLeaf):
                                                                        self.__dict__[name].set(value.get())
                                                                    elif isinstance(value, YLeafList):
                                                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed, self).__setattr__(name, value)
                                                                    else:
                                                                        self.__dict__[name].set(value)
                                                                else:
                                                                    if hasattr(value, "parent") and name != "parent":
                                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                            value.parent = self
                                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                            value.parent = self
                                                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed, self).__setattr__(name, value)

                                                        def has_data(self):
                                                            return (
                                                                self.threshold_evaluation.is_set or
                                                                self.threshold_notification_enabled.is_set or
                                                                self.threshold_relation.is_set or
                                                                self.threshold_severity.is_set or
                                                                self.threshold_value.is_set)

                                                        def has_operation(self):
                                                            return (
                                                                self.yfilter != YFilter.not_set or
                                                                self.threshold_evaluation.yfilter != YFilter.not_set or
                                                                self.threshold_notification_enabled.yfilter != YFilter.not_set or
                                                                self.threshold_relation.yfilter != YFilter.not_set or
                                                                self.threshold_severity.yfilter != YFilter.not_set or
                                                                self.threshold_value.yfilter != YFilter.not_set)

                                                        def get_segment_path(self):
                                                            path_buffer = ""
                                                            path_buffer = "value-detailed" + path_buffer

                                                            return path_buffer

                                                        def get_entity_path(self, ancestor):
                                                            path_buffer = ""
                                                            if (ancestor is None):
                                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                            else:
                                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                            leaf_name_data = LeafDataList()
                                                            if (self.threshold_evaluation.is_set or self.threshold_evaluation.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.threshold_evaluation.get_name_leafdata())
                                                            if (self.threshold_notification_enabled.is_set or self.threshold_notification_enabled.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.threshold_notification_enabled.get_name_leafdata())
                                                            if (self.threshold_relation.is_set or self.threshold_relation.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.threshold_relation.get_name_leafdata())
                                                            if (self.threshold_severity.is_set or self.threshold_severity.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.threshold_severity.get_name_leafdata())
                                                            if (self.threshold_value.is_set or self.threshold_value.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.threshold_value.get_name_leafdata())

                                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                                            return entity_path

                                                        def get_child_by_name(self, child_yang_name, segment_path):
                                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                            if child is not None:
                                                                return child

                                                            return None

                                                        def has_leaf_or_child_of_name(self, name):
                                                            if(name == "threshold-evaluation" or name == "threshold-notification-enabled" or name == "threshold-relation" or name == "threshold-severity" or name == "threshold-value"):
                                                                return True
                                                            return False

                                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                                            if(value_path == "threshold-evaluation"):
                                                                self.threshold_evaluation = value
                                                                self.threshold_evaluation.value_namespace = name_space
                                                                self.threshold_evaluation.value_namespace_prefix = name_space_prefix
                                                            if(value_path == "threshold-notification-enabled"):
                                                                self.threshold_notification_enabled = value
                                                                self.threshold_notification_enabled.value_namespace = name_space
                                                                self.threshold_notification_enabled.value_namespace_prefix = name_space_prefix
                                                            if(value_path == "threshold-relation"):
                                                                self.threshold_relation = value
                                                                self.threshold_relation.value_namespace = name_space
                                                                self.threshold_relation.value_namespace_prefix = name_space_prefix
                                                            if(value_path == "threshold-severity"):
                                                                self.threshold_severity = value
                                                                self.threshold_severity.value_namespace = name_space
                                                                self.threshold_severity.value_namespace_prefix = name_space_prefix
                                                            if(value_path == "threshold-value"):
                                                                self.threshold_value = value
                                                                self.threshold_value.value_namespace = name_space
                                                                self.threshold_value.value_namespace_prefix = name_space_prefix

                                                    def has_data(self):
                                                        return (
                                                            self.type.is_set or
                                                            self.trap.is_set or
                                                            self.value_brief.is_set or
                                                            (self.value_detailed is not None and self.value_detailed.has_data()))

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.type.yfilter != YFilter.not_set or
                                                            self.trap.yfilter != YFilter.not_set or
                                                            self.value_brief.yfilter != YFilter.not_set or
                                                            (self.value_detailed is not None and self.value_detailed.has_operation()))

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "threshold" + "[type='" + self.type.get() + "']" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.type.get_name_leafdata())
                                                        if (self.trap.is_set or self.trap.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.trap.get_name_leafdata())
                                                        if (self.value_brief.is_set or self.value_brief.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.value_brief.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        if (child_yang_name == "value-detailed"):
                                                            if (self.value_detailed is None):
                                                                self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed()
                                                                self.value_detailed.parent = self
                                                                self._children_name_map["value_detailed"] = "value-detailed"
                                                            return self.value_detailed

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "value-detailed" or name == "type" or name == "trap" or name == "value-brief"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "type"):
                                                            self.type = value
                                                            self.type.value_namespace = name_space
                                                            self.type.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "trap"):
                                                            self.trap = value
                                                            self.trap.value_namespace = name_space
                                                            self.trap.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "value-brief"):
                                                            self.value_brief = value
                                                            self.value_brief.value_namespace = name_space
                                                            self.value_brief.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    for c in self.threshold:
                                                        if (c.has_data()):
                                                            return True
                                                    return False

                                                def has_operation(self):
                                                    for c in self.threshold:
                                                        if (c.has_operation()):
                                                            return True
                                                    return self.yfilter != YFilter.not_set

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "thresholds" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    if (child_yang_name == "threshold"):
                                                        for c in self.threshold:
                                                            segment = c.get_segment_path()
                                                            if (segment_path == segment):
                                                                return c
                                                        c = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold()
                                                        c.parent = self
                                                        local_reference_key = "ydk::seg::%s" % segment_path
                                                        self._local_refs[local_reference_key] = c
                                                        self.threshold.append(c)
                                                        return c

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "threshold"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    pass


                                            class ValueDetailed(Entity):
                                                """
                                                Detailed sensor information including
                                                the sensor value
                                                
                                                .. attribute:: age_time_stamp
                                                
                                                	Age of the sensor value; set to the current time if directly access the value from sensor
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: alarm_type
                                                
                                                	Indicates threshold violation
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: data_type
                                                
                                                	Sensor data type enums
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: device_description
                                                
                                                	Device Name
                                                	**type**\:  str
                                                
                                                	**length:** 0..50
                                                
                                                .. attribute:: device_id
                                                
                                                	Identifier for this device
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: field_validity_bitmap
                                                
                                                	Sensor valid bitmap
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: precision
                                                
                                                	Sensor precision range
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: scale
                                                
                                                	Sensor scale enums
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: status
                                                
                                                	Sensor operation state enums
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: units
                                                
                                                	Units of variable being read
                                                	**type**\:  str
                                                
                                                	**length:** 0..50
                                                
                                                .. attribute:: update_rate
                                                
                                                	Sensor value update rate;set to 0 if sensor value is updated and evaluated immediately
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: value
                                                
                                                	Current reading of sensor
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-envmon-oper'
                                                _revision = '2017-01-19'

                                                def __init__(self):
                                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed, self).__init__()

                                                    self.yang_name = "value-detailed"
                                                    self.yang_parent_name = "sensor-name"

                                                    self.age_time_stamp = YLeaf(YType.uint32, "age-time-stamp")

                                                    self.alarm_type = YLeaf(YType.uint32, "alarm-type")

                                                    self.data_type = YLeaf(YType.uint32, "data-type")

                                                    self.device_description = YLeaf(YType.str, "device-description")

                                                    self.device_id = YLeaf(YType.uint32, "device-id")

                                                    self.field_validity_bitmap = YLeaf(YType.uint32, "field-validity-bitmap")

                                                    self.precision = YLeaf(YType.uint32, "precision")

                                                    self.scale = YLeaf(YType.uint32, "scale")

                                                    self.status = YLeaf(YType.uint32, "status")

                                                    self.units = YLeaf(YType.str, "units")

                                                    self.update_rate = YLeaf(YType.uint32, "update-rate")

                                                    self.value = YLeaf(YType.uint32, "value")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("age_time_stamp",
                                                                    "alarm_type",
                                                                    "data_type",
                                                                    "device_description",
                                                                    "device_id",
                                                                    "field_validity_bitmap",
                                                                    "precision",
                                                                    "scale",
                                                                    "status",
                                                                    "units",
                                                                    "update_rate",
                                                                    "value") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.age_time_stamp.is_set or
                                                        self.alarm_type.is_set or
                                                        self.data_type.is_set or
                                                        self.device_description.is_set or
                                                        self.device_id.is_set or
                                                        self.field_validity_bitmap.is_set or
                                                        self.precision.is_set or
                                                        self.scale.is_set or
                                                        self.status.is_set or
                                                        self.units.is_set or
                                                        self.update_rate.is_set or
                                                        self.value.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.age_time_stamp.yfilter != YFilter.not_set or
                                                        self.alarm_type.yfilter != YFilter.not_set or
                                                        self.data_type.yfilter != YFilter.not_set or
                                                        self.device_description.yfilter != YFilter.not_set or
                                                        self.device_id.yfilter != YFilter.not_set or
                                                        self.field_validity_bitmap.yfilter != YFilter.not_set or
                                                        self.precision.yfilter != YFilter.not_set or
                                                        self.scale.yfilter != YFilter.not_set or
                                                        self.status.yfilter != YFilter.not_set or
                                                        self.units.yfilter != YFilter.not_set or
                                                        self.update_rate.yfilter != YFilter.not_set or
                                                        self.value.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "value-detailed" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.age_time_stamp.is_set or self.age_time_stamp.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.age_time_stamp.get_name_leafdata())
                                                    if (self.alarm_type.is_set or self.alarm_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.alarm_type.get_name_leafdata())
                                                    if (self.data_type.is_set or self.data_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.data_type.get_name_leafdata())
                                                    if (self.device_description.is_set or self.device_description.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.device_description.get_name_leafdata())
                                                    if (self.device_id.is_set or self.device_id.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.device_id.get_name_leafdata())
                                                    if (self.field_validity_bitmap.is_set or self.field_validity_bitmap.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.field_validity_bitmap.get_name_leafdata())
                                                    if (self.precision.is_set or self.precision.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.precision.get_name_leafdata())
                                                    if (self.scale.is_set or self.scale.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.scale.get_name_leafdata())
                                                    if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.status.get_name_leafdata())
                                                    if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.units.get_name_leafdata())
                                                    if (self.update_rate.is_set or self.update_rate.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.update_rate.get_name_leafdata())
                                                    if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.value.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "age-time-stamp" or name == "alarm-type" or name == "data-type" or name == "device-description" or name == "device-id" or name == "field-validity-bitmap" or name == "precision" or name == "scale" or name == "status" or name == "units" or name == "update-rate" or name == "value"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "age-time-stamp"):
                                                        self.age_time_stamp = value
                                                        self.age_time_stamp.value_namespace = name_space
                                                        self.age_time_stamp.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "alarm-type"):
                                                        self.alarm_type = value
                                                        self.alarm_type.value_namespace = name_space
                                                        self.alarm_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "data-type"):
                                                        self.data_type = value
                                                        self.data_type.value_namespace = name_space
                                                        self.data_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "device-description"):
                                                        self.device_description = value
                                                        self.device_description.value_namespace = name_space
                                                        self.device_description.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "device-id"):
                                                        self.device_id = value
                                                        self.device_id.value_namespace = name_space
                                                        self.device_id.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "field-validity-bitmap"):
                                                        self.field_validity_bitmap = value
                                                        self.field_validity_bitmap.value_namespace = name_space
                                                        self.field_validity_bitmap.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "precision"):
                                                        self.precision = value
                                                        self.precision.value_namespace = name_space
                                                        self.precision.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "scale"):
                                                        self.scale = value
                                                        self.scale.value_namespace = name_space
                                                        self.scale.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "status"):
                                                        self.status = value
                                                        self.status.value_namespace = name_space
                                                        self.status.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "units"):
                                                        self.units = value
                                                        self.units.value_namespace = name_space
                                                        self.units.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "update-rate"):
                                                        self.update_rate = value
                                                        self.update_rate.value_namespace = name_space
                                                        self.update_rate.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "value"):
                                                        self.value = value
                                                        self.value.value_namespace = name_space
                                                        self.value.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    self.name.is_set or
                                                    self.value_brief.is_set or
                                                    (self.thresholds is not None and self.thresholds.has_data()) or
                                                    (self.value_detailed is not None and self.value_detailed.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.name.yfilter != YFilter.not_set or
                                                    self.value_brief.yfilter != YFilter.not_set or
                                                    (self.thresholds is not None and self.thresholds.has_operation()) or
                                                    (self.value_detailed is not None and self.value_detailed.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "sensor-name" + "[name='" + self.name.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.name.get_name_leafdata())
                                                if (self.value_brief.is_set or self.value_brief.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.value_brief.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "thresholds"):
                                                    if (self.thresholds is None):
                                                        self.thresholds = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds()
                                                        self.thresholds.parent = self
                                                        self._children_name_map["thresholds"] = "thresholds"
                                                    return self.thresholds

                                                if (child_yang_name == "value-detailed"):
                                                    if (self.value_detailed is None):
                                                        self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed()
                                                        self.value_detailed.parent = self
                                                        self._children_name_map["value_detailed"] = "value-detailed"
                                                    return self.value_detailed

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "thresholds" or name == "value-detailed" or name == "name" or name == "value-brief"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "name"):
                                                    self.name = value
                                                    self.name.value_namespace = name_space
                                                    self.name.value_namespace_prefix = name_space_prefix
                                                if(value_path == "value-brief"):
                                                    self.value_brief = value
                                                    self.value_brief.value_namespace = name_space
                                                    self.value_brief.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.sensor_name:
                                                if (c.has_data()):
                                                    return True
                                            return False

                                        def has_operation(self):
                                            for c in self.sensor_name:
                                                if (c.has_operation()):
                                                    return True
                                            return self.yfilter != YFilter.not_set

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "sensor-names" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "sensor-name"):
                                                for c in self.sensor_name:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.sensor_name.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "sensor-name"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            pass

                                    def has_data(self):
                                        return (
                                            self.type.is_set or
                                            (self.sensor_names is not None and self.sensor_names.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.type.yfilter != YFilter.not_set or
                                            (self.sensor_names is not None and self.sensor_names.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "sensor-type" + "[type='" + self.type.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.type.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "sensor-names"):
                                            if (self.sensor_names is None):
                                                self.sensor_names = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames()
                                                self.sensor_names.parent = self
                                                self._children_name_map["sensor_names"] = "sensor-names"
                                            return self.sensor_names

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "sensor-names" or name == "type"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "type"):
                                            self.type = value
                                            self.type.value_namespace = name_space
                                            self.type.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.sensor_type:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.sensor_type:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "sensor-types" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "sensor-type"):
                                        for c in self.sensor_type:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.sensor_type.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "sensor-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.module.is_set or
                                    (self.power is not None and self.power.has_data()) or
                                    (self.sensor_types is not None and self.sensor_types.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.module.yfilter != YFilter.not_set or
                                    (self.power is not None and self.power.has_operation()) or
                                    (self.sensor_types is not None and self.sensor_types.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "module" + "[module='" + self.module.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.module.is_set or self.module.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.module.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "power"):
                                    if (self.power is None):
                                        self.power = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power()
                                        self.power.parent = self
                                        self._children_name_map["power"] = "power"
                                    return self.power

                                if (child_yang_name == "sensor-types"):
                                    if (self.sensor_types is None):
                                        self.sensor_types = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes()
                                        self.sensor_types.parent = self
                                        self._children_name_map["sensor_types"] = "sensor-types"
                                    return self.sensor_types

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "power" or name == "sensor-types" or name == "module"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "module"):
                                    self.module = value
                                    self.module.value_namespace = name_space
                                    self.module.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.module:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.module:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "modules" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "module"):
                                for c in self.module:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.module.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "module"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.slot.is_set or
                            (self.modules is not None and self.modules.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.slot.yfilter != YFilter.not_set or
                            (self.modules is not None and self.modules.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slot" + "[slot='" + self.slot.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slot.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "modules"):
                            if (self.modules is None):
                                self.modules = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules()
                                self.modules.parent = self
                                self._children_name_map["modules"] = "modules"
                            return self.modules

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "modules" or name == "slot"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "slot"):
                            self.slot = value
                            self.slot.value_namespace = name_space
                            self.slot.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.slot:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.slot:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "slots" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "slot"):
                        for c in self.slot:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = EnvironmentalMonitoring.Racks.Rack.Slots.Slot()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.slot.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slot"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.rack.is_set or
                    (self.slots is not None and self.slots.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rack.yfilter != YFilter.not_set or
                    (self.slots is not None and self.slots.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rack" + "[rack='" + self.rack.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring/racks/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rack.is_set or self.rack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rack.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "slots"):
                    if (self.slots is None):
                        self.slots = EnvironmentalMonitoring.Racks.Rack.Slots()
                        self.slots.parent = self
                        self._children_name_map["slots"] = "slots"
                    return self.slots

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "slots" or name == "rack"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rack"):
                    self.rack = value
                    self.rack.value_namespace = name_space
                    self.rack.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rack:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rack:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "racks" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rack"):
                for c in self.rack:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EnvironmentalMonitoring.Racks.Rack()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rack.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rack"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.racks is not None and self.racks.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.racks is not None and self.racks.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring" + path_buffer

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

        if (child_yang_name == "racks"):
            if (self.racks is None):
                self.racks = EnvironmentalMonitoring.Racks()
                self.racks.parent = self
                self._children_name_map["racks"] = "racks"
            return self.racks

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "racks"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EnvironmentalMonitoring()
        return self._top_entity

