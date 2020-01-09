""" Cisco_IOS_XR_asr9k_sc_envmon_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-envmon package operational data.

This module contains definitions
for the following management objects\:
  environmental\-monitoring\-cli\: Environmental Monitoring
    Operational data space
  environmental\-monitoring\: environmental monitoring

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class EnvironmentalMonitoringCli(_Entity_):
    """
    Environmental Monitoring Operational data space
    
    .. attribute:: rack_clis
    
    	Table of racks
    	**type**\:  :py:class:`RackClis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis>`
    
    	**config**\: False
    
    

    """

    _prefix = 'asr9k-sc-envmon-oper'
    _revision = '2017-01-19'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(EnvironmentalMonitoringCli, self).__init__()
        self._top_entity = None

        self.yang_name = "environmental-monitoring-cli"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-sc-envmon-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("rack-clis", ("rack_clis", EnvironmentalMonitoringCli.RackClis))])
        self._leafs = OrderedDict()

        self.rack_clis = EnvironmentalMonitoringCli.RackClis()
        self.rack_clis.parent = self
        self._children_name_map["rack_clis"] = "rack-clis"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring-cli"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EnvironmentalMonitoringCli, [], name, value)


    class RackClis(_Entity_):
        """
        Table of racks
        
        .. attribute:: rack_cli
        
        	Number
        	**type**\: list of  		 :py:class:`RackCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli>`
        
        	**config**\: False
        
        

        """

        _prefix = 'asr9k-sc-envmon-oper'
        _revision = '2017-01-19'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(EnvironmentalMonitoringCli.RackClis, self).__init__()

            self.yang_name = "rack-clis"
            self.yang_parent_name = "environmental-monitoring-cli"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack-cli", ("rack_cli", EnvironmentalMonitoringCli.RackClis.RackCli))])
            self._leafs = OrderedDict()

            self.rack_cli = YList(self)
            self._segment_path = lambda: "rack-clis"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring-cli/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EnvironmentalMonitoringCli.RackClis, [], name, value)


        class RackCli(_Entity_):
            """
            Number
            
            .. attribute:: rack  (key)
            
            	Rack number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: slot_clis
            
            	Table of slots
            	**type**\:  :py:class:`SlotClis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis>`
            
            	**config**\: False
            
            

            """

            _prefix = 'asr9k-sc-envmon-oper'
            _revision = '2017-01-19'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(EnvironmentalMonitoringCli.RackClis.RackCli, self).__init__()

                self.yang_name = "rack-cli"
                self.yang_parent_name = "rack-clis"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rack']
                self._child_classes = OrderedDict([("slot-clis", ("slot_clis", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis))])
                self._leafs = OrderedDict([
                    ('rack', (YLeaf(YType.uint32, 'rack'), ['int'])),
                ])
                self.rack = None

                self.slot_clis = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis()
                self.slot_clis.parent = self
                self._children_name_map["slot_clis"] = "slot-clis"
                self._segment_path = lambda: "rack-cli" + "[rack='" + str(self.rack) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring-cli/rack-clis/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli, ['rack'], name, value)


            class SlotClis(_Entity_):
                """
                Table of slots
                
                .. attribute:: slot_cli
                
                	Name
                	**type**\: list of  		 :py:class:`SlotCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli>`
                
                	**config**\: False
                
                

                """

                _prefix = 'asr9k-sc-envmon-oper'
                _revision = '2017-01-19'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis, self).__init__()

                    self.yang_name = "slot-clis"
                    self.yang_parent_name = "rack-cli"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slot-cli", ("slot_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli))])
                    self._leafs = OrderedDict()

                    self.slot_cli = YList(self)
                    self._segment_path = lambda: "slot-clis"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis, [], name, value)


                class SlotCli(_Entity_):
                    """
                    Name
                    
                    .. attribute:: slot  (key)
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: module_clis
                    
                    	Table of modules
                    	**type**\:  :py:class:`ModuleClis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'asr9k-sc-envmon-oper'
                    _revision = '2017-01-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli, self).__init__()

                        self.yang_name = "slot-cli"
                        self.yang_parent_name = "slot-clis"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['slot']
                        self._child_classes = OrderedDict([("module-clis", ("module_clis", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis))])
                        self._leafs = OrderedDict([
                            ('slot', (YLeaf(YType.str, 'slot'), ['str'])),
                        ])
                        self.slot = None

                        self.module_clis = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis()
                        self.module_clis.parent = self
                        self._children_name_map["module_clis"] = "module-clis"
                        self._segment_path = lambda: "slot-cli" + "[slot='" + str(self.slot) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli, ['slot'], name, value)


                    class ModuleClis(_Entity_):
                        """
                        Table of modules
                        
                        .. attribute:: module_cli
                        
                        	Name
                        	**type**\: list of  		 :py:class:`ModuleCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-sc-envmon-oper'
                        _revision = '2017-01-19'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis, self).__init__()

                            self.yang_name = "module-clis"
                            self.yang_parent_name = "slot-cli"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("module-cli", ("module_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli))])
                            self._leafs = OrderedDict()

                            self.module_cli = YList(self)
                            self._segment_path = lambda: "module-clis"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis, [], name, value)


                        class ModuleCli(_Entity_):
                            """
                            Name
                            
                            .. attribute:: module  (key)
                            
                            	Module name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: sensor_type_clis
                            
                            	Table of sensor types
                            	**type**\:  :py:class:`SensorTypeClis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis>`
                            
                            	**config**\: False
                            
                            .. attribute:: power_cli
                            
                            	Module Power Draw
                            	**type**\:  :py:class:`PowerCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-sc-envmon-oper'
                            _revision = '2017-01-19'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli, self).__init__()

                                self.yang_name = "module-cli"
                                self.yang_parent_name = "module-clis"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['module']
                                self._child_classes = OrderedDict([("sensor-type-clis", ("sensor_type_clis", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis)), ("power-cli", ("power_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli))])
                                self._leafs = OrderedDict([
                                    ('module', (YLeaf(YType.str, 'module'), ['str'])),
                                ])
                                self.module = None

                                self.sensor_type_clis = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis()
                                self.sensor_type_clis.parent = self
                                self._children_name_map["sensor_type_clis"] = "sensor-type-clis"

                                self.power_cli = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli()
                                self.power_cli.parent = self
                                self._children_name_map["power_cli"] = "power-cli"
                                self._segment_path = lambda: "module-cli" + "[module='" + str(self.module) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli, ['module'], name, value)


                            class SensorTypeClis(_Entity_):
                                """
                                Table of sensor types
                                
                                .. attribute:: sensor_type_cli
                                
                                	Type of sensor
                                	**type**\: list of  		 :py:class:`SensorTypeCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-envmon-oper'
                                _revision = '2017-01-19'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis, self).__init__()

                                    self.yang_name = "sensor-type-clis"
                                    self.yang_parent_name = "module-cli"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("sensor-type-cli", ("sensor_type_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli))])
                                    self._leafs = OrderedDict()

                                    self.sensor_type_cli = YList(self)
                                    self._segment_path = lambda: "sensor-type-clis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis, [], name, value)


                                class SensorTypeCli(_Entity_):
                                    """
                                    Type of sensor
                                    
                                    .. attribute:: type  (key)
                                    
                                    	Sensor type
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sensor_name_clis
                                    
                                    	Table of sensors
                                    	**type**\:  :py:class:`SensorNameClis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-envmon-oper'
                                    _revision = '2017-01-19'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli, self).__init__()

                                        self.yang_name = "sensor-type-cli"
                                        self.yang_parent_name = "sensor-type-clis"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['type']
                                        self._child_classes = OrderedDict([("sensor-name-clis", ("sensor_name_clis", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                        ])
                                        self.type = None

                                        self.sensor_name_clis = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis()
                                        self.sensor_name_clis.parent = self
                                        self._children_name_map["sensor_name_clis"] = "sensor-name-clis"
                                        self._segment_path = lambda: "sensor-type-cli" + "[type='" + str(self.type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli, ['type'], name, value)


                                    class SensorNameClis(_Entity_):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor_name_cli
                                        
                                        	Name of sensor
                                        	**type**\: list of  		 :py:class:`SensorNameCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-envmon-oper'
                                        _revision = '2017-01-19'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis, self).__init__()

                                            self.yang_name = "sensor-name-clis"
                                            self.yang_parent_name = "sensor-type-cli"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("sensor-name-cli", ("sensor_name_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli))])
                                            self._leafs = OrderedDict()

                                            self.sensor_name_cli = YList(self)
                                            self._segment_path = lambda: "sensor-name-clis"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis, [], name, value)


                                        class SensorNameCli(_Entity_):
                                            """
                                            Name of sensor
                                            
                                            .. attribute:: name  (key)
                                            
                                            	Sensor name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: value_detailed_cli
                                            
                                            	Detailed sensor information including the sensor value
                                            	**type**\:  :py:class:`ValueDetailedCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ValueDetailedCli>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: threshold_clis
                                            
                                            	The threshold information
                                            	**type**\:  :py:class:`ThresholdClis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: value_brief_cli
                                            
                                            	The sensor value
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-envmon-oper'
                                            _revision = '2017-01-19'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli, self).__init__()

                                                self.yang_name = "sensor-name-cli"
                                                self.yang_parent_name = "sensor-name-clis"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['name']
                                                self._child_classes = OrderedDict([("value-detailed-cli", ("value_detailed_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ValueDetailedCli)), ("threshold-clis", ("threshold_clis", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis))])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('value_brief_cli', (YLeaf(YType.str, 'value-brief-cli'), ['str'])),
                                                ])
                                                self.name = None
                                                self.value_brief_cli = None

                                                self.value_detailed_cli = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ValueDetailedCli()
                                                self.value_detailed_cli.parent = self
                                                self._children_name_map["value_detailed_cli"] = "value-detailed-cli"

                                                self.threshold_clis = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis()
                                                self.threshold_clis.parent = self
                                                self._children_name_map["threshold_clis"] = "threshold-clis"
                                                self._segment_path = lambda: "sensor-name-cli" + "[name='" + str(self.name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli, ['name', 'value_brief_cli'], name, value)


                                            class ValueDetailedCli(_Entity_):
                                                """
                                                Detailed sensor information including
                                                the sensor value
                                                
                                                .. attribute:: field_validity_bitmap
                                                
                                                	Sensor valid bitmap
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: device_description
                                                
                                                	Device Name
                                                	**type**\: str
                                                
                                                	**length:** 0..50
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: units
                                                
                                                	Units of variable being read
                                                	**type**\: str
                                                
                                                	**length:** 0..50
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: device_id
                                                
                                                	Identifier for this device
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: value
                                                
                                                	Current reading of sensor
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: alarm_type
                                                
                                                	Indicates threshold violation
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: data_type
                                                
                                                	Sensor data type enums
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: scale
                                                
                                                	Sensor scale enums
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: precision
                                                
                                                	Sensor precision range
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: status
                                                
                                                	Sensor operation state enums
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: age_time_stamp
                                                
                                                	Age of the sensor value; set to the current time if directly access the value from sensor
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: update_rate
                                                
                                                	Sensor value update rate;set to 0 if sensor value is updated and evaluated immediately
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: average
                                                
                                                	Average sensor value over time interval
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: minimum
                                                
                                                	Minimum Sensor value over time interval
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: maximum
                                                
                                                	Maximum Sensor value over time interval
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: interval
                                                
                                                	Time Interval over which sensor value is monitored
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-envmon-oper'
                                                _revision = '2017-01-19'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ValueDetailedCli, self).__init__()

                                                    self.yang_name = "value-detailed-cli"
                                                    self.yang_parent_name = "sensor-name-cli"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('field_validity_bitmap', (YLeaf(YType.uint32, 'field-validity-bitmap'), ['int'])),
                                                        ('device_description', (YLeaf(YType.str, 'device-description'), ['str'])),
                                                        ('units', (YLeaf(YType.str, 'units'), ['str'])),
                                                        ('device_id', (YLeaf(YType.uint32, 'device-id'), ['int'])),
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('alarm_type', (YLeaf(YType.uint32, 'alarm-type'), ['int'])),
                                                        ('data_type', (YLeaf(YType.uint32, 'data-type'), ['int'])),
                                                        ('scale', (YLeaf(YType.uint32, 'scale'), ['int'])),
                                                        ('precision', (YLeaf(YType.uint32, 'precision'), ['int'])),
                                                        ('status', (YLeaf(YType.uint32, 'status'), ['int'])),
                                                        ('age_time_stamp', (YLeaf(YType.uint32, 'age-time-stamp'), ['int'])),
                                                        ('update_rate', (YLeaf(YType.uint32, 'update-rate'), ['int'])),
                                                        ('average', (YLeaf(YType.int32, 'average'), ['int'])),
                                                        ('minimum', (YLeaf(YType.int32, 'minimum'), ['int'])),
                                                        ('maximum', (YLeaf(YType.int32, 'maximum'), ['int'])),
                                                        ('interval', (YLeaf(YType.int32, 'interval'), ['int'])),
                                                    ])
                                                    self.field_validity_bitmap = None
                                                    self.device_description = None
                                                    self.units = None
                                                    self.device_id = None
                                                    self.value = None
                                                    self.alarm_type = None
                                                    self.data_type = None
                                                    self.scale = None
                                                    self.precision = None
                                                    self.status = None
                                                    self.age_time_stamp = None
                                                    self.update_rate = None
                                                    self.average = None
                                                    self.minimum = None
                                                    self.maximum = None
                                                    self.interval = None
                                                    self._segment_path = lambda: "value-detailed-cli"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ValueDetailedCli, ['field_validity_bitmap', 'device_description', 'units', 'device_id', 'value', 'alarm_type', 'data_type', 'scale', 'precision', 'status', 'age_time_stamp', 'update_rate', 'average', 'minimum', 'maximum', 'interval'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                    return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ValueDetailedCli']['meta_info']


                                            class ThresholdClis(_Entity_):
                                                """
                                                The threshold information
                                                
                                                .. attribute:: threshold_cli
                                                
                                                	Types of thresholds
                                                	**type**\: list of  		 :py:class:`ThresholdCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-envmon-oper'
                                                _revision = '2017-01-19'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis, self).__init__()

                                                    self.yang_name = "threshold-clis"
                                                    self.yang_parent_name = "sensor-name-cli"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("threshold-cli", ("threshold_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli))])
                                                    self._leafs = OrderedDict()

                                                    self.threshold_cli = YList(self)
                                                    self._segment_path = lambda: "threshold-clis"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis, [], name, value)


                                                class ThresholdCli(_Entity_):
                                                    """
                                                    Types of thresholds
                                                    
                                                    .. attribute:: type  (key)
                                                    
                                                    	Threshold type
                                                    	**type**\: str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: value_detailed_cli
                                                    
                                                    	Detailed sensor threshold information
                                                    	**type**\:  :py:class:`ValueDetailedCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli.ValueDetailedCli>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: trap_cli
                                                    
                                                    	Threshold trap enable flag true\-ENABLE, false\-DISABLE
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: value_brief_cli
                                                    
                                                    	Threshold value for the sensor
                                                    	**type**\: str
                                                    
                                                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-envmon-oper'
                                                    _revision = '2017-01-19'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli, self).__init__()

                                                        self.yang_name = "threshold-cli"
                                                        self.yang_parent_name = "threshold-clis"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['type']
                                                        self._child_classes = OrderedDict([("value-detailed-cli", ("value_detailed_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli.ValueDetailedCli))])
                                                        self._leafs = OrderedDict([
                                                            ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                                            ('trap_cli', (YLeaf(YType.boolean, 'trap-cli'), ['bool'])),
                                                            ('value_brief_cli', (YLeaf(YType.str, 'value-brief-cli'), ['str'])),
                                                        ])
                                                        self.type = None
                                                        self.trap_cli = None
                                                        self.value_brief_cli = None

                                                        self.value_detailed_cli = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli.ValueDetailedCli()
                                                        self.value_detailed_cli.parent = self
                                                        self._children_name_map["value_detailed_cli"] = "value-detailed-cli"
                                                        self._segment_path = lambda: "threshold-cli" + "[type='" + str(self.type) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli, ['type', 'trap_cli', 'value_brief_cli'], name, value)


                                                    class ValueDetailedCli(_Entity_):
                                                        """
                                                        Detailed sensor threshold
                                                        information
                                                        
                                                        .. attribute:: threshold_severity
                                                        
                                                        	Indicates minor, major, critical severities
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: threshold_relation
                                                        
                                                        	Indicates relation between sensor value and threshold
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: threshold_value
                                                        
                                                        	Value of the configured threshold
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: threshold_evaluation
                                                        
                                                        	Indicates the result of the most recent evaluation of the thresholD
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: threshold_notification_enabled
                                                        
                                                        	Indicates whether or not a notification should result, in case of threshold violation
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-envmon-oper'
                                                        _revision = '2017-01-19'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli.ValueDetailedCli, self).__init__()

                                                            self.yang_name = "value-detailed-cli"
                                                            self.yang_parent_name = "threshold-cli"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('threshold_severity', (YLeaf(YType.uint32, 'threshold-severity'), ['int'])),
                                                                ('threshold_relation', (YLeaf(YType.uint32, 'threshold-relation'), ['int'])),
                                                                ('threshold_value', (YLeaf(YType.uint32, 'threshold-value'), ['int'])),
                                                                ('threshold_evaluation', (YLeaf(YType.boolean, 'threshold-evaluation'), ['bool'])),
                                                                ('threshold_notification_enabled', (YLeaf(YType.boolean, 'threshold-notification-enabled'), ['bool'])),
                                                            ])
                                                            self.threshold_severity = None
                                                            self.threshold_relation = None
                                                            self.threshold_value = None
                                                            self.threshold_evaluation = None
                                                            self.threshold_notification_enabled = None
                                                            self._segment_path = lambda: "value-detailed-cli"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli.ValueDetailedCli, ['threshold_severity', 'threshold_relation', 'threshold_value', 'threshold_evaluation', 'threshold_notification_enabled'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                            return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli.ValueDetailedCli']['meta_info']

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                        return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis.ThresholdCli']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                    return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli.ThresholdClis']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis.SensorNameCli']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                            return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli.SensorNameClis']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                        return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis.SensorTypeCli']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                    return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.SensorTypeClis']['meta_info']


                            class PowerCli(_Entity_):
                                """
                                Module Power Draw
                                
                                .. attribute:: power_bag_cli
                                
                                	Detailed power bag information
                                	**type**\:  :py:class:`PowerBagCli <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli.PowerBagCli>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-envmon-oper'
                                _revision = '2017-01-19'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli, self).__init__()

                                    self.yang_name = "power-cli"
                                    self.yang_parent_name = "module-cli"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("power-bag-cli", ("power_bag_cli", EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli.PowerBagCli))])
                                    self._leafs = OrderedDict()

                                    self.power_bag_cli = EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli.PowerBagCli()
                                    self.power_bag_cli.parent = self
                                    self._children_name_map["power_bag_cli"] = "power-bag-cli"
                                    self._segment_path = lambda: "power-cli"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli, [], name, value)


                                class PowerBagCli(_Entity_):
                                    """
                                    Detailed power bag information
                                    
                                    .. attribute:: power_value
                                    
                                    	Current Power Value of the Unit
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_max_value
                                    
                                    	Max Power Value of the Unit
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_unit_multiplier
                                    
                                    	Unit Multiplier of Power
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_accuracy
                                    
                                    	Accuracy of the Power Value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_measure_caliber
                                    
                                    	Measure Caliber
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_current_type
                                    
                                    	Current Type of the Unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_origin
                                    
                                    	The Power Origin of the Unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_admin_state
                                    
                                    	Admin Status of the Unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_oper_state
                                    
                                    	Oper Status of the Unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_state_enter_reason
                                    
                                    	Enter Reason for the State
                                    	**type**\: str
                                    
                                    	**length:** 0..50
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-envmon-oper'
                                    _revision = '2017-01-19'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli.PowerBagCli, self).__init__()

                                        self.yang_name = "power-bag-cli"
                                        self.yang_parent_name = "power-cli"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('power_value', (YLeaf(YType.int32, 'power-value'), ['int'])),
                                            ('power_max_value', (YLeaf(YType.int32, 'power-max-value'), ['int'])),
                                            ('power_unit_multiplier', (YLeaf(YType.uint32, 'power-unit-multiplier'), ['int'])),
                                            ('power_accuracy', (YLeaf(YType.uint32, 'power-accuracy'), ['int'])),
                                            ('power_measure_caliber', (YLeaf(YType.uint32, 'power-measure-caliber'), ['int'])),
                                            ('power_current_type', (YLeaf(YType.uint32, 'power-current-type'), ['int'])),
                                            ('power_origin', (YLeaf(YType.uint32, 'power-origin'), ['int'])),
                                            ('power_admin_state', (YLeaf(YType.uint32, 'power-admin-state'), ['int'])),
                                            ('power_oper_state', (YLeaf(YType.uint32, 'power-oper-state'), ['int'])),
                                            ('power_state_enter_reason', (YLeaf(YType.str, 'power-state-enter-reason'), ['str'])),
                                        ])
                                        self.power_value = None
                                        self.power_max_value = None
                                        self.power_unit_multiplier = None
                                        self.power_accuracy = None
                                        self.power_measure_caliber = None
                                        self.power_current_type = None
                                        self.power_origin = None
                                        self.power_admin_state = None
                                        self.power_oper_state = None
                                        self.power_state_enter_reason = None
                                        self._segment_path = lambda: "power-bag-cli"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli.PowerBagCli, ['power_value', 'power_max_value', 'power_unit_multiplier', 'power_accuracy', 'power_measure_caliber', 'power_current_type', 'power_origin', 'power_admin_state', 'power_oper_state', 'power_state_enter_reason'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                        return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli.PowerBagCli']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                    return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli.PowerCli']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis.ModuleCli']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                            return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli.ModuleClis']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                        return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis.SlotCli']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                    return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli.SlotClis']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                return meta._meta_table['EnvironmentalMonitoringCli.RackClis.RackCli']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
            return meta._meta_table['EnvironmentalMonitoringCli.RackClis']['meta_info']

    def clone_ptr(self):
        self._top_entity = EnvironmentalMonitoringCli()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
        return meta._meta_table['EnvironmentalMonitoringCli']['meta_info']


class EnvironmentalMonitoring(_Entity_):
    """
    environmental monitoring
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks>`
    
    	**config**\: False
    
    

    """

    _prefix = 'asr9k-sc-envmon-oper'
    _revision = '2017-01-19'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(EnvironmentalMonitoring, self).__init__()
        self._top_entity = None

        self.yang_name = "environmental-monitoring"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-sc-envmon-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("racks", ("racks", EnvironmentalMonitoring.Racks))])
        self._leafs = OrderedDict()

        self.racks = EnvironmentalMonitoring.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(EnvironmentalMonitoring, [], name, value)


    class Racks(_Entity_):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Number
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack>`
        
        	**config**\: False
        
        

        """

        _prefix = 'asr9k-sc-envmon-oper'
        _revision = '2017-01-19'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(EnvironmentalMonitoring.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "environmental-monitoring"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack", ("rack", EnvironmentalMonitoring.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(EnvironmentalMonitoring.Racks, [], name, value)


        class Rack(_Entity_):
            """
            Number
            
            .. attribute:: rack  (key)
            
            	Rack number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots>`
            
            	**config**\: False
            
            

            """

            _prefix = 'asr9k-sc-envmon-oper'
            _revision = '2017-01-19'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(EnvironmentalMonitoring.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rack']
                self._child_classes = OrderedDict([("slots", ("slots", EnvironmentalMonitoring.Racks.Rack.Slots))])
                self._leafs = OrderedDict([
                    ('rack', (YLeaf(YType.uint32, 'rack'), ['int'])),
                ])
                self.rack = None

                self.slots = EnvironmentalMonitoring.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._segment_path = lambda: "rack" + "[rack='" + str(self.rack) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-envmon-oper:environmental-monitoring/racks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(EnvironmentalMonitoring.Racks.Rack, ['rack'], name, value)


            class Slots(_Entity_):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Name
                	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot>`
                
                	**config**\: False
                
                

                """

                _prefix = 'asr9k-sc-envmon-oper'
                _revision = '2017-01-19'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(EnvironmentalMonitoring.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slot", ("slot", EnvironmentalMonitoring.Racks.Rack.Slots.Slot))])
                    self._leafs = OrderedDict()

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots, [], name, value)


                class Slot(_Entity_):
                    """
                    Name
                    
                    .. attribute:: slot  (key)
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: modules
                    
                    	Table of modules
                    	**type**\:  :py:class:`Modules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'asr9k-sc-envmon-oper'
                    _revision = '2017-01-19'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['slot']
                        self._child_classes = OrderedDict([("modules", ("modules", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules))])
                        self._leafs = OrderedDict([
                            ('slot', (YLeaf(YType.str, 'slot'), ['str'])),
                        ])
                        self.slot = None

                        self.modules = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules()
                        self.modules.parent = self
                        self._children_name_map["modules"] = "modules"
                        self._segment_path = lambda: "slot" + "[slot='" + str(self.slot) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot, ['slot'], name, value)


                    class Modules(_Entity_):
                        """
                        Table of modules
                        
                        .. attribute:: module
                        
                        	Name
                        	**type**\: list of  		 :py:class:`Module <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-sc-envmon-oper'
                        _revision = '2017-01-19'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules, self).__init__()

                            self.yang_name = "modules"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("module", ("module", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module))])
                            self._leafs = OrderedDict()

                            self.module = YList(self)
                            self._segment_path = lambda: "modules"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules, [], name, value)


                        class Module(_Entity_):
                            """
                            Name
                            
                            .. attribute:: module  (key)
                            
                            	Module name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            	**config**\: False
                            
                            .. attribute:: power
                            
                            	Module Power Draw
                            	**type**\:  :py:class:`Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power>`
                            
                            	**config**\: False
                            
                            .. attribute:: sensor_types
                            
                            	Table of sensor types
                            	**type**\:  :py:class:`SensorTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-sc-envmon-oper'
                            _revision = '2017-01-19'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module, self).__init__()

                                self.yang_name = "module"
                                self.yang_parent_name = "modules"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['module']
                                self._child_classes = OrderedDict([("power", ("power", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power)), ("sensor-types", ("sensor_types", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes))])
                                self._leafs = OrderedDict([
                                    ('module', (YLeaf(YType.str, 'module'), ['str'])),
                                ])
                                self.module = None

                                self.power = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power()
                                self.power.parent = self
                                self._children_name_map["power"] = "power"

                                self.sensor_types = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes()
                                self.sensor_types.parent = self
                                self._children_name_map["sensor_types"] = "sensor-types"
                                self._segment_path = lambda: "module" + "[module='" + str(self.module) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module, ['module'], name, value)


                            class Power(_Entity_):
                                """
                                Module Power Draw
                                
                                .. attribute:: power_bag
                                
                                	Detailed power bag information
                                	**type**\:  :py:class:`PowerBag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-envmon-oper'
                                _revision = '2017-01-19'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power, self).__init__()

                                    self.yang_name = "power"
                                    self.yang_parent_name = "module"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("power-bag", ("power_bag", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag))])
                                    self._leafs = OrderedDict()

                                    self.power_bag = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag()
                                    self.power_bag.parent = self
                                    self._children_name_map["power_bag"] = "power-bag"
                                    self._segment_path = lambda: "power"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power, [], name, value)


                                class PowerBag(_Entity_):
                                    """
                                    Detailed power bag information
                                    
                                    .. attribute:: power_value
                                    
                                    	Current Power Value of the Unit
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_max_value
                                    
                                    	Max Power Value of the Unit
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_unit_multiplier
                                    
                                    	Unit Multiplier of Power
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_accuracy
                                    
                                    	Accuracy of the Power Value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_measure_caliber
                                    
                                    	Measure Caliber
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_current_type
                                    
                                    	Current Type of the Unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_origin
                                    
                                    	The Power Origin of the Unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_admin_state
                                    
                                    	Admin Status of the Unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_oper_state
                                    
                                    	Oper Status of the Unit
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: power_state_enter_reason
                                    
                                    	Enter Reason for the State
                                    	**type**\: str
                                    
                                    	**length:** 0..50
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-envmon-oper'
                                    _revision = '2017-01-19'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag, self).__init__()

                                        self.yang_name = "power-bag"
                                        self.yang_parent_name = "power"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('power_value', (YLeaf(YType.int32, 'power-value'), ['int'])),
                                            ('power_max_value', (YLeaf(YType.int32, 'power-max-value'), ['int'])),
                                            ('power_unit_multiplier', (YLeaf(YType.uint32, 'power-unit-multiplier'), ['int'])),
                                            ('power_accuracy', (YLeaf(YType.uint32, 'power-accuracy'), ['int'])),
                                            ('power_measure_caliber', (YLeaf(YType.uint32, 'power-measure-caliber'), ['int'])),
                                            ('power_current_type', (YLeaf(YType.uint32, 'power-current-type'), ['int'])),
                                            ('power_origin', (YLeaf(YType.uint32, 'power-origin'), ['int'])),
                                            ('power_admin_state', (YLeaf(YType.uint32, 'power-admin-state'), ['int'])),
                                            ('power_oper_state', (YLeaf(YType.uint32, 'power-oper-state'), ['int'])),
                                            ('power_state_enter_reason', (YLeaf(YType.str, 'power-state-enter-reason'), ['str'])),
                                        ])
                                        self.power_value = None
                                        self.power_max_value = None
                                        self.power_unit_multiplier = None
                                        self.power_accuracy = None
                                        self.power_measure_caliber = None
                                        self.power_current_type = None
                                        self.power_origin = None
                                        self.power_admin_state = None
                                        self.power_oper_state = None
                                        self.power_state_enter_reason = None
                                        self._segment_path = lambda: "power-bag"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag, ['power_value', 'power_max_value', 'power_unit_multiplier', 'power_accuracy', 'power_measure_caliber', 'power_current_type', 'power_origin', 'power_admin_state', 'power_oper_state', 'power_state_enter_reason'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                        return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power']['meta_info']


                            class SensorTypes(_Entity_):
                                """
                                Table of sensor types
                                
                                .. attribute:: sensor_type
                                
                                	Type of sensor
                                	**type**\: list of  		 :py:class:`SensorType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-envmon-oper'
                                _revision = '2017-01-19'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes, self).__init__()

                                    self.yang_name = "sensor-types"
                                    self.yang_parent_name = "module"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("sensor-type", ("sensor_type", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType))])
                                    self._leafs = OrderedDict()

                                    self.sensor_type = YList(self)
                                    self._segment_path = lambda: "sensor-types"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes, [], name, value)


                                class SensorType(_Entity_):
                                    """
                                    Type of sensor
                                    
                                    .. attribute:: type  (key)
                                    
                                    	Sensor type
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sensor_names
                                    
                                    	Table of sensors
                                    	**type**\:  :py:class:`SensorNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-envmon-oper'
                                    _revision = '2017-01-19'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType, self).__init__()

                                        self.yang_name = "sensor-type"
                                        self.yang_parent_name = "sensor-types"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['type']
                                        self._child_classes = OrderedDict([("sensor-names", ("sensor_names", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                        ])
                                        self.type = None

                                        self.sensor_names = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames()
                                        self.sensor_names.parent = self
                                        self._children_name_map["sensor_names"] = "sensor-names"
                                        self._segment_path = lambda: "sensor-type" + "[type='" + str(self.type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType, ['type'], name, value)


                                    class SensorNames(_Entity_):
                                        """
                                        Table of sensors
                                        
                                        .. attribute:: sensor_name
                                        
                                        	Name of sensor
                                        	**type**\: list of  		 :py:class:`SensorName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-envmon-oper'
                                        _revision = '2017-01-19'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames, self).__init__()

                                            self.yang_name = "sensor-names"
                                            self.yang_parent_name = "sensor-type"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("sensor-name", ("sensor_name", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName))])
                                            self._leafs = OrderedDict()

                                            self.sensor_name = YList(self)
                                            self._segment_path = lambda: "sensor-names"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames, [], name, value)


                                        class SensorName(_Entity_):
                                            """
                                            Name of sensor
                                            
                                            .. attribute:: name  (key)
                                            
                                            	Sensor name
                                            	**type**\: str
                                            
                                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: thresholds
                                            
                                            	The threshold information
                                            	**type**\:  :py:class:`Thresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: value_detailed
                                            
                                            	Detailed sensor information including the sensor value
                                            	**type**\:  :py:class:`ValueDetailed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: value_brief
                                            
                                            	The sensor value
                                            	**type**\: str
                                            
                                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-envmon-oper'
                                            _revision = '2017-01-19'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName, self).__init__()

                                                self.yang_name = "sensor-name"
                                                self.yang_parent_name = "sensor-names"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['name']
                                                self._child_classes = OrderedDict([("thresholds", ("thresholds", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds)), ("value-detailed", ("value_detailed", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed))])
                                                self._leafs = OrderedDict([
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('value_brief', (YLeaf(YType.str, 'value-brief'), ['str'])),
                                                ])
                                                self.name = None
                                                self.value_brief = None

                                                self.thresholds = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds()
                                                self.thresholds.parent = self
                                                self._children_name_map["thresholds"] = "thresholds"

                                                self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed()
                                                self.value_detailed.parent = self
                                                self._children_name_map["value_detailed"] = "value-detailed"
                                                self._segment_path = lambda: "sensor-name" + "[name='" + str(self.name) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName, ['name', 'value_brief'], name, value)


                                            class Thresholds(_Entity_):
                                                """
                                                The threshold information
                                                
                                                .. attribute:: threshold
                                                
                                                	Types of thresholds
                                                	**type**\: list of  		 :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-envmon-oper'
                                                _revision = '2017-01-19'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds, self).__init__()

                                                    self.yang_name = "thresholds"
                                                    self.yang_parent_name = "sensor-name"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("threshold", ("threshold", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold))])
                                                    self._leafs = OrderedDict()

                                                    self.threshold = YList(self)
                                                    self._segment_path = lambda: "thresholds"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds, [], name, value)


                                                class Threshold(_Entity_):
                                                    """
                                                    Types of thresholds
                                                    
                                                    .. attribute:: type  (key)
                                                    
                                                    	Threshold type
                                                    	**type**\: str
                                                    
                                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: value_detailed
                                                    
                                                    	Detailed sensor threshold information
                                                    	**type**\:  :py:class:`ValueDetailed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_oper.EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: trap
                                                    
                                                    	Threshold trap enable flag true\-ENABLE, false\-DISABLE
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: value_brief
                                                    
                                                    	Threshold value for the sensor
                                                    	**type**\: str
                                                    
                                                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-envmon-oper'
                                                    _revision = '2017-01-19'

                                                    def __init__(self):
                                                        if sys.version_info > (3,):
                                                            super().__init__()
                                                        else:
                                                            super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold, self).__init__()

                                                        self.yang_name = "threshold"
                                                        self.yang_parent_name = "thresholds"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['type']
                                                        self._child_classes = OrderedDict([("value-detailed", ("value_detailed", EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed))])
                                                        self._leafs = OrderedDict([
                                                            ('type', (YLeaf(YType.str, 'type'), ['str'])),
                                                            ('trap', (YLeaf(YType.boolean, 'trap'), ['bool'])),
                                                            ('value_brief', (YLeaf(YType.str, 'value-brief'), ['str'])),
                                                        ])
                                                        self.type = None
                                                        self.trap = None
                                                        self.value_brief = None

                                                        self.value_detailed = EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed()
                                                        self.value_detailed.parent = self
                                                        self._children_name_map["value_detailed"] = "value-detailed"
                                                        self._segment_path = lambda: "threshold" + "[type='" + str(self.type) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold, ['type', 'trap', 'value_brief'], name, value)


                                                    class ValueDetailed(_Entity_):
                                                        """
                                                        Detailed sensor threshold
                                                        information
                                                        
                                                        .. attribute:: threshold_severity
                                                        
                                                        	Indicates minor, major, critical severities
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: threshold_relation
                                                        
                                                        	Indicates relation between sensor value and threshold
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: threshold_value
                                                        
                                                        	Value of the configured threshold
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: threshold_evaluation
                                                        
                                                        	Indicates the result of the most recent evaluation of the thresholD
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: threshold_notification_enabled
                                                        
                                                        	Indicates whether or not a notification should result, in case of threshold violation
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-envmon-oper'
                                                        _revision = '2017-01-19'

                                                        def __init__(self):
                                                            if sys.version_info > (3,):
                                                                super().__init__()
                                                            else:
                                                                super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed, self).__init__()

                                                            self.yang_name = "value-detailed"
                                                            self.yang_parent_name = "threshold"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('threshold_severity', (YLeaf(YType.uint32, 'threshold-severity'), ['int'])),
                                                                ('threshold_relation', (YLeaf(YType.uint32, 'threshold-relation'), ['int'])),
                                                                ('threshold_value', (YLeaf(YType.uint32, 'threshold-value'), ['int'])),
                                                                ('threshold_evaluation', (YLeaf(YType.boolean, 'threshold-evaluation'), ['bool'])),
                                                                ('threshold_notification_enabled', (YLeaf(YType.boolean, 'threshold-notification-enabled'), ['bool'])),
                                                            ])
                                                            self.threshold_severity = None
                                                            self.threshold_relation = None
                                                            self.threshold_value = None
                                                            self.threshold_evaluation = None
                                                            self.threshold_notification_enabled = None
                                                            self._segment_path = lambda: "value-detailed"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed, ['threshold_severity', 'threshold_relation', 'threshold_value', 'threshold_evaluation', 'threshold_notification_enabled'], name, value)

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                            return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed']['meta_info']

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                        return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold']['meta_info']

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds']['meta_info']


                                            class ValueDetailed(_Entity_):
                                                """
                                                Detailed sensor information including
                                                the sensor value
                                                
                                                .. attribute:: field_validity_bitmap
                                                
                                                	Sensor valid bitmap
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: device_description
                                                
                                                	Device Name
                                                	**type**\: str
                                                
                                                	**length:** 0..50
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: units
                                                
                                                	Units of variable being read
                                                	**type**\: str
                                                
                                                	**length:** 0..50
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: device_id
                                                
                                                	Identifier for this device
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: value
                                                
                                                	Current reading of sensor
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: alarm_type
                                                
                                                	Indicates threshold violation
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: data_type
                                                
                                                	Sensor data type enums
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: scale
                                                
                                                	Sensor scale enums
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: precision
                                                
                                                	Sensor precision range
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: status
                                                
                                                	Sensor operation state enums
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: age_time_stamp
                                                
                                                	Age of the sensor value; set to the current time if directly access the value from sensor
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: update_rate
                                                
                                                	Sensor value update rate;set to 0 if sensor value is updated and evaluated immediately
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: average
                                                
                                                	Average sensor value over time interval
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: minimum
                                                
                                                	Minimum Sensor value over time interval
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: maximum
                                                
                                                	Maximum Sensor value over time interval
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: interval
                                                
                                                	Time Interval over which sensor value is monitored
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-envmon-oper'
                                                _revision = '2017-01-19'

                                                def __init__(self):
                                                    if sys.version_info > (3,):
                                                        super().__init__()
                                                    else:
                                                        super(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed, self).__init__()

                                                    self.yang_name = "value-detailed"
                                                    self.yang_parent_name = "sensor-name"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('field_validity_bitmap', (YLeaf(YType.uint32, 'field-validity-bitmap'), ['int'])),
                                                        ('device_description', (YLeaf(YType.str, 'device-description'), ['str'])),
                                                        ('units', (YLeaf(YType.str, 'units'), ['str'])),
                                                        ('device_id', (YLeaf(YType.uint32, 'device-id'), ['int'])),
                                                        ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                        ('alarm_type', (YLeaf(YType.uint32, 'alarm-type'), ['int'])),
                                                        ('data_type', (YLeaf(YType.uint32, 'data-type'), ['int'])),
                                                        ('scale', (YLeaf(YType.uint32, 'scale'), ['int'])),
                                                        ('precision', (YLeaf(YType.uint32, 'precision'), ['int'])),
                                                        ('status', (YLeaf(YType.uint32, 'status'), ['int'])),
                                                        ('age_time_stamp', (YLeaf(YType.uint32, 'age-time-stamp'), ['int'])),
                                                        ('update_rate', (YLeaf(YType.uint32, 'update-rate'), ['int'])),
                                                        ('average', (YLeaf(YType.int32, 'average'), ['int'])),
                                                        ('minimum', (YLeaf(YType.int32, 'minimum'), ['int'])),
                                                        ('maximum', (YLeaf(YType.int32, 'maximum'), ['int'])),
                                                        ('interval', (YLeaf(YType.int32, 'interval'), ['int'])),
                                                    ])
                                                    self.field_validity_bitmap = None
                                                    self.device_description = None
                                                    self.units = None
                                                    self.device_id = None
                                                    self.value = None
                                                    self.alarm_type = None
                                                    self.data_type = None
                                                    self.scale = None
                                                    self.precision = None
                                                    self.status = None
                                                    self.age_time_stamp = None
                                                    self.update_rate = None
                                                    self.average = None
                                                    self.minimum = None
                                                    self.maximum = None
                                                    self.interval = None
                                                    self._segment_path = lambda: "value-detailed"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed, ['field_validity_bitmap', 'device_description', 'units', 'device_id', 'value', 'alarm_type', 'data_type', 'scale', 'precision', 'status', 'age_time_stamp', 'update_rate', 'average', 'minimum', 'maximum', 'interval'], name, value)

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed']['meta_info']

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                                return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                            return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                        return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                                return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                            return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                        return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                    return meta._meta_table['EnvironmentalMonitoring.Racks.Rack.Slots']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
                return meta._meta_table['EnvironmentalMonitoring.Racks.Rack']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
            return meta._meta_table['EnvironmentalMonitoring.Racks']['meta_info']

    def clone_ptr(self):
        self._top_entity = EnvironmentalMonitoring()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_envmon_oper as meta
        return meta._meta_table['EnvironmentalMonitoring']['meta_info']


