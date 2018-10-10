""" Cisco_IOS_XR_sysadmin_envmon_ui 

This module contains definitions
for the Calvados model objects.

This module holds chassis, cards Enviroment data.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Environment(Entity):
    """
    
    
    .. attribute:: oper
    
    	environment operational (show) data
    	**type**\:  :py:class:`Oper <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper>`
    
    .. attribute:: all
    
    	
    	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All>`
    
    .. attribute:: config
    
    	environment configurational data
    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config>`
    
    .. attribute:: trace
    
    	show traceable processes
    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Trace>`
    
    

    """

    _prefix = 'envmon'
    _revision = '2018-02-06'

    def __init__(self):
        super(Environment, self).__init__()
        self._top_entity = None

        self.yang_name = "environment"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-envmon-ui"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("oper", ("oper", Environment.Oper)), ("all", ("all", Environment.All)), ("config", ("config", Environment.Config)), ("trace", ("trace", Environment.Trace))])
        self._leafs = OrderedDict()

        self.oper = Environment.Oper()
        self.oper.parent = self
        self._children_name_map["oper"] = "oper"

        self.all = Environment.All()
        self.all.parent = self
        self._children_name_map["all"] = "all"

        self.config = Environment.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"

        self.trace = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Environment, [], name, value)


    class Oper(Entity):
        """
        environment operational (show) data
        
        .. attribute:: temperatures
        
        	
        	**type**\:  :py:class:`Temperatures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Temperatures>`
        
        .. attribute:: voltages
        
        	
        	**type**\:  :py:class:`Voltages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Voltages>`
        
        .. attribute:: current
        
        	
        	**type**\:  :py:class:`Current <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Current>`
        
        .. attribute:: fan
        
        	
        	**type**\:  :py:class:`Fan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Fan>`
        
        .. attribute:: power
        
        	
        	**type**\:  :py:class:`Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Power>`
        
        .. attribute:: altitude
        
        	
        	**type**\:  :py:class:`Altitude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Altitude>`
        
        

        """

        _prefix = 'envmon'
        _revision = '2018-02-06'

        def __init__(self):
            super(Environment.Oper, self).__init__()

            self.yang_name = "oper"
            self.yang_parent_name = "environment"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("temperatures", ("temperatures", Environment.Oper.Temperatures)), ("voltages", ("voltages", Environment.Oper.Voltages)), ("current", ("current", Environment.Oper.Current)), ("fan", ("fan", Environment.Oper.Fan)), ("power", ("power", Environment.Oper.Power)), ("altitude", ("altitude", Environment.Oper.Altitude))])
            self._leafs = OrderedDict()

            self.temperatures = Environment.Oper.Temperatures()
            self.temperatures.parent = self
            self._children_name_map["temperatures"] = "temperatures"

            self.voltages = Environment.Oper.Voltages()
            self.voltages.parent = self
            self._children_name_map["voltages"] = "voltages"

            self.current = Environment.Oper.Current()
            self.current.parent = self
            self._children_name_map["current"] = "current"

            self.fan = Environment.Oper.Fan()
            self.fan.parent = self
            self._children_name_map["fan"] = "fan"

            self.power = Environment.Oper.Power()
            self.power.parent = self
            self._children_name_map["power"] = "power"

            self.altitude = Environment.Oper.Altitude()
            self.altitude.parent = self
            self._children_name_map["altitude"] = "altitude"
            self._segment_path = lambda: "oper"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Environment.Oper, [], name, value)


        class Temperatures(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Temperatures.Location>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Oper.Temperatures, self).__init__()

                self.yang_name = "temperatures"
                self.yang_parent_name = "oper"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Environment.Oper.Temperatures.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "temperatures"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Oper.Temperatures, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                .. attribute:: loc_header
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: print_header
                
                	
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: sensor_attributes
                
                	
                	**type**\: list of  		 :py:class:`SensorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Temperatures.Location.SensorAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Oper.Temperatures.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "temperatures"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("sensor_attributes", ("sensor_attributes", Environment.Oper.Temperatures.Location.SensorAttributes))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ('loc_header', (YLeaf(YType.uint32, 'loc_header'), ['int'])),
                        ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                    ])
                    self.location = None
                    self.loc_header = None
                    self.print_header = None

                    self.sensor_attributes = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/temperatures/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Oper.Temperatures.Location, ['location', 'loc_header', 'print_header'], name, value)


                class SensorAttributes(Entity):
                    """
                    
                    
                    .. attribute:: sensor  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: sensor_id
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: alarm
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: temperature_value
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: critical_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: major_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: minor_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: minor_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: major_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: critical_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Oper.Temperatures.Location.SensorAttributes, self).__init__()

                        self.yang_name = "sensor_attributes"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensor']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensor', (YLeaf(YType.str, 'sensor'), ['str'])),
                            ('sensor_id', (YLeaf(YType.str, 'sensor_id'), ['str'])),
                            ('alarm', (YLeaf(YType.str, 'alarm'), ['str'])),
                            ('temperature_value', (YLeaf(YType.str, 'temperature_value'), ['str'])),
                            ('value', (YLeaf(YType.int32, 'value'), ['int'])),
                            ('critical_lo', (YLeaf(YType.int32, 'critical_lo'), ['int'])),
                            ('major_lo', (YLeaf(YType.int32, 'major_lo'), ['int'])),
                            ('minor_lo', (YLeaf(YType.int32, 'minor_lo'), ['int'])),
                            ('minor_hi', (YLeaf(YType.int32, 'minor_hi'), ['int'])),
                            ('major_hi', (YLeaf(YType.int32, 'major_hi'), ['int'])),
                            ('critical_hi', (YLeaf(YType.int32, 'critical_hi'), ['int'])),
                        ])
                        self.sensor = None
                        self.sensor_id = None
                        self.alarm = None
                        self.temperature_value = None
                        self.value = None
                        self.critical_lo = None
                        self.major_lo = None
                        self.minor_lo = None
                        self.minor_hi = None
                        self.major_hi = None
                        self.critical_hi = None
                        self._segment_path = lambda: "sensor_attributes" + "[sensor='" + str(self.sensor) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Oper.Temperatures.Location.SensorAttributes, ['sensor', 'sensor_id', 'alarm', 'temperature_value', 'value', 'critical_lo', 'major_lo', 'minor_lo', 'minor_hi', 'major_hi', 'critical_hi'], name, value)


        class Voltages(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Voltages.Location>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Oper.Voltages, self).__init__()

                self.yang_name = "voltages"
                self.yang_parent_name = "oper"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Environment.Oper.Voltages.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "voltages"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Oper.Voltages, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                .. attribute:: print_header
                
                	
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: loc_header
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sensor_attributes
                
                	
                	**type**\: list of  		 :py:class:`SensorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Voltages.Location.SensorAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Oper.Voltages.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "voltages"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("sensor_attributes", ("sensor_attributes", Environment.Oper.Voltages.Location.SensorAttributes))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                        ('loc_header', (YLeaf(YType.uint32, 'loc_header'), ['int'])),
                    ])
                    self.location = None
                    self.print_header = None
                    self.loc_header = None

                    self.sensor_attributes = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/voltages/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Oper.Voltages.Location, ['location', 'print_header', 'loc_header'], name, value)


                class SensorAttributes(Entity):
                    """
                    
                    
                    .. attribute:: sensor  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: sensor_id
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: alarm
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: temperature_value
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: critical_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: major_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: minor_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: minor_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: major_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: critical_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Oper.Voltages.Location.SensorAttributes, self).__init__()

                        self.yang_name = "sensor_attributes"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensor']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensor', (YLeaf(YType.str, 'sensor'), ['str'])),
                            ('sensor_id', (YLeaf(YType.str, 'sensor_id'), ['str'])),
                            ('alarm', (YLeaf(YType.str, 'alarm'), ['str'])),
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ('temperature_value', (YLeaf(YType.int32, 'temperature_value'), ['int'])),
                            ('critical_lo', (YLeaf(YType.int32, 'critical_lo'), ['int'])),
                            ('major_lo', (YLeaf(YType.int32, 'major_lo'), ['int'])),
                            ('minor_lo', (YLeaf(YType.int32, 'minor_lo'), ['int'])),
                            ('minor_hi', (YLeaf(YType.int32, 'minor_hi'), ['int'])),
                            ('major_hi', (YLeaf(YType.int32, 'major_hi'), ['int'])),
                            ('critical_hi', (YLeaf(YType.int32, 'critical_hi'), ['int'])),
                        ])
                        self.sensor = None
                        self.sensor_id = None
                        self.alarm = None
                        self.value = None
                        self.temperature_value = None
                        self.critical_lo = None
                        self.major_lo = None
                        self.minor_lo = None
                        self.minor_hi = None
                        self.major_hi = None
                        self.critical_hi = None
                        self._segment_path = lambda: "sensor_attributes" + "[sensor='" + str(self.sensor) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Oper.Voltages.Location.SensorAttributes, ['sensor', 'sensor_id', 'alarm', 'value', 'temperature_value', 'critical_lo', 'major_lo', 'minor_lo', 'minor_hi', 'major_hi', 'critical_hi'], name, value)


        class Current(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Current.Location>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Oper.Current, self).__init__()

                self.yang_name = "current"
                self.yang_parent_name = "oper"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Environment.Oper.Current.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "current"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Oper.Current, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                .. attribute:: print_header
                
                	
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: loc_header
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sensor_attributes
                
                	
                	**type**\: list of  		 :py:class:`SensorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Current.Location.SensorAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Oper.Current.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "current"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("sensor_attributes", ("sensor_attributes", Environment.Oper.Current.Location.SensorAttributes))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                        ('loc_header', (YLeaf(YType.uint32, 'loc_header'), ['int'])),
                    ])
                    self.location = None
                    self.print_header = None
                    self.loc_header = None

                    self.sensor_attributes = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/current/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Oper.Current.Location, ['location', 'print_header', 'loc_header'], name, value)


                class SensorAttributes(Entity):
                    """
                    
                    
                    .. attribute:: sensor  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: sensor_id
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: alarm
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: temperature_value
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Oper.Current.Location.SensorAttributes, self).__init__()

                        self.yang_name = "sensor_attributes"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensor']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensor', (YLeaf(YType.str, 'sensor'), ['str'])),
                            ('sensor_id', (YLeaf(YType.str, 'sensor_id'), ['str'])),
                            ('alarm', (YLeaf(YType.str, 'alarm'), ['str'])),
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ('temperature_value', (YLeaf(YType.int32, 'temperature_value'), ['int'])),
                        ])
                        self.sensor = None
                        self.sensor_id = None
                        self.alarm = None
                        self.value = None
                        self.temperature_value = None
                        self._segment_path = lambda: "sensor_attributes" + "[sensor='" + str(self.sensor) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Oper.Current.Location.SensorAttributes, ['sensor', 'sensor_id', 'alarm', 'value', 'temperature_value'], name, value)


        class Fan(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Fan.Location>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Oper.Fan, self).__init__()

                self.yang_name = "fan"
                self.yang_parent_name = "oper"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Environment.Oper.Fan.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "fan"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Oper.Fan, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                .. attribute:: print_header
                
                	
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: loc_header
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: fan_attributes
                
                	
                	**type**\: list of  		 :py:class:`FanAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Fan.Location.FanAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Oper.Fan.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "fan"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("fan_attributes", ("fan_attributes", Environment.Oper.Fan.Location.FanAttributes))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                        ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                        ('loc_header', (YLeaf(YType.uint32, 'loc_header'), ['int'])),
                    ])
                    self.location = None
                    self.print_header = None
                    self.loc_header = None

                    self.fan_attributes = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/fan/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Oper.Fan.Location, ['location', 'print_header', 'loc_header'], name, value)


                class FanAttributes(Entity):
                    """
                    
                    
                    .. attribute:: logical_slot  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: print_fan_header
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: fru_pid
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: fans_speed
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: fan_header
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speed_space
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Oper.Fan.Location.FanAttributes, self).__init__()

                        self.yang_name = "fan_attributes"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['logical_slot']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('logical_slot', (YLeaf(YType.str, 'logical_slot'), ['str'])),
                            ('print_fan_header', (YLeaf(YType.str, 'print_fan_header'), ['str'])),
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('fru_pid', (YLeaf(YType.str, 'fru_PID'), ['str'])),
                            ('fans_speed', (YLeaf(YType.str, 'fans_speed'), ['str'])),
                            ('fan_header', (YLeaf(YType.uint32, 'fan_header'), ['int'])),
                            ('speed_space', (YLeaf(YType.uint32, 'speed_space'), ['int'])),
                        ])
                        self.logical_slot = None
                        self.print_fan_header = None
                        self.location = None
                        self.fru_pid = None
                        self.fans_speed = None
                        self.fan_header = None
                        self.speed_space = None
                        self._segment_path = lambda: "fan_attributes" + "[logical_slot='" + str(self.logical_slot) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Oper.Fan.Location.FanAttributes, ['logical_slot', 'print_fan_header', 'location', 'fru_pid', 'fans_speed', 'fan_header', 'speed_space'], name, value)


        class Power(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Power.Location>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Oper.Power, self).__init__()

                self.yang_name = "power"
                self.yang_parent_name = "oper"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Environment.Oper.Power.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "power"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Oper.Power, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                .. attribute:: pem_attributes
                
                	
                	**type**\: list of  		 :py:class:`PemAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Power.Location.PemAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Oper.Power.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "power"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("pem_attributes", ("pem_attributes", Environment.Oper.Power.Location.PemAttributes))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.pem_attributes = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/power/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Oper.Power.Location, ['location'], name, value)


                class PemAttributes(Entity):
                    """
                    
                    
                    .. attribute:: pem  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: pem_id
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: card_type
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: ps_type
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: shelf_num
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: supply_type
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: input_voltage
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: input_current
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: output_voltage
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: output_current
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: status
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: input_power_to_ps
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_current_to_ps
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: output_power_from_ps
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_current_from_ps
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: power_allocated
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: power_consumed
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: power_status
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: confgd_power_redundancy_mode
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: usable_power_capacity
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: protection_power_capacity
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: power_resrv_and_alloc
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: system_power_used
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: system_power_input
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: power_level
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: output_header
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: output_footer
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: ps_sum_footer
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Oper.Power.Location.PemAttributes, self).__init__()

                        self.yang_name = "pem_attributes"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pem']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pem', (YLeaf(YType.str, 'pem'), ['str'])),
                            ('pem_id', (YLeaf(YType.str, 'pem_id'), ['str'])),
                            ('card_type', (YLeaf(YType.str, 'card_type'), ['str'])),
                            ('ps_type', (YLeaf(YType.str, 'ps_type'), ['str'])),
                            ('shelf_num', (YLeaf(YType.uint16, 'shelf_num'), ['int'])),
                            ('supply_type', (YLeaf(YType.str, 'supply_type'), ['str'])),
                            ('input_voltage', (YLeaf(YType.str, 'input_voltage'), ['str'])),
                            ('input_current', (YLeaf(YType.str, 'input_current'), ['str'])),
                            ('output_voltage', (YLeaf(YType.str, 'output_voltage'), ['str'])),
                            ('output_current', (YLeaf(YType.str, 'output_current'), ['str'])),
                            ('status', (YLeaf(YType.str, 'status'), ['str'])),
                            ('input_power_to_ps', (YLeaf(YType.uint32, 'input_power_to_ps'), ['int'])),
                            ('input_current_to_ps', (YLeaf(YType.str, 'input_current_to_ps'), ['str'])),
                            ('output_power_from_ps', (YLeaf(YType.uint32, 'output_power_from_ps'), ['int'])),
                            ('output_current_from_ps', (YLeaf(YType.str, 'output_current_from_ps'), ['str'])),
                            ('power_allocated', (YLeaf(YType.uint32, 'power_allocated'), ['int'])),
                            ('power_consumed', (YLeaf(YType.str, 'power_consumed'), ['str'])),
                            ('power_status', (YLeaf(YType.str, 'power_status'), ['str'])),
                            ('confgd_power_redundancy_mode', (YLeaf(YType.str, 'confgd_power_redundancy_mode'), ['str'])),
                            ('usable_power_capacity', (YLeaf(YType.uint32, 'usable_power_capacity'), ['int'])),
                            ('protection_power_capacity', (YLeaf(YType.uint32, 'protection_power_capacity'), ['int'])),
                            ('power_resrv_and_alloc', (YLeaf(YType.uint32, 'power_resrv_and_alloc'), ['int'])),
                            ('system_power_used', (YLeaf(YType.uint32, 'system_power_used'), ['int'])),
                            ('system_power_input', (YLeaf(YType.uint32, 'system_power_input'), ['int'])),
                            ('power_level', (YLeaf(YType.uint16, 'power_level'), ['int'])),
                            ('output_header', (YLeaf(YType.uint16, 'output_header'), ['int'])),
                            ('output_footer', (YLeaf(YType.uint16, 'output_footer'), ['int'])),
                            ('ps_sum_footer', (YLeaf(YType.uint16, 'ps_sum_footer'), ['int'])),
                        ])
                        self.pem = None
                        self.pem_id = None
                        self.card_type = None
                        self.ps_type = None
                        self.shelf_num = None
                        self.supply_type = None
                        self.input_voltage = None
                        self.input_current = None
                        self.output_voltage = None
                        self.output_current = None
                        self.status = None
                        self.input_power_to_ps = None
                        self.input_current_to_ps = None
                        self.output_power_from_ps = None
                        self.output_current_from_ps = None
                        self.power_allocated = None
                        self.power_consumed = None
                        self.power_status = None
                        self.confgd_power_redundancy_mode = None
                        self.usable_power_capacity = None
                        self.protection_power_capacity = None
                        self.power_resrv_and_alloc = None
                        self.system_power_used = None
                        self.system_power_input = None
                        self.power_level = None
                        self.output_header = None
                        self.output_footer = None
                        self.ps_sum_footer = None
                        self._segment_path = lambda: "pem_attributes" + "[pem='" + str(self.pem) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Oper.Power.Location.PemAttributes, ['pem', 'pem_id', 'card_type', 'ps_type', 'shelf_num', 'supply_type', 'input_voltage', 'input_current', 'output_voltage', 'output_current', 'status', 'input_power_to_ps', 'input_current_to_ps', 'output_power_from_ps', 'output_current_from_ps', 'power_allocated', 'power_consumed', 'power_status', 'confgd_power_redundancy_mode', 'usable_power_capacity', 'protection_power_capacity', 'power_resrv_and_alloc', 'system_power_used', 'system_power_input', 'power_level', 'output_header', 'output_footer', 'ps_sum_footer'], name, value)


        class Altitude(Entity):
            """
            
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Altitude.Location>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Oper.Altitude, self).__init__()

                self.yang_name = "altitude"
                self.yang_parent_name = "oper"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", Environment.Oper.Altitude.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "altitude"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Oper.Altitude, [], name, value)


            class Location(Entity):
                """
                
                
                .. attribute:: location  (key)
                
                	
                	**type**\: str
                
                .. attribute:: alt_attributes
                
                	
                	**type**\: list of  		 :py:class:`AltAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Oper.Altitude.Location.AltAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Oper.Altitude.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "altitude"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['location']
                    self._child_classes = OrderedDict([("alt_attributes", ("alt_attributes", Environment.Oper.Altitude.Location.AltAttributes))])
                    self._leafs = OrderedDict([
                        ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ])
                    self.location = None

                    self.alt_attributes = YList(self)
                    self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/oper/altitude/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Oper.Altitude.Location, ['location'], name, value)


                class AltAttributes(Entity):
                    """
                    
                    
                    .. attribute:: sensor  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: rack
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sensor_value
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: source
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: print_header
                    
                    	
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Oper.Altitude.Location.AltAttributes, self).__init__()

                        self.yang_name = "alt_attributes"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensor']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensor', (YLeaf(YType.str, 'sensor'), ['str'])),
                            ('rack', (YLeaf(YType.uint32, 'rack'), ['int'])),
                            ('sensor_value', (YLeaf(YType.str, 'sensor_value'), ['str'])),
                            ('source', (YLeaf(YType.str, 'source'), ['str'])),
                            ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                        ])
                        self.sensor = None
                        self.rack = None
                        self.sensor_value = None
                        self.source = None
                        self.print_header = None
                        self._segment_path = lambda: "alt_attributes" + "[sensor='" + str(self.sensor) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Oper.Altitude.Location.AltAttributes, ['sensor', 'rack', 'sensor_value', 'source', 'print_header'], name, value)


    class All(Entity):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location>`
        
        

        """

        _prefix = 'envmon'
        _revision = '2018-02-06'

        def __init__(self):
            super(Environment.All, self).__init__()

            self.yang_name = "all"
            self.yang_parent_name = "environment"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("location", ("location", Environment.All.Location))])
            self._leafs = OrderedDict()

            self.location = YList(self)
            self._segment_path = lambda: "all"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Environment.All, [], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: location  (key)
            
            	
            	**type**\: str
            
            .. attribute:: temperatures
            
            	
            	**type**\: list of  		 :py:class:`Temperatures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Temperatures>`
            
            .. attribute:: voltages
            
            	
            	**type**\: list of  		 :py:class:`Voltages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Voltages>`
            
            .. attribute:: current
            
            	
            	**type**\: list of  		 :py:class:`Current <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Current>`
            
            .. attribute:: fan
            
            	
            	**type**\: list of  		 :py:class:`Fan <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Fan>`
            
            .. attribute:: power
            
            	
            	**type**\: list of  		 :py:class:`Power <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Power>`
            
            .. attribute:: altitude
            
            	
            	**type**\: list of  		 :py:class:`Altitude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Altitude>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.All.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "all"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['location']
                self._child_classes = OrderedDict([("temperatures", ("temperatures", Environment.All.Location.Temperatures)), ("voltages", ("voltages", Environment.All.Location.Voltages)), ("current", ("current", Environment.All.Location.Current)), ("fan", ("fan", Environment.All.Location.Fan)), ("power", ("power", Environment.All.Location.Power)), ("altitude", ("altitude", Environment.All.Location.Altitude))])
                self._leafs = OrderedDict([
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.location = None

                self.temperatures = YList(self)
                self.voltages = YList(self)
                self.current = YList(self)
                self.fan = YList(self)
                self.power = YList(self)
                self.altitude = YList(self)
                self._segment_path = lambda: "location" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/all/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.All.Location, ['location'], name, value)


            class Temperatures(Entity):
                """
                
                
                .. attribute:: loc_iden  (key)
                
                	
                	**type**\: str
                
                .. attribute:: print_header
                
                	
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: sensor_attributes
                
                	
                	**type**\: list of  		 :py:class:`SensorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Temperatures.SensorAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.All.Location.Temperatures, self).__init__()

                    self.yang_name = "temperatures"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['loc_iden']
                    self._child_classes = OrderedDict([("sensor_attributes", ("sensor_attributes", Environment.All.Location.Temperatures.SensorAttributes))])
                    self._leafs = OrderedDict([
                        ('loc_iden', (YLeaf(YType.str, 'loc_iden'), ['str'])),
                        ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                    ])
                    self.loc_iden = None
                    self.print_header = None

                    self.sensor_attributes = YList(self)
                    self._segment_path = lambda: "temperatures" + "[loc_iden='" + str(self.loc_iden) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.All.Location.Temperatures, ['loc_iden', 'print_header'], name, value)


                class SensorAttributes(Entity):
                    """
                    
                    
                    .. attribute:: sensor  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: sensor_id
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: alarm
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: temperature_value
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: critical_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: major_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: minor_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: minor_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: major_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: critical_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.All.Location.Temperatures.SensorAttributes, self).__init__()

                        self.yang_name = "sensor_attributes"
                        self.yang_parent_name = "temperatures"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensor']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensor', (YLeaf(YType.str, 'sensor'), ['str'])),
                            ('sensor_id', (YLeaf(YType.str, 'sensor_id'), ['str'])),
                            ('alarm', (YLeaf(YType.str, 'alarm'), ['str'])),
                            ('temperature_value', (YLeaf(YType.str, 'temperature_value'), ['str'])),
                            ('value', (YLeaf(YType.int32, 'value'), ['int'])),
                            ('critical_lo', (YLeaf(YType.int32, 'critical_lo'), ['int'])),
                            ('major_lo', (YLeaf(YType.int32, 'major_lo'), ['int'])),
                            ('minor_lo', (YLeaf(YType.int32, 'minor_lo'), ['int'])),
                            ('minor_hi', (YLeaf(YType.int32, 'minor_hi'), ['int'])),
                            ('major_hi', (YLeaf(YType.int32, 'major_hi'), ['int'])),
                            ('critical_hi', (YLeaf(YType.int32, 'critical_hi'), ['int'])),
                        ])
                        self.sensor = None
                        self.sensor_id = None
                        self.alarm = None
                        self.temperature_value = None
                        self.value = None
                        self.critical_lo = None
                        self.major_lo = None
                        self.minor_lo = None
                        self.minor_hi = None
                        self.major_hi = None
                        self.critical_hi = None
                        self._segment_path = lambda: "sensor_attributes" + "[sensor='" + str(self.sensor) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.All.Location.Temperatures.SensorAttributes, ['sensor', 'sensor_id', 'alarm', 'temperature_value', 'value', 'critical_lo', 'major_lo', 'minor_lo', 'minor_hi', 'major_hi', 'critical_hi'], name, value)


            class Voltages(Entity):
                """
                
                
                .. attribute:: loc_iden  (key)
                
                	
                	**type**\: str
                
                .. attribute:: print_header
                
                	
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: sensor_attributes
                
                	
                	**type**\: list of  		 :py:class:`SensorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Voltages.SensorAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.All.Location.Voltages, self).__init__()

                    self.yang_name = "voltages"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['loc_iden']
                    self._child_classes = OrderedDict([("sensor_attributes", ("sensor_attributes", Environment.All.Location.Voltages.SensorAttributes))])
                    self._leafs = OrderedDict([
                        ('loc_iden', (YLeaf(YType.str, 'loc_iden'), ['str'])),
                        ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                    ])
                    self.loc_iden = None
                    self.print_header = None

                    self.sensor_attributes = YList(self)
                    self._segment_path = lambda: "voltages" + "[loc_iden='" + str(self.loc_iden) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.All.Location.Voltages, ['loc_iden', 'print_header'], name, value)


                class SensorAttributes(Entity):
                    """
                    
                    
                    .. attribute:: sensor  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: sensor_id
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: alarm
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: temperature_value
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: critical_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: major_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: minor_lo
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: minor_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: major_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: critical_hi
                    
                    	
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.All.Location.Voltages.SensorAttributes, self).__init__()

                        self.yang_name = "sensor_attributes"
                        self.yang_parent_name = "voltages"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensor']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensor', (YLeaf(YType.str, 'sensor'), ['str'])),
                            ('sensor_id', (YLeaf(YType.str, 'sensor_id'), ['str'])),
                            ('alarm', (YLeaf(YType.str, 'alarm'), ['str'])),
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ('temperature_value', (YLeaf(YType.int32, 'temperature_value'), ['int'])),
                            ('critical_lo', (YLeaf(YType.int32, 'critical_lo'), ['int'])),
                            ('major_lo', (YLeaf(YType.int32, 'major_lo'), ['int'])),
                            ('minor_lo', (YLeaf(YType.int32, 'minor_lo'), ['int'])),
                            ('minor_hi', (YLeaf(YType.int32, 'minor_hi'), ['int'])),
                            ('major_hi', (YLeaf(YType.int32, 'major_hi'), ['int'])),
                            ('critical_hi', (YLeaf(YType.int32, 'critical_hi'), ['int'])),
                        ])
                        self.sensor = None
                        self.sensor_id = None
                        self.alarm = None
                        self.value = None
                        self.temperature_value = None
                        self.critical_lo = None
                        self.major_lo = None
                        self.minor_lo = None
                        self.minor_hi = None
                        self.major_hi = None
                        self.critical_hi = None
                        self._segment_path = lambda: "sensor_attributes" + "[sensor='" + str(self.sensor) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.All.Location.Voltages.SensorAttributes, ['sensor', 'sensor_id', 'alarm', 'value', 'temperature_value', 'critical_lo', 'major_lo', 'minor_lo', 'minor_hi', 'major_hi', 'critical_hi'], name, value)


            class Current(Entity):
                """
                
                
                .. attribute:: loc_iden  (key)
                
                	
                	**type**\: str
                
                .. attribute:: print_header
                
                	
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: sensor_attributes
                
                	
                	**type**\: list of  		 :py:class:`SensorAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Current.SensorAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.All.Location.Current, self).__init__()

                    self.yang_name = "current"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['loc_iden']
                    self._child_classes = OrderedDict([("sensor_attributes", ("sensor_attributes", Environment.All.Location.Current.SensorAttributes))])
                    self._leafs = OrderedDict([
                        ('loc_iden', (YLeaf(YType.str, 'loc_iden'), ['str'])),
                        ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                    ])
                    self.loc_iden = None
                    self.print_header = None

                    self.sensor_attributes = YList(self)
                    self._segment_path = lambda: "current" + "[loc_iden='" + str(self.loc_iden) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.All.Location.Current, ['loc_iden', 'print_header'], name, value)


                class SensorAttributes(Entity):
                    """
                    
                    
                    .. attribute:: sensor  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: sensor_id
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.All.Location.Current.SensorAttributes, self).__init__()

                        self.yang_name = "sensor_attributes"
                        self.yang_parent_name = "current"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensor']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensor', (YLeaf(YType.str, 'sensor'), ['str'])),
                            ('sensor_id', (YLeaf(YType.str, 'sensor_id'), ['str'])),
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                        ])
                        self.sensor = None
                        self.sensor_id = None
                        self.value = None
                        self._segment_path = lambda: "sensor_attributes" + "[sensor='" + str(self.sensor) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.All.Location.Current.SensorAttributes, ['sensor', 'sensor_id', 'value'], name, value)


            class Fan(Entity):
                """
                
                
                .. attribute:: loc_iden  (key)
                
                	
                	**type**\: str
                
                .. attribute:: fan_attributes
                
                	
                	**type**\: list of  		 :py:class:`FanAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Fan.FanAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.All.Location.Fan, self).__init__()

                    self.yang_name = "fan"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['loc_iden']
                    self._child_classes = OrderedDict([("fan_attributes", ("fan_attributes", Environment.All.Location.Fan.FanAttributes))])
                    self._leafs = OrderedDict([
                        ('loc_iden', (YLeaf(YType.str, 'loc_iden'), ['str'])),
                    ])
                    self.loc_iden = None

                    self.fan_attributes = YList(self)
                    self._segment_path = lambda: "fan" + "[loc_iden='" + str(self.loc_iden) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.All.Location.Fan, ['loc_iden'], name, value)


                class FanAttributes(Entity):
                    """
                    
                    
                    .. attribute:: logical_slot  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: print_fan_header
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: fru_pid
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: fans_speed
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: fan_header
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: speed_space
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.All.Location.Fan.FanAttributes, self).__init__()

                        self.yang_name = "fan_attributes"
                        self.yang_parent_name = "fan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['logical_slot']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('logical_slot', (YLeaf(YType.str, 'logical_slot'), ['str'])),
                            ('print_fan_header', (YLeaf(YType.str, 'print_fan_header'), ['str'])),
                            ('location', (YLeaf(YType.str, 'location'), ['str'])),
                            ('fru_pid', (YLeaf(YType.str, 'fru_PID'), ['str'])),
                            ('fans_speed', (YLeaf(YType.str, 'fans_speed'), ['str'])),
                            ('fan_header', (YLeaf(YType.uint32, 'fan_header'), ['int'])),
                            ('speed_space', (YLeaf(YType.uint32, 'speed_space'), ['int'])),
                        ])
                        self.logical_slot = None
                        self.print_fan_header = None
                        self.location = None
                        self.fru_pid = None
                        self.fans_speed = None
                        self.fan_header = None
                        self.speed_space = None
                        self._segment_path = lambda: "fan_attributes" + "[logical_slot='" + str(self.logical_slot) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.All.Location.Fan.FanAttributes, ['logical_slot', 'print_fan_header', 'location', 'fru_pid', 'fans_speed', 'fan_header', 'speed_space'], name, value)


            class Power(Entity):
                """
                
                
                .. attribute:: loc_iden  (key)
                
                	
                	**type**\: str
                
                .. attribute:: pem_attributes
                
                	
                	**type**\: list of  		 :py:class:`PemAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Power.PemAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.All.Location.Power, self).__init__()

                    self.yang_name = "power"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['loc_iden']
                    self._child_classes = OrderedDict([("pem_attributes", ("pem_attributes", Environment.All.Location.Power.PemAttributes))])
                    self._leafs = OrderedDict([
                        ('loc_iden', (YLeaf(YType.str, 'loc_iden'), ['str'])),
                    ])
                    self.loc_iden = None

                    self.pem_attributes = YList(self)
                    self._segment_path = lambda: "power" + "[loc_iden='" + str(self.loc_iden) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.All.Location.Power, ['loc_iden'], name, value)


                class PemAttributes(Entity):
                    """
                    
                    
                    .. attribute:: pem  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: pem_id
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: card_type
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: ps_type
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: shelf_num
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: supply_type
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: input_voltage
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: input_current
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: output_voltage
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: output_current
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: status
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: input_power_to_ps
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_current_to_ps
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: output_power_from_ps
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_current_from_ps
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: power_allocated
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: power_consumed
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: power_status
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: confgd_power_redundancy_mode
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: usable_power_capacity
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: protection_power_capacity
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: power_resrv_and_alloc
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: system_power_used
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: system_power_input
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: power_level
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: output_header
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: output_footer
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: ps_sum_footer
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.All.Location.Power.PemAttributes, self).__init__()

                        self.yang_name = "pem_attributes"
                        self.yang_parent_name = "power"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pem']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pem', (YLeaf(YType.str, 'pem'), ['str'])),
                            ('pem_id', (YLeaf(YType.str, 'pem_id'), ['str'])),
                            ('card_type', (YLeaf(YType.str, 'card_type'), ['str'])),
                            ('ps_type', (YLeaf(YType.str, 'ps_type'), ['str'])),
                            ('shelf_num', (YLeaf(YType.uint16, 'shelf_num'), ['int'])),
                            ('supply_type', (YLeaf(YType.str, 'supply_type'), ['str'])),
                            ('input_voltage', (YLeaf(YType.str, 'input_voltage'), ['str'])),
                            ('input_current', (YLeaf(YType.str, 'input_current'), ['str'])),
                            ('output_voltage', (YLeaf(YType.str, 'output_voltage'), ['str'])),
                            ('output_current', (YLeaf(YType.str, 'output_current'), ['str'])),
                            ('status', (YLeaf(YType.str, 'status'), ['str'])),
                            ('input_power_to_ps', (YLeaf(YType.uint32, 'input_power_to_ps'), ['int'])),
                            ('input_current_to_ps', (YLeaf(YType.str, 'input_current_to_ps'), ['str'])),
                            ('output_power_from_ps', (YLeaf(YType.uint32, 'output_power_from_ps'), ['int'])),
                            ('output_current_from_ps', (YLeaf(YType.str, 'output_current_from_ps'), ['str'])),
                            ('power_allocated', (YLeaf(YType.uint32, 'power_allocated'), ['int'])),
                            ('power_consumed', (YLeaf(YType.str, 'power_consumed'), ['str'])),
                            ('power_status', (YLeaf(YType.str, 'power_status'), ['str'])),
                            ('confgd_power_redundancy_mode', (YLeaf(YType.str, 'confgd_power_redundancy_mode'), ['str'])),
                            ('usable_power_capacity', (YLeaf(YType.uint32, 'usable_power_capacity'), ['int'])),
                            ('protection_power_capacity', (YLeaf(YType.uint32, 'protection_power_capacity'), ['int'])),
                            ('power_resrv_and_alloc', (YLeaf(YType.uint32, 'power_resrv_and_alloc'), ['int'])),
                            ('system_power_used', (YLeaf(YType.uint32, 'system_power_used'), ['int'])),
                            ('system_power_input', (YLeaf(YType.uint32, 'system_power_input'), ['int'])),
                            ('power_level', (YLeaf(YType.uint16, 'power_level'), ['int'])),
                            ('output_header', (YLeaf(YType.uint16, 'output_header'), ['int'])),
                            ('output_footer', (YLeaf(YType.uint16, 'output_footer'), ['int'])),
                            ('ps_sum_footer', (YLeaf(YType.uint16, 'ps_sum_footer'), ['int'])),
                        ])
                        self.pem = None
                        self.pem_id = None
                        self.card_type = None
                        self.ps_type = None
                        self.shelf_num = None
                        self.supply_type = None
                        self.input_voltage = None
                        self.input_current = None
                        self.output_voltage = None
                        self.output_current = None
                        self.status = None
                        self.input_power_to_ps = None
                        self.input_current_to_ps = None
                        self.output_power_from_ps = None
                        self.output_current_from_ps = None
                        self.power_allocated = None
                        self.power_consumed = None
                        self.power_status = None
                        self.confgd_power_redundancy_mode = None
                        self.usable_power_capacity = None
                        self.protection_power_capacity = None
                        self.power_resrv_and_alloc = None
                        self.system_power_used = None
                        self.system_power_input = None
                        self.power_level = None
                        self.output_header = None
                        self.output_footer = None
                        self.ps_sum_footer = None
                        self._segment_path = lambda: "pem_attributes" + "[pem='" + str(self.pem) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.All.Location.Power.PemAttributes, ['pem', 'pem_id', 'card_type', 'ps_type', 'shelf_num', 'supply_type', 'input_voltage', 'input_current', 'output_voltage', 'output_current', 'status', 'input_power_to_ps', 'input_current_to_ps', 'output_power_from_ps', 'output_current_from_ps', 'power_allocated', 'power_consumed', 'power_status', 'confgd_power_redundancy_mode', 'usable_power_capacity', 'protection_power_capacity', 'power_resrv_and_alloc', 'system_power_used', 'system_power_input', 'power_level', 'output_header', 'output_footer', 'ps_sum_footer'], name, value)


            class Altitude(Entity):
                """
                
                
                .. attribute:: loc_iden  (key)
                
                	
                	**type**\: str
                
                .. attribute:: alt_attributes
                
                	
                	**type**\: list of  		 :py:class:`AltAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.All.Location.Altitude.AltAttributes>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.All.Location.Altitude, self).__init__()

                    self.yang_name = "altitude"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['loc_iden']
                    self._child_classes = OrderedDict([("alt_attributes", ("alt_attributes", Environment.All.Location.Altitude.AltAttributes))])
                    self._leafs = OrderedDict([
                        ('loc_iden', (YLeaf(YType.str, 'loc_iden'), ['str'])),
                    ])
                    self.loc_iden = None

                    self.alt_attributes = YList(self)
                    self._segment_path = lambda: "altitude" + "[loc_iden='" + str(self.loc_iden) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.All.Location.Altitude, ['loc_iden'], name, value)


                class AltAttributes(Entity):
                    """
                    
                    
                    .. attribute:: sensor  (key)
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: print_header
                    
                    	
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: rack
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sensor_value
                    
                    	
                    	**type**\: str
                    
                    .. attribute:: source
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.All.Location.Altitude.AltAttributes, self).__init__()

                        self.yang_name = "alt_attributes"
                        self.yang_parent_name = "altitude"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['sensor']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sensor', (YLeaf(YType.str, 'sensor'), ['str'])),
                            ('print_header', (YLeaf(YType.boolean, 'print_header'), ['bool'])),
                            ('rack', (YLeaf(YType.uint32, 'rack'), ['int'])),
                            ('sensor_value', (YLeaf(YType.str, 'sensor_value'), ['str'])),
                            ('source', (YLeaf(YType.str, 'source'), ['str'])),
                        ])
                        self.sensor = None
                        self.print_header = None
                        self.rack = None
                        self.sensor_value = None
                        self.source = None
                        self._segment_path = lambda: "alt_attributes" + "[sensor='" + str(self.sensor) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.All.Location.Altitude.AltAttributes, ['sensor', 'print_header', 'rack', 'sensor_value', 'source'], name, value)


    class Config(Entity):
        """
        environment configurational data
        
        .. attribute:: router
        
        	
        	**type**\:  :py:class:`Router <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Router>`
        
        .. attribute:: air_filter
        
        	
        	**type**\:  :py:class:`AirFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.AirFilter>`
        
        .. attribute:: fan_ctrl
        
        	
        	**type**\:  :py:class:`FanCtrl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.FanCtrl>`
        
        .. attribute:: temperature
        
        	
        	**type**\:  :py:class:`Temperature <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Temperature>`
        
        .. attribute:: monitoring
        
        	
        	**type**\:  :py:class:`Monitoring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Monitoring>`
        
        .. attribute:: raise_fan_speed
        
        	
        	**type**\: int
        
        	**range:** 0..100
        
        .. attribute:: fan_ctrl_optics
        
        	
        	**type**\: int
        
        	**range:** 0..1
        
        .. attribute:: graceful_shutdown
        
        	
        	**type**\: int
        
        	**range:** 0..1
        
        

        """

        _prefix = 'envmon'
        _revision = '2018-02-06'

        def __init__(self):
            super(Environment.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "environment"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("router", ("router", Environment.Config.Router)), ("air-filter", ("air_filter", Environment.Config.AirFilter)), ("fan-ctrl", ("fan_ctrl", Environment.Config.FanCtrl)), ("temperature", ("temperature", Environment.Config.Temperature)), ("monitoring", ("monitoring", Environment.Config.Monitoring))])
            self._leafs = OrderedDict([
                ('raise_fan_speed', (YLeaf(YType.uint32, 'raise-fan-speed'), ['int'])),
                ('fan_ctrl_optics', (YLeaf(YType.uint32, 'fan-ctrl-optics'), ['int'])),
                ('graceful_shutdown', (YLeaf(YType.uint32, 'graceful-shutdown'), ['int'])),
            ])
            self.raise_fan_speed = None
            self.fan_ctrl_optics = None
            self.graceful_shutdown = None

            self.router = Environment.Config.Router()
            self.router.parent = self
            self._children_name_map["router"] = "router"

            self.air_filter = Environment.Config.AirFilter()
            self.air_filter.parent = self
            self._children_name_map["air_filter"] = "air-filter"

            self.fan_ctrl = Environment.Config.FanCtrl()
            self.fan_ctrl.parent = self
            self._children_name_map["fan_ctrl"] = "fan-ctrl"

            self.temperature = Environment.Config.Temperature()
            self.temperature.parent = self
            self._children_name_map["temperature"] = "temperature"

            self.monitoring = Environment.Config.Monitoring()
            self.monitoring.parent = self
            self._children_name_map["monitoring"] = "monitoring"
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Environment.Config, ['raise_fan_speed', 'fan_ctrl_optics', 'graceful_shutdown'], name, value)


        class Router(Entity):
            """
            
            
            .. attribute:: altitude
            
            	
            	**type**\:  :py:class:`Altitude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Router.Altitude>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Config.Router, self).__init__()

                self.yang_name = "router"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("altitude", ("altitude", Environment.Config.Router.Altitude))])
                self._leafs = OrderedDict()

                self.altitude = Environment.Config.Router.Altitude()
                self.altitude.parent = self
                self._children_name_map["altitude"] = "altitude"
                self._segment_path = lambda: "router"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Config.Router, [], name, value)


            class Altitude(Entity):
                """
                
                
                .. attribute:: all
                
                	
                	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Router.Altitude.All>`
                
                .. attribute:: rack_loc
                
                	
                	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Router.Altitude.RackLoc>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Config.Router.Altitude, self).__init__()

                    self.yang_name = "altitude"
                    self.yang_parent_name = "router"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("all", ("all", Environment.Config.Router.Altitude.All)), ("rack_loc", ("rack_loc", Environment.Config.Router.Altitude.RackLoc))])
                    self._leafs = OrderedDict()

                    self.all = Environment.Config.Router.Altitude.All()
                    self.all.parent = self
                    self._children_name_map["all"] = "all"

                    self.rack_loc = Environment.Config.Router.Altitude.RackLoc()
                    self.rack_loc.parent = self
                    self._children_name_map["rack_loc"] = "rack_loc"
                    self._segment_path = lambda: "altitude"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/router/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Config.Router.Altitude, [], name, value)


                class All(Entity):
                    """
                    
                    
                    .. attribute:: num_meters
                    
                    	
                    	**type**\: int
                    
                    	**range:** 1..4000
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Config.Router.Altitude.All, self).__init__()

                        self.yang_name = "all"
                        self.yang_parent_name = "altitude"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('num_meters', (YLeaf(YType.uint32, 'num_meters'), ['int'])),
                        ])
                        self.num_meters = None
                        self._segment_path = lambda: "all"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/router/altitude/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Config.Router.Altitude.All, ['num_meters'], name, value)


                class RackLoc(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Router.Altitude.RackLoc.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Config.Router.Altitude.RackLoc, self).__init__()

                        self.yang_name = "rack_loc"
                        self.yang_parent_name = "altitude"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Environment.Config.Router.Altitude.RackLoc.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "rack_loc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/router/altitude/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Config.Router.Altitude.RackLoc, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rackid  (key)
                        
                        	
                        	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                        
                        .. attribute:: num_meters
                        
                        	
                        	**type**\: int
                        
                        	**range:** 1..4000
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(Environment.Config.Router.Altitude.RackLoc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rack_loc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rackid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                                ('num_meters', (YLeaf(YType.uint32, 'num_meters'), ['int'])),
                            ])
                            self.rackid = None
                            self.num_meters = None
                            self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/router/altitude/rack_loc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Environment.Config.Router.Altitude.RackLoc.Location, ['rackid', 'num_meters'], name, value)


        class AirFilter(Entity):
            """
            
            
            .. attribute:: replaced
            
            	
            	**type**\:  :py:class:`Replaced <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.AirFilter.Replaced>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Config.AirFilter, self).__init__()

                self.yang_name = "air-filter"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("replaced", ("replaced", Environment.Config.AirFilter.Replaced))])
                self._leafs = OrderedDict()

                self.replaced = Environment.Config.AirFilter.Replaced()
                self.replaced.parent = self
                self._children_name_map["replaced"] = "replaced"
                self._segment_path = lambda: "air-filter"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Config.AirFilter, [], name, value)


            class Replaced(Entity):
                """
                
                
                .. attribute:: all
                
                	
                	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.AirFilter.Replaced.All>`
                
                .. attribute:: rack_loc
                
                	
                	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.AirFilter.Replaced.RackLoc>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Config.AirFilter.Replaced, self).__init__()

                    self.yang_name = "replaced"
                    self.yang_parent_name = "air-filter"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("all", ("all", Environment.Config.AirFilter.Replaced.All)), ("rack_loc", ("rack_loc", Environment.Config.AirFilter.Replaced.RackLoc))])
                    self._leafs = OrderedDict()

                    self.all = Environment.Config.AirFilter.Replaced.All()
                    self.all.parent = self
                    self._children_name_map["all"] = "all"

                    self.rack_loc = Environment.Config.AirFilter.Replaced.RackLoc()
                    self.rack_loc.parent = self
                    self._children_name_map["rack_loc"] = "rack_loc"
                    self._segment_path = lambda: "replaced"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/air-filter/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Config.AirFilter.Replaced, [], name, value)


                class All(Entity):
                    """
                    
                    
                    .. attribute:: date
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Config.AirFilter.Replaced.All, self).__init__()

                        self.yang_name = "all"
                        self.yang_parent_name = "replaced"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('date', (YLeaf(YType.str, 'date'), ['str'])),
                        ])
                        self.date = None
                        self._segment_path = lambda: "all"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/air-filter/replaced/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Config.AirFilter.Replaced.All, ['date'], name, value)


                class RackLoc(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.AirFilter.Replaced.RackLoc.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Config.AirFilter.Replaced.RackLoc, self).__init__()

                        self.yang_name = "rack_loc"
                        self.yang_parent_name = "replaced"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Environment.Config.AirFilter.Replaced.RackLoc.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "rack_loc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/air-filter/replaced/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Config.AirFilter.Replaced.RackLoc, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rackid  (key)
                        
                        	
                        	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                        
                        .. attribute:: date
                        
                        	
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(Environment.Config.AirFilter.Replaced.RackLoc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rack_loc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rackid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                                ('date', (YLeaf(YType.str, 'date'), ['str'])),
                            ])
                            self.rackid = None
                            self.date = None
                            self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/air-filter/replaced/rack_loc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Environment.Config.AirFilter.Replaced.RackLoc.Location, ['rackid', 'date'], name, value)


        class FanCtrl(Entity):
            """
            
            
            .. attribute:: disable
            
            	
            	**type**\:  :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.FanCtrl.Disable>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Config.FanCtrl, self).__init__()

                self.yang_name = "fan-ctrl"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disable", ("disable", Environment.Config.FanCtrl.Disable))])
                self._leafs = OrderedDict()

                self.disable = Environment.Config.FanCtrl.Disable()
                self.disable.parent = self
                self._children_name_map["disable"] = "disable"
                self._segment_path = lambda: "fan-ctrl"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Config.FanCtrl, [], name, value)


            class Disable(Entity):
                """
                
                
                .. attribute:: rack_loc
                
                	
                	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.FanCtrl.Disable.RackLoc>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Config.FanCtrl.Disable, self).__init__()

                    self.yang_name = "disable"
                    self.yang_parent_name = "fan-ctrl"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rack_loc", ("rack_loc", Environment.Config.FanCtrl.Disable.RackLoc))])
                    self._leafs = OrderedDict()

                    self.rack_loc = Environment.Config.FanCtrl.Disable.RackLoc()
                    self.rack_loc.parent = self
                    self._children_name_map["rack_loc"] = "rack_loc"
                    self._segment_path = lambda: "disable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/fan-ctrl/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Config.FanCtrl.Disable, [], name, value)


                class RackLoc(Entity):
                    """
                    
                    
                    .. attribute:: all
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.FanCtrl.Disable.RackLoc.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Config.FanCtrl.Disable.RackLoc, self).__init__()

                        self.yang_name = "rack_loc"
                        self.yang_parent_name = "disable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Environment.Config.FanCtrl.Disable.RackLoc.Location))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.location = YList(self)
                        self._segment_path = lambda: "rack_loc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/fan-ctrl/disable/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Config.FanCtrl.Disable.RackLoc, ['all'], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rackid  (key)
                        
                        	
                        	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(Environment.Config.FanCtrl.Disable.RackLoc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rack_loc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rackid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                            ])
                            self.rackid = None
                            self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/fan-ctrl/disable/rack_loc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Environment.Config.FanCtrl.Disable.RackLoc.Location, ['rackid'], name, value)


        class Temperature(Entity):
            """
            
            
            .. attribute:: disable
            
            	
            	**type**\:  :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Temperature.Disable>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Config.Temperature, self).__init__()

                self.yang_name = "temperature"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disable", ("disable", Environment.Config.Temperature.Disable))])
                self._leafs = OrderedDict()

                self.disable = Environment.Config.Temperature.Disable()
                self.disable.parent = self
                self._children_name_map["disable"] = "disable"
                self._segment_path = lambda: "temperature"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Config.Temperature, [], name, value)


            class Disable(Entity):
                """
                
                
                .. attribute:: rack_loc
                
                	
                	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Temperature.Disable.RackLoc>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Config.Temperature.Disable, self).__init__()

                    self.yang_name = "disable"
                    self.yang_parent_name = "temperature"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rack_loc", ("rack_loc", Environment.Config.Temperature.Disable.RackLoc))])
                    self._leafs = OrderedDict()

                    self.rack_loc = Environment.Config.Temperature.Disable.RackLoc()
                    self.rack_loc.parent = self
                    self._children_name_map["rack_loc"] = "rack_loc"
                    self._segment_path = lambda: "disable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/temperature/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Config.Temperature.Disable, [], name, value)


                class RackLoc(Entity):
                    """
                    
                    
                    .. attribute:: all
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Temperature.Disable.RackLoc.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Config.Temperature.Disable.RackLoc, self).__init__()

                        self.yang_name = "rack_loc"
                        self.yang_parent_name = "disable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Environment.Config.Temperature.Disable.RackLoc.Location))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.location = YList(self)
                        self._segment_path = lambda: "rack_loc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/temperature/disable/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Config.Temperature.Disable.RackLoc, ['all'], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rackid  (key)
                        
                        	
                        	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(Environment.Config.Temperature.Disable.RackLoc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rack_loc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rackid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                            ])
                            self.rackid = None
                            self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/temperature/disable/rack_loc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Environment.Config.Temperature.Disable.RackLoc.Location, ['rackid'], name, value)


        class Monitoring(Entity):
            """
            
            
            .. attribute:: disable
            
            	
            	**type**\:  :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Monitoring.Disable>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Config.Monitoring, self).__init__()

                self.yang_name = "monitoring"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disable", ("disable", Environment.Config.Monitoring.Disable))])
                self._leafs = OrderedDict()

                self.disable = Environment.Config.Monitoring.Disable()
                self.disable.parent = self
                self._children_name_map["disable"] = "disable"
                self._segment_path = lambda: "monitoring"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Config.Monitoring, [], name, value)


            class Disable(Entity):
                """
                
                
                .. attribute:: rack_loc
                
                	
                	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Monitoring.Disable.RackLoc>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Config.Monitoring.Disable, self).__init__()

                    self.yang_name = "disable"
                    self.yang_parent_name = "monitoring"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rack_loc", ("rack_loc", Environment.Config.Monitoring.Disable.RackLoc))])
                    self._leafs = OrderedDict()

                    self.rack_loc = Environment.Config.Monitoring.Disable.RackLoc()
                    self.rack_loc.parent = self
                    self._children_name_map["rack_loc"] = "rack_loc"
                    self._segment_path = lambda: "disable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/monitoring/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Config.Monitoring.Disable, [], name, value)


                class RackLoc(Entity):
                    """
                    
                    
                    .. attribute:: all
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Config.Monitoring.Disable.RackLoc.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Config.Monitoring.Disable.RackLoc, self).__init__()

                        self.yang_name = "rack_loc"
                        self.yang_parent_name = "disable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", Environment.Config.Monitoring.Disable.RackLoc.Location))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.location = YList(self)
                        self._segment_path = lambda: "rack_loc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/monitoring/disable/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Config.Monitoring.Disable.RackLoc, ['all'], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rackid  (key)
                        
                        	
                        	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(Environment.Config.Monitoring.Disable.RackLoc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rack_loc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rackid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                            ])
                            self.rackid = None
                            self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/config/monitoring/disable/rack_loc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Environment.Config.Monitoring.Disable.RackLoc.Location, ['rackid'], name, value)


    class Trace(Entity):
        """
        show traceable processes
        
        .. attribute:: buffer  (key)
        
        	
        	**type**\: str
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Trace.Location>`
        
        

        """

        _prefix = 'envmon'
        _revision = '2018-02-06'

        def __init__(self):
            super(Environment.Trace, self).__init__()

            self.yang_name = "trace"
            self.yang_parent_name = "environment"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['buffer']
            self._child_classes = OrderedDict([("location", ("location", Environment.Trace.Location))])
            self._leafs = OrderedDict([
                ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
            ])
            self.buffer = None

            self.location = YList(self)
            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:environment/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Environment.Trace, [u'buffer'], name, value)


        class Location(Entity):
            """
            
            
            .. attribute:: location_name  (key)
            
            	
            	**type**\: str
            
            .. attribute:: all_options
            
            	
            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Trace.Location.AllOptions>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(Environment.Trace.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "trace"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['location_name']
                self._child_classes = OrderedDict([("all-options", ("all_options", Environment.Trace.Location.AllOptions))])
                self._leafs = OrderedDict([
                    ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                ])
                self.location_name = None

                self.all_options = YList(self)
                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Environment.Trace.Location, [u'location_name'], name, value)


            class AllOptions(Entity):
                """
                
                
                .. attribute:: option  (key)
                
                	
                	**type**\: str
                
                .. attribute:: trace_blocks
                
                	
                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.Environment.Trace.Location.AllOptions.TraceBlocks>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(Environment.Trace.Location.AllOptions, self).__init__()

                    self.yang_name = "all-options"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['option']
                    self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Environment.Trace.Location.AllOptions.TraceBlocks))])
                    self._leafs = OrderedDict([
                        ('option', (YLeaf(YType.str, 'option'), ['str'])),
                    ])
                    self.option = None

                    self.trace_blocks = YList(self)
                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Environment.Trace.Location.AllOptions, [u'option'], name, value)


                class TraceBlocks(Entity):
                    """
                    
                    
                    .. attribute:: data
                    
                    	Trace output block
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(Environment.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                        self.yang_name = "trace-blocks"
                        self.yang_parent_name = "all-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('data', (YLeaf(YType.str, 'data'), ['str'])),
                        ])
                        self.data = None
                        self._segment_path = lambda: "trace-blocks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Environment.Trace.Location.AllOptions.TraceBlocks, [u'data'], name, value)

    def clone_ptr(self):
        self._top_entity = Environment()
        return self._top_entity

class PowerMgmt(Entity):
    """
    
    
    .. attribute:: config
    
    	Power Trays and PEMs configurational data
    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config>`
    
    

    """

    _prefix = 'envmon'
    _revision = '2018-02-06'

    def __init__(self):
        super(PowerMgmt, self).__init__()
        self._top_entity = None

        self.yang_name = "power-mgmt"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-envmon-ui"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", PowerMgmt.Config))])
        self._leafs = OrderedDict()

        self.config = PowerMgmt.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PowerMgmt, [], name, value)


    class Config(Entity):
        """
        Power Trays and PEMs configurational data
        
        .. attribute:: action
        
        	
        	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Action>`
        
        .. attribute:: single_feed_mode
        
        	
        	**type**\:  :py:class:`SingleFeedMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.SingleFeedMode>`
        
        .. attribute:: extended_temp
        
        	
        	**type**\:  :py:class:`ExtendedTemp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.ExtendedTemp>`
        
        .. attribute:: redundancy_num_pms
        
        	
        	**type**\:  :py:class:`RedundancyNumPms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.RedundancyNumPms>`
        
        .. attribute:: progressive
        
        	
        	**type**\:  :py:class:`Progressive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Progressive>`
        
        

        """

        _prefix = 'envmon'
        _revision = '2018-02-06'

        def __init__(self):
            super(PowerMgmt.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "power-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("action", ("action", PowerMgmt.Config.Action)), ("single-feed-mode", ("single_feed_mode", PowerMgmt.Config.SingleFeedMode)), ("extended-temp", ("extended_temp", PowerMgmt.Config.ExtendedTemp)), ("redundancy-num-pms", ("redundancy_num_pms", PowerMgmt.Config.RedundancyNumPms)), ("progressive", ("progressive", PowerMgmt.Config.Progressive))])
            self._leafs = OrderedDict()

            self.action = PowerMgmt.Config.Action()
            self.action.parent = self
            self._children_name_map["action"] = "action"

            self.single_feed_mode = PowerMgmt.Config.SingleFeedMode()
            self.single_feed_mode.parent = self
            self._children_name_map["single_feed_mode"] = "single-feed-mode"

            self.extended_temp = PowerMgmt.Config.ExtendedTemp()
            self.extended_temp.parent = self
            self._children_name_map["extended_temp"] = "extended-temp"

            self.redundancy_num_pms = PowerMgmt.Config.RedundancyNumPms()
            self.redundancy_num_pms.parent = self
            self._children_name_map["redundancy_num_pms"] = "redundancy-num-pms"

            self.progressive = PowerMgmt.Config.Progressive()
            self.progressive.parent = self
            self._children_name_map["progressive"] = "progressive"
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PowerMgmt.Config, [], name, value)


        class Action(Entity):
            """
            
            
            .. attribute:: disable
            
            	
            	**type**\:  :py:class:`Disable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Action.Disable>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(PowerMgmt.Config.Action, self).__init__()

                self.yang_name = "action"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("disable", ("disable", PowerMgmt.Config.Action.Disable))])
                self._leafs = OrderedDict()

                self.disable = PowerMgmt.Config.Action.Disable()
                self.disable.parent = self
                self._children_name_map["disable"] = "disable"
                self._segment_path = lambda: "action"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PowerMgmt.Config.Action, [], name, value)


            class Disable(Entity):
                """
                
                
                .. attribute:: rack_loc
                
                	
                	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Action.Disable.RackLoc>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(PowerMgmt.Config.Action.Disable, self).__init__()

                    self.yang_name = "disable"
                    self.yang_parent_name = "action"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rack_loc", ("rack_loc", PowerMgmt.Config.Action.Disable.RackLoc))])
                    self._leafs = OrderedDict()

                    self.rack_loc = PowerMgmt.Config.Action.Disable.RackLoc()
                    self.rack_loc.parent = self
                    self._children_name_map["rack_loc"] = "rack_loc"
                    self._segment_path = lambda: "disable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/action/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PowerMgmt.Config.Action.Disable, [], name, value)


                class RackLoc(Entity):
                    """
                    
                    
                    .. attribute:: all
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Action.Disable.RackLoc.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(PowerMgmt.Config.Action.Disable.RackLoc, self).__init__()

                        self.yang_name = "rack_loc"
                        self.yang_parent_name = "disable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", PowerMgmt.Config.Action.Disable.RackLoc.Location))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.location = YList(self)
                        self._segment_path = lambda: "rack_loc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/action/disable/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PowerMgmt.Config.Action.Disable.RackLoc, ['all'], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rackid  (key)
                        
                        	
                        	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(PowerMgmt.Config.Action.Disable.RackLoc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rack_loc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rackid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                            ])
                            self.rackid = None
                            self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/action/disable/rack_loc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PowerMgmt.Config.Action.Disable.RackLoc.Location, ['rackid'], name, value)


        class SingleFeedMode(Entity):
            """
            
            
            .. attribute:: enable
            
            	
            	**type**\:  :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.SingleFeedMode.Enable>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(PowerMgmt.Config.SingleFeedMode, self).__init__()

                self.yang_name = "single-feed-mode"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("enable", ("enable", PowerMgmt.Config.SingleFeedMode.Enable))])
                self._leafs = OrderedDict()

                self.enable = PowerMgmt.Config.SingleFeedMode.Enable()
                self.enable.parent = self
                self._children_name_map["enable"] = "enable"
                self._segment_path = lambda: "single-feed-mode"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PowerMgmt.Config.SingleFeedMode, [], name, value)


            class Enable(Entity):
                """
                
                
                .. attribute:: rack_loc
                
                	
                	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.SingleFeedMode.Enable.RackLoc>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(PowerMgmt.Config.SingleFeedMode.Enable, self).__init__()

                    self.yang_name = "enable"
                    self.yang_parent_name = "single-feed-mode"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rack_loc", ("rack_loc", PowerMgmt.Config.SingleFeedMode.Enable.RackLoc))])
                    self._leafs = OrderedDict()

                    self.rack_loc = PowerMgmt.Config.SingleFeedMode.Enable.RackLoc()
                    self.rack_loc.parent = self
                    self._children_name_map["rack_loc"] = "rack_loc"
                    self._segment_path = lambda: "enable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/single-feed-mode/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PowerMgmt.Config.SingleFeedMode.Enable, [], name, value)


                class RackLoc(Entity):
                    """
                    
                    
                    .. attribute:: all
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.SingleFeedMode.Enable.RackLoc.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(PowerMgmt.Config.SingleFeedMode.Enable.RackLoc, self).__init__()

                        self.yang_name = "rack_loc"
                        self.yang_parent_name = "enable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", PowerMgmt.Config.SingleFeedMode.Enable.RackLoc.Location))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.location = YList(self)
                        self._segment_path = lambda: "rack_loc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/single-feed-mode/enable/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PowerMgmt.Config.SingleFeedMode.Enable.RackLoc, ['all'], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rackid  (key)
                        
                        	
                        	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(PowerMgmt.Config.SingleFeedMode.Enable.RackLoc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rack_loc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rackid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                            ])
                            self.rackid = None
                            self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/single-feed-mode/enable/rack_loc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PowerMgmt.Config.SingleFeedMode.Enable.RackLoc.Location, ['rackid'], name, value)


        class ExtendedTemp(Entity):
            """
            
            
            .. attribute:: enable
            
            	
            	**type**\:  :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.ExtendedTemp.Enable>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(PowerMgmt.Config.ExtendedTemp, self).__init__()

                self.yang_name = "extended-temp"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("enable", ("enable", PowerMgmt.Config.ExtendedTemp.Enable))])
                self._leafs = OrderedDict()

                self.enable = PowerMgmt.Config.ExtendedTemp.Enable()
                self.enable.parent = self
                self._children_name_map["enable"] = "enable"
                self._segment_path = lambda: "extended-temp"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PowerMgmt.Config.ExtendedTemp, [], name, value)


            class Enable(Entity):
                """
                
                
                .. attribute:: rack_loc
                
                	
                	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.ExtendedTemp.Enable.RackLoc>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(PowerMgmt.Config.ExtendedTemp.Enable, self).__init__()

                    self.yang_name = "enable"
                    self.yang_parent_name = "extended-temp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rack_loc", ("rack_loc", PowerMgmt.Config.ExtendedTemp.Enable.RackLoc))])
                    self._leafs = OrderedDict()

                    self.rack_loc = PowerMgmt.Config.ExtendedTemp.Enable.RackLoc()
                    self.rack_loc.parent = self
                    self._children_name_map["rack_loc"] = "rack_loc"
                    self._segment_path = lambda: "enable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/extended-temp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PowerMgmt.Config.ExtendedTemp.Enable, [], name, value)


                class RackLoc(Entity):
                    """
                    
                    
                    .. attribute:: all
                    
                    	
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.ExtendedTemp.Enable.RackLoc.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(PowerMgmt.Config.ExtendedTemp.Enable.RackLoc, self).__init__()

                        self.yang_name = "rack_loc"
                        self.yang_parent_name = "enable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", PowerMgmt.Config.ExtendedTemp.Enable.RackLoc.Location))])
                        self._leafs = OrderedDict([
                            ('all', (YLeaf(YType.empty, 'all'), ['Empty'])),
                        ])
                        self.all = None

                        self.location = YList(self)
                        self._segment_path = lambda: "rack_loc"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/extended-temp/enable/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PowerMgmt.Config.ExtendedTemp.Enable.RackLoc, ['all'], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: rackid  (key)
                        
                        	
                        	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(PowerMgmt.Config.ExtendedTemp.Enable.RackLoc.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "rack_loc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['rackid']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                            ])
                            self.rackid = None
                            self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/extended-temp/enable/rack_loc/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PowerMgmt.Config.ExtendedTemp.Enable.RackLoc.Location, ['rackid'], name, value)


        class RedundancyNumPms(Entity):
            """
            
            
            .. attribute:: all
            
            	
            	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.RedundancyNumPms.All>`
            
            .. attribute:: rack_loc
            
            	
            	**type**\:  :py:class:`RackLoc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.RedundancyNumPms.RackLoc>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(PowerMgmt.Config.RedundancyNumPms, self).__init__()

                self.yang_name = "redundancy-num-pms"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("all", ("all", PowerMgmt.Config.RedundancyNumPms.All)), ("rack_loc", ("rack_loc", PowerMgmt.Config.RedundancyNumPms.RackLoc))])
                self._leafs = OrderedDict()

                self.all = PowerMgmt.Config.RedundancyNumPms.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"

                self.rack_loc = PowerMgmt.Config.RedundancyNumPms.RackLoc()
                self.rack_loc.parent = self
                self._children_name_map["rack_loc"] = "rack_loc"
                self._segment_path = lambda: "redundancy-num-pms"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PowerMgmt.Config.RedundancyNumPms, [], name, value)


            class All(Entity):
                """
                
                
                .. attribute:: num_pm
                
                	
                	**type**\: int
                
                	**range:** 0..1
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(PowerMgmt.Config.RedundancyNumPms.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "redundancy-num-pms"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('num_pm', (YLeaf(YType.uint32, 'num_pm'), ['int'])),
                    ])
                    self.num_pm = None
                    self._segment_path = lambda: "all"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/redundancy-num-pms/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PowerMgmt.Config.RedundancyNumPms.All, ['num_pm'], name, value)


            class RackLoc(Entity):
                """
                
                
                .. attribute:: location
                
                	
                	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.RedundancyNumPms.RackLoc.Location>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(PowerMgmt.Config.RedundancyNumPms.RackLoc, self).__init__()

                    self.yang_name = "rack_loc"
                    self.yang_parent_name = "redundancy-num-pms"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("location", ("location", PowerMgmt.Config.RedundancyNumPms.RackLoc.Location))])
                    self._leafs = OrderedDict()

                    self.location = YList(self)
                    self._segment_path = lambda: "rack_loc"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/redundancy-num-pms/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PowerMgmt.Config.RedundancyNumPms.RackLoc, [], name, value)


                class Location(Entity):
                    """
                    
                    
                    .. attribute:: rackid  (key)
                    
                    	
                    	**type**\:  :py:class:`RackId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types.RackId>`
                    
                    .. attribute:: num_pm
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(PowerMgmt.Config.RedundancyNumPms.RackLoc.Location, self).__init__()

                        self.yang_name = "location"
                        self.yang_parent_name = "rack_loc"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rackid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rackid', (YLeaf(YType.enumeration, 'rackId'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_types', 'RackId', '')])),
                            ('num_pm', (YLeaf(YType.uint32, 'num_pm'), ['int'])),
                        ])
                        self.rackid = None
                        self.num_pm = None
                        self._segment_path = lambda: "location" + "[rackId='" + str(self.rackid) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/redundancy-num-pms/rack_loc/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PowerMgmt.Config.RedundancyNumPms.RackLoc.Location, ['rackid', 'num_pm'], name, value)


        class Progressive(Entity):
            """
            
            
            .. attribute:: enable
            
            	
            	**type**\: list of  		 :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Progressive.Enable>`
            
            

            """

            _prefix = 'envmon'
            _revision = '2018-02-06'

            def __init__(self):
                super(PowerMgmt.Config.Progressive, self).__init__()

                self.yang_name = "progressive"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("enable", ("enable", PowerMgmt.Config.Progressive.Enable))])
                self._leafs = OrderedDict()

                self.enable = YList(self)
                self._segment_path = lambda: "progressive"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PowerMgmt.Config.Progressive, [], name, value)


            class Enable(Entity):
                """
                
                
                .. attribute:: enabled  (key)
                
                	
                	**type**\:  :py:class:`Enabled <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Progressive.Enable.Enabled>`
                
                .. attribute:: syslog_threshold
                
                	
                	**type**\: int
                
                	**range:** 3000..72000
                
                .. attribute:: shutdown_threshold
                
                	
                	**type**\: int
                
                	**range:** 3000..72000
                
                .. attribute:: priority
                
                	
                	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Progressive.Enable.Priority>`
                
                

                """

                _prefix = 'envmon'
                _revision = '2018-02-06'

                def __init__(self):
                    super(PowerMgmt.Config.Progressive.Enable, self).__init__()

                    self.yang_name = "enable"
                    self.yang_parent_name = "progressive"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['enabled']
                    self._child_classes = OrderedDict([("priority", ("priority", PowerMgmt.Config.Progressive.Enable.Priority))])
                    self._leafs = OrderedDict([
                        ('enabled', (YLeaf(YType.enumeration, 'enabled'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui', 'PowerMgmt', 'Config.Progressive.Enable.Enabled')])),
                        ('syslog_threshold', (YLeaf(YType.uint32, 'syslog-threshold'), ['int'])),
                        ('shutdown_threshold', (YLeaf(YType.uint32, 'shutdown-threshold'), ['int'])),
                    ])
                    self.enabled = None
                    self.syslog_threshold = None
                    self.shutdown_threshold = None

                    self.priority = PowerMgmt.Config.Progressive.Enable.Priority()
                    self.priority.parent = self
                    self._children_name_map["priority"] = "priority"
                    self._segment_path = lambda: "enable" + "[enabled='" + str(self.enabled) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-envmon-ui:power-mgmt/config/progressive/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PowerMgmt.Config.Progressive.Enable, ['enabled', 'syslog_threshold', 'shutdown_threshold'], name, value)

                class Enabled(Enum):
                    """
                    Enabled (Enum Class)

                    .. data:: enable = 0

                    """

                    enable = Enum.YLeaf(0, "enable")



                class Priority(Entity):
                    """
                    
                    
                    .. attribute:: location
                    
                    	
                    	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_envmon_ui.PowerMgmt.Config.Progressive.Enable.Priority.Location>`
                    
                    

                    """

                    _prefix = 'envmon'
                    _revision = '2018-02-06'

                    def __init__(self):
                        super(PowerMgmt.Config.Progressive.Enable.Priority, self).__init__()

                        self.yang_name = "priority"
                        self.yang_parent_name = "enable"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("location", ("location", PowerMgmt.Config.Progressive.Enable.Priority.Location))])
                        self._leafs = OrderedDict()

                        self.location = YList(self)
                        self._segment_path = lambda: "priority"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PowerMgmt.Config.Progressive.Enable.Priority, [], name, value)


                    class Location(Entity):
                        """
                        
                        
                        .. attribute:: loc  (key)
                        
                        	
                        	**type**\: str
                        
                        	**pattern:** 0/([0\-9]\|1[0\-9])
                        
                        .. attribute:: prior
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..19
                        
                        

                        """

                        _prefix = 'envmon'
                        _revision = '2018-02-06'

                        def __init__(self):
                            super(PowerMgmt.Config.Progressive.Enable.Priority.Location, self).__init__()

                            self.yang_name = "location"
                            self.yang_parent_name = "priority"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['loc']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('loc', (YLeaf(YType.str, 'loc'), ['str'])),
                                ('prior', (YLeaf(YType.uint32, 'prior'), ['int'])),
                            ])
                            self.loc = None
                            self.prior = None
                            self._segment_path = lambda: "location" + "[loc='" + str(self.loc) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PowerMgmt.Config.Progressive.Enable.Priority.Location, ['loc', 'prior'], name, value)

    def clone_ptr(self):
        self._top_entity = PowerMgmt()
        return self._top_entity

