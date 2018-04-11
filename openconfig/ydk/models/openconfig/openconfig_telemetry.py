""" openconfig_telemetry 

Data model which creates the configuration for the telemetry
systems and functions on the device.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class TelemetryStreamProtocol(Enum):
    """
    TelemetryStreamProtocol (Enum Class)

    Selectable protocols for transport

    of the telemetry stream

    .. data:: TCP = 0

    	TCP protocol transport for the stream

    .. data:: UDP = 1

    	UDP protocol transport for the stream

    """

    TCP = Enum.YLeaf(0, "TCP")

    UDP = Enum.YLeaf(1, "UDP")



class TelemetrySystem(Entity):
    """
    Top level configuration and state for the
    device's telemetry system.
    
    .. attribute:: sensor_groups
    
    	Top level container for sensor\-groups
    	**type**\:  :py:class:`SensorGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups>`
    
    .. attribute:: destination_groups
    
    	Top level container for destination group configuration and state
    	**type**\:  :py:class:`DestinationGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups>`
    
    .. attribute:: subscriptions
    
    	This container holds information for both persistent and dynamic telemetry subscriptions
    	**type**\:  :py:class:`Subscriptions <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions>`
    
    

    """

    _prefix = 'oc-telemetry'
    _revision = '2016-02-04'

    def __init__(self):
        super(TelemetrySystem, self).__init__()
        self._top_entity = None

        self.yang_name = "telemetry-system"
        self.yang_parent_name = "openconfig-telemetry"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("sensor-groups", ("sensor_groups", TelemetrySystem.SensorGroups)), ("destination-groups", ("destination_groups", TelemetrySystem.DestinationGroups)), ("subscriptions", ("subscriptions", TelemetrySystem.Subscriptions))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.sensor_groups = TelemetrySystem.SensorGroups()
        self.sensor_groups.parent = self
        self._children_name_map["sensor_groups"] = "sensor-groups"
        self._children_yang_names.add("sensor-groups")

        self.destination_groups = TelemetrySystem.DestinationGroups()
        self.destination_groups.parent = self
        self._children_name_map["destination_groups"] = "destination-groups"
        self._children_yang_names.add("destination-groups")

        self.subscriptions = TelemetrySystem.Subscriptions()
        self.subscriptions.parent = self
        self._children_name_map["subscriptions"] = "subscriptions"
        self._children_yang_names.add("subscriptions")
        self._segment_path = lambda: "openconfig-telemetry:telemetry-system"


    class SensorGroups(Entity):
        """
        Top level container for sensor\-groups.
        
        .. attribute:: sensor_group
        
        	List of telemetry sensory groups on the local system, where a sensor grouping represents a resuable grouping of multiple paths and exclude filters
        	**type**\: list of  		 :py:class:`SensorGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            super(TelemetrySystem.SensorGroups, self).__init__()

            self.yang_name = "sensor-groups"
            self.yang_parent_name = "telemetry-system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sensor-group", ("sensor_group", TelemetrySystem.SensorGroups.SensorGroup))])
            self._leafs = OrderedDict()

            self.sensor_group = YList(self)
            self._segment_path = lambda: "sensor-groups"
            self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetrySystem.SensorGroups, [], name, value)


        class SensorGroup(Entity):
            """
            List of telemetry sensory groups on the local
            system, where a sensor grouping represents a resuable
            grouping of multiple paths and exclude filters.
            
            .. attribute:: sensor_group_id  (key)
            
            	Reference to the name or identifier of the sensor grouping
            	**type**\: str
            
            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
            
            .. attribute:: config
            
            	Configuration parameters relating to the telemetry sensor grouping
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
            
            .. attribute:: state
            
            	State information relating to the telemetry sensor group
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.State>`
            
            .. attribute:: sensor_paths
            
            	Top level container to hold a set of sensor paths grouped together
            	**type**\:  :py:class:`SensorPaths <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                super(TelemetrySystem.SensorGroups.SensorGroup, self).__init__()

                self.yang_name = "sensor-group"
                self.yang_parent_name = "sensor-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sensor_group_id']
                self._child_container_classes = OrderedDict([("config", ("config", TelemetrySystem.SensorGroups.SensorGroup.Config)), ("state", ("state", TelemetrySystem.SensorGroups.SensorGroup.State)), ("sensor-paths", ("sensor_paths", TelemetrySystem.SensorGroups.SensorGroup.SensorPaths))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sensor_group_id', YLeaf(YType.str, 'sensor-group-id')),
                ])
                self.sensor_group_id = None

                self.config = TelemetrySystem.SensorGroups.SensorGroup.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = TelemetrySystem.SensorGroups.SensorGroup.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.sensor_paths = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths()
                self.sensor_paths.parent = self
                self._children_name_map["sensor_paths"] = "sensor-paths"
                self._children_yang_names.add("sensor-paths")
                self._segment_path = lambda: "sensor-group" + "[sensor-group-id='" + str(self.sensor_group_id) + "']"
                self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/sensor-groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetrySystem.SensorGroups.SensorGroup, ['sensor_group_id'], name, value)


            class Config(Entity):
                """
                Configuration parameters relating to the
                telemetry sensor grouping
                
                .. attribute:: sensor_group_id
                
                	Name or identifier for the sensor group itself. Will be referenced by other configuration specifying a sensor group
                	**type**\: str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.SensorGroups.SensorGroup.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "sensor-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('sensor_group_id', YLeaf(YType.str, 'sensor-group-id')),
                    ])
                    self.sensor_group_id = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetrySystem.SensorGroups.SensorGroup.Config, ['sensor_group_id'], name, value)


            class State(Entity):
                """
                State information relating to the telemetry
                sensor group
                
                .. attribute:: sensor_group_id
                
                	Name or identifier for the sensor group itself. Will be referenced by other configuration specifying a sensor group
                	**type**\: str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.SensorGroups.SensorGroup.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "sensor-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('sensor_group_id', YLeaf(YType.str, 'sensor-group-id')),
                    ])
                    self.sensor_group_id = None
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetrySystem.SensorGroups.SensorGroup.State, ['sensor_group_id'], name, value)


            class SensorPaths(Entity):
                """
                Top level container to hold a set of sensor
                paths grouped together
                
                .. attribute:: sensor_path
                
                	List of paths in the model which together comprise a sensor grouping. Filters for each path to exclude items are also provided
                	**type**\: list of  		 :py:class:`SensorPath <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths, self).__init__()

                    self.yang_name = "sensor-paths"
                    self.yang_parent_name = "sensor-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("sensor-path", ("sensor_path", TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath))])
                    self._leafs = OrderedDict()

                    self.sensor_path = YList(self)
                    self._segment_path = lambda: "sensor-paths"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths, [], name, value)


                class SensorPath(Entity):
                    """
                    List of paths in the model which together
                    comprise a sensor grouping. Filters for each path
                    to exclude items are also provided.
                    
                    .. attribute:: path  (key)
                    
                    	Reference to the path of interest
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`path <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters to configure a set of data model paths as a sensor grouping
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config>`
                    
                    .. attribute:: state
                    
                    	Configuration parameters to configure a set of data model paths as a sensor grouping
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath, self).__init__()

                        self.yang_name = "sensor-path"
                        self.yang_parent_name = "sensor-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['path']
                        self._child_container_classes = OrderedDict([("config", ("config", TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config)), ("state", ("state", TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('path', YLeaf(YType.str, 'path')),
                        ])
                        self.path = None

                        self.config = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "sensor-path" + "[path='" + str(self.path) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath, ['path'], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters to configure a set
                        of data model paths as a sensor grouping
                        
                        .. attribute:: path
                        
                        	Path to a section of operational state of interest (the sensor)
                        	**type**\: str
                        
                        .. attribute:: exclude_filter
                        
                        	Filter to exclude certain values out of the state values
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "sensor-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('path', YLeaf(YType.str, 'path')),
                                ('exclude_filter', YLeaf(YType.str, 'exclude-filter')),
                            ])
                            self.path = None
                            self.exclude_filter = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config, ['path', 'exclude_filter'], name, value)


                    class State(Entity):
                        """
                        Configuration parameters to configure a set
                        of data model paths as a sensor grouping
                        
                        .. attribute:: path
                        
                        	Path to a section of operational state of interest (the sensor)
                        	**type**\: str
                        
                        .. attribute:: exclude_filter
                        
                        	Filter to exclude certain values out of the state values
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "sensor-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('path', YLeaf(YType.str, 'path')),
                                ('exclude_filter', YLeaf(YType.str, 'exclude-filter')),
                            ])
                            self.path = None
                            self.exclude_filter = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State, ['path', 'exclude_filter'], name, value)


    class DestinationGroups(Entity):
        """
        Top level container for destination group configuration
        and state.
        
        .. attribute:: destination_group
        
        	List of destination\-groups. Destination groups allow the reuse of common telemetry destinations across the telemetry configuration. An operator references a set of destinations via the configurable destination\-group\-identifier.  A destination group may contain one or more telemetry destinations
        	**type**\: list of  		 :py:class:`DestinationGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            super(TelemetrySystem.DestinationGroups, self).__init__()

            self.yang_name = "destination-groups"
            self.yang_parent_name = "telemetry-system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("destination-group", ("destination_group", TelemetrySystem.DestinationGroups.DestinationGroup))])
            self._leafs = OrderedDict()

            self.destination_group = YList(self)
            self._segment_path = lambda: "destination-groups"
            self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetrySystem.DestinationGroups, [], name, value)


        class DestinationGroup(Entity):
            """
            List of destination\-groups. Destination groups allow the
            reuse of common telemetry destinations across the
            telemetry configuration. An operator references a
            set of destinations via the configurable
            destination\-group\-identifier.
            
            A destination group may contain one or more telemetry
            destinations
            
            .. attribute:: group_id  (key)
            
            	Unique identifier for the destination group
            	**type**\: str
            
            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Config>`
            
            .. attribute:: config
            
            	Top level config container for destination groups
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Config>`
            
            .. attribute:: state
            
            	Top level state container for destination groups
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.State>`
            
            .. attribute:: destinations
            
            	The destination container lists the destination information such as IP address and port of the telemetry messages from the network element
            	**type**\:  :py:class:`Destinations <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                super(TelemetrySystem.DestinationGroups.DestinationGroup, self).__init__()

                self.yang_name = "destination-group"
                self.yang_parent_name = "destination-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group_id']
                self._child_container_classes = OrderedDict([("config", ("config", TelemetrySystem.DestinationGroups.DestinationGroup.Config)), ("state", ("state", TelemetrySystem.DestinationGroups.DestinationGroup.State)), ("destinations", ("destinations", TelemetrySystem.DestinationGroups.DestinationGroup.Destinations))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('group_id', YLeaf(YType.str, 'group-id')),
                ])
                self.group_id = None

                self.config = TelemetrySystem.DestinationGroups.DestinationGroup.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = TelemetrySystem.DestinationGroups.DestinationGroup.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.destinations = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations()
                self.destinations.parent = self
                self._children_name_map["destinations"] = "destinations"
                self._children_yang_names.add("destinations")
                self._segment_path = lambda: "destination-group" + "[group-id='" + str(self.group_id) + "']"
                self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/destination-groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetrySystem.DestinationGroups.DestinationGroup, ['group_id'], name, value)


            class Config(Entity):
                """
                Top level config container for destination groups
                
                .. attribute:: group_id
                
                	Unique identifier for the destination group
                	**type**\: str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.DestinationGroups.DestinationGroup.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "destination-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('group_id', YLeaf(YType.str, 'group-id')),
                    ])
                    self.group_id = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetrySystem.DestinationGroups.DestinationGroup.Config, ['group_id'], name, value)


            class State(Entity):
                """
                Top level state container for destination groups
                
                .. attribute:: group_id
                
                	Unique identifier for destination group
                	**type**\: str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.DestinationGroups.DestinationGroup.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "destination-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('group_id', YLeaf(YType.str, 'group-id')),
                    ])
                    self.group_id = None
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetrySystem.DestinationGroups.DestinationGroup.State, ['group_id'], name, value)


            class Destinations(Entity):
                """
                The destination container lists the destination
                information such as IP address and port of the
                telemetry messages from the network element.
                
                .. attribute:: destination
                
                	List of telemetry stream destinations
                	**type**\: list of  		 :py:class:`Destination <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations, self).__init__()

                    self.yang_name = "destinations"
                    self.yang_parent_name = "destination-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("destination", ("destination", TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination))])
                    self._leafs = OrderedDict()

                    self.destination = YList(self)
                    self._segment_path = lambda: "destinations"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations, [], name, value)


                class Destination(Entity):
                    """
                    List of telemetry stream destinations
                    
                    .. attribute:: destination_address  (key)
                    
                    	Reference to the destination address of the telemetry stream
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**refers to**\:  :py:class:`destination_address <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config>`
                    
                    .. attribute:: destination_port  (key)
                    
                    	Reference to the port number of the stream destination
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`destination_port <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to telemetry destinations
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with telemetry destinations
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination, self).__init__()

                        self.yang_name = "destination"
                        self.yang_parent_name = "destinations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['destination_address','destination_port']
                        self._child_container_classes = OrderedDict([("config", ("config", TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config)), ("state", ("state", TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('destination_address', YLeaf(YType.str, 'destination-address')),
                            ('destination_port', YLeaf(YType.str, 'destination-port')),
                        ])
                        self.destination_address = None
                        self.destination_port = None

                        self.config = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "destination" + "[destination-address='" + str(self.destination_address) + "']" + "[destination-port='" + str(self.destination_port) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination, ['destination_address', 'destination_port'], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters relating to
                        telemetry destinations
                        
                        .. attribute:: destination_address
                        
                        	IP address of the telemetry stream destination
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_port
                        
                        	Protocol (udp or tcp) port number for the telemetry stream destination
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_protocol
                        
                        	Protocol used to transmit telemetry data to the collector
                        	**type**\:  :py:class:`TelemetryStreamProtocol <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocol>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "destination"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('destination_address', YLeaf(YType.str, 'destination-address')),
                                ('destination_port', YLeaf(YType.uint16, 'destination-port')),
                                ('destination_protocol', YLeaf(YType.enumeration, 'destination-protocol')),
                            ])
                            self.destination_address = None
                            self.destination_port = None
                            self.destination_protocol = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config, ['destination_address', 'destination_port', 'destination_protocol'], name, value)


                    class State(Entity):
                        """
                        State information associated with
                        telemetry destinations
                        
                        .. attribute:: destination_address
                        
                        	IP address of the telemetry stream destination
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: destination_port
                        
                        	Protocol (udp or tcp) port number for the telemetry stream destination
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_protocol
                        
                        	Protocol used to transmit telemetry data to the collector
                        	**type**\:  :py:class:`TelemetryStreamProtocol <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocol>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "destination"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('destination_address', YLeaf(YType.str, 'destination-address')),
                                ('destination_port', YLeaf(YType.uint16, 'destination-port')),
                                ('destination_protocol', YLeaf(YType.enumeration, 'destination-protocol')),
                            ])
                            self.destination_address = None
                            self.destination_port = None
                            self.destination_protocol = None
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State, ['destination_address', 'destination_port', 'destination_protocol'], name, value)


    class Subscriptions(Entity):
        """
        This container holds information for both persistent
        and dynamic telemetry subscriptions.
        
        .. attribute:: persistent
        
        	This container holds information relating to persistent telemetry subscriptions. A persistent telemetry subscription is configued locally on the device through configuration, and is persistent across device restarts or other redundancy changes
        	**type**\:  :py:class:`Persistent <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent>`
        
        .. attribute:: dynamic
        
        	This container holds information relating to dynamic telemetry subscriptions. A dynamic subscription is typically configured through an RPC channel, and does not persist across device restarts, or if the RPC channel is reset or otherwise torn down
        	**type**\:  :py:class:`Dynamic <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            super(TelemetrySystem.Subscriptions, self).__init__()

            self.yang_name = "subscriptions"
            self.yang_parent_name = "telemetry-system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("persistent", ("persistent", TelemetrySystem.Subscriptions.Persistent)), ("dynamic", ("dynamic", TelemetrySystem.Subscriptions.Dynamic))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.persistent = TelemetrySystem.Subscriptions.Persistent()
            self.persistent.parent = self
            self._children_name_map["persistent"] = "persistent"
            self._children_yang_names.add("persistent")

            self.dynamic = TelemetrySystem.Subscriptions.Dynamic()
            self.dynamic.parent = self
            self._children_name_map["dynamic"] = "dynamic"
            self._children_yang_names.add("dynamic")
            self._segment_path = lambda: "subscriptions"
            self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/%s" % self._segment_path()


        class Persistent(Entity):
            """
            This container holds information relating to persistent
            telemetry subscriptions. A persistent telemetry
            subscription is configued locally on the device through
            configuration, and is persistent across device restarts or
            other redundancy changes.
            
            .. attribute:: subscription
            
            	List of telemetry subscriptions. A telemetry subscription consists of a set of collection destinations, stream attributes, and associated paths to state information in the model (sensor data)
            	**type**\: list of  		 :py:class:`Subscription <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                super(TelemetrySystem.Subscriptions.Persistent, self).__init__()

                self.yang_name = "persistent"
                self.yang_parent_name = "subscriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("subscription", ("subscription", TelemetrySystem.Subscriptions.Persistent.Subscription))])
                self._leafs = OrderedDict()

                self.subscription = YList(self)
                self._segment_path = lambda: "persistent"
                self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/subscriptions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetrySystem.Subscriptions.Persistent, [], name, value)


            class Subscription(Entity):
                """
                List of telemetry subscriptions. A telemetry
                subscription consists of a set of collection
                destinations, stream attributes, and associated paths to
                state information in the model (sensor data)
                
                .. attribute:: subscription_id  (key)
                
                	Reference to the identifier of the subscription itself. The id will be the handle to refer to the subscription once created
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**refers to**\:  :py:class:`subscription_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.Config>`
                
                .. attribute:: config
                
                	Config parameters relating to the telemetry subscriptions on the local device
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.Config>`
                
                .. attribute:: state
                
                	State parameters relating to the telemetry subscriptions on the local device
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.State>`
                
                .. attribute:: sensor_profiles
                
                	A sensor profile is a set of sensor groups or individual sensor paths which are associated with a telemetry subscription. This is the source of the telemetry data for the subscription to send to the defined collectors
                	**type**\:  :py:class:`SensorProfiles <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles>`
                
                .. attribute:: destination_groups
                
                	A subscription may specify destination addresses. If the subscription supplies destination addresses, the network element will be the initiator of the telemetry streaming, sending it to the destination(s) specified.  If the destination set is omitted, the subscription preconfigures certain elements such as paths and sample intervals under a specified subscription ID. In this case, the network element will NOT initiate an outbound connection for telemetry, but will wait for an inbound connection from a network management system.  It is expected that the network management system connecting to the network element will reference the preconfigured subscription ID when initiating a subscription
                	**type**\:  :py:class:`DestinationGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.Subscriptions.Persistent.Subscription, self).__init__()

                    self.yang_name = "subscription"
                    self.yang_parent_name = "persistent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['subscription_id']
                    self._child_container_classes = OrderedDict([("config", ("config", TelemetrySystem.Subscriptions.Persistent.Subscription.Config)), ("state", ("state", TelemetrySystem.Subscriptions.Persistent.Subscription.State)), ("sensor-profiles", ("sensor_profiles", TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles)), ("destination-groups", ("destination_groups", TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('subscription_id', YLeaf(YType.str, 'subscription-id')),
                    ])
                    self.subscription_id = None

                    self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.sensor_profiles = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles()
                    self.sensor_profiles.parent = self
                    self._children_name_map["sensor_profiles"] = "sensor-profiles"
                    self._children_yang_names.add("sensor-profiles")

                    self.destination_groups = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups()
                    self.destination_groups.parent = self
                    self._children_name_map["destination_groups"] = "destination-groups"
                    self._children_yang_names.add("destination-groups")
                    self._segment_path = lambda: "subscription" + "[subscription-id='" + str(self.subscription_id) + "']"
                    self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/subscriptions/persistent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription, ['subscription_id'], name, value)


                class Config(Entity):
                    """
                    Config parameters relating to the telemetry
                    subscriptions on the local device
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: local_source_address
                    
                    	The IP address which will be the source of packets from the device to a telemetry collector destination
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\: int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('subscription_id', YLeaf(YType.uint64, 'subscription-id')),
                            ('local_source_address', YLeaf(YType.str, 'local-source-address')),
                            ('originated_qos_marking', YLeaf(YType.uint8, 'originated-qos-marking')),
                        ])
                        self.subscription_id = None
                        self.local_source_address = None
                        self.originated_qos_marking = None
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.Config, ['subscription_id', 'local_source_address', 'originated_qos_marking'], name, value)


                class State(Entity):
                    """
                    State parameters relating to the telemetry
                    subscriptions on the local device
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: local_source_address
                    
                    	The IP address which will be the source of packets from the device to a telemetry collector destination
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\: int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('subscription_id', YLeaf(YType.uint64, 'subscription-id')),
                            ('local_source_address', YLeaf(YType.str, 'local-source-address')),
                            ('originated_qos_marking', YLeaf(YType.uint8, 'originated-qos-marking')),
                        ])
                        self.subscription_id = None
                        self.local_source_address = None
                        self.originated_qos_marking = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.State, ['subscription_id', 'local_source_address', 'originated_qos_marking'], name, value)


                class SensorProfiles(Entity):
                    """
                    A sensor profile is a set of sensor groups or
                    individual sensor paths which are associated with a
                    telemetry subscription. This is the source of the
                    telemetry data for the subscription to send to the
                    defined collectors.
                    
                    .. attribute:: sensor_profile
                    
                    	List of telemetry sensor groups used in the subscription
                    	**type**\: list of  		 :py:class:`SensorProfile <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles, self).__init__()

                        self.yang_name = "sensor-profiles"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("sensor-profile", ("sensor_profile", TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile))])
                        self._leafs = OrderedDict()

                        self.sensor_profile = YList(self)
                        self._segment_path = lambda: "sensor-profiles"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles, [], name, value)


                    class SensorProfile(Entity):
                        """
                        List of telemetry sensor groups used
                        in the subscription
                        
                        .. attribute:: sensor_group  (key)
                        
                        	Reference to the telemetry sensor group name
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`sensor_group <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to the sensor profile for a subscription
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the sensor profile for a subscription
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile, self).__init__()

                            self.yang_name = "sensor-profile"
                            self.yang_parent_name = "sensor-profiles"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sensor_group']
                            self._child_container_classes = OrderedDict([("config", ("config", TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config)), ("state", ("state", TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sensor_group', YLeaf(YType.str, 'sensor-group')),
                            ])
                            self.sensor_group = None

                            self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "sensor-profile" + "[sensor-group='" + str(self.sensor_group) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile, ['sensor_group'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters related to the sensor
                            profile for a subscription
                            
                            .. attribute:: sensor_group
                            
                            	Reference to the sensor group which is used in the profile
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
                            
                            .. attribute:: sample_interval
                            
                            	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: heartbeat_interval
                            
                            	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: suppress_redundant
                            
                            	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "sensor-profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sensor_group', YLeaf(YType.str, 'sensor-group')),
                                    ('sample_interval', YLeaf(YType.uint64, 'sample-interval')),
                                    ('heartbeat_interval', YLeaf(YType.uint64, 'heartbeat-interval')),
                                    ('suppress_redundant', YLeaf(YType.boolean, 'suppress-redundant')),
                                ])
                                self.sensor_group = None
                                self.sample_interval = None
                                self.heartbeat_interval = None
                                self.suppress_redundant = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config, ['sensor_group', 'sample_interval', 'heartbeat_interval', 'suppress_redundant'], name, value)


                        class State(Entity):
                            """
                            State information relating to the sensor profile
                            for a subscription
                            
                            .. attribute:: sensor_group
                            
                            	Reference to the sensor group which is used in the profile
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
                            
                            .. attribute:: sample_interval
                            
                            	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: heartbeat_interval
                            
                            	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: suppress_redundant
                            
                            	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "sensor-profile"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sensor_group', YLeaf(YType.str, 'sensor-group')),
                                    ('sample_interval', YLeaf(YType.uint64, 'sample-interval')),
                                    ('heartbeat_interval', YLeaf(YType.uint64, 'heartbeat-interval')),
                                    ('suppress_redundant', YLeaf(YType.boolean, 'suppress-redundant')),
                                ])
                                self.sensor_group = None
                                self.sample_interval = None
                                self.heartbeat_interval = None
                                self.suppress_redundant = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State, ['sensor_group', 'sample_interval', 'heartbeat_interval', 'suppress_redundant'], name, value)


                class DestinationGroups(Entity):
                    """
                    A subscription may specify destination addresses.
                    If the subscription supplies destination addresses,
                    the network element will be the initiator of the
                    telemetry streaming, sending it to the destination(s)
                    specified.
                    
                    If the destination set is omitted, the subscription
                    preconfigures certain elements such as paths and
                    sample intervals under a specified subscription ID.
                    In this case, the network element will NOT initiate an
                    outbound connection for telemetry, but will wait for
                    an inbound connection from a network management
                    system.
                    
                    It is expected that the network management system
                    connecting to the network element will reference
                    the preconfigured subscription ID when initiating
                    a subscription.
                    
                    .. attribute:: destination_group
                    
                    	Identifier of the previously defined destination group
                    	**type**\: list of  		 :py:class:`DestinationGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups, self).__init__()

                        self.yang_name = "destination-groups"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("destination-group", ("destination_group", TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup))])
                        self._leafs = OrderedDict()

                        self.destination_group = YList(self)
                        self._segment_path = lambda: "destination-groups"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups, [], name, value)


                    class DestinationGroup(Entity):
                        """
                        Identifier of the previously defined destination
                        group
                        
                        .. attribute:: group_id  (key)
                        
                        	The destination group id references a configured group of destinations for the telemetry stream
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to telemetry destinations
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config>`
                        
                        .. attribute:: state
                        
                        	State information related to telemetry destinations
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup, self).__init__()

                            self.yang_name = "destination-group"
                            self.yang_parent_name = "destination-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['group_id']
                            self._child_container_classes = OrderedDict([("config", ("config", TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config)), ("state", ("state", TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('group_id', YLeaf(YType.str, 'group-id')),
                            ])
                            self.group_id = None

                            self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "destination-group" + "[group-id='" + str(self.group_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup, ['group_id'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters related to telemetry
                            destinations.
                            
                            .. attribute:: group_id
                            
                            	The destination group id references a reusable group of destination addresses and ports for the telemetry stream
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "destination-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_id', YLeaf(YType.str, 'group-id')),
                                ])
                                self.group_id = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config, ['group_id'], name, value)


                        class State(Entity):
                            """
                            State information related to telemetry
                            destinations
                            
                            .. attribute:: group_id
                            
                            	The destination group id references a reusable group of destination addresses and ports for the telemetry stream
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "destination-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('group_id', YLeaf(YType.str, 'group-id')),
                                ])
                                self.group_id = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State, ['group_id'], name, value)


        class Dynamic(Entity):
            """
            This container holds information relating to dynamic
            telemetry subscriptions. A dynamic subscription is
            typically configured through an RPC channel, and does not
            persist across device restarts, or if the RPC channel is
            reset or otherwise torn down.
            
            .. attribute:: subscription
            
            	List representation of telemetry subscriptions that are configured via an inline RPC, otherwise known as dynamic telemetry subscriptions
            	**type**\: list of  		 :py:class:`Subscription <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                super(TelemetrySystem.Subscriptions.Dynamic, self).__init__()

                self.yang_name = "dynamic"
                self.yang_parent_name = "subscriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("subscription", ("subscription", TelemetrySystem.Subscriptions.Dynamic.Subscription))])
                self._leafs = OrderedDict()

                self.subscription = YList(self)
                self._segment_path = lambda: "dynamic"
                self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/subscriptions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetrySystem.Subscriptions.Dynamic, [], name, value)


            class Subscription(Entity):
                """
                List representation of telemetry subscriptions that
                are configured via an inline RPC, otherwise known
                as dynamic telemetry subscriptions.
                
                .. attribute:: subscription_id  (key)
                
                	Reference to the identifier of the subscription itself. The id will be the handle to refer to the subscription once created
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**refers to**\:  :py:class:`subscription_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.State>`
                
                .. attribute:: state
                
                	State information relating to dynamic telemetry subscriptions
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.State>`
                
                .. attribute:: sensor_paths
                
                	Top level container to hold a set of sensor paths grouped together
                	**type**\:  :py:class:`SensorPaths <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.Subscriptions.Dynamic.Subscription, self).__init__()

                    self.yang_name = "subscription"
                    self.yang_parent_name = "dynamic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['subscription_id']
                    self._child_container_classes = OrderedDict([("state", ("state", TelemetrySystem.Subscriptions.Dynamic.Subscription.State)), ("sensor-paths", ("sensor_paths", TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('subscription_id', YLeaf(YType.str, 'subscription-id')),
                    ])
                    self.subscription_id = None

                    self.state = TelemetrySystem.Subscriptions.Dynamic.Subscription.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.sensor_paths = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths()
                    self.sensor_paths.parent = self
                    self._children_name_map["sensor_paths"] = "sensor-paths"
                    self._children_yang_names.add("sensor-paths")
                    self._segment_path = lambda: "subscription" + "[subscription-id='" + str(self.subscription_id) + "']"
                    self._absolute_path = lambda: "openconfig-telemetry:telemetry-system/subscriptions/dynamic/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetrySystem.Subscriptions.Dynamic.Subscription, ['subscription_id'], name, value)


                class State(Entity):
                    """
                    State information relating to dynamic telemetry
                    subscriptions.
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: destination_address
                    
                    	IP address of the telemetry stream destination
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_port
                    
                    	Protocol (udp or tcp) port number for the telemetry stream destination
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_protocol
                    
                    	Protocol used to transmit telemetry data to the collector
                    	**type**\:  :py:class:`TelemetryStreamProtocol <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocol>`
                    
                    .. attribute:: sample_interval
                    
                    	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: heartbeat_interval
                    
                    	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: suppress_redundant
                    
                    	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                    	**type**\: bool
                    
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\: int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Dynamic.Subscription.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('subscription_id', YLeaf(YType.uint64, 'subscription-id')),
                            ('destination_address', YLeaf(YType.str, 'destination-address')),
                            ('destination_port', YLeaf(YType.uint16, 'destination-port')),
                            ('destination_protocol', YLeaf(YType.enumeration, 'destination-protocol')),
                            ('sample_interval', YLeaf(YType.uint64, 'sample-interval')),
                            ('heartbeat_interval', YLeaf(YType.uint64, 'heartbeat-interval')),
                            ('suppress_redundant', YLeaf(YType.boolean, 'suppress-redundant')),
                            ('originated_qos_marking', YLeaf(YType.uint8, 'originated-qos-marking')),
                        ])
                        self.subscription_id = None
                        self.destination_address = None
                        self.destination_port = None
                        self.destination_protocol = None
                        self.sample_interval = None
                        self.heartbeat_interval = None
                        self.suppress_redundant = None
                        self.originated_qos_marking = None
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetrySystem.Subscriptions.Dynamic.Subscription.State, ['subscription_id', 'destination_address', 'destination_port', 'destination_protocol', 'sample_interval', 'heartbeat_interval', 'suppress_redundant', 'originated_qos_marking'], name, value)


                class SensorPaths(Entity):
                    """
                    Top level container to hold a set of sensor
                    paths grouped together
                    
                    .. attribute:: sensor_path
                    
                    	List of paths in the model which together comprise a sensor grouping. Filters for each path to exclude items are also provided
                    	**type**\: list of  		 :py:class:`SensorPath <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths, self).__init__()

                        self.yang_name = "sensor-paths"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("sensor-path", ("sensor_path", TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath))])
                        self._leafs = OrderedDict()

                        self.sensor_path = YList(self)
                        self._segment_path = lambda: "sensor-paths"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths, [], name, value)


                    class SensorPath(Entity):
                        """
                        List of paths in the model which together
                        comprise a sensor grouping. Filters for each path
                        to exclude items are also provided.
                        
                        .. attribute:: path  (key)
                        
                        	Reference to the path of interest
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`path <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State>`
                        
                        .. attribute:: state
                        
                        	State information for a dynamic subscription's paths of interest
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath, self).__init__()

                            self.yang_name = "sensor-path"
                            self.yang_parent_name = "sensor-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['path']
                            self._child_container_classes = OrderedDict([("state", ("state", TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('path', YLeaf(YType.str, 'path')),
                            ])
                            self.path = None

                            self.state = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "sensor-path" + "[path='" + str(self.path) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath, ['path'], name, value)


                        class State(Entity):
                            """
                            State information for a dynamic subscription's
                            paths of interest
                            
                            .. attribute:: path
                            
                            	Path to a section of operational state of interest (the sensor)
                            	**type**\: str
                            
                            .. attribute:: exclude_filter
                            
                            	Filter to exclude certain values out of the state values
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "sensor-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('path', YLeaf(YType.str, 'path')),
                                    ('exclude_filter', YLeaf(YType.str, 'exclude-filter')),
                                ])
                                self.path = None
                                self.exclude_filter = None
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State, ['path', 'exclude_filter'], name, value)

    def clone_ptr(self):
        self._top_entity = TelemetrySystem()
        return self._top_entity

