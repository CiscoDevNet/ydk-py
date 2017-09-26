""" Cisco_IOS_XR_asr9k_sc_envmon_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-envmon package operational data.

This module contains definitions
for the following management objects\:
  environmental\-monitoring\: Environmental Monitoring Operational
    data space

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"racks" : ("racks", EnvironmentalMonitoring.Racks)}
        self._child_list_classes = {}

        self.racks = EnvironmentalMonitoring.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rack" : ("rack", EnvironmentalMonitoring.Racks.Rack)}

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EnvironmentalMonitoring.Racks, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"slots" : ("slots", EnvironmentalMonitoring.Racks.Rack.Slots)}
                self._child_list_classes = {}

                self.rack = YLeaf(YType.int32, "rack")

                self.slots = EnvironmentalMonitoring.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._children_yang_names.add("slots")
                self._segment_path = lambda: "rack" + "[rack='" + self.rack.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring/racks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EnvironmentalMonitoring.Racks.Rack, ['rack'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"slot" : ("slot", EnvironmentalMonitoring.Racks.Rack.Slots.Slot)}

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"

                def __setattr__(self, name, value):
                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"modules" : ("modules", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules)}
                        self._child_list_classes = {}

                        self.slot = YLeaf(YType.str, "slot")

                        self.modules = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules()
                        self.modules.parent = self
                        self._children_name_map["modules"] = "modules"
                        self._children_yang_names.add("modules")
                        self._segment_path = lambda: "slot" + "[slot='" + self.slot.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot, ['slot'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"module" : ("module", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module)}

                            self.module = YList(self)
                            self._segment_path = lambda: "modules"

                        def __setattr__(self, name, value):
                            self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"power" : ("power", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power), "sensor-types" : ("sensor_types", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes)}
                                self._child_list_classes = {}

                                self.module = YLeaf(YType.str, "module")

                                self.power = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power()
                                self.power.parent = self
                                self._children_name_map["power"] = "power"
                                self._children_yang_names.add("power")

                                self.sensor_types = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes()
                                self.sensor_types.parent = self
                                self._children_name_map["sensor_types"] = "sensor-types"
                                self._children_yang_names.add("sensor-types")
                                self._segment_path = lambda: "module" + "[module='" + self.module.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module, ['module'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"power-bag" : ("power_bag", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag)}
                                    self._child_list_classes = {}

                                    self.power_bag = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag()
                                    self.power_bag.parent = self
                                    self._children_name_map["power_bag"] = "power-bag"
                                    self._children_yang_names.add("power-bag")
                                    self._segment_path = lambda: "power"


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

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
                                        self._segment_path = lambda: "power-bag"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag, ['power_accuracy', 'power_admin_state', 'power_current_type', 'power_max_value', 'power_measure_caliber', 'power_oper_state', 'power_origin', 'power_state_enter_reason', 'power_unit_multiplier', 'power_value'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"sensor-type" : ("sensor_type", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType)}

                                    self.sensor_type = YList(self)
                                    self._segment_path = lambda: "sensor-types"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes, [], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"sensor-names" : ("sensor_names", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames)}
                                        self._child_list_classes = {}

                                        self.type = YLeaf(YType.str, "type")

                                        self.sensor_names = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames()
                                        self.sensor_names.parent = self
                                        self._children_name_map["sensor_names"] = "sensor-names"
                                        self._children_yang_names.add("sensor-names")
                                        self._segment_path = lambda: "sensor-type" + "[type='" + self.type.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType, ['type'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"sensor-name" : ("sensor_name", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName)}

                                            self.sensor_name = YList(self)
                                            self._segment_path = lambda: "sensor-names"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames, [], name, value)


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
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"thresholds" : ("thresholds", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds), "value-detailed" : ("value_detailed", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed)}
                                                self._child_list_classes = {}

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
                                                self._segment_path = lambda: "sensor-name" + "[name='" + self.name.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName, ['name', 'value_brief'], name, value)


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
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {"threshold" : ("threshold", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold)}

                                                    self.threshold = YList(self)
                                                    self._segment_path = lambda: "thresholds"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds, [], name, value)


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
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {"value-detailed" : ("value_detailed", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed)}
                                                        self._child_list_classes = {}

                                                        self.type = YLeaf(YType.str, "type")

                                                        self.trap = YLeaf(YType.boolean, "trap")

                                                        self.value_brief = YLeaf(YType.int32, "value-brief")

                                                        self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed()
                                                        self.value_detailed.parent = self
                                                        self._children_name_map["value_detailed"] = "value-detailed"
                                                        self._children_yang_names.add("value-detailed")
                                                        self._segment_path = lambda: "threshold" + "[type='" + self.type.get() + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold, ['type', 'trap', 'value_brief'], name, value)


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
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.threshold_evaluation = YLeaf(YType.boolean, "threshold-evaluation")

                                                            self.threshold_notification_enabled = YLeaf(YType.boolean, "threshold-notification-enabled")

                                                            self.threshold_relation = YLeaf(YType.uint32, "threshold-relation")

                                                            self.threshold_severity = YLeaf(YType.uint32, "threshold-severity")

                                                            self.threshold_value = YLeaf(YType.uint32, "threshold-value")
                                                            self._segment_path = lambda: "value-detailed"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed, ['threshold_evaluation', 'threshold_notification_enabled', 'threshold_relation', 'threshold_severity', 'threshold_value'], name, value)


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
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

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
                                                    self._segment_path = lambda: "value-detailed"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed, ['age_time_stamp', 'alarm_type', 'data_type', 'device_description', 'device_id', 'field_validity_bitmap', 'precision', 'scale', 'status', 'units', 'update_rate', 'value'], name, value)

    def clone_ptr(self):
        self._top_entity = EnvironmentalMonitoring()
        return self._top_entity

