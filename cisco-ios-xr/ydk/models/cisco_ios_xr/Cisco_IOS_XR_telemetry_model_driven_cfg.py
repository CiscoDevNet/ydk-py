""" Cisco_IOS_XR_telemetry_model_driven_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR telemetry\-model\-driven package configuration.

This module contains definitions
for the following management objects\:
  telemetry\-model\-driven\: Model Driven Telemetry configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EncodeType(Enum):
    """
    EncodeType

    Encode type

    .. data:: gpb = 2

    	GPB

    .. data:: self_describing_gpb = 3

    	SELF DESCRIBING GPB

    """

    gpb = Enum.YLeaf(2, "gpb")

    self_describing_gpb = Enum.YLeaf(3, "self-describing-gpb")


class ProtoType(Enum):
    """
    ProtoType

    Proto type

    .. data:: grpc = 1

    	GRPC

    .. data:: tcp = 2

    	tcp

    """

    grpc = Enum.YLeaf(1, "grpc")

    tcp = Enum.YLeaf(2, "tcp")



class TelemetryModelDriven(Entity):
    """
    Model Driven Telemetry configuration
    
    .. attribute:: destination_groups
    
    	Destination Group configuration
    	**type**\:   :py:class:`DestinationGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups>`
    
    .. attribute:: enable
    
    	Enable Model Driven Telemetry
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: sensor_groups
    
    	Sensor group configuration
    	**type**\:   :py:class:`SensorGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups>`
    
    .. attribute:: subscriptions
    
    	Streaming Telemetry Subscription
    	**type**\:   :py:class:`Subscriptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions>`
    
    

    """

    _prefix = 'telemetry-model-driven-cfg'
    _revision = '2017-01-30'

    def __init__(self):
        super(TelemetryModelDriven, self).__init__()
        self._top_entity = None

        self.yang_name = "telemetry-model-driven"
        self.yang_parent_name = "Cisco-IOS-XR-telemetry-model-driven-cfg"

        self.enable = YLeaf(YType.empty, "enable")

        self.destination_groups = TelemetryModelDriven.DestinationGroups()
        self.destination_groups.parent = self
        self._children_name_map["destination_groups"] = "destination-groups"
        self._children_yang_names.add("destination-groups")

        self.sensor_groups = TelemetryModelDriven.SensorGroups()
        self.sensor_groups.parent = self
        self._children_name_map["sensor_groups"] = "sensor-groups"
        self._children_yang_names.add("sensor-groups")

        self.subscriptions = TelemetryModelDriven.Subscriptions()
        self.subscriptions.parent = self
        self._children_name_map["subscriptions"] = "subscriptions"
        self._children_yang_names.add("subscriptions")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(TelemetryModelDriven, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(TelemetryModelDriven, self).__setattr__(name, value)


    class SensorGroups(Entity):
        """
        Sensor group configuration
        
        .. attribute:: sensor_group
        
        	Sensor group configuration
        	**type**\: list of    :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2017-01-30'

        def __init__(self):
            super(TelemetryModelDriven.SensorGroups, self).__init__()

            self.yang_name = "sensor-groups"
            self.yang_parent_name = "telemetry-model-driven"

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
                        super(TelemetryModelDriven.SensorGroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TelemetryModelDriven.SensorGroups, self).__setattr__(name, value)


        class SensorGroup(Entity):
            """
            Sensor group configuration
            
            .. attribute:: sensor_group_identifier  <key>
            
            	The identifier for this group
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: sensor_paths
            
            	Sensor path configuration
            	**type**\:   :py:class:`SensorPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths>`
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2017-01-30'

            def __init__(self):
                super(TelemetryModelDriven.SensorGroups.SensorGroup, self).__init__()

                self.yang_name = "sensor-group"
                self.yang_parent_name = "sensor-groups"

                self.sensor_group_identifier = YLeaf(YType.str, "sensor-group-identifier")

                self.sensor_paths = TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths()
                self.sensor_paths.parent = self
                self._children_name_map["sensor_paths"] = "sensor-paths"
                self._children_yang_names.add("sensor-paths")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sensor_group_identifier") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TelemetryModelDriven.SensorGroups.SensorGroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetryModelDriven.SensorGroups.SensorGroup, self).__setattr__(name, value)


            class SensorPaths(Entity):
                """
                Sensor path configuration
                
                .. attribute:: sensor_path
                
                	Sensor path configuration
                	**type**\: list of    :py:class:`SensorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2017-01-30'

                def __init__(self):
                    super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths, self).__init__()

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
                                super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths, self).__setattr__(name, value)


                class SensorPath(Entity):
                    """
                    Sensor path configuration
                    
                    .. attribute:: telemetry_sensor_path  <key>
                    
                    	Sensor Path
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2017-01-30'

                    def __init__(self):
                        super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath, self).__init__()

                        self.yang_name = "sensor-path"
                        self.yang_parent_name = "sensor-paths"

                        self.telemetry_sensor_path = YLeaf(YType.str, "telemetry-sensor-path")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("telemetry_sensor_path") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath, self).__setattr__(name, value)

                    def has_data(self):
                        return self.telemetry_sensor_path.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.telemetry_sensor_path.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sensor-path" + "[telemetry-sensor-path='" + self.telemetry_sensor_path.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.telemetry_sensor_path.is_set or self.telemetry_sensor_path.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.telemetry_sensor_path.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "telemetry-sensor-path"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "telemetry-sensor-path"):
                            self.telemetry_sensor_path = value
                            self.telemetry_sensor_path.value_namespace = name_space
                            self.telemetry_sensor_path.value_namespace_prefix = name_space_prefix

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
                        c = TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths.SensorPath()
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
                    self.sensor_group_identifier.is_set or
                    (self.sensor_paths is not None and self.sensor_paths.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sensor_group_identifier.yfilter != YFilter.not_set or
                    (self.sensor_paths is not None and self.sensor_paths.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sensor-group" + "[sensor-group-identifier='" + self.sensor_group_identifier.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/sensor-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sensor_group_identifier.is_set or self.sensor_group_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sensor_group_identifier.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sensor-paths"):
                    if (self.sensor_paths is None):
                        self.sensor_paths = TelemetryModelDriven.SensorGroups.SensorGroup.SensorPaths()
                        self.sensor_paths.parent = self
                        self._children_name_map["sensor_paths"] = "sensor-paths"
                    return self.sensor_paths

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sensor-paths" or name == "sensor-group-identifier"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sensor-group-identifier"):
                    self.sensor_group_identifier = value
                    self.sensor_group_identifier.value_namespace = name_space
                    self.sensor_group_identifier.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/%s" % self.get_segment_path()
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
                c = TelemetryModelDriven.SensorGroups.SensorGroup()
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


    class Subscriptions(Entity):
        """
        Streaming Telemetry Subscription
        
        .. attribute:: subscription
        
        	Streaming Telemetry Subscription
        	**type**\: list of    :py:class:`Subscription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2017-01-30'

        def __init__(self):
            super(TelemetryModelDriven.Subscriptions, self).__init__()

            self.yang_name = "subscriptions"
            self.yang_parent_name = "telemetry-model-driven"

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
                        super(TelemetryModelDriven.Subscriptions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TelemetryModelDriven.Subscriptions, self).__setattr__(name, value)


        class Subscription(Entity):
            """
            Streaming Telemetry Subscription
            
            .. attribute:: subscription_identifier  <key>
            
            	Subscription identifier string
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: destination_profiles
            
            	Associate Destination Groups with Subscription
            	**type**\:   :py:class:`DestinationProfiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles>`
            
            .. attribute:: sensor_profiles
            
            	Associate Sensor Groups with Subscription
            	**type**\:   :py:class:`SensorProfiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles>`
            
            .. attribute:: source_interface
            
            	Source address to use for streaming telemetry information
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2017-01-30'

            def __init__(self):
                super(TelemetryModelDriven.Subscriptions.Subscription, self).__init__()

                self.yang_name = "subscription"
                self.yang_parent_name = "subscriptions"

                self.subscription_identifier = YLeaf(YType.str, "subscription-identifier")

                self.source_interface = YLeaf(YType.str, "source-interface")

                self.destination_profiles = TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles()
                self.destination_profiles.parent = self
                self._children_name_map["destination_profiles"] = "destination-profiles"
                self._children_yang_names.add("destination-profiles")

                self.sensor_profiles = TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles()
                self.sensor_profiles.parent = self
                self._children_name_map["sensor_profiles"] = "sensor-profiles"
                self._children_yang_names.add("sensor-profiles")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("subscription_identifier",
                                "source_interface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TelemetryModelDriven.Subscriptions.Subscription, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetryModelDriven.Subscriptions.Subscription, self).__setattr__(name, value)


            class SensorProfiles(Entity):
                """
                Associate Sensor Groups with Subscription
                
                .. attribute:: sensor_profile
                
                	Associate Sensor Group with Subscription
                	**type**\: list of    :py:class:`SensorProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2017-01-30'

                def __init__(self):
                    super(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles, self).__init__()

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
                                super(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles, self).__setattr__(name, value)


                class SensorProfile(Entity):
                    """
                    Associate Sensor Group with Subscription
                    
                    .. attribute:: sensorgroupid  <key>
                    
                    	Reference to the telemetry sensor group name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: sample_interval
                    
                    	Sample interval in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: strict_timer
                    
                    	use strict timer
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2017-01-30'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile, self).__init__()

                        self.yang_name = "sensor-profile"
                        self.yang_parent_name = "sensor-profiles"

                        self.sensorgroupid = YLeaf(YType.str, "sensorgroupid")

                        self.sample_interval = YLeaf(YType.uint32, "sample-interval")

                        self.strict_timer = YLeaf(YType.empty, "strict-timer")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("sensorgroupid",
                                        "sample_interval",
                                        "strict_timer") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.sensorgroupid.is_set or
                            self.sample_interval.is_set or
                            self.strict_timer.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.sensorgroupid.yfilter != YFilter.not_set or
                            self.sample_interval.yfilter != YFilter.not_set or
                            self.strict_timer.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sensor-profile" + "[sensorgroupid='" + self.sensorgroupid.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.sensorgroupid.is_set or self.sensorgroupid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sensorgroupid.get_name_leafdata())
                        if (self.sample_interval.is_set or self.sample_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sample_interval.get_name_leafdata())
                        if (self.strict_timer.is_set or self.strict_timer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.strict_timer.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sensorgroupid" or name == "sample-interval" or name == "strict-timer"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "sensorgroupid"):
                            self.sensorgroupid = value
                            self.sensorgroupid.value_namespace = name_space
                            self.sensorgroupid.value_namespace_prefix = name_space_prefix
                        if(value_path == "sample-interval"):
                            self.sample_interval = value
                            self.sample_interval.value_namespace = name_space
                            self.sample_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "strict-timer"):
                            self.strict_timer = value
                            self.strict_timer.value_namespace = name_space
                            self.strict_timer.value_namespace_prefix = name_space_prefix

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
                        c = TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles.SensorProfile()
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


            class DestinationProfiles(Entity):
                """
                Associate Destination Groups with Subscription
                
                .. attribute:: destination_profile
                
                	Associate Destination Group with Subscription
                	**type**\: list of    :py:class:`DestinationProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2017-01-30'

                def __init__(self):
                    super(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles, self).__init__()

                    self.yang_name = "destination-profiles"
                    self.yang_parent_name = "subscription"

                    self.destination_profile = YList(self)

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
                                super(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles, self).__setattr__(name, value)


                class DestinationProfile(Entity):
                    """
                    Associate Destination Group with Subscription
                    
                    .. attribute:: destination_id  <key>
                    
                    	Destination Id to associate with Subscription
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2017-01-30'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile, self).__init__()

                        self.yang_name = "destination-profile"
                        self.yang_parent_name = "destination-profiles"

                        self.destination_id = YLeaf(YType.str, "destination-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("destination_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile, self).__setattr__(name, value)

                    def has_data(self):
                        return self.destination_id.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.destination_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-profile" + "[destination-id='" + self.destination_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.destination_id.is_set or self.destination_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "destination-id"):
                            self.destination_id = value
                            self.destination_id.value_namespace = name_space
                            self.destination_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.destination_profile:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.destination_profile:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destination-profiles" + path_buffer

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

                    if (child_yang_name == "destination-profile"):
                        for c in self.destination_profile:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles.DestinationProfile()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.destination_profile.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.subscription_identifier.is_set or
                    self.source_interface.is_set or
                    (self.destination_profiles is not None and self.destination_profiles.has_data()) or
                    (self.sensor_profiles is not None and self.sensor_profiles.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.subscription_identifier.yfilter != YFilter.not_set or
                    self.source_interface.yfilter != YFilter.not_set or
                    (self.destination_profiles is not None and self.destination_profiles.has_operation()) or
                    (self.sensor_profiles is not None and self.sensor_profiles.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "subscription" + "[subscription-identifier='" + self.subscription_identifier.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/subscriptions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.subscription_identifier.is_set or self.subscription_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.subscription_identifier.get_name_leafdata())
                if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_interface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "destination-profiles"):
                    if (self.destination_profiles is None):
                        self.destination_profiles = TelemetryModelDriven.Subscriptions.Subscription.DestinationProfiles()
                        self.destination_profiles.parent = self
                        self._children_name_map["destination_profiles"] = "destination-profiles"
                    return self.destination_profiles

                if (child_yang_name == "sensor-profiles"):
                    if (self.sensor_profiles is None):
                        self.sensor_profiles = TelemetryModelDriven.Subscriptions.Subscription.SensorProfiles()
                        self.sensor_profiles.parent = self
                        self._children_name_map["sensor_profiles"] = "sensor-profiles"
                    return self.sensor_profiles

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination-profiles" or name == "sensor-profiles" or name == "subscription-identifier" or name == "source-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "subscription-identifier"):
                    self.subscription_identifier = value
                    self.subscription_identifier.value_namespace = name_space
                    self.subscription_identifier.value_namespace_prefix = name_space_prefix
                if(value_path == "source-interface"):
                    self.source_interface = value
                    self.source_interface.value_namespace = name_space
                    self.source_interface.value_namespace_prefix = name_space_prefix

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
            path_buffer = "subscriptions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/%s" % self.get_segment_path()
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
                c = TelemetryModelDriven.Subscriptions.Subscription()
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


    class DestinationGroups(Entity):
        """
        Destination Group configuration
        
        .. attribute:: destination_group
        
        	Destination Group
        	**type**\: list of    :py:class:`DestinationGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-cfg'
        _revision = '2017-01-30'

        def __init__(self):
            super(TelemetryModelDriven.DestinationGroups, self).__init__()

            self.yang_name = "destination-groups"
            self.yang_parent_name = "telemetry-model-driven"

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
                        super(TelemetryModelDriven.DestinationGroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TelemetryModelDriven.DestinationGroups, self).__setattr__(name, value)


        class DestinationGroup(Entity):
            """
            Destination Group
            
            .. attribute:: destination_id  <key>
            
            	destination group id string
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ipv4_destinations
            
            	Destination address configuration
            	**type**\:   :py:class:`Ipv4Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations>`
            
            .. attribute:: ipv6_destinations
            
            	Destination address configuration
            	**type**\:   :py:class:`Ipv6Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations>`
            
            .. attribute:: vrf
            
            	Vrf for the destination group
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'telemetry-model-driven-cfg'
            _revision = '2017-01-30'

            def __init__(self):
                super(TelemetryModelDriven.DestinationGroups.DestinationGroup, self).__init__()

                self.yang_name = "destination-group"
                self.yang_parent_name = "destination-groups"

                self.destination_id = YLeaf(YType.str, "destination-id")

                self.vrf = YLeaf(YType.str, "vrf")

                self.ipv4_destinations = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations()
                self.ipv4_destinations.parent = self
                self._children_name_map["ipv4_destinations"] = "ipv4-destinations"
                self._children_yang_names.add("ipv4-destinations")

                self.ipv6_destinations = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations()
                self.ipv6_destinations.parent = self
                self._children_name_map["ipv6_destinations"] = "ipv6-destinations"
                self._children_yang_names.add("ipv6-destinations")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("destination_id",
                                "vrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TelemetryModelDriven.DestinationGroups.DestinationGroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetryModelDriven.DestinationGroups.DestinationGroup, self).__setattr__(name, value)


            class Ipv6Destinations(Entity):
                """
                Destination address configuration
                
                .. attribute:: ipv6_destination
                
                	destination IP address
                	**type**\: list of    :py:class:`Ipv6Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2017-01-30'

                def __init__(self):
                    super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations, self).__init__()

                    self.yang_name = "ipv6-destinations"
                    self.yang_parent_name = "destination-group"

                    self.ipv6_destination = YList(self)

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
                                super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations, self).__setattr__(name, value)


                class Ipv6Destination(Entity):
                    """
                    destination IP address
                    
                    .. attribute:: ipv6_address  <key>
                    
                    	Destination IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_port  <key>
                    
                    	destination port
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: encoding
                    
                    	Encoding used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`EncodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.EncodeType>`
                    
                    .. attribute:: protocol
                    
                    	Transport Protocol used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2017-01-30'

                    def __init__(self):
                        super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination, self).__init__()

                        self.yang_name = "ipv6-destination"
                        self.yang_parent_name = "ipv6-destinations"

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        self.destination_port = YLeaf(YType.uint16, "destination-port")

                        self.encoding = YLeaf(YType.enumeration, "encoding")

                        self.protocol = None
                        self._children_name_map["protocol"] = "protocol"
                        self._children_yang_names.add("protocol")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipv6_address",
                                        "destination_port",
                                        "encoding") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination, self).__setattr__(name, value)


                    class Protocol(Entity):
                        """
                        Transport Protocol used to transmit telemetry
                        data to the collector
                        
                        .. attribute:: no_tls
                        
                        	no tls
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: packetsize
                        
                        	udp packetsize
                        	**type**\:  int
                        
                        	**range:** 484..65507
                        
                        	**default value**\: 1472
                        
                        .. attribute:: protocol
                        
                        	protocol
                        	**type**\:   :py:class:`ProtoType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.ProtoType>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: tls_hostname
                        
                        	tls hostname
                        	**type**\:  str
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'telemetry-model-driven-cfg'
                        _revision = '2017-01-30'

                        def __init__(self):
                            super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "ipv6-destination"
                            self.is_presence_container = True

                            self.no_tls = YLeaf(YType.int32, "no-tls")

                            self.packetsize = YLeaf(YType.uint32, "packetsize")

                            self.protocol = YLeaf(YType.enumeration, "protocol")

                            self.tls_hostname = YLeaf(YType.str, "tls-hostname")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("no_tls",
                                            "packetsize",
                                            "protocol",
                                            "tls_hostname") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.no_tls.is_set or
                                self.packetsize.is_set or
                                self.protocol.is_set or
                                self.tls_hostname.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.no_tls.yfilter != YFilter.not_set or
                                self.packetsize.yfilter != YFilter.not_set or
                                self.protocol.yfilter != YFilter.not_set or
                                self.tls_hostname.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protocol" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.no_tls.is_set or self.no_tls.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_tls.get_name_leafdata())
                            if (self.packetsize.is_set or self.packetsize.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packetsize.get_name_leafdata())
                            if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol.get_name_leafdata())
                            if (self.tls_hostname.is_set or self.tls_hostname.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tls_hostname.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "no-tls" or name == "packetsize" or name == "protocol" or name == "tls-hostname"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "no-tls"):
                                self.no_tls = value
                                self.no_tls.value_namespace = name_space
                                self.no_tls.value_namespace_prefix = name_space_prefix
                            if(value_path == "packetsize"):
                                self.packetsize = value
                                self.packetsize.value_namespace = name_space
                                self.packetsize.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol"):
                                self.protocol = value
                                self.protocol.value_namespace = name_space
                                self.protocol.value_namespace_prefix = name_space_prefix
                            if(value_path == "tls-hostname"):
                                self.tls_hostname = value
                                self.tls_hostname.value_namespace = name_space
                                self.tls_hostname.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.ipv6_address.is_set or
                            self.destination_port.is_set or
                            self.encoding.is_set or
                            (self.protocol is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set or
                            self.destination_port.yfilter != YFilter.not_set or
                            self.encoding.yfilter != YFilter.not_set or
                            (self.protocol is not None and self.protocol.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-destination" + "[ipv6-address='" + self.ipv6_address.get() + "']" + "[destination-port='" + self.destination_port.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                        if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_port.get_name_leafdata())
                        if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encoding.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "protocol"):
                            if (self.protocol is None):
                                self.protocol = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination.Protocol()
                                self.protocol.parent = self
                                self._children_name_map["protocol"] = "protocol"
                            return self.protocol

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol" or name == "ipv6-address" or name == "destination-port" or name == "encoding"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipv6-address"):
                            self.ipv6_address = value
                            self.ipv6_address.value_namespace = name_space
                            self.ipv6_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-port"):
                            self.destination_port = value
                            self.destination_port.value_namespace = name_space
                            self.destination_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "encoding"):
                            self.encoding = value
                            self.encoding.value_namespace = name_space
                            self.encoding.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ipv6_destination:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipv6_destination:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6-destinations" + path_buffer

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

                    if (child_yang_name == "ipv6-destination"):
                        for c in self.ipv6_destination:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations.Ipv6Destination()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv6_destination.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv6-destination"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Ipv4Destinations(Entity):
                """
                Destination address configuration
                
                .. attribute:: ipv4_destination
                
                	destination IP address
                	**type**\: list of    :py:class:`Ipv4Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination>`
                
                

                """

                _prefix = 'telemetry-model-driven-cfg'
                _revision = '2017-01-30'

                def __init__(self):
                    super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations, self).__init__()

                    self.yang_name = "ipv4-destinations"
                    self.yang_parent_name = "destination-group"

                    self.ipv4_destination = YList(self)

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
                                super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations, self).__setattr__(name, value)


                class Ipv4Destination(Entity):
                    """
                    destination IP address
                    
                    .. attribute:: ipv4_address  <key>
                    
                    	Destination IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_port  <key>
                    
                    	destination port
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: encoding
                    
                    	Encoding used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`EncodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.EncodeType>`
                    
                    .. attribute:: protocol
                    
                    	Transport Protocol used to transmit telemetry data to the collector
                    	**type**\:   :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-cfg'
                    _revision = '2017-01-30'

                    def __init__(self):
                        super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination, self).__init__()

                        self.yang_name = "ipv4-destination"
                        self.yang_parent_name = "ipv4-destinations"

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.destination_port = YLeaf(YType.uint16, "destination-port")

                        self.encoding = YLeaf(YType.enumeration, "encoding")

                        self.protocol = None
                        self._children_name_map["protocol"] = "protocol"
                        self._children_yang_names.add("protocol")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipv4_address",
                                        "destination_port",
                                        "encoding") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination, self).__setattr__(name, value)


                    class Protocol(Entity):
                        """
                        Transport Protocol used to transmit telemetry
                        data to the collector
                        
                        .. attribute:: no_tls
                        
                        	no tls
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: packetsize
                        
                        	udp packetsize
                        	**type**\:  int
                        
                        	**range:** 484..65507
                        
                        	**default value**\: 1472
                        
                        .. attribute:: protocol
                        
                        	protocol
                        	**type**\:   :py:class:`ProtoType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_cfg.ProtoType>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: tls_hostname
                        
                        	tls hostname
                        	**type**\:  str
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'telemetry-model-driven-cfg'
                        _revision = '2017-01-30'

                        def __init__(self):
                            super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "ipv4-destination"
                            self.is_presence_container = True

                            self.no_tls = YLeaf(YType.int32, "no-tls")

                            self.packetsize = YLeaf(YType.uint32, "packetsize")

                            self.protocol = YLeaf(YType.enumeration, "protocol")

                            self.tls_hostname = YLeaf(YType.str, "tls-hostname")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("no_tls",
                                            "packetsize",
                                            "protocol",
                                            "tls_hostname") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.no_tls.is_set or
                                self.packetsize.is_set or
                                self.protocol.is_set or
                                self.tls_hostname.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.no_tls.yfilter != YFilter.not_set or
                                self.packetsize.yfilter != YFilter.not_set or
                                self.protocol.yfilter != YFilter.not_set or
                                self.tls_hostname.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "protocol" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.no_tls.is_set or self.no_tls.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_tls.get_name_leafdata())
                            if (self.packetsize.is_set or self.packetsize.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packetsize.get_name_leafdata())
                            if (self.protocol.is_set or self.protocol.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol.get_name_leafdata())
                            if (self.tls_hostname.is_set or self.tls_hostname.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tls_hostname.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "no-tls" or name == "packetsize" or name == "protocol" or name == "tls-hostname"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "no-tls"):
                                self.no_tls = value
                                self.no_tls.value_namespace = name_space
                                self.no_tls.value_namespace_prefix = name_space_prefix
                            if(value_path == "packetsize"):
                                self.packetsize = value
                                self.packetsize.value_namespace = name_space
                                self.packetsize.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol"):
                                self.protocol = value
                                self.protocol.value_namespace = name_space
                                self.protocol.value_namespace_prefix = name_space_prefix
                            if(value_path == "tls-hostname"):
                                self.tls_hostname = value
                                self.tls_hostname.value_namespace = name_space
                                self.tls_hostname.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.ipv4_address.is_set or
                            self.destination_port.is_set or
                            self.encoding.is_set or
                            (self.protocol is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipv4_address.yfilter != YFilter.not_set or
                            self.destination_port.yfilter != YFilter.not_set or
                            self.encoding.yfilter != YFilter.not_set or
                            (self.protocol is not None and self.protocol.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4-destination" + "[ipv4-address='" + self.ipv4_address.get() + "']" + "[destination-port='" + self.destination_port.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                        if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_port.get_name_leafdata())
                        if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encoding.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "protocol"):
                            if (self.protocol is None):
                                self.protocol = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination.Protocol()
                                self.protocol.parent = self
                                self._children_name_map["protocol"] = "protocol"
                            return self.protocol

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "protocol" or name == "ipv4-address" or name == "destination-port" or name == "encoding"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipv4-address"):
                            self.ipv4_address = value
                            self.ipv4_address.value_namespace = name_space
                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-port"):
                            self.destination_port = value
                            self.destination_port.value_namespace = name_space
                            self.destination_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "encoding"):
                            self.encoding = value
                            self.encoding.value_namespace = name_space
                            self.encoding.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ipv4_destination:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ipv4_destination:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4-destinations" + path_buffer

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

                    if (child_yang_name == "ipv4-destination"):
                        for c in self.ipv4_destination:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations.Ipv4Destination()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ipv4_destination.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4-destination"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.destination_id.is_set or
                    self.vrf.is_set or
                    (self.ipv4_destinations is not None and self.ipv4_destinations.has_data()) or
                    (self.ipv6_destinations is not None and self.ipv6_destinations.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.destination_id.yfilter != YFilter.not_set or
                    self.vrf.yfilter != YFilter.not_set or
                    (self.ipv4_destinations is not None and self.ipv4_destinations.has_operation()) or
                    (self.ipv6_destinations is not None and self.ipv6_destinations.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "destination-group" + "[destination-id='" + self.destination_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/destination-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.destination_id.is_set or self.destination_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination_id.get_name_leafdata())
                if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4-destinations"):
                    if (self.ipv4_destinations is None):
                        self.ipv4_destinations = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv4Destinations()
                        self.ipv4_destinations.parent = self
                        self._children_name_map["ipv4_destinations"] = "ipv4-destinations"
                    return self.ipv4_destinations

                if (child_yang_name == "ipv6-destinations"):
                    if (self.ipv6_destinations is None):
                        self.ipv6_destinations = TelemetryModelDriven.DestinationGroups.DestinationGroup.Ipv6Destinations()
                        self.ipv6_destinations.parent = self
                        self._children_name_map["ipv6_destinations"] = "ipv6-destinations"
                    return self.ipv6_destinations

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4-destinations" or name == "ipv6-destinations" or name == "destination-id" or name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "destination-id"):
                    self.destination_id = value
                    self.destination_id.value_namespace = name_space
                    self.destination_id.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf"):
                    self.vrf = value
                    self.vrf.value_namespace = name_space
                    self.vrf.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven/%s" % self.get_segment_path()
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
                c = TelemetryModelDriven.DestinationGroups.DestinationGroup()
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
            self.enable.is_set or
            (self.destination_groups is not None and self.destination_groups.has_data()) or
            (self.sensor_groups is not None and self.sensor_groups.has_data()) or
            (self.subscriptions is not None and self.subscriptions.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            (self.destination_groups is not None and self.destination_groups.has_operation()) or
            (self.sensor_groups is not None and self.sensor_groups.has_operation()) or
            (self.subscriptions is not None and self.subscriptions.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-telemetry-model-driven-cfg:telemetry-model-driven" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "destination-groups"):
            if (self.destination_groups is None):
                self.destination_groups = TelemetryModelDriven.DestinationGroups()
                self.destination_groups.parent = self
                self._children_name_map["destination_groups"] = "destination-groups"
            return self.destination_groups

        if (child_yang_name == "sensor-groups"):
            if (self.sensor_groups is None):
                self.sensor_groups = TelemetryModelDriven.SensorGroups()
                self.sensor_groups.parent = self
                self._children_name_map["sensor_groups"] = "sensor-groups"
            return self.sensor_groups

        if (child_yang_name == "subscriptions"):
            if (self.subscriptions is None):
                self.subscriptions = TelemetryModelDriven.Subscriptions()
                self.subscriptions.parent = self
                self._children_name_map["subscriptions"] = "subscriptions"
            return self.subscriptions

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "destination-groups" or name == "sensor-groups" or name == "subscriptions" or name == "enable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = TelemetryModelDriven()
        return self._top_entity

