""" Cisco_IOS_XE_platform_oper 

This module contains a collection of YANG definitions
for monitoring of platform components.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PlatformCompType(Enum):
    """
    PlatformCompType

    Component Type

    .. data:: comp_chassis = 0

    .. data:: comp_backplane = 1

    .. data:: comp_power_supply = 2

    .. data:: comp_fan = 3

    .. data:: comp_sensor = 4

    .. data:: comp_module = 5

    .. data:: comp_linecard = 6

    .. data:: comp_port = 7

    .. data:: comp_cpu = 8

    .. data:: comp_operating_system = 9

    .. data:: comp_optical_channel = 10

    .. data:: CONTAINER = 11

    """

    comp_chassis = Enum.YLeaf(0, "comp-chassis")

    comp_backplane = Enum.YLeaf(1, "comp-backplane")

    comp_power_supply = Enum.YLeaf(2, "comp-power-supply")

    comp_fan = Enum.YLeaf(3, "comp-fan")

    comp_sensor = Enum.YLeaf(4, "comp-sensor")

    comp_module = Enum.YLeaf(5, "comp-module")

    comp_linecard = Enum.YLeaf(6, "comp-linecard")

    comp_port = Enum.YLeaf(7, "comp-port")

    comp_cpu = Enum.YLeaf(8, "comp-cpu")

    comp_operating_system = Enum.YLeaf(9, "comp-operating-system")

    comp_optical_channel = Enum.YLeaf(10, "comp-optical-channel")

    CONTAINER = Enum.YLeaf(11, "CONTAINER")


class PlatformPropValueType(Enum):
    """
    PlatformPropValueType

    Property value type

    .. data:: property_string = 0

    .. data:: property_boolean = 1

    .. data:: property_int64 = 2

    .. data:: property_uint64 = 3

    .. data:: property_decimal64 = 4

    """

    property_string = Enum.YLeaf(0, "property-string")

    property_boolean = Enum.YLeaf(1, "property-boolean")

    property_int64 = Enum.YLeaf(2, "property-int64")

    property_uint64 = Enum.YLeaf(3, "property-uint64")

    property_decimal64 = Enum.YLeaf(4, "property-decimal64")



class Components(Entity):
    """
    Enclosing container for the components in the system
    
    .. attribute:: component
    
    	List of components, keyed by component name
    	**type**\: list of    :py:class:`Component <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component>`
    
    

    """

    _prefix = 'platform-ios-xe-oper'
    _revision = '2017-02-06'

    def __init__(self):
        super(Components, self).__init__()
        self._top_entity = None

        self.yang_name = "components"
        self.yang_parent_name = "Cisco-IOS-XE-platform-oper"

        self.component = YList(self)

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
                    super(Components, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Components, self).__setattr__(name, value)


    class Component(Entity):
        """
        List of components, keyed by component name
        
        .. attribute:: cname  <key>
        
        	References component name
        	**type**\:  str
        
        .. attribute:: platform_properties
        
        	Platform component properties
        	**type**\:   :py:class:`PlatformProperties <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformProperties>`
        
        .. attribute:: platform_subcomponents
        
        	Platform subcomponents
        	**type**\:   :py:class:`PlatformSubcomponents <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformSubcomponents>`
        
        .. attribute:: state
        
        	Operational state data for each component
        	**type**\:   :py:class:`State <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.State>`
        
        

        """

        _prefix = 'platform-ios-xe-oper'
        _revision = '2017-02-06'

        def __init__(self):
            super(Components.Component, self).__init__()

            self.yang_name = "component"
            self.yang_parent_name = "components"

            self.cname = YLeaf(YType.str, "cname")

            self.platform_properties = Components.Component.PlatformProperties()
            self.platform_properties.parent = self
            self._children_name_map["platform_properties"] = "platform-properties"
            self._children_yang_names.add("platform-properties")

            self.platform_subcomponents = Components.Component.PlatformSubcomponents()
            self.platform_subcomponents.parent = self
            self._children_name_map["platform_subcomponents"] = "platform-subcomponents"
            self._children_yang_names.add("platform-subcomponents")

            self.state = Components.Component.State()
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
                if name in ("cname") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Components.Component, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Components.Component, self).__setattr__(name, value)


        class State(Entity):
            """
            Operational state data for each component
            
            .. attribute:: description
            
            	System\-supplied description of the component
            	**type**\:  str
            
            .. attribute:: id
            
            	Unique identifier assigned to the component by the system
            	**type**\:  str
            
            .. attribute:: mfg_name
            
            	System\-supplied identifier for the manufacturer of the component.  This data is particularly useful when a component manufacturer is different than the overall device vendor
            	**type**\:  str
            
            .. attribute:: part_no
            
            	System\-assigned part number for the component.  This should be present in particular if the component is also an FRU (field replacable unit)
            	**type**\:  str
            
            .. attribute:: serial_no
            
            	System\-assigned serial number of the component
            	**type**\:  str
            
            .. attribute:: temp
            
            	Temperature in degrees Celsius of the component. Values include the instantaneous, average, minimum, and maximum statistics. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
            	**type**\:   :py:class:`Temp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.State.Temp>`
            
            .. attribute:: type
            
            	Type of component as identified by the system
            	**type**\:   :py:class:`PlatformCompType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.PlatformCompType>`
            
            .. attribute:: version
            
            	System\-defined version string for a hardware, firmware, or software component
            	**type**\:  str
            
            

            """

            _prefix = 'platform-ios-xe-oper'
            _revision = '2017-02-06'

            def __init__(self):
                super(Components.Component.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "component"

                self.description = YLeaf(YType.str, "description")

                self.id = YLeaf(YType.str, "id")

                self.mfg_name = YLeaf(YType.str, "mfg-name")

                self.part_no = YLeaf(YType.str, "part-no")

                self.serial_no = YLeaf(YType.str, "serial-no")

                self.type = YLeaf(YType.enumeration, "type")

                self.version = YLeaf(YType.str, "version")

                self.temp = Components.Component.State.Temp()
                self.temp.parent = self
                self._children_name_map["temp"] = "temp"
                self._children_yang_names.add("temp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("description",
                                "id",
                                "mfg_name",
                                "part_no",
                                "serial_no",
                                "type",
                                "version") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Components.Component.State, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Components.Component.State, self).__setattr__(name, value)


            class Temp(Entity):
                """
                Temperature in degrees Celsius of the component. Values include
                the instantaneous, average, minimum, and maximum statistics. If
                avg/min/max statistics are not supported, the target is expected
                to just supply the instant value
                
                .. attribute:: temp_avg
                
                	Arithmetic mean value of the statistic over a sampling period
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                .. attribute:: temp_instant
                
                	Instantaneous temperature value of a component
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                .. attribute:: temp_max
                
                	High water mark value of the statistic over a sampling period
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                .. attribute:: temp_min
                
                	Low water mark value of the statistic over a sampling period
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                

                """

                _prefix = 'platform-ios-xe-oper'
                _revision = '2017-02-06'

                def __init__(self):
                    super(Components.Component.State.Temp, self).__init__()

                    self.yang_name = "temp"
                    self.yang_parent_name = "state"

                    self.temp_avg = YLeaf(YType.str, "temp-avg")

                    self.temp_instant = YLeaf(YType.str, "temp-instant")

                    self.temp_max = YLeaf(YType.str, "temp-max")

                    self.temp_min = YLeaf(YType.str, "temp-min")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("temp_avg",
                                    "temp_instant",
                                    "temp_max",
                                    "temp_min") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.State.Temp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.State.Temp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.temp_avg.is_set or
                        self.temp_instant.is_set or
                        self.temp_max.is_set or
                        self.temp_min.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.temp_avg.yfilter != YFilter.not_set or
                        self.temp_instant.yfilter != YFilter.not_set or
                        self.temp_max.yfilter != YFilter.not_set or
                        self.temp_min.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "temp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.temp_avg.is_set or self.temp_avg.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temp_avg.get_name_leafdata())
                    if (self.temp_instant.is_set or self.temp_instant.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temp_instant.get_name_leafdata())
                    if (self.temp_max.is_set or self.temp_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temp_max.get_name_leafdata())
                    if (self.temp_min.is_set or self.temp_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.temp_min.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "temp-avg" or name == "temp-instant" or name == "temp-max" or name == "temp-min"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "temp-avg"):
                        self.temp_avg = value
                        self.temp_avg.value_namespace = name_space
                        self.temp_avg.value_namespace_prefix = name_space_prefix
                    if(value_path == "temp-instant"):
                        self.temp_instant = value
                        self.temp_instant.value_namespace = name_space
                        self.temp_instant.value_namespace_prefix = name_space_prefix
                    if(value_path == "temp-max"):
                        self.temp_max = value
                        self.temp_max.value_namespace = name_space
                        self.temp_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "temp-min"):
                        self.temp_min = value
                        self.temp_min.value_namespace = name_space
                        self.temp_min.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.description.is_set or
                    self.id.is_set or
                    self.mfg_name.is_set or
                    self.part_no.is_set or
                    self.serial_no.is_set or
                    self.type.is_set or
                    self.version.is_set or
                    (self.temp is not None and self.temp.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set or
                    self.mfg_name.yfilter != YFilter.not_set or
                    self.part_no.yfilter != YFilter.not_set or
                    self.serial_no.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.version.yfilter != YFilter.not_set or
                    (self.temp is not None and self.temp.has_operation()))

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
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())
                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id.get_name_leafdata())
                if (self.mfg_name.is_set or self.mfg_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mfg_name.get_name_leafdata())
                if (self.part_no.is_set or self.part_no.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.part_no.get_name_leafdata())
                if (self.serial_no.is_set or self.serial_no.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.serial_no.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.version.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "temp"):
                    if (self.temp is None):
                        self.temp = Components.Component.State.Temp()
                        self.temp.parent = self
                        self._children_name_map["temp"] = "temp"
                    return self.temp

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "temp" or name == "description" or name == "id" or name == "mfg-name" or name == "part-no" or name == "serial-no" or name == "type" or name == "version"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix
                if(value_path == "id"):
                    self.id = value
                    self.id.value_namespace = name_space
                    self.id.value_namespace_prefix = name_space_prefix
                if(value_path == "mfg-name"):
                    self.mfg_name = value
                    self.mfg_name.value_namespace = name_space
                    self.mfg_name.value_namespace_prefix = name_space_prefix
                if(value_path == "part-no"):
                    self.part_no = value
                    self.part_no.value_namespace = name_space
                    self.part_no.value_namespace_prefix = name_space_prefix
                if(value_path == "serial-no"):
                    self.serial_no = value
                    self.serial_no.value_namespace = name_space
                    self.serial_no.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "version"):
                    self.version = value
                    self.version.value_namespace = name_space
                    self.version.value_namespace_prefix = name_space_prefix


        class PlatformProperties(Entity):
            """
            Platform component properties
            
            .. attribute:: platform_property
            
            	List of platform component properties
            	**type**\: list of    :py:class:`PlatformProperty <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformProperties.PlatformProperty>`
            
            

            """

            _prefix = 'platform-ios-xe-oper'
            _revision = '2017-02-06'

            def __init__(self):
                super(Components.Component.PlatformProperties, self).__init__()

                self.yang_name = "platform-properties"
                self.yang_parent_name = "component"

                self.platform_property = YList(self)

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
                            super(Components.Component.PlatformProperties, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Components.Component.PlatformProperties, self).__setattr__(name, value)


            class PlatformProperty(Entity):
                """
                List of platform component properties
                
                .. attribute:: name  <key>
                
                	Property name
                	**type**\:  str
                
                .. attribute:: configurable
                
                	Indication of whether the property is user\-configurable
                	**type**\:  bool
                
                .. attribute:: parent_platform_component_cname_key
                
                	Name of the parent component
                	**type**\:  str
                
                .. attribute:: value
                
                	Property value
                	**type**\:   :py:class:`Value <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformProperties.PlatformProperty.Value>`
                
                

                """

                _prefix = 'platform-ios-xe-oper'
                _revision = '2017-02-06'

                def __init__(self):
                    super(Components.Component.PlatformProperties.PlatformProperty, self).__init__()

                    self.yang_name = "platform-property"
                    self.yang_parent_name = "platform-properties"

                    self.name = YLeaf(YType.str, "name")

                    self.configurable = YLeaf(YType.boolean, "configurable")

                    self.parent_platform_component_cname_key = YLeaf(YType.str, "parent-platform-component-cname-key")

                    self.value = Components.Component.PlatformProperties.PlatformProperty.Value()
                    self.value.parent = self
                    self._children_name_map["value"] = "value"
                    self._children_yang_names.add("value")

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
                                    "configurable",
                                    "parent_platform_component_cname_key") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.PlatformProperties.PlatformProperty, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.PlatformProperties.PlatformProperty, self).__setattr__(name, value)


                class Value(Entity):
                    """
                    Property value
                    
                    .. attribute:: boolean
                    
                    	Boolean property value
                    	**type**\:  bool
                    
                    .. attribute:: decimal
                    
                    	Decimal64 property value
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: intsixfour
                    
                    	Integer64 property value
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    .. attribute:: string
                    
                    	String property value
                    	**type**\:  str
                    
                    .. attribute:: uintsixfour
                    
                    	Unsigned integer64 property value
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'platform-ios-xe-oper'
                    _revision = '2017-02-06'

                    def __init__(self):
                        super(Components.Component.PlatformProperties.PlatformProperty.Value, self).__init__()

                        self.yang_name = "value"
                        self.yang_parent_name = "platform-property"

                        self.boolean = YLeaf(YType.boolean, "boolean")

                        self.decimal = YLeaf(YType.str, "decimal")

                        self.intsixfour = YLeaf(YType.int64, "intsixfour")

                        self.string = YLeaf(YType.str, "string")

                        self.uintsixfour = YLeaf(YType.uint64, "uintsixfour")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("boolean",
                                        "decimal",
                                        "intsixfour",
                                        "string",
                                        "uintsixfour") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.PlatformProperties.PlatformProperty.Value, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.PlatformProperties.PlatformProperty.Value, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.boolean.is_set or
                            self.decimal.is_set or
                            self.intsixfour.is_set or
                            self.string.is_set or
                            self.uintsixfour.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.boolean.yfilter != YFilter.not_set or
                            self.decimal.yfilter != YFilter.not_set or
                            self.intsixfour.yfilter != YFilter.not_set or
                            self.string.yfilter != YFilter.not_set or
                            self.uintsixfour.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "value" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.boolean.is_set or self.boolean.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.boolean.get_name_leafdata())
                        if (self.decimal.is_set or self.decimal.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.decimal.get_name_leafdata())
                        if (self.intsixfour.is_set or self.intsixfour.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.intsixfour.get_name_leafdata())
                        if (self.string.is_set or self.string.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.string.get_name_leafdata())
                        if (self.uintsixfour.is_set or self.uintsixfour.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uintsixfour.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "boolean" or name == "decimal" or name == "intsixfour" or name == "string" or name == "uintsixfour"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "boolean"):
                            self.boolean = value
                            self.boolean.value_namespace = name_space
                            self.boolean.value_namespace_prefix = name_space_prefix
                        if(value_path == "decimal"):
                            self.decimal = value
                            self.decimal.value_namespace = name_space
                            self.decimal.value_namespace_prefix = name_space_prefix
                        if(value_path == "intsixfour"):
                            self.intsixfour = value
                            self.intsixfour.value_namespace = name_space
                            self.intsixfour.value_namespace_prefix = name_space_prefix
                        if(value_path == "string"):
                            self.string = value
                            self.string.value_namespace = name_space
                            self.string.value_namespace_prefix = name_space_prefix
                        if(value_path == "uintsixfour"):
                            self.uintsixfour = value
                            self.uintsixfour.value_namespace = name_space
                            self.uintsixfour.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.configurable.is_set or
                        self.parent_platform_component_cname_key.is_set or
                        (self.value is not None and self.value.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.configurable.yfilter != YFilter.not_set or
                        self.parent_platform_component_cname_key.yfilter != YFilter.not_set or
                        (self.value is not None and self.value.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "platform-property" + "[name='" + self.name.get() + "']" + path_buffer

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
                    if (self.configurable.is_set or self.configurable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configurable.get_name_leafdata())
                    if (self.parent_platform_component_cname_key.is_set or self.parent_platform_component_cname_key.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.parent_platform_component_cname_key.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "value"):
                        if (self.value is None):
                            self.value = Components.Component.PlatformProperties.PlatformProperty.Value()
                            self.value.parent = self
                            self._children_name_map["value"] = "value"
                        return self.value

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "value" or name == "name" or name == "configurable" or name == "parent-platform-component-cname-key"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "configurable"):
                        self.configurable = value
                        self.configurable.value_namespace = name_space
                        self.configurable.value_namespace_prefix = name_space_prefix
                    if(value_path == "parent-platform-component-cname-key"):
                        self.parent_platform_component_cname_key = value
                        self.parent_platform_component_cname_key.value_namespace = name_space
                        self.parent_platform_component_cname_key.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.platform_property:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.platform_property:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "platform-properties" + path_buffer

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

                if (child_yang_name == "platform-property"):
                    for c in self.platform_property:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Components.Component.PlatformProperties.PlatformProperty()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.platform_property.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "platform-property"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class PlatformSubcomponents(Entity):
            """
            Platform subcomponents
            
            .. attribute:: platform_subcomponent
            
            	List of platform subcomponents
            	**type**\: list of    :py:class:`PlatformSubcomponent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_oper.Components.Component.PlatformSubcomponents.PlatformSubcomponent>`
            
            

            """

            _prefix = 'platform-ios-xe-oper'
            _revision = '2017-02-06'

            def __init__(self):
                super(Components.Component.PlatformSubcomponents, self).__init__()

                self.yang_name = "platform-subcomponents"
                self.yang_parent_name = "component"

                self.platform_subcomponent = YList(self)

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
                            super(Components.Component.PlatformSubcomponents, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Components.Component.PlatformSubcomponents, self).__setattr__(name, value)


            class PlatformSubcomponent(Entity):
                """
                List of platform subcomponents
                
                .. attribute:: name  <key>
                
                	Subcomponent name
                	**type**\:  str
                
                .. attribute:: parent_platform_component_cname_key
                
                	Name of the parent component
                	**type**\:  str
                
                

                """

                _prefix = 'platform-ios-xe-oper'
                _revision = '2017-02-06'

                def __init__(self):
                    super(Components.Component.PlatformSubcomponents.PlatformSubcomponent, self).__init__()

                    self.yang_name = "platform-subcomponent"
                    self.yang_parent_name = "platform-subcomponents"

                    self.name = YLeaf(YType.str, "name")

                    self.parent_platform_component_cname_key = YLeaf(YType.str, "parent-platform-component-cname-key")

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
                                    "parent_platform_component_cname_key") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.PlatformSubcomponents.PlatformSubcomponent, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.PlatformSubcomponents.PlatformSubcomponent, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.parent_platform_component_cname_key.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.parent_platform_component_cname_key.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "platform-subcomponent" + "[name='" + self.name.get() + "']" + path_buffer

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
                    if (self.parent_platform_component_cname_key.is_set or self.parent_platform_component_cname_key.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.parent_platform_component_cname_key.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name" or name == "parent-platform-component-cname-key"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "parent-platform-component-cname-key"):
                        self.parent_platform_component_cname_key = value
                        self.parent_platform_component_cname_key.value_namespace = name_space
                        self.parent_platform_component_cname_key.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.platform_subcomponent:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.platform_subcomponent:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "platform-subcomponents" + path_buffer

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

                if (child_yang_name == "platform-subcomponent"):
                    for c in self.platform_subcomponent:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Components.Component.PlatformSubcomponents.PlatformSubcomponent()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.platform_subcomponent.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "platform-subcomponent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.cname.is_set or
                (self.platform_properties is not None and self.platform_properties.has_data()) or
                (self.platform_subcomponents is not None and self.platform_subcomponents.has_data()) or
                (self.state is not None and self.state.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cname.yfilter != YFilter.not_set or
                (self.platform_properties is not None and self.platform_properties.has_operation()) or
                (self.platform_subcomponents is not None and self.platform_subcomponents.has_operation()) or
                (self.state is not None and self.state.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "component" + "[cname='" + self.cname.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-platform-oper:components/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cname.is_set or self.cname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cname.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "platform-properties"):
                if (self.platform_properties is None):
                    self.platform_properties = Components.Component.PlatformProperties()
                    self.platform_properties.parent = self
                    self._children_name_map["platform_properties"] = "platform-properties"
                return self.platform_properties

            if (child_yang_name == "platform-subcomponents"):
                if (self.platform_subcomponents is None):
                    self.platform_subcomponents = Components.Component.PlatformSubcomponents()
                    self.platform_subcomponents.parent = self
                    self._children_name_map["platform_subcomponents"] = "platform-subcomponents"
                return self.platform_subcomponents

            if (child_yang_name == "state"):
                if (self.state is None):
                    self.state = Components.Component.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                return self.state

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "platform-properties" or name == "platform-subcomponents" or name == "state" or name == "cname"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cname"):
                self.cname = value
                self.cname.value_namespace = name_space
                self.cname.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.component:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.component:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-platform-oper:components" + path_buffer

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

        if (child_yang_name == "component"):
            for c in self.component:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = Components.Component()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.component.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "component"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Components()
        return self._top_entity

