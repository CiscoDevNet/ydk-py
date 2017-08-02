""" openconfig_telemetry 

Data model which creates the configuration for the telemetry
systems and functions on the device.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class TelemetryStreamProtocol(Enum):
    """
    TelemetryStreamProtocol

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
    
    .. attribute:: destination_groups
    
    	Top level container for destination group configuration and state
    	**type**\:   :py:class:`DestinationGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups>`
    
    .. attribute:: sensor_groups
    
    	Top level container for sensor\-groups
    	**type**\:   :py:class:`SensorGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups>`
    
    .. attribute:: subscriptions
    
    	This container holds information for both persistent and dynamic telemetry subscriptions
    	**type**\:   :py:class:`Subscriptions <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions>`
    
    

    """

    _prefix = 'oc-telemetry'
    _revision = '2016-02-04'

    def __init__(self):
        super(TelemetrySystem, self).__init__()
        self._top_entity = None

        self.yang_name = "telemetry-system"
        self.yang_parent_name = "openconfig-telemetry"

        self.destination_groups = TelemetrySystem.DestinationGroups()
        self.destination_groups.parent = self
        self._children_name_map["destination_groups"] = "destination-groups"
        self._children_yang_names.add("destination-groups")

        self.sensor_groups = TelemetrySystem.SensorGroups()
        self.sensor_groups.parent = self
        self._children_name_map["sensor_groups"] = "sensor-groups"
        self._children_yang_names.add("sensor-groups")

        self.subscriptions = TelemetrySystem.Subscriptions()
        self.subscriptions.parent = self
        self._children_name_map["subscriptions"] = "subscriptions"
        self._children_yang_names.add("subscriptions")


    class SensorGroups(Entity):
        """
        Top level container for sensor\-groups.
        
        .. attribute:: sensor_group
        
        	List of telemetry sensory groups on the local system, where a sensor grouping represents a resuable grouping of multiple paths and exclude filters
        	**type**\: list of    :py:class:`SensorGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            super(TelemetrySystem.SensorGroups, self).__init__()

            self.yang_name = "sensor-groups"
            self.yang_parent_name = "telemetry-system"

            self.sensor_group = YList(self)

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
                        super(TelemetrySystem.SensorGroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TelemetrySystem.SensorGroups, self).__setattr__(name, value)


        class SensorGroup(Entity):
            """
            List of telemetry sensory groups on the local
            system, where a sensor grouping represents a resuable
            grouping of multiple paths and exclude filters.
            
            .. attribute:: sensor_group_id  <key>
            
            	Reference to the name or identifier of the sensor grouping
            	**type**\:  str
            
            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
            
            .. attribute:: config
            
            	Configuration parameters relating to the telemetry sensor grouping
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
            
            .. attribute:: sensor_paths
            
            	Top level container to hold a set of sensor paths grouped together
            	**type**\:   :py:class:`SensorPaths <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths>`
            
            .. attribute:: state
            
            	State information relating to the telemetry sensor group
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.State>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                super(TelemetrySystem.SensorGroups.SensorGroup, self).__init__()

                self.yang_name = "sensor-group"
                self.yang_parent_name = "sensor-groups"

                self.sensor_group_id = YLeaf(YType.str, "sensor-group-id")

                self.config = TelemetrySystem.SensorGroups.SensorGroup.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.sensor_paths = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths()
                self.sensor_paths.parent = self
                self._children_name_map["sensor_paths"] = "sensor-paths"
                self._children_yang_names.add("sensor-paths")

                self.state = TelemetrySystem.SensorGroups.SensorGroup.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sensor_group_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TelemetrySystem.SensorGroups.SensorGroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetrySystem.SensorGroups.SensorGroup, self).__setattr__(name, value)


            class Config(Entity):
                """
                Configuration parameters relating to the
                telemetry sensor grouping
                
                .. attribute:: sensor_group_id
                
                	Name or identifier for the sensor group itself. Will be referenced by other configuration specifying a sensor group
                	**type**\:  str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.SensorGroups.SensorGroup.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "sensor-group"

                    self.sensor_group_id = YLeaf(YType.str, "sensor-group-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("sensor_group_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetrySystem.SensorGroups.SensorGroup.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetrySystem.SensorGroups.SensorGroup.Config, self).__setattr__(name, value)

                def has_data(self):
                    return self.sensor_group_id.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.sensor_group_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "config" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.sensor_group_id.is_set or self.sensor_group_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sensor_group_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sensor-group-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "sensor-group-id"):
                        self.sensor_group_id = value
                        self.sensor_group_id.value_namespace = name_space
                        self.sensor_group_id.value_namespace_prefix = name_space_prefix


            class State(Entity):
                """
                State information relating to the telemetry
                sensor group
                
                .. attribute:: sensor_group_id
                
                	Name or identifier for the sensor group itself. Will be referenced by other configuration specifying a sensor group
                	**type**\:  str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.SensorGroups.SensorGroup.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "sensor-group"

                    self.sensor_group_id = YLeaf(YType.str, "sensor-group-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("sensor_group_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetrySystem.SensorGroups.SensorGroup.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetrySystem.SensorGroups.SensorGroup.State, self).__setattr__(name, value)

                def has_data(self):
                    return self.sensor_group_id.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.sensor_group_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.sensor_group_id.is_set or self.sensor_group_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sensor_group_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sensor-group-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "sensor-group-id"):
                        self.sensor_group_id = value
                        self.sensor_group_id.value_namespace = name_space
                        self.sensor_group_id.value_namespace_prefix = name_space_prefix


            class SensorPaths(Entity):
                """
                Top level container to hold a set of sensor
                paths grouped together
                
                .. attribute:: sensor_path
                
                	List of paths in the model which together comprise a sensor grouping. Filters for each path to exclude items are also provided
                	**type**\: list of    :py:class:`SensorPath <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths, self).__init__()

                    self.yang_name = "sensor-paths"
                    self.yang_parent_name = "sensor-group"

                    self.sensor_path = YList(self)

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
                                super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths, self).__setattr__(name, value)


                class SensorPath(Entity):
                    """
                    List of paths in the model which together
                    comprise a sensor grouping. Filters for each path
                    to exclude items are also provided.
                    
                    .. attribute:: path  <key>
                    
                    	Reference to the path of interest
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`path <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters to configure a set of data model paths as a sensor grouping
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config>`
                    
                    .. attribute:: state
                    
                    	Configuration parameters to configure a set of data model paths as a sensor grouping
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath, self).__init__()

                        self.yang_name = "sensor-path"
                        self.yang_parent_name = "sensor-paths"

                        self.path = YLeaf(YType.str, "path")

                        self.config = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("path") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration parameters to configure a set
                        of data model paths as a sensor grouping
                        
                        .. attribute:: exclude_filter
                        
                        	Filter to exclude certain values out of the state values
                        	**type**\:  str
                        
                        .. attribute:: path
                        
                        	Path to a section of operational state of interest (the sensor)
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "sensor-path"

                            self.exclude_filter = YLeaf(YType.str, "exclude-filter")

                            self.path = YLeaf(YType.str, "path")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("exclude_filter",
                                            "path") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.exclude_filter.is_set or
                                self.path.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.exclude_filter.yfilter != YFilter.not_set or
                                self.path.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "config" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.exclude_filter.is_set or self.exclude_filter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.exclude_filter.get_name_leafdata())
                            if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "exclude-filter" or name == "path"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "exclude-filter"):
                                self.exclude_filter = value
                                self.exclude_filter.value_namespace = name_space
                                self.exclude_filter.value_namespace_prefix = name_space_prefix
                            if(value_path == "path"):
                                self.path = value
                                self.path.value_namespace = name_space
                                self.path.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        Configuration parameters to configure a set
                        of data model paths as a sensor grouping
                        
                        .. attribute:: exclude_filter
                        
                        	Filter to exclude certain values out of the state values
                        	**type**\:  str
                        
                        .. attribute:: path
                        
                        	Path to a section of operational state of interest (the sensor)
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "sensor-path"

                            self.exclude_filter = YLeaf(YType.str, "exclude-filter")

                            self.path = YLeaf(YType.str, "path")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("exclude_filter",
                                            "path") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.exclude_filter.is_set or
                                self.path.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.exclude_filter.yfilter != YFilter.not_set or
                                self.path.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "state" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.exclude_filter.is_set or self.exclude_filter.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.exclude_filter.get_name_leafdata())
                            if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "exclude-filter" or name == "path"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "exclude-filter"):
                                self.exclude_filter = value
                                self.exclude_filter.value_namespace = name_space
                                self.exclude_filter.value_namespace_prefix = name_space_prefix
                            if(value_path == "path"):
                                self.path = value
                                self.path.value_namespace = name_space
                                self.path.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.path.is_set or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.path.yfilter != YFilter.not_set or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sensor-path" + "[path='" + self.path.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config" or name == "state" or name == "path"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "path"):
                            self.path = value
                            self.path.value_namespace = name_space
                            self.path.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.sensor_path:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.sensor_path:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sensor-paths" + path_buffer

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

                    if (child_yang_name == "sensor-path"):
                        for c in self.sensor_path:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths.SensorPath()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.sensor_path.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sensor-path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.sensor_group_id.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.sensor_paths is not None and self.sensor_paths.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sensor_group_id.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.sensor_paths is not None and self.sensor_paths.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sensor-group" + "[sensor-group-id='" + self.sensor_group_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-telemetry:telemetry-system/sensor-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sensor_group_id.is_set or self.sensor_group_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sensor_group_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = TelemetrySystem.SensorGroups.SensorGroup.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "sensor-paths"):
                    if (self.sensor_paths is None):
                        self.sensor_paths = TelemetrySystem.SensorGroups.SensorGroup.SensorPaths()
                        self.sensor_paths.parent = self
                        self._children_name_map["sensor_paths"] = "sensor-paths"
                    return self.sensor_paths

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = TelemetrySystem.SensorGroups.SensorGroup.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "sensor-paths" or name == "state" or name == "sensor-group-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sensor-group-id"):
                    self.sensor_group_id = value
                    self.sensor_group_id.value_namespace = name_space
                    self.sensor_group_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sensor_group:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sensor_group:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sensor-groups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-telemetry:telemetry-system/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sensor-group"):
                for c in self.sensor_group:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TelemetrySystem.SensorGroups.SensorGroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sensor_group.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sensor-group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class DestinationGroups(Entity):
        """
        Top level container for destination group configuration
        and state.
        
        .. attribute:: destination_group
        
        	List of destination\-groups. Destination groups allow the reuse of common telemetry destinations across the telemetry configuration. An operator references a set of destinations via the configurable destination\-group\-identifier.  A destination group may contain one or more telemetry destinations
        	**type**\: list of    :py:class:`DestinationGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            super(TelemetrySystem.DestinationGroups, self).__init__()

            self.yang_name = "destination-groups"
            self.yang_parent_name = "telemetry-system"

            self.destination_group = YList(self)

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
                        super(TelemetrySystem.DestinationGroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TelemetrySystem.DestinationGroups, self).__setattr__(name, value)


        class DestinationGroup(Entity):
            """
            List of destination\-groups. Destination groups allow the
            reuse of common telemetry destinations across the
            telemetry configuration. An operator references a
            set of destinations via the configurable
            destination\-group\-identifier.
            
            A destination group may contain one or more telemetry
            destinations
            
            .. attribute:: group_id  <key>
            
            	Unique identifier for the destination group
            	**type**\:  str
            
            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Config>`
            
            .. attribute:: config
            
            	Top level config container for destination groups
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Config>`
            
            .. attribute:: destinations
            
            	The destination container lists the destination information such as IP address and port of the telemetry messages from the network element
            	**type**\:   :py:class:`Destinations <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations>`
            
            .. attribute:: state
            
            	Top level state container for destination groups
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.State>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                super(TelemetrySystem.DestinationGroups.DestinationGroup, self).__init__()

                self.yang_name = "destination-group"
                self.yang_parent_name = "destination-groups"

                self.group_id = YLeaf(YType.str, "group-id")

                self.config = TelemetrySystem.DestinationGroups.DestinationGroup.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.destinations = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations()
                self.destinations.parent = self
                self._children_name_map["destinations"] = "destinations"
                self._children_yang_names.add("destinations")

                self.state = TelemetrySystem.DestinationGroups.DestinationGroup.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("group_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TelemetrySystem.DestinationGroups.DestinationGroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetrySystem.DestinationGroups.DestinationGroup, self).__setattr__(name, value)


            class Config(Entity):
                """
                Top level config container for destination groups
                
                .. attribute:: group_id
                
                	Unique identifier for the destination group
                	**type**\:  str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.DestinationGroups.DestinationGroup.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "destination-group"

                    self.group_id = YLeaf(YType.str, "group-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("group_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetrySystem.DestinationGroups.DestinationGroup.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetrySystem.DestinationGroups.DestinationGroup.Config, self).__setattr__(name, value)

                def has_data(self):
                    return self.group_id.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.group_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "config" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "group-id"):
                        self.group_id = value
                        self.group_id.value_namespace = name_space
                        self.group_id.value_namespace_prefix = name_space_prefix


            class State(Entity):
                """
                Top level state container for destination groups
                
                .. attribute:: group_id
                
                	Unique identifier for destination group
                	**type**\:  str
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.DestinationGroups.DestinationGroup.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "destination-group"

                    self.group_id = YLeaf(YType.str, "group-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("group_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetrySystem.DestinationGroups.DestinationGroup.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetrySystem.DestinationGroups.DestinationGroup.State, self).__setattr__(name, value)

                def has_data(self):
                    return self.group_id.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.group_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "group-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "group-id"):
                        self.group_id = value
                        self.group_id.value_namespace = name_space
                        self.group_id.value_namespace_prefix = name_space_prefix


            class Destinations(Entity):
                """
                The destination container lists the destination
                information such as IP address and port of the
                telemetry messages from the network element.
                
                .. attribute:: destination
                
                	List of telemetry stream destinations
                	**type**\: list of    :py:class:`Destination <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations, self).__init__()

                    self.yang_name = "destinations"
                    self.yang_parent_name = "destination-group"

                    self.destination = YList(self)

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
                                super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations, self).__setattr__(name, value)


                class Destination(Entity):
                    """
                    List of telemetry stream destinations
                    
                    .. attribute:: destination_address  <key>
                    
                    	Reference to the destination address of the telemetry stream
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: destination_port  <key>
                    
                    	Reference to the port number of the stream destination
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`destination_port <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to telemetry destinations
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with telemetry destinations
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination, self).__init__()

                        self.yang_name = "destination"
                        self.yang_parent_name = "destinations"

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.destination_port = YLeaf(YType.str, "destination-port")

                        self.config = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("destination_address",
                                        "destination_port") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration parameters relating to
                        telemetry destinations
                        
                        .. attribute:: destination_address
                        
                        	IP address of the telemetry stream destination
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: destination_port
                        
                        	Protocol (udp or tcp) port number for the telemetry stream destination
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_protocol
                        
                        	Protocol used to transmit telemetry data to the collector
                        	**type**\:   :py:class:`TelemetryStreamProtocol <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocol>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "destination"

                            self.destination_address = YLeaf(YType.str, "destination-address")

                            self.destination_port = YLeaf(YType.uint16, "destination-port")

                            self.destination_protocol = YLeaf(YType.enumeration, "destination-protocol")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("destination_address",
                                            "destination_port",
                                            "destination_protocol") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.destination_address.is_set or
                                self.destination_port.is_set or
                                self.destination_protocol.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.destination_address.yfilter != YFilter.not_set or
                                self.destination_port.yfilter != YFilter.not_set or
                                self.destination_protocol.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "config" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_address.get_name_leafdata())
                            if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_port.get_name_leafdata())
                            if (self.destination_protocol.is_set or self.destination_protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_protocol.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "destination-address" or name == "destination-port" or name == "destination-protocol"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "destination-address"):
                                self.destination_address = value
                                self.destination_address.value_namespace = name_space
                                self.destination_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-port"):
                                self.destination_port = value
                                self.destination_port.value_namespace = name_space
                                self.destination_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-protocol"):
                                self.destination_protocol = value
                                self.destination_protocol.value_namespace = name_space
                                self.destination_protocol.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        State information associated with
                        telemetry destinations
                        
                        .. attribute:: destination_address
                        
                        	IP address of the telemetry stream destination
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: destination_port
                        
                        	Protocol (udp or tcp) port number for the telemetry stream destination
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_protocol
                        
                        	Protocol used to transmit telemetry data to the collector
                        	**type**\:   :py:class:`TelemetryStreamProtocol <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocol>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "destination"

                            self.destination_address = YLeaf(YType.str, "destination-address")

                            self.destination_port = YLeaf(YType.uint16, "destination-port")

                            self.destination_protocol = YLeaf(YType.enumeration, "destination-protocol")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("destination_address",
                                            "destination_port",
                                            "destination_protocol") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.destination_address.is_set or
                                self.destination_port.is_set or
                                self.destination_protocol.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.destination_address.yfilter != YFilter.not_set or
                                self.destination_port.yfilter != YFilter.not_set or
                                self.destination_protocol.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "state" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_address.get_name_leafdata())
                            if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_port.get_name_leafdata())
                            if (self.destination_protocol.is_set or self.destination_protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_protocol.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "destination-address" or name == "destination-port" or name == "destination-protocol"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "destination-address"):
                                self.destination_address = value
                                self.destination_address.value_namespace = name_space
                                self.destination_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-port"):
                                self.destination_port = value
                                self.destination_port.value_namespace = name_space
                                self.destination_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-protocol"):
                                self.destination_protocol = value
                                self.destination_protocol.value_namespace = name_space
                                self.destination_protocol.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.destination_address.is_set or
                            self.destination_port.is_set or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.destination_port.yfilter != YFilter.not_set or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination" + "[destination-address='" + self.destination_address.get() + "']" + "[destination-port='" + self.destination_port.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_port.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config" or name == "state" or name == "destination-address" or name == "destination-port"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-port"):
                            self.destination_port = value
                            self.destination_port.value_namespace = name_space
                            self.destination_port.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.destination:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.destination:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destinations" + path_buffer

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

                    if (child_yang_name == "destination"):
                        for c in self.destination:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations.Destination()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.destination.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.group_id.is_set or
                    (self.config is not None and self.config.has_data()) or
                    (self.destinations is not None and self.destinations.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.group_id.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.destinations is not None and self.destinations.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "destination-group" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-telemetry:telemetry-system/destination-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.group_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = TelemetrySystem.DestinationGroups.DestinationGroup.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "destinations"):
                    if (self.destinations is None):
                        self.destinations = TelemetrySystem.DestinationGroups.DestinationGroup.Destinations()
                        self.destinations.parent = self
                        self._children_name_map["destinations"] = "destinations"
                    return self.destinations

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = TelemetrySystem.DestinationGroups.DestinationGroup.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "destinations" or name == "state" or name == "group-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "group-id"):
                    self.group_id = value
                    self.group_id.value_namespace = name_space
                    self.group_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.destination_group:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.destination_group:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "destination-groups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-telemetry:telemetry-system/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "destination-group"):
                for c in self.destination_group:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TelemetrySystem.DestinationGroups.DestinationGroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.destination_group.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "destination-group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Subscriptions(Entity):
        """
        This container holds information for both persistent
        and dynamic telemetry subscriptions.
        
        .. attribute:: dynamic
        
        	This container holds information relating to dynamic telemetry subscriptions. A dynamic subscription is typically configured through an RPC channel, and does not persist across device restarts, or if the RPC channel is reset or otherwise torn down
        	**type**\:   :py:class:`Dynamic <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic>`
        
        .. attribute:: persistent
        
        	This container holds information relating to persistent telemetry subscriptions. A persistent telemetry subscription is configued locally on the device through configuration, and is persistent across device restarts or other redundancy changes
        	**type**\:   :py:class:`Persistent <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent>`
        
        

        """

        _prefix = 'oc-telemetry'
        _revision = '2016-02-04'

        def __init__(self):
            super(TelemetrySystem.Subscriptions, self).__init__()

            self.yang_name = "subscriptions"
            self.yang_parent_name = "telemetry-system"

            self.dynamic = TelemetrySystem.Subscriptions.Dynamic()
            self.dynamic.parent = self
            self._children_name_map["dynamic"] = "dynamic"
            self._children_yang_names.add("dynamic")

            self.persistent = TelemetrySystem.Subscriptions.Persistent()
            self.persistent.parent = self
            self._children_name_map["persistent"] = "persistent"
            self._children_yang_names.add("persistent")


        class Persistent(Entity):
            """
            This container holds information relating to persistent
            telemetry subscriptions. A persistent telemetry
            subscription is configued locally on the device through
            configuration, and is persistent across device restarts or
            other redundancy changes.
            
            .. attribute:: subscription
            
            	List of telemetry subscriptions. A telemetry subscription consists of a set of collection destinations, stream attributes, and associated paths to state information in the model (sensor data)
            	**type**\: list of    :py:class:`Subscription <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                super(TelemetrySystem.Subscriptions.Persistent, self).__init__()

                self.yang_name = "persistent"
                self.yang_parent_name = "subscriptions"

                self.subscription = YList(self)

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
                            super(TelemetrySystem.Subscriptions.Persistent, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetrySystem.Subscriptions.Persistent, self).__setattr__(name, value)


            class Subscription(Entity):
                """
                List of telemetry subscriptions. A telemetry
                subscription consists of a set of collection
                destinations, stream attributes, and associated paths to
                state information in the model (sensor data)
                
                .. attribute:: subscription_id  <key>
                
                	Reference to the identifier of the subscription itself. The id will be the handle to refer to the subscription once created
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**refers to**\:  :py:class:`subscription_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.Config>`
                
                .. attribute:: config
                
                	Config parameters relating to the telemetry subscriptions on the local device
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.Config>`
                
                .. attribute:: destination_groups
                
                	A subscription may specify destination addresses. If the subscription supplies destination addresses, the network element will be the initiator of the telemetry streaming, sending it to the destination(s) specified.  If the destination set is omitted, the subscription preconfigures certain elements such as paths and sample intervals under a specified subscription ID. In this case, the network element will NOT initiate an outbound connection for telemetry, but will wait for an inbound connection from a network management system.  It is expected that the network management system connecting to the network element will reference the preconfigured subscription ID when initiating a subscription
                	**type**\:   :py:class:`DestinationGroups <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups>`
                
                .. attribute:: sensor_profiles
                
                	A sensor profile is a set of sensor groups or individual sensor paths which are associated with a telemetry subscription. This is the source of the telemetry data for the subscription to send to the defined collectors
                	**type**\:   :py:class:`SensorProfiles <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles>`
                
                .. attribute:: state
                
                	State parameters relating to the telemetry subscriptions on the local device
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.State>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.Subscriptions.Persistent.Subscription, self).__init__()

                    self.yang_name = "subscription"
                    self.yang_parent_name = "persistent"

                    self.subscription_id = YLeaf(YType.str, "subscription-id")

                    self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.destination_groups = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups()
                    self.destination_groups.parent = self
                    self._children_name_map["destination_groups"] = "destination-groups"
                    self._children_yang_names.add("destination-groups")

                    self.sensor_profiles = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles()
                    self.sensor_profiles.parent = self
                    self._children_name_map["sensor_profiles"] = "sensor-profiles"
                    self._children_yang_names.add("sensor-profiles")

                    self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("subscription_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetrySystem.Subscriptions.Persistent.Subscription, self).__setattr__(name, value)


                class Config(Entity):
                    """
                    Config parameters relating to the telemetry
                    subscriptions on the local device
                    
                    .. attribute:: local_source_address
                    
                    	The IP address which will be the source of packets from the device to a telemetry collector destination
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "subscription"

                        self.local_source_address = YLeaf(YType.str, "local-source-address")

                        self.originated_qos_marking = YLeaf(YType.uint8, "originated-qos-marking")

                        self.subscription_id = YLeaf(YType.uint64, "subscription-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("local_source_address",
                                        "originated_qos_marking",
                                        "subscription_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetrySystem.Subscriptions.Persistent.Subscription.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.Config, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.local_source_address.is_set or
                            self.originated_qos_marking.is_set or
                            self.subscription_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.local_source_address.yfilter != YFilter.not_set or
                            self.originated_qos_marking.yfilter != YFilter.not_set or
                            self.subscription_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "config" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.local_source_address.is_set or self.local_source_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_source_address.get_name_leafdata())
                        if (self.originated_qos_marking.is_set or self.originated_qos_marking.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.originated_qos_marking.get_name_leafdata())
                        if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscription_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local-source-address" or name == "originated-qos-marking" or name == "subscription-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "local-source-address"):
                            self.local_source_address = value
                            self.local_source_address.value_namespace = name_space
                            self.local_source_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "originated-qos-marking"):
                            self.originated_qos_marking = value
                            self.originated_qos_marking.value_namespace = name_space
                            self.originated_qos_marking.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscription-id"):
                            self.subscription_id = value
                            self.subscription_id.value_namespace = name_space
                            self.subscription_id.value_namespace_prefix = name_space_prefix


                class State(Entity):
                    """
                    State parameters relating to the telemetry
                    subscriptions on the local device
                    
                    .. attribute:: local_source_address
                    
                    	The IP address which will be the source of packets from the device to a telemetry collector destination
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "subscription"

                        self.local_source_address = YLeaf(YType.str, "local-source-address")

                        self.originated_qos_marking = YLeaf(YType.uint8, "originated-qos-marking")

                        self.subscription_id = YLeaf(YType.uint64, "subscription-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("local_source_address",
                                        "originated_qos_marking",
                                        "subscription_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetrySystem.Subscriptions.Persistent.Subscription.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.State, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.local_source_address.is_set or
                            self.originated_qos_marking.is_set or
                            self.subscription_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.local_source_address.yfilter != YFilter.not_set or
                            self.originated_qos_marking.yfilter != YFilter.not_set or
                            self.subscription_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "state" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.local_source_address.is_set or self.local_source_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_source_address.get_name_leafdata())
                        if (self.originated_qos_marking.is_set or self.originated_qos_marking.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.originated_qos_marking.get_name_leafdata())
                        if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscription_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local-source-address" or name == "originated-qos-marking" or name == "subscription-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "local-source-address"):
                            self.local_source_address = value
                            self.local_source_address.value_namespace = name_space
                            self.local_source_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "originated-qos-marking"):
                            self.originated_qos_marking = value
                            self.originated_qos_marking.value_namespace = name_space
                            self.originated_qos_marking.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscription-id"):
                            self.subscription_id = value
                            self.subscription_id.value_namespace = name_space
                            self.subscription_id.value_namespace_prefix = name_space_prefix


                class SensorProfiles(Entity):
                    """
                    A sensor profile is a set of sensor groups or
                    individual sensor paths which are associated with a
                    telemetry subscription. This is the source of the
                    telemetry data for the subscription to send to the
                    defined collectors.
                    
                    .. attribute:: sensor_profile
                    
                    	List of telemetry sensor groups used in the subscription
                    	**type**\: list of    :py:class:`SensorProfile <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles, self).__init__()

                        self.yang_name = "sensor-profiles"
                        self.yang_parent_name = "subscription"

                        self.sensor_profile = YList(self)

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
                                    super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles, self).__setattr__(name, value)


                    class SensorProfile(Entity):
                        """
                        List of telemetry sensor groups used
                        in the subscription
                        
                        .. attribute:: sensor_group  <key>
                        
                        	Reference to the telemetry sensor group name
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`sensor_group <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to the sensor profile for a subscription
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config>`
                        
                        .. attribute:: state
                        
                        	State information relating to the sensor profile for a subscription
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile, self).__init__()

                            self.yang_name = "sensor-profile"
                            self.yang_parent_name = "sensor-profiles"

                            self.sensor_group = YLeaf(YType.str, "sensor-group")

                            self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("sensor_group") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile, self).__setattr__(name, value)


                        class Config(Entity):
                            """
                            Configuration parameters related to the sensor
                            profile for a subscription
                            
                            .. attribute:: heartbeat_interval
                            
                            	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sample_interval
                            
                            	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sensor_group
                            
                            	Reference to the sensor group which is used in the profile
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
                            
                            .. attribute:: suppress_redundant
                            
                            	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "sensor-profile"

                                self.heartbeat_interval = YLeaf(YType.uint64, "heartbeat-interval")

                                self.sample_interval = YLeaf(YType.uint64, "sample-interval")

                                self.sensor_group = YLeaf(YType.str, "sensor-group")

                                self.suppress_redundant = YLeaf(YType.boolean, "suppress-redundant")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("heartbeat_interval",
                                                "sample_interval",
                                                "sensor_group",
                                                "suppress_redundant") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.heartbeat_interval.is_set or
                                    self.sample_interval.is_set or
                                    self.sensor_group.is_set or
                                    self.suppress_redundant.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.heartbeat_interval.yfilter != YFilter.not_set or
                                    self.sample_interval.yfilter != YFilter.not_set or
                                    self.sensor_group.yfilter != YFilter.not_set or
                                    self.suppress_redundant.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "config" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.heartbeat_interval.is_set or self.heartbeat_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.heartbeat_interval.get_name_leafdata())
                                if (self.sample_interval.is_set or self.sample_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_interval.get_name_leafdata())
                                if (self.sensor_group.is_set or self.sensor_group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sensor_group.get_name_leafdata())
                                if (self.suppress_redundant.is_set or self.suppress_redundant.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_redundant.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "heartbeat-interval" or name == "sample-interval" or name == "sensor-group" or name == "suppress-redundant"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "heartbeat-interval"):
                                    self.heartbeat_interval = value
                                    self.heartbeat_interval.value_namespace = name_space
                                    self.heartbeat_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "sample-interval"):
                                    self.sample_interval = value
                                    self.sample_interval.value_namespace = name_space
                                    self.sample_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "sensor-group"):
                                    self.sensor_group = value
                                    self.sensor_group.value_namespace = name_space
                                    self.sensor_group.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-redundant"):
                                    self.suppress_redundant = value
                                    self.suppress_redundant.value_namespace = name_space
                                    self.suppress_redundant.value_namespace_prefix = name_space_prefix


                        class State(Entity):
                            """
                            State information relating to the sensor profile
                            for a subscription
                            
                            .. attribute:: heartbeat_interval
                            
                            	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sample_interval
                            
                            	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sensor_group
                            
                            	Reference to the sensor group which is used in the profile
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`sensor_group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.SensorGroups.SensorGroup.Config>`
                            
                            .. attribute:: suppress_redundant
                            
                            	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "sensor-profile"

                                self.heartbeat_interval = YLeaf(YType.uint64, "heartbeat-interval")

                                self.sample_interval = YLeaf(YType.uint64, "sample-interval")

                                self.sensor_group = YLeaf(YType.str, "sensor-group")

                                self.suppress_redundant = YLeaf(YType.boolean, "suppress-redundant")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("heartbeat_interval",
                                                "sample_interval",
                                                "sensor_group",
                                                "suppress_redundant") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.heartbeat_interval.is_set or
                                    self.sample_interval.is_set or
                                    self.sensor_group.is_set or
                                    self.suppress_redundant.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.heartbeat_interval.yfilter != YFilter.not_set or
                                    self.sample_interval.yfilter != YFilter.not_set or
                                    self.sensor_group.yfilter != YFilter.not_set or
                                    self.suppress_redundant.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "state" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.heartbeat_interval.is_set or self.heartbeat_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.heartbeat_interval.get_name_leafdata())
                                if (self.sample_interval.is_set or self.sample_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_interval.get_name_leafdata())
                                if (self.sensor_group.is_set or self.sensor_group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sensor_group.get_name_leafdata())
                                if (self.suppress_redundant.is_set or self.suppress_redundant.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.suppress_redundant.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "heartbeat-interval" or name == "sample-interval" or name == "sensor-group" or name == "suppress-redundant"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "heartbeat-interval"):
                                    self.heartbeat_interval = value
                                    self.heartbeat_interval.value_namespace = name_space
                                    self.heartbeat_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "sample-interval"):
                                    self.sample_interval = value
                                    self.sample_interval.value_namespace = name_space
                                    self.sample_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "sensor-group"):
                                    self.sensor_group = value
                                    self.sensor_group.value_namespace = name_space
                                    self.sensor_group.value_namespace_prefix = name_space_prefix
                                if(value_path == "suppress-redundant"):
                                    self.suppress_redundant = value
                                    self.suppress_redundant.value_namespace = name_space
                                    self.suppress_redundant.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.sensor_group.is_set or
                                (self.config is not None and self.config.has_data()) or
                                (self.state is not None and self.state.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sensor_group.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()) or
                                (self.state is not None and self.state.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sensor-profile" + "[sensor-group='" + self.sensor_group.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.sensor_group.is_set or self.sensor_group.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sensor_group.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            if (child_yang_name == "state"):
                                if (self.state is None):
                                    self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                return self.state

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "config" or name == "state" or name == "sensor-group"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "sensor-group"):
                                self.sensor_group = value
                                self.sensor_group.value_namespace = name_space
                                self.sensor_group.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sensor_profile:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.sensor_profile:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sensor-profiles" + path_buffer

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

                        if (child_yang_name == "sensor-profile"):
                            for c in self.sensor_profile:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles.SensorProfile()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sensor_profile.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sensor-profile"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    	**type**\: list of    :py:class:`DestinationGroup <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups, self).__init__()

                        self.yang_name = "destination-groups"
                        self.yang_parent_name = "subscription"

                        self.destination_group = YList(self)

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
                                    super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups, self).__setattr__(name, value)


                    class DestinationGroup(Entity):
                        """
                        Identifier of the previously defined destination
                        group
                        
                        .. attribute:: group_id  <key>
                        
                        	The destination group id references a configured group of destinations for the telemetry stream
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to telemetry destinations
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config>`
                        
                        .. attribute:: state
                        
                        	State information related to telemetry destinations
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup, self).__init__()

                            self.yang_name = "destination-group"
                            self.yang_parent_name = "destination-groups"

                            self.group_id = YLeaf(YType.str, "group-id")

                            self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup, self).__setattr__(name, value)


                        class Config(Entity):
                            """
                            Configuration parameters related to telemetry
                            destinations.
                            
                            .. attribute:: group_id
                            
                            	The destination group id references a reusable group of destination addresses and ports for the telemetry stream
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "destination-group"

                                self.group_id = YLeaf(YType.str, "group-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config, self).__setattr__(name, value)

                            def has_data(self):
                                return self.group_id.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "config" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-id"):
                                    self.group_id = value
                                    self.group_id.value_namespace = name_space
                                    self.group_id.value_namespace_prefix = name_space_prefix


                        class State(Entity):
                            """
                            State information related to telemetry
                            destinations
                            
                            .. attribute:: group_id
                            
                            	The destination group id references a reusable group of destination addresses and ports for the telemetry stream
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`group_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.DestinationGroups.DestinationGroup>`
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "destination-group"

                                self.group_id = YLeaf(YType.str, "group-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("group_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State, self).__setattr__(name, value)

                            def has_data(self):
                                return self.group_id.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.group_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "state" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "group-id"):
                                    self.group_id = value
                                    self.group_id.value_namespace = name_space
                                    self.group_id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.group_id.is_set or
                                (self.config is not None and self.config.has_data()) or
                                (self.state is not None and self.state.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_id.yfilter != YFilter.not_set or
                                (self.config is not None and self.config.has_operation()) or
                                (self.state is not None and self.state.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "destination-group" + "[group-id='" + self.group_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "config"):
                                if (self.config is None):
                                    self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                return self.config

                            if (child_yang_name == "state"):
                                if (self.state is None):
                                    self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                return self.state

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "config" or name == "state" or name == "group-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-id"):
                                self.group_id = value
                                self.group_id.value_namespace = name_space
                                self.group_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.destination_group:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.destination_group:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-groups" + path_buffer

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

                        if (child_yang_name == "destination-group"):
                            for c in self.destination_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups.DestinationGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.destination_group.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-group"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.subscription_id.is_set or
                        (self.config is not None and self.config.has_data()) or
                        (self.destination_groups is not None and self.destination_groups.has_data()) or
                        (self.sensor_profiles is not None and self.sensor_profiles.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.subscription_id.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.destination_groups is not None and self.destination_groups.has_operation()) or
                        (self.sensor_profiles is not None and self.sensor_profiles.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "subscription" + "[subscription-id='" + self.subscription_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "openconfig-telemetry:telemetry-system/subscriptions/persistent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.subscription_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = TelemetrySystem.Subscriptions.Persistent.Subscription.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "destination-groups"):
                        if (self.destination_groups is None):
                            self.destination_groups = TelemetrySystem.Subscriptions.Persistent.Subscription.DestinationGroups()
                            self.destination_groups.parent = self
                            self._children_name_map["destination_groups"] = "destination-groups"
                        return self.destination_groups

                    if (child_yang_name == "sensor-profiles"):
                        if (self.sensor_profiles is None):
                            self.sensor_profiles = TelemetrySystem.Subscriptions.Persistent.Subscription.SensorProfiles()
                            self.sensor_profiles.parent = self
                            self._children_name_map["sensor_profiles"] = "sensor-profiles"
                        return self.sensor_profiles

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = TelemetrySystem.Subscriptions.Persistent.Subscription.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "destination-groups" or name == "sensor-profiles" or name == "state" or name == "subscription-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "subscription-id"):
                        self.subscription_id = value
                        self.subscription_id.value_namespace = name_space
                        self.subscription_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.subscription:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.subscription:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "persistent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-telemetry:telemetry-system/subscriptions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "subscription"):
                    for c in self.subscription:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = TelemetrySystem.Subscriptions.Persistent.Subscription()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.subscription.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "subscription"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Dynamic(Entity):
            """
            This container holds information relating to dynamic
            telemetry subscriptions. A dynamic subscription is
            typically configured through an RPC channel, and does not
            persist across device restarts, or if the RPC channel is
            reset or otherwise torn down.
            
            .. attribute:: subscription
            
            	List representation of telemetry subscriptions that are configured via an inline RPC, otherwise known as dynamic telemetry subscriptions
            	**type**\: list of    :py:class:`Subscription <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription>`
            
            

            """

            _prefix = 'oc-telemetry'
            _revision = '2016-02-04'

            def __init__(self):
                super(TelemetrySystem.Subscriptions.Dynamic, self).__init__()

                self.yang_name = "dynamic"
                self.yang_parent_name = "subscriptions"

                self.subscription = YList(self)

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
                            super(TelemetrySystem.Subscriptions.Dynamic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetrySystem.Subscriptions.Dynamic, self).__setattr__(name, value)


            class Subscription(Entity):
                """
                List representation of telemetry subscriptions that
                are configured via an inline RPC, otherwise known
                as dynamic telemetry subscriptions.
                
                .. attribute:: subscription_id  <key>
                
                	Reference to the identifier of the subscription itself. The id will be the handle to refer to the subscription once created
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**refers to**\:  :py:class:`subscription_id <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.State>`
                
                .. attribute:: sensor_paths
                
                	Top level container to hold a set of sensor paths grouped together
                	**type**\:   :py:class:`SensorPaths <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths>`
                
                .. attribute:: state
                
                	State information relating to dynamic telemetry subscriptions
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.State>`
                
                

                """

                _prefix = 'oc-telemetry'
                _revision = '2016-02-04'

                def __init__(self):
                    super(TelemetrySystem.Subscriptions.Dynamic.Subscription, self).__init__()

                    self.yang_name = "subscription"
                    self.yang_parent_name = "dynamic"

                    self.subscription_id = YLeaf(YType.str, "subscription-id")

                    self.sensor_paths = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths()
                    self.sensor_paths.parent = self
                    self._children_name_map["sensor_paths"] = "sensor-paths"
                    self._children_yang_names.add("sensor-paths")

                    self.state = TelemetrySystem.Subscriptions.Dynamic.Subscription.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("subscription_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetrySystem.Subscriptions.Dynamic.Subscription, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetrySystem.Subscriptions.Dynamic.Subscription, self).__setattr__(name, value)


                class State(Entity):
                    """
                    State information relating to dynamic telemetry
                    subscriptions.
                    
                    .. attribute:: destination_address
                    
                    	IP address of the telemetry stream destination
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: destination_port
                    
                    	Protocol (udp or tcp) port number for the telemetry stream destination
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_protocol
                    
                    	Protocol used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`TelemetryStreamProtocol <ydk.models.openconfig.openconfig_telemetry.TelemetryStreamProtocol>`
                    
                    .. attribute:: heartbeat_interval
                    
                    	Maximum time interval in seconds that may pass between updates from a device to a telemetry collector. If this interval expires, but there is no updated data to send (such as if suppress\_updates has been configured), the device must send a telemetry message to the collector
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: originated_qos_marking
                    
                    	DSCP marking of packets generated by the telemetry subsystem on the network device
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: sample_interval
                    
                    	Time in milliseconds between the device's sample of a telemetry data source. For example, setting this to 100 would require the local device to collect the telemetry data every 100 milliseconds. There can be latency or jitter in transmitting the data, but the sample must occur at the specified interval.  The timestamp must reflect the actual time when the data was sampled, not simply the previous sample timestamp + sample\-interval.  If sample\-interval is set to 0, the telemetry sensor becomes event based. The sensor must then emit data upon every change of the underlying data source
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: subscription_id
                    
                    	Identifer of the telemetry subscription. Will be used by configuration operations needing to modify or delete the telemetry subscription
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: suppress_redundant
                    
                    	Boolean flag to control suppression of redundant telemetry updates to the collector platform. If this flag is set to TRUE, then the collector will only send an update at the configured interval if a subscribed data value has changed. Otherwise, the device will not send an update to the collector until expiration of the heartbeat interval
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Dynamic.Subscription.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "subscription"

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.destination_port = YLeaf(YType.uint16, "destination-port")

                        self.destination_protocol = YLeaf(YType.enumeration, "destination-protocol")

                        self.heartbeat_interval = YLeaf(YType.uint64, "heartbeat-interval")

                        self.originated_qos_marking = YLeaf(YType.uint8, "originated-qos-marking")

                        self.sample_interval = YLeaf(YType.uint64, "sample-interval")

                        self.subscription_id = YLeaf(YType.uint64, "subscription-id")

                        self.suppress_redundant = YLeaf(YType.boolean, "suppress-redundant")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("destination_address",
                                        "destination_port",
                                        "destination_protocol",
                                        "heartbeat_interval",
                                        "originated_qos_marking",
                                        "sample_interval",
                                        "subscription_id",
                                        "suppress_redundant") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetrySystem.Subscriptions.Dynamic.Subscription.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetrySystem.Subscriptions.Dynamic.Subscription.State, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.destination_address.is_set or
                            self.destination_port.is_set or
                            self.destination_protocol.is_set or
                            self.heartbeat_interval.is_set or
                            self.originated_qos_marking.is_set or
                            self.sample_interval.is_set or
                            self.subscription_id.is_set or
                            self.suppress_redundant.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.destination_port.yfilter != YFilter.not_set or
                            self.destination_protocol.yfilter != YFilter.not_set or
                            self.heartbeat_interval.yfilter != YFilter.not_set or
                            self.originated_qos_marking.yfilter != YFilter.not_set or
                            self.sample_interval.yfilter != YFilter.not_set or
                            self.subscription_id.yfilter != YFilter.not_set or
                            self.suppress_redundant.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "state" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_port.get_name_leafdata())
                        if (self.destination_protocol.is_set or self.destination_protocol.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_protocol.get_name_leafdata())
                        if (self.heartbeat_interval.is_set or self.heartbeat_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.heartbeat_interval.get_name_leafdata())
                        if (self.originated_qos_marking.is_set or self.originated_qos_marking.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.originated_qos_marking.get_name_leafdata())
                        if (self.sample_interval.is_set or self.sample_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sample_interval.get_name_leafdata())
                        if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.subscription_id.get_name_leafdata())
                        if (self.suppress_redundant.is_set or self.suppress_redundant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.suppress_redundant.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-address" or name == "destination-port" or name == "destination-protocol" or name == "heartbeat-interval" or name == "originated-qos-marking" or name == "sample-interval" or name == "subscription-id" or name == "suppress-redundant"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-port"):
                            self.destination_port = value
                            self.destination_port.value_namespace = name_space
                            self.destination_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-protocol"):
                            self.destination_protocol = value
                            self.destination_protocol.value_namespace = name_space
                            self.destination_protocol.value_namespace_prefix = name_space_prefix
                        if(value_path == "heartbeat-interval"):
                            self.heartbeat_interval = value
                            self.heartbeat_interval.value_namespace = name_space
                            self.heartbeat_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "originated-qos-marking"):
                            self.originated_qos_marking = value
                            self.originated_qos_marking.value_namespace = name_space
                            self.originated_qos_marking.value_namespace_prefix = name_space_prefix
                        if(value_path == "sample-interval"):
                            self.sample_interval = value
                            self.sample_interval.value_namespace = name_space
                            self.sample_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "subscription-id"):
                            self.subscription_id = value
                            self.subscription_id.value_namespace = name_space
                            self.subscription_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "suppress-redundant"):
                            self.suppress_redundant = value
                            self.suppress_redundant.value_namespace = name_space
                            self.suppress_redundant.value_namespace_prefix = name_space_prefix


                class SensorPaths(Entity):
                    """
                    Top level container to hold a set of sensor
                    paths grouped together
                    
                    .. attribute:: sensor_path
                    
                    	List of paths in the model which together comprise a sensor grouping. Filters for each path to exclude items are also provided
                    	**type**\: list of    :py:class:`SensorPath <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath>`
                    
                    

                    """

                    _prefix = 'oc-telemetry'
                    _revision = '2016-02-04'

                    def __init__(self):
                        super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths, self).__init__()

                        self.yang_name = "sensor-paths"
                        self.yang_parent_name = "subscription"

                        self.sensor_path = YList(self)

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
                                    super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths, self).__setattr__(name, value)


                    class SensorPath(Entity):
                        """
                        List of paths in the model which together
                        comprise a sensor grouping. Filters for each path
                        to exclude items are also provided.
                        
                        .. attribute:: path  <key>
                        
                        	Reference to the path of interest
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`path <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State>`
                        
                        .. attribute:: state
                        
                        	State information for a dynamic subscription's paths of interest
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_telemetry.TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State>`
                        
                        

                        """

                        _prefix = 'oc-telemetry'
                        _revision = '2016-02-04'

                        def __init__(self):
                            super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath, self).__init__()

                            self.yang_name = "sensor-path"
                            self.yang_parent_name = "sensor-paths"

                            self.path = YLeaf(YType.str, "path")

                            self.state = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("path") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath, self).__setattr__(name, value)


                        class State(Entity):
                            """
                            State information for a dynamic subscription's
                            paths of interest
                            
                            .. attribute:: exclude_filter
                            
                            	Filter to exclude certain values out of the state values
                            	**type**\:  str
                            
                            .. attribute:: path
                            
                            	Path to a section of operational state of interest (the sensor)
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'oc-telemetry'
                            _revision = '2016-02-04'

                            def __init__(self):
                                super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "sensor-path"

                                self.exclude_filter = YLeaf(YType.str, "exclude-filter")

                                self.path = YLeaf(YType.str, "path")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("exclude_filter",
                                                "path") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.exclude_filter.is_set or
                                    self.path.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.exclude_filter.yfilter != YFilter.not_set or
                                    self.path.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "state" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.exclude_filter.is_set or self.exclude_filter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.exclude_filter.get_name_leafdata())
                                if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "exclude-filter" or name == "path"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "exclude-filter"):
                                    self.exclude_filter = value
                                    self.exclude_filter.value_namespace = name_space
                                    self.exclude_filter.value_namespace_prefix = name_space_prefix
                                if(value_path == "path"):
                                    self.path = value
                                    self.path.value_namespace = name_space
                                    self.path.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.path.is_set or
                                (self.state is not None and self.state.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.path.yfilter != YFilter.not_set or
                                (self.state is not None and self.state.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sensor-path" + "[path='" + self.path.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "state"):
                                if (self.state is None):
                                    self.state = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                return self.state

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "state" or name == "path"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "path"):
                                self.path = value
                                self.path.value_namespace = name_space
                                self.path.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sensor_path:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.sensor_path:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sensor-paths" + path_buffer

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

                        if (child_yang_name == "sensor-path"):
                            for c in self.sensor_path:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths.SensorPath()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sensor_path.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sensor-path"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.subscription_id.is_set or
                        (self.sensor_paths is not None and self.sensor_paths.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.subscription_id.yfilter != YFilter.not_set or
                        (self.sensor_paths is not None and self.sensor_paths.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "subscription" + "[subscription-id='" + self.subscription_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "openconfig-telemetry:telemetry-system/subscriptions/dynamic/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.subscription_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "sensor-paths"):
                        if (self.sensor_paths is None):
                            self.sensor_paths = TelemetrySystem.Subscriptions.Dynamic.Subscription.SensorPaths()
                            self.sensor_paths.parent = self
                            self._children_name_map["sensor_paths"] = "sensor-paths"
                        return self.sensor_paths

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = TelemetrySystem.Subscriptions.Dynamic.Subscription.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sensor-paths" or name == "state" or name == "subscription-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "subscription-id"):
                        self.subscription_id = value
                        self.subscription_id.value_namespace = name_space
                        self.subscription_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.subscription:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.subscription:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "dynamic" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "openconfig-telemetry:telemetry-system/subscriptions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "subscription"):
                    for c in self.subscription:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = TelemetrySystem.Subscriptions.Dynamic.Subscription()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.subscription.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "subscription"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.dynamic is not None and self.dynamic.has_data()) or
                (self.persistent is not None and self.persistent.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.dynamic is not None and self.dynamic.has_operation()) or
                (self.persistent is not None and self.persistent.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "subscriptions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-telemetry:telemetry-system/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "dynamic"):
                if (self.dynamic is None):
                    self.dynamic = TelemetrySystem.Subscriptions.Dynamic()
                    self.dynamic.parent = self
                    self._children_name_map["dynamic"] = "dynamic"
                return self.dynamic

            if (child_yang_name == "persistent"):
                if (self.persistent is None):
                    self.persistent = TelemetrySystem.Subscriptions.Persistent()
                    self.persistent.parent = self
                    self._children_name_map["persistent"] = "persistent"
                return self.persistent

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "dynamic" or name == "persistent"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.destination_groups is not None and self.destination_groups.has_data()) or
            (self.sensor_groups is not None and self.sensor_groups.has_data()) or
            (self.subscriptions is not None and self.subscriptions.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.destination_groups is not None and self.destination_groups.has_operation()) or
            (self.sensor_groups is not None and self.sensor_groups.has_operation()) or
            (self.subscriptions is not None and self.subscriptions.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "openconfig-telemetry:telemetry-system" + path_buffer

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

        if (child_yang_name == "destination-groups"):
            if (self.destination_groups is None):
                self.destination_groups = TelemetrySystem.DestinationGroups()
                self.destination_groups.parent = self
                self._children_name_map["destination_groups"] = "destination-groups"
            return self.destination_groups

        if (child_yang_name == "sensor-groups"):
            if (self.sensor_groups is None):
                self.sensor_groups = TelemetrySystem.SensorGroups()
                self.sensor_groups.parent = self
                self._children_name_map["sensor_groups"] = "sensor-groups"
            return self.sensor_groups

        if (child_yang_name == "subscriptions"):
            if (self.subscriptions is None):
                self.subscriptions = TelemetrySystem.Subscriptions()
                self.subscriptions.parent = self
                self._children_name_map["subscriptions"] = "subscriptions"
            return self.subscriptions

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "destination-groups" or name == "sensor-groups" or name == "subscriptions"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TelemetrySystem()
        return self._top_entity

