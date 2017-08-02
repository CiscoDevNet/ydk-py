""" Cisco_IOS_XR_manageability_object_tracking_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-object\-tracking package configuration.

This module contains definitions
for the following management objects\:
  object\-trackings\: Object Tracking configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ObjectTrackings(Entity):
    """
    Object Tracking configuration
    
    .. attribute:: object_tracking
    
    	Track name \- maximum 32 characters
    	**type**\: list of    :py:class:`ObjectTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking>`
    
    

    """

    _prefix = 'manageability-object-tracking-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(ObjectTrackings, self).__init__()
        self._top_entity = None

        self.yang_name = "object-trackings"
        self.yang_parent_name = "Cisco-IOS-XR-manageability-object-tracking-cfg"

        self.object_tracking = YList(self)

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
                    super(ObjectTrackings, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(ObjectTrackings, self).__setattr__(name, value)


    class ObjectTracking(Entity):
        """
        Track name \- maximum 32 characters
        
        .. attribute:: track_name  <key>
        
        	Track name
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: delay_down
        
        	Track delay down time
        	**type**\:  int
        
        	**range:** 1..10
        
        	**units**\: second
        
        .. attribute:: delay_up
        
        	Delay up in seconds
        	**type**\:  int
        
        	**range:** 1..10
        
        	**units**\: second
        
        .. attribute:: enable
        
        	Enable the Track
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_boolean_list
        
        	Track type boolean list
        	**type**\:   :py:class:`TypeBooleanList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList>`
        
        .. attribute:: type_boolean_list_and_enable
        
        	Enable track type boolean list and
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_boolean_list_or_enable
        
        	Enable track type boolean list or
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_interface
        
        	Track type line\-protocol
        	**type**\:   :py:class:`TypeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeInterface>`
        
        .. attribute:: type_interface_enable
        
        	Enable track type Interface
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: type_list
        
        	Track type boolean list
        	**type**\:   :py:class:`TypeList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList>`
        
        .. attribute:: type_route
        
        	Track type route ipv4
        	**type**\:   :py:class:`TypeRoute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeRoute>`
        
        .. attribute:: type_route_enable
        
        	Enable track type Route
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'manageability-object-tracking-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTrackings.ObjectTracking, self).__init__()

            self.yang_name = "object-tracking"
            self.yang_parent_name = "object-trackings"

            self.track_name = YLeaf(YType.str, "track-name")

            self.delay_down = YLeaf(YType.uint32, "delay-down")

            self.delay_up = YLeaf(YType.uint32, "delay-up")

            self.enable = YLeaf(YType.empty, "enable")

            self.type_boolean_list_and_enable = YLeaf(YType.empty, "type-boolean-list-and-enable")

            self.type_boolean_list_or_enable = YLeaf(YType.empty, "type-boolean-list-or-enable")

            self.type_interface_enable = YLeaf(YType.empty, "type-interface-enable")

            self.type_route_enable = YLeaf(YType.empty, "type-route-enable")

            self.type_boolean_list = ObjectTrackings.ObjectTracking.TypeBooleanList()
            self.type_boolean_list.parent = self
            self._children_name_map["type_boolean_list"] = "type-boolean-list"
            self._children_yang_names.add("type-boolean-list")

            self.type_interface = ObjectTrackings.ObjectTracking.TypeInterface()
            self.type_interface.parent = self
            self._children_name_map["type_interface"] = "type-interface"
            self._children_yang_names.add("type-interface")

            self.type_list = ObjectTrackings.ObjectTracking.TypeList()
            self.type_list.parent = self
            self._children_name_map["type_list"] = "type-list"
            self._children_yang_names.add("type-list")

            self.type_route = ObjectTrackings.ObjectTracking.TypeRoute()
            self.type_route.parent = self
            self._children_name_map["type_route"] = "type-route"
            self._children_yang_names.add("type-route")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("track_name",
                            "delay_down",
                            "delay_up",
                            "enable",
                            "type_boolean_list_and_enable",
                            "type_boolean_list_or_enable",
                            "type_interface_enable",
                            "type_route_enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ObjectTrackings.ObjectTracking, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTrackings.ObjectTracking, self).__setattr__(name, value)


        class TypeInterface(Entity):
            """
            Track type line\-protocol
            
            .. attribute:: interface
            
            	The name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeInterface, self).__init__()

                self.yang_name = "type-interface"
                self.yang_parent_name = "object-tracking"

                self.interface = YLeaf(YType.str, "interface")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTrackings.ObjectTracking.TypeInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTrackings.ObjectTracking.TypeInterface, self).__setattr__(name, value)

            def has_data(self):
                return self.interface.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "type-interface" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface"):
                    self.interface = value
                    self.interface.value_namespace = name_space
                    self.interface.value_namespace_prefix = name_space_prefix


        class TypeList(Entity):
            """
            Track type boolean list
            
            .. attribute:: threshold_percentage
            
            	Track type threshold percentage
            	**type**\:   :py:class:`ThresholdPercentage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage>`
            
            .. attribute:: threshold_percentage_object
            
            	Track type threshold percentage
            	**type**\:   :py:class:`ThresholdPercentageObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject>`
            
            .. attribute:: threshold_weight
            
            	Track type threshold weight
            	**type**\:   :py:class:`ThresholdWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight>`
            
            .. attribute:: threshold_weight_object
            
            	Track type threshold weight
            	**type**\:   :py:class:`ThresholdWeightObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject>`
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeList, self).__init__()

                self.yang_name = "type-list"
                self.yang_parent_name = "object-tracking"

                self.threshold_percentage = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage()
                self.threshold_percentage.parent = self
                self._children_name_map["threshold_percentage"] = "threshold-percentage"
                self._children_yang_names.add("threshold-percentage")

                self.threshold_percentage_object = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject()
                self.threshold_percentage_object.parent = self
                self._children_name_map["threshold_percentage_object"] = "threshold-percentage-object"
                self._children_yang_names.add("threshold-percentage-object")

                self.threshold_weight = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight()
                self.threshold_weight.parent = self
                self._children_name_map["threshold_weight"] = "threshold-weight"
                self._children_yang_names.add("threshold-weight")

                self.threshold_weight_object = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject()
                self.threshold_weight_object.parent = self
                self._children_name_map["threshold_weight_object"] = "threshold-weight-object"
                self._children_yang_names.add("threshold-weight-object")


            class ThresholdWeight(Entity):
                """
                Track type threshold weight
                
                .. attribute:: threshold_limits
                
                	Threshold Limits
                	**type**\:   :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight, self).__init__()

                    self.yang_name = "threshold-weight"
                    self.yang_parent_name = "type-list"

                    self.threshold_limits = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits()
                    self.threshold_limits.parent = self
                    self._children_name_map["threshold_limits"] = "threshold-limits"
                    self._children_yang_names.add("threshold-limits")


                class ThresholdLimits(Entity):
                    """
                    Threshold Limits
                    
                    .. attribute:: threshold_up_values
                    
                    	Threshold limit at which track is set to UP state
                    	**type**\:   :py:class:`ThresholdUpValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits, self).__init__()

                        self.yang_name = "threshold-limits"
                        self.yang_parent_name = "threshold-weight"

                        self.threshold_up_values = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues()
                        self.threshold_up_values.parent = self
                        self._children_name_map["threshold_up_values"] = "threshold-up-values"
                        self._children_yang_names.add("threshold-up-values")


                    class ThresholdUpValues(Entity):
                        """
                        Threshold limit at which track is set to UP
                        state
                        
                        .. attribute:: threshold_up_value
                        
                        	Threshold limit at which track is set to UP state
                        	**type**\: list of    :py:class:`ThresholdUpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue>`
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues, self).__init__()

                            self.yang_name = "threshold-up-values"
                            self.yang_parent_name = "threshold-limits"

                            self.threshold_up_value = YList(self)

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
                                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues, self).__setattr__(name, value)


                        class ThresholdUpValue(Entity):
                            """
                            Threshold limit at which track is set to UP
                            state
                            
                            .. attribute:: up  <key>
                            
                            	Up value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold_down
                            
                            	Threshold limit at which track is set to Down state
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'manageability-object-tracking-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, self).__init__()

                                self.yang_name = "threshold-up-value"
                                self.yang_parent_name = "threshold-up-values"

                                self.up = YLeaf(YType.int32, "up")

                                self.threshold_down = YLeaf(YType.int32, "threshold-down")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("up",
                                                "threshold_down") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.up.is_set or
                                    self.threshold_down.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.up.yfilter != YFilter.not_set or
                                    self.threshold_down.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold-up-value" + "[up='" + self.up.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.up.get_name_leafdata())
                                if (self.threshold_down.is_set or self.threshold_down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_down.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "up" or name == "threshold-down"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "up"):
                                    self.up = value
                                    self.up.value_namespace = name_space
                                    self.up.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-down"):
                                    self.threshold_down = value
                                    self.threshold_down.value_namespace = name_space
                                    self.threshold_down.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.threshold_up_value:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.threshold_up_value:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "threshold-up-values" + path_buffer

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

                            if (child_yang_name == "threshold-up-value"):
                                for c in self.threshold_up_value:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.threshold_up_value.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold-up-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.threshold_up_values is not None and self.threshold_up_values.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.threshold_up_values is not None and self.threshold_up_values.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "threshold-limits" + path_buffer

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

                        if (child_yang_name == "threshold-up-values"):
                            if (self.threshold_up_values is None):
                                self.threshold_up_values = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues()
                                self.threshold_up_values.parent = self
                                self._children_name_map["threshold_up_values"] = "threshold-up-values"
                            return self.threshold_up_values

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "threshold-up-values"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.threshold_limits is not None and self.threshold_limits.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.threshold_limits is not None and self.threshold_limits.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "threshold-weight" + path_buffer

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

                    if (child_yang_name == "threshold-limits"):
                        if (self.threshold_limits is None):
                            self.threshold_limits = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits()
                            self.threshold_limits.parent = self
                            self._children_name_map["threshold_limits"] = "threshold-limits"
                        return self.threshold_limits

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "threshold-limits"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ThresholdPercentageObject(Entity):
                """
                Track type threshold percentage
                
                .. attribute:: object
                
                	Track name object
                	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject, self).__init__()

                    self.yang_name = "threshold-percentage-object"
                    self.yang_parent_name = "type-list"

                    self.object = YList(self)

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
                                super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject, self).__setattr__(name, value)


                class Object(Entity):
                    """
                    Track name object
                    
                    .. attribute:: object  <key>
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_weight
                    
                    	Weight of object
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object, self).__init__()

                        self.yang_name = "object"
                        self.yang_parent_name = "threshold-percentage-object"

                        self.object = YLeaf(YType.str, "object")

                        self.object_weight = YLeaf(YType.int32, "object-weight")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object",
                                        "object_weight") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object.is_set or
                            self.object_weight.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object.yfilter != YFilter.not_set or
                            self.object_weight.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "object" + "[object='" + self.object.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object.is_set or self.object.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object.get_name_leafdata())
                        if (self.object_weight.is_set or self.object_weight.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_weight.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object" or name == "object-weight"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object"):
                            self.object = value
                            self.object.value_namespace = name_space
                            self.object.value_namespace_prefix = name_space_prefix
                        if(value_path == "object-weight"):
                            self.object_weight = value
                            self.object_weight.value_namespace = name_space
                            self.object_weight.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.object:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.object:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "threshold-percentage-object" + path_buffer

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

                    if (child_yang_name == "object"):
                        for c in self.object:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.object.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "object"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ThresholdPercentage(Entity):
                """
                Track type threshold percentage
                
                .. attribute:: threshold_limits
                
                	Threshold Limits
                	**type**\:   :py:class:`ThresholdLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage, self).__init__()

                    self.yang_name = "threshold-percentage"
                    self.yang_parent_name = "type-list"

                    self.threshold_limits = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits()
                    self.threshold_limits.parent = self
                    self._children_name_map["threshold_limits"] = "threshold-limits"
                    self._children_yang_names.add("threshold-limits")


                class ThresholdLimits(Entity):
                    """
                    Threshold Limits
                    
                    .. attribute:: threshold_up_values
                    
                    	Threshold limit at which track is set to UP state
                    	**type**\:   :py:class:`ThresholdUpValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits, self).__init__()

                        self.yang_name = "threshold-limits"
                        self.yang_parent_name = "threshold-percentage"

                        self.threshold_up_values = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues()
                        self.threshold_up_values.parent = self
                        self._children_name_map["threshold_up_values"] = "threshold-up-values"
                        self._children_yang_names.add("threshold-up-values")


                    class ThresholdUpValues(Entity):
                        """
                        Threshold limit at which track is set to UP
                        state
                        
                        .. attribute:: threshold_up_value
                        
                        	Threshold limit at which track is set to UP state
                        	**type**\: list of    :py:class:`ThresholdUpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue>`
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues, self).__init__()

                            self.yang_name = "threshold-up-values"
                            self.yang_parent_name = "threshold-limits"

                            self.threshold_up_value = YList(self)

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
                                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues, self).__setattr__(name, value)


                        class ThresholdUpValue(Entity):
                            """
                            Threshold limit at which track is set to UP
                            state
                            
                            .. attribute:: up  <key>
                            
                            	Up value
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: threshold_down
                            
                            	Threshold limit at which track is set to Down state
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'manageability-object-tracking-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, self).__init__()

                                self.yang_name = "threshold-up-value"
                                self.yang_parent_name = "threshold-up-values"

                                self.up = YLeaf(YType.int32, "up")

                                self.threshold_down = YLeaf(YType.int32, "threshold-down")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("up",
                                                "threshold_down") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.up.is_set or
                                    self.threshold_down.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.up.yfilter != YFilter.not_set or
                                    self.threshold_down.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "threshold-up-value" + "[up='" + self.up.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.up.get_name_leafdata())
                                if (self.threshold_down.is_set or self.threshold_down.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.threshold_down.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "up" or name == "threshold-down"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "up"):
                                    self.up = value
                                    self.up.value_namespace = name_space
                                    self.up.value_namespace_prefix = name_space_prefix
                                if(value_path == "threshold-down"):
                                    self.threshold_down = value
                                    self.threshold_down.value_namespace = name_space
                                    self.threshold_down.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.threshold_up_value:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.threshold_up_value:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "threshold-up-values" + path_buffer

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

                            if (child_yang_name == "threshold-up-value"):
                                for c in self.threshold_up_value:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.threshold_up_value.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "threshold-up-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.threshold_up_values is not None and self.threshold_up_values.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.threshold_up_values is not None and self.threshold_up_values.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "threshold-limits" + path_buffer

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

                        if (child_yang_name == "threshold-up-values"):
                            if (self.threshold_up_values is None):
                                self.threshold_up_values = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues()
                                self.threshold_up_values.parent = self
                                self._children_name_map["threshold_up_values"] = "threshold-up-values"
                            return self.threshold_up_values

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "threshold-up-values"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.threshold_limits is not None and self.threshold_limits.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.threshold_limits is not None and self.threshold_limits.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "threshold-percentage" + path_buffer

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

                    if (child_yang_name == "threshold-limits"):
                        if (self.threshold_limits is None):
                            self.threshold_limits = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits()
                            self.threshold_limits.parent = self
                            self._children_name_map["threshold_limits"] = "threshold-limits"
                        return self.threshold_limits

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "threshold-limits"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ThresholdWeightObject(Entity):
                """
                Track type threshold weight
                
                .. attribute:: object
                
                	Track name object
                	**type**\: list of    :py:class:`Object <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject, self).__init__()

                    self.yang_name = "threshold-weight-object"
                    self.yang_parent_name = "type-list"

                    self.object = YList(self)

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
                                super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject, self).__setattr__(name, value)


                class Object(Entity):
                    """
                    Track name object
                    
                    .. attribute:: object  <key>
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_weight
                    
                    	Weight of object
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object, self).__init__()

                        self.yang_name = "object"
                        self.yang_parent_name = "threshold-weight-object"

                        self.object = YLeaf(YType.str, "object")

                        self.object_weight = YLeaf(YType.int32, "object-weight")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object",
                                        "object_weight") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object.is_set or
                            self.object_weight.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object.yfilter != YFilter.not_set or
                            self.object_weight.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "object" + "[object='" + self.object.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object.is_set or self.object.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object.get_name_leafdata())
                        if (self.object_weight.is_set or self.object_weight.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_weight.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object" or name == "object-weight"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object"):
                            self.object = value
                            self.object.value_namespace = name_space
                            self.object.value_namespace_prefix = name_space_prefix
                        if(value_path == "object-weight"):
                            self.object_weight = value
                            self.object_weight.value_namespace = name_space
                            self.object_weight.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.object:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.object:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "threshold-weight-object" + path_buffer

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

                    if (child_yang_name == "object"):
                        for c in self.object:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.object.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "object"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.threshold_percentage is not None and self.threshold_percentage.has_data()) or
                    (self.threshold_percentage_object is not None and self.threshold_percentage_object.has_data()) or
                    (self.threshold_weight is not None and self.threshold_weight.has_data()) or
                    (self.threshold_weight_object is not None and self.threshold_weight_object.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.threshold_percentage is not None and self.threshold_percentage.has_operation()) or
                    (self.threshold_percentage_object is not None and self.threshold_percentage_object.has_operation()) or
                    (self.threshold_weight is not None and self.threshold_weight.has_operation()) or
                    (self.threshold_weight_object is not None and self.threshold_weight_object.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "type-list" + path_buffer

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

                if (child_yang_name == "threshold-percentage"):
                    if (self.threshold_percentage is None):
                        self.threshold_percentage = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage()
                        self.threshold_percentage.parent = self
                        self._children_name_map["threshold_percentage"] = "threshold-percentage"
                    return self.threshold_percentage

                if (child_yang_name == "threshold-percentage-object"):
                    if (self.threshold_percentage_object is None):
                        self.threshold_percentage_object = ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject()
                        self.threshold_percentage_object.parent = self
                        self._children_name_map["threshold_percentage_object"] = "threshold-percentage-object"
                    return self.threshold_percentage_object

                if (child_yang_name == "threshold-weight"):
                    if (self.threshold_weight is None):
                        self.threshold_weight = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight()
                        self.threshold_weight.parent = self
                        self._children_name_map["threshold_weight"] = "threshold-weight"
                    return self.threshold_weight

                if (child_yang_name == "threshold-weight-object"):
                    if (self.threshold_weight_object is None):
                        self.threshold_weight_object = ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject()
                        self.threshold_weight_object.parent = self
                        self._children_name_map["threshold_weight_object"] = "threshold-weight-object"
                    return self.threshold_weight_object

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "threshold-percentage" or name == "threshold-percentage-object" or name == "threshold-weight" or name == "threshold-weight-object"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class TypeRoute(Entity):
            """
            Track type route ipv4
            
            .. attribute:: ip_address
            
            	set track IPv4 address
            	**type**\:   :py:class:`IpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeRoute.IpAddress>`
            
            	**presence node**\: True
            
            .. attribute:: vrf
            
            	VRF tag \- use 'default' for the DEFAULT vrf
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeRoute, self).__init__()

                self.yang_name = "type-route"
                self.yang_parent_name = "object-tracking"

                self.vrf = YLeaf(YType.str, "vrf")

                self.ip_address = None
                self._children_name_map["ip_address"] = "ip-address"
                self._children_yang_names.add("ip-address")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTrackings.ObjectTracking.TypeRoute, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTrackings.ObjectTracking.TypeRoute, self).__setattr__(name, value)


            class IpAddress(Entity):
                """
                set track IPv4 address
                
                .. attribute:: address
                
                	IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mask
                
                	Mask
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeRoute.IpAddress, self).__init__()

                    self.yang_name = "ip-address"
                    self.yang_parent_name = "type-route"
                    self.is_presence_container = True

                    self.address = YLeaf(YType.str, "address")

                    self.mask = YLeaf(YType.str, "mask")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address",
                                    "mask") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTrackings.ObjectTracking.TypeRoute.IpAddress, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTrackings.ObjectTracking.TypeRoute.IpAddress, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.mask.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.mask.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip-address" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mask.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "mask"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "mask"):
                        self.mask = value
                        self.mask.value_namespace = name_space
                        self.mask.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.vrf.is_set or
                    (self.ip_address is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf.yfilter != YFilter.not_set or
                    (self.ip_address is not None and self.ip_address.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "type-route" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ip-address"):
                    if (self.ip_address is None):
                        self.ip_address = ObjectTrackings.ObjectTracking.TypeRoute.IpAddress()
                        self.ip_address.parent = self
                        self._children_name_map["ip_address"] = "ip-address"
                    return self.ip_address

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ip-address" or name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf"):
                    self.vrf = value
                    self.vrf.value_namespace = name_space
                    self.vrf.value_namespace_prefix = name_space_prefix


        class TypeBooleanList(Entity):
            """
            Track type boolean list
            
            .. attribute:: and_objects
            
            	Track type boolean and list
            	**type**\:   :py:class:`AndObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects>`
            
            .. attribute:: or_objects
            
            	Track type boolean or list
            	**type**\:   :py:class:`OrObjects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects>`
            
            

            """

            _prefix = 'manageability-object-tracking-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTrackings.ObjectTracking.TypeBooleanList, self).__init__()

                self.yang_name = "type-boolean-list"
                self.yang_parent_name = "object-tracking"

                self.and_objects = ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects()
                self.and_objects.parent = self
                self._children_name_map["and_objects"] = "and-objects"
                self._children_yang_names.add("and-objects")

                self.or_objects = ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects()
                self.or_objects.parent = self
                self._children_name_map["or_objects"] = "or-objects"
                self._children_yang_names.add("or-objects")


            class OrObjects(Entity):
                """
                Track type boolean or list
                
                .. attribute:: or_object
                
                	Track name \- maximum 32 characters
                	**type**\: list of    :py:class:`OrObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects, self).__init__()

                    self.yang_name = "or-objects"
                    self.yang_parent_name = "type-boolean-list"

                    self.or_object = YList(self)

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
                                super(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects, self).__setattr__(name, value)


                class OrObject(Entity):
                    """
                    Track name \- maximum 32 characters
                    
                    .. attribute:: object  <key>
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_sign
                    
                    	Tracked Object sign (with or without not)
                    	**type**\:   :py:class:`ObjectTrackingBooleanSign <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes.ObjectTrackingBooleanSign>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject, self).__init__()

                        self.yang_name = "or-object"
                        self.yang_parent_name = "or-objects"

                        self.object = YLeaf(YType.str, "object")

                        self.object_sign = YLeaf(YType.enumeration, "object-sign")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object",
                                        "object_sign") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object.is_set or
                            self.object_sign.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object.yfilter != YFilter.not_set or
                            self.object_sign.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "or-object" + "[object='" + self.object.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object.is_set or self.object.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object.get_name_leafdata())
                        if (self.object_sign.is_set or self.object_sign.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_sign.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object" or name == "object-sign"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object"):
                            self.object = value
                            self.object.value_namespace = name_space
                            self.object.value_namespace_prefix = name_space_prefix
                        if(value_path == "object-sign"):
                            self.object_sign = value
                            self.object_sign.value_namespace = name_space
                            self.object_sign.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.or_object:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.or_object:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "or-objects" + path_buffer

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

                    if (child_yang_name == "or-object"):
                        for c in self.or_object:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.or_object.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "or-object"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AndObjects(Entity):
                """
                Track type boolean and list
                
                .. attribute:: and_object
                
                	Track name \- maximum 32 characters
                	**type**\: list of    :py:class:`AndObject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg.ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject>`
                
                

                """

                _prefix = 'manageability-object-tracking-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects, self).__init__()

                    self.yang_name = "and-objects"
                    self.yang_parent_name = "type-boolean-list"

                    self.and_object = YList(self)

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
                                super(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects, self).__setattr__(name, value)


                class AndObject(Entity):
                    """
                    Track name \- maximum 32 characters
                    
                    .. attribute:: object_name  <key>
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: object_sign
                    
                    	Tracked Object sign (with or without not)
                    	**type**\:   :py:class:`ObjectTrackingBooleanSign <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes.ObjectTrackingBooleanSign>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject, self).__init__()

                        self.yang_name = "and-object"
                        self.yang_parent_name = "and-objects"

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.object_sign = YLeaf(YType.enumeration, "object-sign")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name",
                                        "object_sign") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            self.object_sign.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            self.object_sign.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "and-object" + "[object-name='" + self.object_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())
                        if (self.object_sign.is_set or self.object_sign.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_sign.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object-name" or name == "object-sign"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "object-sign"):
                            self.object_sign = value
                            self.object_sign.value_namespace = name_space
                            self.object_sign.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.and_object:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.and_object:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "and-objects" + path_buffer

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

                    if (child_yang_name == "and-object"):
                        for c in self.and_object:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.and_object.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "and-object"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.and_objects is not None and self.and_objects.has_data()) or
                    (self.or_objects is not None and self.or_objects.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.and_objects is not None and self.and_objects.has_operation()) or
                    (self.or_objects is not None and self.or_objects.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "type-boolean-list" + path_buffer

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

                if (child_yang_name == "and-objects"):
                    if (self.and_objects is None):
                        self.and_objects = ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects()
                        self.and_objects.parent = self
                        self._children_name_map["and_objects"] = "and-objects"
                    return self.and_objects

                if (child_yang_name == "or-objects"):
                    if (self.or_objects is None):
                        self.or_objects = ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects()
                        self.or_objects.parent = self
                        self._children_name_map["or_objects"] = "or-objects"
                    return self.or_objects

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "and-objects" or name == "or-objects"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.track_name.is_set or
                self.delay_down.is_set or
                self.delay_up.is_set or
                self.enable.is_set or
                self.type_boolean_list_and_enable.is_set or
                self.type_boolean_list_or_enable.is_set or
                self.type_interface_enable.is_set or
                self.type_route_enable.is_set or
                (self.type_boolean_list is not None and self.type_boolean_list.has_data()) or
                (self.type_interface is not None and self.type_interface.has_data()) or
                (self.type_list is not None and self.type_list.has_data()) or
                (self.type_route is not None and self.type_route.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.track_name.yfilter != YFilter.not_set or
                self.delay_down.yfilter != YFilter.not_set or
                self.delay_up.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                self.type_boolean_list_and_enable.yfilter != YFilter.not_set or
                self.type_boolean_list_or_enable.yfilter != YFilter.not_set or
                self.type_interface_enable.yfilter != YFilter.not_set or
                self.type_route_enable.yfilter != YFilter.not_set or
                (self.type_boolean_list is not None and self.type_boolean_list.has_operation()) or
                (self.type_interface is not None and self.type_interface.has_operation()) or
                (self.type_list is not None and self.type_list.has_operation()) or
                (self.type_route is not None and self.type_route.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "object-tracking" + "[track-name='" + self.track_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-cfg:object-trackings/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.track_name.is_set or self.track_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.track_name.get_name_leafdata())
            if (self.delay_down.is_set or self.delay_down.yfilter != YFilter.not_set):
                leaf_name_data.append(self.delay_down.get_name_leafdata())
            if (self.delay_up.is_set or self.delay_up.yfilter != YFilter.not_set):
                leaf_name_data.append(self.delay_up.get_name_leafdata())
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())
            if (self.type_boolean_list_and_enable.is_set or self.type_boolean_list_and_enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type_boolean_list_and_enable.get_name_leafdata())
            if (self.type_boolean_list_or_enable.is_set or self.type_boolean_list_or_enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type_boolean_list_or_enable.get_name_leafdata())
            if (self.type_interface_enable.is_set or self.type_interface_enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type_interface_enable.get_name_leafdata())
            if (self.type_route_enable.is_set or self.type_route_enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type_route_enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "type-boolean-list"):
                if (self.type_boolean_list is None):
                    self.type_boolean_list = ObjectTrackings.ObjectTracking.TypeBooleanList()
                    self.type_boolean_list.parent = self
                    self._children_name_map["type_boolean_list"] = "type-boolean-list"
                return self.type_boolean_list

            if (child_yang_name == "type-interface"):
                if (self.type_interface is None):
                    self.type_interface = ObjectTrackings.ObjectTracking.TypeInterface()
                    self.type_interface.parent = self
                    self._children_name_map["type_interface"] = "type-interface"
                return self.type_interface

            if (child_yang_name == "type-list"):
                if (self.type_list is None):
                    self.type_list = ObjectTrackings.ObjectTracking.TypeList()
                    self.type_list.parent = self
                    self._children_name_map["type_list"] = "type-list"
                return self.type_list

            if (child_yang_name == "type-route"):
                if (self.type_route is None):
                    self.type_route = ObjectTrackings.ObjectTracking.TypeRoute()
                    self.type_route.parent = self
                    self._children_name_map["type_route"] = "type-route"
                return self.type_route

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "type-boolean-list" or name == "type-interface" or name == "type-list" or name == "type-route" or name == "track-name" or name == "delay-down" or name == "delay-up" or name == "enable" or name == "type-boolean-list-and-enable" or name == "type-boolean-list-or-enable" or name == "type-interface-enable" or name == "type-route-enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "track-name"):
                self.track_name = value
                self.track_name.value_namespace = name_space
                self.track_name.value_namespace_prefix = name_space_prefix
            if(value_path == "delay-down"):
                self.delay_down = value
                self.delay_down.value_namespace = name_space
                self.delay_down.value_namespace_prefix = name_space_prefix
            if(value_path == "delay-up"):
                self.delay_up = value
                self.delay_up.value_namespace = name_space
                self.delay_up.value_namespace_prefix = name_space_prefix
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix
            if(value_path == "type-boolean-list-and-enable"):
                self.type_boolean_list_and_enable = value
                self.type_boolean_list_and_enable.value_namespace = name_space
                self.type_boolean_list_and_enable.value_namespace_prefix = name_space_prefix
            if(value_path == "type-boolean-list-or-enable"):
                self.type_boolean_list_or_enable = value
                self.type_boolean_list_or_enable.value_namespace = name_space
                self.type_boolean_list_or_enable.value_namespace_prefix = name_space_prefix
            if(value_path == "type-interface-enable"):
                self.type_interface_enable = value
                self.type_interface_enable.value_namespace = name_space
                self.type_interface_enable.value_namespace_prefix = name_space_prefix
            if(value_path == "type-route-enable"):
                self.type_route_enable = value
                self.type_route_enable.value_namespace = name_space
                self.type_route_enable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.object_tracking:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.object_tracking:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-cfg:object-trackings" + path_buffer

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

        if (child_yang_name == "object-tracking"):
            for c in self.object_tracking:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = ObjectTrackings.ObjectTracking()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.object_tracking.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "object-tracking"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ObjectTrackings()
        return self._top_entity

