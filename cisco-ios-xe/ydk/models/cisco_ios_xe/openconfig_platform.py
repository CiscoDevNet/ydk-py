""" openconfig_platform 

This module defines a data model for representing a system
component inventory, which can include hardware or software
elements arranged in an arbitrary structure. The primary
relationship supported by the model is containment, e.g.,
components containing subcomponents.
It is expected that this model reflects every field replacable
unit on the device at a minimum (i.e., additional information
may be supplied about non\-replacable components).
Every element in the inventory is termed a 'component' with each
component expected to have a unique name and type, and optionally
a unique system\-assigned identifier and FRU number.  The
uniqueness is guaranteed by the system within the device.
Components may have properties defined by the system that are
modeled as a list of key\-value pairs. These may or may not be
user\-configurable.  The model provides a flag for the system
to optionally indicate which properties are user configurable.
Each component also has a list of 'subcomponents' which are
references to other components. Appearance in a list of
subcomponents indicates a containment relationship as described
above.  For example, a linecard component may have a list of
references to port components that reside on the linecard.
This schema is generic to allow devices to express their own
platform\-specific structure.  It may be augmented by additional
component type\-specific schemas that provide a common structure
for well\-known component types.  In these cases, the system is
expected to populate the common component schema, and may
optionally also represent the component and its properties in the
generic structure.
The properties for each component may include dynamic values,
e.g., in the 'state' part of the schema.  For example, a CPU
component may report its utilization, temperature, or other
physical properties.  The intent is to capture all platform\-
specific physical data in one location, including inventory
(presence or absence of a component) and state (physical
attributes or status).

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Components(Entity):
    """
    Enclosing container for the components in the system.
    
    .. attribute:: component
    
    	List of components, keyed by component name
    	**type**\: list of    :py:class:`Component <ydk.models.openconfig.openconfig_platform.Components.Component>`
    
    

    """

    _prefix = 'oc-platform'
    _revision = '2016-06-06'

    def __init__(self):
        super(Components, self).__init__()
        self._top_entity = None

        self.yang_name = "components"
        self.yang_parent_name = "openconfig-platform"

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
        List of components, keyed by component name.
        
        .. attribute:: name  <key>
        
        	References the component name
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
        
        .. attribute:: config
        
        	Configuration data for each component
        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
        
        .. attribute:: optical_channel
        
        	Enclosing container for the list of optical channels
        	**type**\:   :py:class:`OpticalChannel <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel>`
        
        .. attribute:: properties
        
        	Enclosing container 
        	**type**\:   :py:class:`Properties <ydk.models.openconfig.openconfig_platform.Components.Component.Properties>`
        
        .. attribute:: state
        
        	Operational state data for each component
        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.State>`
        
        .. attribute:: subcomponents
        
        	Enclosing container for subcomponent references
        	**type**\:   :py:class:`Subcomponents <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents>`
        
        .. attribute:: transceiver
        
        	Top\-level container for client port transceiver data
        	**type**\:   :py:class:`Transceiver <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver>`
        
        

        """

        _prefix = 'oc-platform'
        _revision = '2016-06-06'

        def __init__(self):
            super(Components.Component, self).__init__()

            self.yang_name = "component"
            self.yang_parent_name = "components"

            self.name = YLeaf(YType.str, "name")

            self.config = Components.Component.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"
            self._children_yang_names.add("config")

            self.optical_channel = Components.Component.OpticalChannel()
            self.optical_channel.parent = self
            self._children_name_map["optical_channel"] = "optical-channel"
            self._children_yang_names.add("optical-channel")

            self.properties = Components.Component.Properties()
            self.properties.parent = self
            self._children_name_map["properties"] = "properties"
            self._children_yang_names.add("properties")

            self.state = Components.Component.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._children_yang_names.add("state")

            self.subcomponents = Components.Component.Subcomponents()
            self.subcomponents.parent = self
            self._children_name_map["subcomponents"] = "subcomponents"
            self._children_yang_names.add("subcomponents")

            self.transceiver = Components.Component.Transceiver()
            self.transceiver.parent = self
            self._children_name_map["transceiver"] = "transceiver"
            self._children_yang_names.add("transceiver")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("name") and name in self.__dict__:
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


        class Config(Entity):
            """
            Configuration data for each component
            
            .. attribute:: name
            
            	Device name for the component \-\- this will not be a configurable parameter on many implementations
            	**type**\:  str
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                super(Components.Component.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "component"

                self.name = YLeaf(YType.str, "name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Components.Component.Config, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Components.Component.Config, self).__setattr__(name, value)

            def has_data(self):
                return self.name.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set)

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
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix


        class State(Entity):
            """
            Operational state data for each component
            
            .. attribute:: description
            
            	System\-supplied description of the component
            	**type**\:  str
            
            .. attribute:: id
            
            	Unique identifier assigned by the system for the component
            	**type**\:  str
            
            .. attribute:: mfg_name
            
            	System\-supplied identifier for the manufacturer of the component.  This data is particularly useful when a component manufacturer is different than the overall device vendor
            	**type**\:  str
            
            .. attribute:: name
            
            	Device name for the component \-\- this will not be a configurable parameter on many implementations
            	**type**\:  str
            
            .. attribute:: part_no
            
            	System\-assigned part number for the component.  This should be present in particular if the component is also an FRU (field replacable unit)
            	**type**\:  str
            
            .. attribute:: serial_no
            
            	System\-assigned serial number of the component
            	**type**\:  str
            
            .. attribute:: type
            
            	Type of component as identified by the system
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`Openconfig_Hardware_Component <ydk.models.openconfig.openconfig_platform_types.Openconfig_Hardware_Component>`
            
            
            ----
            	**type**\:   :py:class:`Openconfig_Software_Component <ydk.models.openconfig.openconfig_platform_types.Openconfig_Software_Component>`
            
            
            ----
            .. attribute:: version
            
            	System\-defined version string for a hardware, firmware, or software component
            	**type**\:  str
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                super(Components.Component.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "component"

                self.description = YLeaf(YType.str, "description")

                self.id = YLeaf(YType.str, "id")

                self.mfg_name = YLeaf(YType.str, "mfg-name")

                self.name = YLeaf(YType.str, "name")

                self.part_no = YLeaf(YType.str, "part-no")

                self.serial_no = YLeaf(YType.str, "serial-no")

                self.type = YLeaf(YType.str, "type")

                self.version = YLeaf(YType.str, "version")

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
                                "name",
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

            def has_data(self):
                return (
                    self.description.is_set or
                    self.id.is_set or
                    self.mfg_name.is_set or
                    self.name.is_set or
                    self.part_no.is_set or
                    self.serial_no.is_set or
                    self.type.is_set or
                    self.version.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set or
                    self.mfg_name.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.part_no.yfilter != YFilter.not_set or
                    self.serial_no.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.version.yfilter != YFilter.not_set)

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
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
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

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "description" or name == "id" or name == "mfg-name" or name == "name" or name == "part-no" or name == "serial-no" or name == "type" or name == "version"):
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
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
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


        class Properties(Entity):
            """
            Enclosing container 
            
            .. attribute:: property
            
            	List of system properties for the component
            	**type**\: list of    :py:class:`Property <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                super(Components.Component.Properties, self).__init__()

                self.yang_name = "properties"
                self.yang_parent_name = "component"

                self.property = YList(self)

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
                            super(Components.Component.Properties, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Components.Component.Properties, self).__setattr__(name, value)


            class Property(Entity):
                """
                List of system properties for the component
                
                .. attribute:: name  <key>
                
                	Reference to the property name
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.Config>`
                
                .. attribute:: config
                
                	Configuration data for each property
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.Config>`
                
                .. attribute:: state
                
                	Operational state data for each property
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.State>`
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2016-06-06'

                def __init__(self):
                    super(Components.Component.Properties.Property, self).__init__()

                    self.yang_name = "property"
                    self.yang_parent_name = "properties"

                    self.name = YLeaf(YType.str, "name")

                    self.config = Components.Component.Properties.Property.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Components.Component.Properties.Property.State()
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
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.Properties.Property, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.Properties.Property, self).__setattr__(name, value)


                class Config(Entity):
                    """
                    Configuration data for each property
                    
                    .. attribute:: name
                    
                    	System\-supplied name of the property \-\- this is typically non\-configurable
                    	**type**\:  str
                    
                    .. attribute:: value
                    
                    	Property values can take on a variety of types.  Signed and unsigned integer types may be provided in smaller sizes, e.g., int8, uint16, etc
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    
                    ----
                    	**type**\:  bool
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    
                    ----
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    
                    ----
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        super(Components.Component.Properties.Property.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "property"

                        self.name = YLeaf(YType.str, "name")

                        self.value = YLeaf(YType.str, "value")

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
                                        "value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.Properties.Property.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.Properties.Property.Config, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.name.is_set or
                            self.value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set)

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
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
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
                        if(name == "name" or name == "value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix


                class State(Entity):
                    """
                    Operational state data for each property
                    
                    .. attribute:: configurable
                    
                    	Indication whether the property is user\-configurable
                    	**type**\:  bool
                    
                    .. attribute:: name
                    
                    	System\-supplied name of the property \-\- this is typically non\-configurable
                    	**type**\:  str
                    
                    .. attribute:: value
                    
                    	Property values can take on a variety of types.  Signed and unsigned integer types may be provided in smaller sizes, e.g., int8, uint16, etc
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    
                    ----
                    	**type**\:  bool
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    
                    ----
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    
                    ----
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        super(Components.Component.Properties.Property.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "property"

                        self.configurable = YLeaf(YType.boolean, "configurable")

                        self.name = YLeaf(YType.str, "name")

                        self.value = YLeaf(YType.str, "value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("configurable",
                                        "name",
                                        "value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.Properties.Property.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.Properties.Property.State, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.configurable.is_set or
                            self.name.is_set or
                            self.value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.configurable.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set)

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
                        if (self.configurable.is_set or self.configurable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configurable.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
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
                        if(name == "configurable" or name == "name" or name == "value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "configurable"):
                            self.configurable = value
                            self.configurable.value_namespace = name_space
                            self.configurable.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        (self.config is not None and self.config.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "property" + "[name='" + self.name.get() + "']" + path_buffer

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

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = Components.Component.Properties.Property.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = Components.Component.Properties.Property.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "state" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.property:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.property:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "properties" + path_buffer

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

                if (child_yang_name == "property"):
                    for c in self.property:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Components.Component.Properties.Property()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.property.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "property"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Subcomponents(Entity):
            """
            Enclosing container for subcomponent references
            
            .. attribute:: subcomponent
            
            	List of subcomponent references
            	**type**\: list of    :py:class:`Subcomponent <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                super(Components.Component.Subcomponents, self).__init__()

                self.yang_name = "subcomponents"
                self.yang_parent_name = "component"

                self.subcomponent = YList(self)

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
                            super(Components.Component.Subcomponents, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Components.Component.Subcomponents, self).__setattr__(name, value)


            class Subcomponent(Entity):
                """
                List of subcomponent references
                
                .. attribute:: name  <key>
                
                	Reference to the name list key
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.Config>`
                
                .. attribute:: config
                
                	Configuration data 
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.Config>`
                
                .. attribute:: state
                
                	Operational state data 
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.State>`
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2016-06-06'

                def __init__(self):
                    super(Components.Component.Subcomponents.Subcomponent, self).__init__()

                    self.yang_name = "subcomponent"
                    self.yang_parent_name = "subcomponents"

                    self.name = YLeaf(YType.str, "name")

                    self.config = Components.Component.Subcomponents.Subcomponent.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Components.Component.Subcomponents.Subcomponent.State()
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
                        if name in ("name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.Subcomponents.Subcomponent, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.Subcomponents.Subcomponent, self).__setattr__(name, value)


                class Config(Entity):
                    """
                    Configuration data 
                    
                    .. attribute:: name
                    
                    	Reference to the name of the subcomponent
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        super(Components.Component.Subcomponents.Subcomponent.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "subcomponent"

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.Subcomponents.Subcomponent.Config, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.Subcomponents.Subcomponent.Config, self).__setattr__(name, value)

                    def has_data(self):
                        return self.name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

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
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


                class State(Entity):
                    """
                    Operational state data 
                    
                    .. attribute:: name
                    
                    	Reference to the name of the subcomponent
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        super(Components.Component.Subcomponents.Subcomponent.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "subcomponent"

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.Subcomponents.Subcomponent.State, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.Subcomponents.Subcomponent.State, self).__setattr__(name, value)

                    def has_data(self):
                        return self.name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

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
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        (self.config is not None and self.config.has_data()) or
                        (self.state is not None and self.state.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        (self.config is not None and self.config.has_operation()) or
                        (self.state is not None and self.state.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "subcomponent" + "[name='" + self.name.get() + "']" + path_buffer

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

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "config"):
                        if (self.config is None):
                            self.config = Components.Component.Subcomponents.Subcomponent.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                        return self.config

                    if (child_yang_name == "state"):
                        if (self.state is None):
                            self.state = Components.Component.Subcomponents.Subcomponent.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                        return self.state

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "config" or name == "state" or name == "name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.subcomponent:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.subcomponent:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "subcomponents" + path_buffer

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

                if (child_yang_name == "subcomponent"):
                    for c in self.subcomponent:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Components.Component.Subcomponents.Subcomponent()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.subcomponent.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "subcomponent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Transceiver(Entity):
            """
            Top\-level container for client port transceiver data
            
            .. attribute:: config
            
            	Configuration data for client port transceivers
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.Config>`
            
            .. attribute:: physical_channels
            
            	Enclosing container for client channels
            	**type**\:   :py:class:`PhysicalChannels <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels>`
            
            .. attribute:: state
            
            	Operational state data for client port transceivers
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State>`
            
            

            """

            _prefix = 'oc-transceiver'
            _revision = '2016-05-24'

            def __init__(self):
                super(Components.Component.Transceiver, self).__init__()

                self.yang_name = "transceiver"
                self.yang_parent_name = "component"

                self.config = Components.Component.Transceiver.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.physical_channels = Components.Component.Transceiver.PhysicalChannels()
                self.physical_channels.parent = self
                self._children_name_map["physical_channels"] = "physical-channels"
                self._children_yang_names.add("physical-channels")

                self.state = Components.Component.Transceiver.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")


            class Config(Entity):
                """
                Configuration data for client port transceivers
                
                .. attribute:: enabled
                
                	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                	**type**\:  bool
                
                .. attribute:: form_factor
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not plugable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre\-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system
                	**type**\:   :py:class:`Transceiver_Form_Factor_Type <ydk.models.openconfig.openconfig_transport_types.Transceiver_Form_Factor_Type>`
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2016-05-24'

                def __init__(self):
                    super(Components.Component.Transceiver.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "transceiver"

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.form_factor = YLeaf(YType.identityref, "form-factor")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("enabled",
                                    "form_factor") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.Transceiver.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.Transceiver.Config, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.enabled.is_set or
                        self.form_factor.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.form_factor.yfilter != YFilter.not_set)

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
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.form_factor.is_set or self.form_factor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.form_factor.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "enabled" or name == "form-factor"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "form-factor"):
                        self.form_factor = value
                        self.form_factor.value_namespace = name_space
                        self.form_factor.value_namespace_prefix = name_space_prefix


            class State(Entity):
                """
                Operational state data for client port transceivers
                
                .. attribute:: connector_type
                
                	Connector type used on this port
                	**type**\:   :py:class:`Fiber_Connector_Type <ydk.models.openconfig.openconfig_transport_types.Fiber_Connector_Type>`
                
                .. attribute:: date_code
                
                	Representation of the transceiver date code, typically stored as YYMMDD.  The time portion of the value is undefined and not intended to be read
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: enabled
                
                	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                	**type**\:  bool
                
                .. attribute:: ethernet_compliance_code
                
                	Ethernet PMD that the transceiver supports. The SFF/QSFP MSAs have registers for this and CFP MSA has similar
                	**type**\:   :py:class:`Ethernet_Pmd_Type <ydk.models.openconfig.openconfig_transport_types.Ethernet_Pmd_Type>`
                
                .. attribute:: fault_condition
                
                	Indicates if a fault condition exists in the transceiver
                	**type**\:  bool
                
                .. attribute:: form_factor
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not plugable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre\-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system
                	**type**\:   :py:class:`Transceiver_Form_Factor_Type <ydk.models.openconfig.openconfig_transport_types.Transceiver_Form_Factor_Type>`
                
                .. attribute:: internal_temp
                
                	Internally measured temperature in degrees Celsius. MSA valid range is between \-40 and +125C. Accuracy shall be better than +/\- 3 degC over the whole temperature range
                	**type**\:  int
                
                	**range:** \-40..125
                
                .. attribute:: otn_compliance_code
                
                	OTN application code supported by the port
                	**type**\:   :py:class:`Otn_Application_Code <ydk.models.openconfig.openconfig_transport_types.Otn_Application_Code>`
                
                .. attribute:: present
                
                	Indicates whether a transceiver is present in the specified client port
                	**type**\:   :py:class:`Present <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.Present>`
                
                .. attribute:: serial_no
                
                	Transceiver serial number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part serial number is undefined, all 16 octets = 0h
                	**type**\:  str
                
                	**length:** 1..16
                
                .. attribute:: sonet_sdh_compliance_code
                
                	SONET/SDH application code supported by the port
                	**type**\:   :py:class:`Sonet_Application_Code <ydk.models.openconfig.openconfig_transport_types.Sonet_Application_Code>`
                
                .. attribute:: vendor
                
                	Full name of transceiver vendor. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h)
                	**type**\:  str
                
                	**length:** 1..16
                
                .. attribute:: vendor_part
                
                	Transceiver vendor's part number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part number is undefined, all 16 octets = 0h
                	**type**\:  str
                
                	**length:** 1..16
                
                .. attribute:: vendor_rev
                
                	Transceiver vendor's revision number. 2\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h)
                	**type**\:  str
                
                	**length:** 1..2
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2016-05-24'

                def __init__(self):
                    super(Components.Component.Transceiver.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "transceiver"

                    self.connector_type = YLeaf(YType.identityref, "connector-type")

                    self.date_code = YLeaf(YType.str, "date-code")

                    self.enabled = YLeaf(YType.boolean, "enabled")

                    self.ethernet_compliance_code = YLeaf(YType.identityref, "ethernet-compliance-code")

                    self.fault_condition = YLeaf(YType.boolean, "fault-condition")

                    self.form_factor = YLeaf(YType.identityref, "form-factor")

                    self.internal_temp = YLeaf(YType.int16, "internal-temp")

                    self.otn_compliance_code = YLeaf(YType.identityref, "otn-compliance-code")

                    self.present = YLeaf(YType.enumeration, "present")

                    self.serial_no = YLeaf(YType.str, "serial-no")

                    self.sonet_sdh_compliance_code = YLeaf(YType.identityref, "sonet-sdh-compliance-code")

                    self.vendor = YLeaf(YType.str, "vendor")

                    self.vendor_part = YLeaf(YType.str, "vendor-part")

                    self.vendor_rev = YLeaf(YType.str, "vendor-rev")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("connector_type",
                                    "date_code",
                                    "enabled",
                                    "ethernet_compliance_code",
                                    "fault_condition",
                                    "form_factor",
                                    "internal_temp",
                                    "otn_compliance_code",
                                    "present",
                                    "serial_no",
                                    "sonet_sdh_compliance_code",
                                    "vendor",
                                    "vendor_part",
                                    "vendor_rev") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.Transceiver.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.Transceiver.State, self).__setattr__(name, value)

                class Present(Enum):
                    """
                    Present

                    Indicates whether a transceiver is present in

                    the specified client port.

                    .. data:: PRESENT = 0

                    	Transceiver is present on the port

                    .. data:: NOT_PRESENT = 1

                    	Transceiver is not present on the port

                    """

                    PRESENT = Enum.YLeaf(0, "PRESENT")

                    NOT_PRESENT = Enum.YLeaf(1, "NOT_PRESENT")


                def has_data(self):
                    return (
                        self.connector_type.is_set or
                        self.date_code.is_set or
                        self.enabled.is_set or
                        self.ethernet_compliance_code.is_set or
                        self.fault_condition.is_set or
                        self.form_factor.is_set or
                        self.internal_temp.is_set or
                        self.otn_compliance_code.is_set or
                        self.present.is_set or
                        self.serial_no.is_set or
                        self.sonet_sdh_compliance_code.is_set or
                        self.vendor.is_set or
                        self.vendor_part.is_set or
                        self.vendor_rev.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.connector_type.yfilter != YFilter.not_set or
                        self.date_code.yfilter != YFilter.not_set or
                        self.enabled.yfilter != YFilter.not_set or
                        self.ethernet_compliance_code.yfilter != YFilter.not_set or
                        self.fault_condition.yfilter != YFilter.not_set or
                        self.form_factor.yfilter != YFilter.not_set or
                        self.internal_temp.yfilter != YFilter.not_set or
                        self.otn_compliance_code.yfilter != YFilter.not_set or
                        self.present.yfilter != YFilter.not_set or
                        self.serial_no.yfilter != YFilter.not_set or
                        self.sonet_sdh_compliance_code.yfilter != YFilter.not_set or
                        self.vendor.yfilter != YFilter.not_set or
                        self.vendor_part.yfilter != YFilter.not_set or
                        self.vendor_rev.yfilter != YFilter.not_set)

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
                    if (self.connector_type.is_set or self.connector_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.connector_type.get_name_leafdata())
                    if (self.date_code.is_set or self.date_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.date_code.get_name_leafdata())
                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enabled.get_name_leafdata())
                    if (self.ethernet_compliance_code.is_set or self.ethernet_compliance_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ethernet_compliance_code.get_name_leafdata())
                    if (self.fault_condition.is_set or self.fault_condition.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fault_condition.get_name_leafdata())
                    if (self.form_factor.is_set or self.form_factor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.form_factor.get_name_leafdata())
                    if (self.internal_temp.is_set or self.internal_temp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.internal_temp.get_name_leafdata())
                    if (self.otn_compliance_code.is_set or self.otn_compliance_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.otn_compliance_code.get_name_leafdata())
                    if (self.present.is_set or self.present.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.present.get_name_leafdata())
                    if (self.serial_no.is_set or self.serial_no.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.serial_no.get_name_leafdata())
                    if (self.sonet_sdh_compliance_code.is_set or self.sonet_sdh_compliance_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sonet_sdh_compliance_code.get_name_leafdata())
                    if (self.vendor.is_set or self.vendor.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vendor.get_name_leafdata())
                    if (self.vendor_part.is_set or self.vendor_part.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vendor_part.get_name_leafdata())
                    if (self.vendor_rev.is_set or self.vendor_rev.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vendor_rev.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "connector-type" or name == "date-code" or name == "enabled" or name == "ethernet-compliance-code" or name == "fault-condition" or name == "form-factor" or name == "internal-temp" or name == "otn-compliance-code" or name == "present" or name == "serial-no" or name == "sonet-sdh-compliance-code" or name == "vendor" or name == "vendor-part" or name == "vendor-rev"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "connector-type"):
                        self.connector_type = value
                        self.connector_type.value_namespace = name_space
                        self.connector_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "date-code"):
                        self.date_code = value
                        self.date_code.value_namespace = name_space
                        self.date_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "enabled"):
                        self.enabled = value
                        self.enabled.value_namespace = name_space
                        self.enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "ethernet-compliance-code"):
                        self.ethernet_compliance_code = value
                        self.ethernet_compliance_code.value_namespace = name_space
                        self.ethernet_compliance_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "fault-condition"):
                        self.fault_condition = value
                        self.fault_condition.value_namespace = name_space
                        self.fault_condition.value_namespace_prefix = name_space_prefix
                    if(value_path == "form-factor"):
                        self.form_factor = value
                        self.form_factor.value_namespace = name_space
                        self.form_factor.value_namespace_prefix = name_space_prefix
                    if(value_path == "internal-temp"):
                        self.internal_temp = value
                        self.internal_temp.value_namespace = name_space
                        self.internal_temp.value_namespace_prefix = name_space_prefix
                    if(value_path == "otn-compliance-code"):
                        self.otn_compliance_code = value
                        self.otn_compliance_code.value_namespace = name_space
                        self.otn_compliance_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "present"):
                        self.present = value
                        self.present.value_namespace = name_space
                        self.present.value_namespace_prefix = name_space_prefix
                    if(value_path == "serial-no"):
                        self.serial_no = value
                        self.serial_no.value_namespace = name_space
                        self.serial_no.value_namespace_prefix = name_space_prefix
                    if(value_path == "sonet-sdh-compliance-code"):
                        self.sonet_sdh_compliance_code = value
                        self.sonet_sdh_compliance_code.value_namespace = name_space
                        self.sonet_sdh_compliance_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "vendor"):
                        self.vendor = value
                        self.vendor.value_namespace = name_space
                        self.vendor.value_namespace_prefix = name_space_prefix
                    if(value_path == "vendor-part"):
                        self.vendor_part = value
                        self.vendor_part.value_namespace = name_space
                        self.vendor_part.value_namespace_prefix = name_space_prefix
                    if(value_path == "vendor-rev"):
                        self.vendor_rev = value
                        self.vendor_rev.value_namespace = name_space
                        self.vendor_rev.value_namespace_prefix = name_space_prefix


            class PhysicalChannels(Entity):
                """
                Enclosing container for client channels
                
                .. attribute:: channel
                
                	List of client channels, keyed by index within a physical client port.  A physical port with a single channel would have a single zero\-indexed element
                	**type**\: list of    :py:class:`Channel <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2016-05-24'

                def __init__(self):
                    super(Components.Component.Transceiver.PhysicalChannels, self).__init__()

                    self.yang_name = "physical-channels"
                    self.yang_parent_name = "transceiver"

                    self.channel = YList(self)

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
                                super(Components.Component.Transceiver.PhysicalChannels, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.Transceiver.PhysicalChannels, self).__setattr__(name, value)


                class Channel(Entity):
                    """
                    List of client channels, keyed by index within a physical
                    client port.  A physical port with a single channel would
                    have a single zero\-indexed element
                    
                    .. attribute:: index  <key>
                    
                    	Reference to the index number of the channel
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for physical channels
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for channels
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State>`
                    
                    

                    """

                    _prefix = 'oc-transceiver'
                    _revision = '2016-05-24'

                    def __init__(self):
                        super(Components.Component.Transceiver.PhysicalChannels.Channel, self).__init__()

                        self.yang_name = "channel"
                        self.yang_parent_name = "physical-channels"

                        self.index = YLeaf(YType.str, "index")

                        self.config = Components.Component.Transceiver.PhysicalChannels.Channel.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Components.Component.Transceiver.PhysicalChannels.Channel.State()
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
                            if name in ("index") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.Transceiver.PhysicalChannels.Channel, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.Transceiver.PhysicalChannels.Channel, self).__setattr__(name, value)


                    class Config(Entity):
                        """
                        Configuration data for physical channels
                        
                        .. attribute:: description
                        
                        	Text description for the client physical channel
                        	**type**\:  str
                        
                        .. attribute:: index
                        
                        	Index of the physical channnel or lane within a physical client port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: target_output_power
                        
                        	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dBm
                        
                        .. attribute:: tx_laser
                        
                        	Enable (true) or disable (false) the transmit label for the channel
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'oc-transceiver'
                        _revision = '2016-05-24'

                        def __init__(self):
                            super(Components.Component.Transceiver.PhysicalChannels.Channel.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "channel"

                            self.description = YLeaf(YType.str, "description")

                            self.index = YLeaf(YType.uint16, "index")

                            self.target_output_power = YLeaf(YType.str, "target-output-power")

                            self.tx_laser = YLeaf(YType.boolean, "tx-laser")

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
                                            "index",
                                            "target_output_power",
                                            "tx_laser") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Components.Component.Transceiver.PhysicalChannels.Channel.Config, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Components.Component.Transceiver.PhysicalChannels.Channel.Config, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.description.is_set or
                                self.index.is_set or
                                self.target_output_power.is_set or
                                self.tx_laser.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.description.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.target_output_power.yfilter != YFilter.not_set or
                                self.tx_laser.yfilter != YFilter.not_set)

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
                            if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.description.get_name_leafdata())
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.target_output_power.is_set or self.target_output_power.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.target_output_power.get_name_leafdata())
                            if (self.tx_laser.is_set or self.tx_laser.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tx_laser.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "description" or name == "index" or name == "target-output-power" or name == "tx-laser"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "description"):
                                self.description = value
                                self.description.value_namespace = name_space
                                self.description.value_namespace_prefix = name_space_prefix
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "target-output-power"):
                                self.target_output_power = value
                                self.target_output_power.value_namespace = name_space
                                self.target_output_power.value_namespace_prefix = name_space_prefix
                            if(value_path == "tx-laser"):
                                self.tx_laser = value
                                self.tx_laser.value_namespace = name_space
                                self.tx_laser.value_namespace_prefix = name_space_prefix


                    class State(Entity):
                        """
                        Operational state data for channels
                        
                        .. attribute:: description
                        
                        	Text description for the client physical channel
                        	**type**\:  str
                        
                        .. attribute:: index
                        
                        	Index of the physical channnel or lane within a physical client port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: input_power
                        
                        	The input optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:   :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower>`
                        
                        .. attribute:: laser_bias_current
                        
                        	The current applied by the system to the transmit laser to achieve the output power.  The current is expressed in mA with up to one decimal precision. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:   :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent>`
                        
                        .. attribute:: output_frequency
                        
                        	The frequency in MHz of the individual physical channel (e.g. ITU C50 \- 195.0THz and would be reported as 195,000,000 MHz in this model). This attribute is not configurable on most client ports
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: output_power
                        
                        	The output optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:   :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower>`
                        
                        .. attribute:: target_output_power
                        
                        	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dBm
                        
                        .. attribute:: tx_laser
                        
                        	Enable (true) or disable (false) the transmit label for the channel
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'oc-transceiver'
                        _revision = '2016-05-24'

                        def __init__(self):
                            super(Components.Component.Transceiver.PhysicalChannels.Channel.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "channel"

                            self.description = YLeaf(YType.str, "description")

                            self.index = YLeaf(YType.uint16, "index")

                            self.output_frequency = YLeaf(YType.uint64, "output-frequency")

                            self.target_output_power = YLeaf(YType.str, "target-output-power")

                            self.tx_laser = YLeaf(YType.boolean, "tx-laser")

                            self.input_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower()
                            self.input_power.parent = self
                            self._children_name_map["input_power"] = "input-power"
                            self._children_yang_names.add("input-power")

                            self.laser_bias_current = Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent()
                            self.laser_bias_current.parent = self
                            self._children_name_map["laser_bias_current"] = "laser-bias-current"
                            self._children_yang_names.add("laser-bias-current")

                            self.output_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower()
                            self.output_power.parent = self
                            self._children_name_map["output_power"] = "output-power"
                            self._children_yang_names.add("output-power")

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
                                            "index",
                                            "output_frequency",
                                            "target_output_power",
                                            "tx_laser") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Components.Component.Transceiver.PhysicalChannels.Channel.State, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Components.Component.Transceiver.PhysicalChannels.Channel.State, self).__setattr__(name, value)


                        class OutputPower(Entity):
                            """
                            The output optical power of this port in units of 0.01dBm.
                            If the port is an aggregate of multiple physical channels,
                            this attribute is the total power or sum of all channels. If
                            avg/min/max statistics are not supported, the target is
                            expected to just supply the instant value
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: max
                            
                            	The maximum value of the statitic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2016-05-24'

                            def __init__(self):
                                super(Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower, self).__init__()

                                self.yang_name = "output-power"
                                self.yang_parent_name = "state"

                                self.avg = YLeaf(YType.str, "avg")

                                self.instant = YLeaf(YType.str, "instant")

                                self.max = YLeaf(YType.str, "max")

                                self.min = YLeaf(YType.str, "min")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("avg",
                                                "instant",
                                                "max",
                                                "min") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.avg.is_set or
                                    self.instant.is_set or
                                    self.max.is_set or
                                    self.min.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.avg.yfilter != YFilter.not_set or
                                    self.instant.yfilter != YFilter.not_set or
                                    self.max.yfilter != YFilter.not_set or
                                    self.min.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "output-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.avg.get_name_leafdata())
                                if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.instant.get_name_leafdata())
                                if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max.get_name_leafdata())
                                if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.min.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "avg"):
                                    self.avg = value
                                    self.avg.value_namespace = name_space
                                    self.avg.value_namespace_prefix = name_space_prefix
                                if(value_path == "instant"):
                                    self.instant = value
                                    self.instant.value_namespace = name_space
                                    self.instant.value_namespace_prefix = name_space_prefix
                                if(value_path == "max"):
                                    self.max = value
                                    self.max.value_namespace = name_space
                                    self.max.value_namespace_prefix = name_space_prefix
                                if(value_path == "min"):
                                    self.min = value
                                    self.min.value_namespace = name_space
                                    self.min.value_namespace_prefix = name_space_prefix


                        class InputPower(Entity):
                            """
                            The input optical power of this port in units of 0.01dBm.
                            If the port is an aggregate of multiple physical channels,
                            this attribute is the total power or sum of all channels.
                            If avg/min/max statistics are not supported, the target is
                            expected to just supply the instant value
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: max
                            
                            	The maximum value of the statitic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2016-05-24'

                            def __init__(self):
                                super(Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower, self).__init__()

                                self.yang_name = "input-power"
                                self.yang_parent_name = "state"

                                self.avg = YLeaf(YType.str, "avg")

                                self.instant = YLeaf(YType.str, "instant")

                                self.max = YLeaf(YType.str, "max")

                                self.min = YLeaf(YType.str, "min")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("avg",
                                                "instant",
                                                "max",
                                                "min") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.avg.is_set or
                                    self.instant.is_set or
                                    self.max.is_set or
                                    self.min.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.avg.yfilter != YFilter.not_set or
                                    self.instant.yfilter != YFilter.not_set or
                                    self.max.yfilter != YFilter.not_set or
                                    self.min.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "input-power" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.avg.get_name_leafdata())
                                if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.instant.get_name_leafdata())
                                if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max.get_name_leafdata())
                                if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.min.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "avg"):
                                    self.avg = value
                                    self.avg.value_namespace = name_space
                                    self.avg.value_namespace_prefix = name_space_prefix
                                if(value_path == "instant"):
                                    self.instant = value
                                    self.instant.value_namespace = name_space
                                    self.instant.value_namespace_prefix = name_space_prefix
                                if(value_path == "max"):
                                    self.max = value
                                    self.max.value_namespace = name_space
                                    self.max.value_namespace_prefix = name_space_prefix
                                if(value_path == "min"):
                                    self.min = value
                                    self.min.value_namespace = name_space
                                    self.min.value_namespace_prefix = name_space_prefix


                        class LaserBiasCurrent(Entity):
                            """
                            The current applied by the system to the transmit laser to
                            achieve the output power.  The current is expressed in mA
                            with up to one decimal precision. If avg/min/max statistics
                            are not supported, the target is expected to just supply
                            the instant value
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: max
                            
                            	The maximum value of the statitic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2016-05-24'

                            def __init__(self):
                                super(Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent, self).__init__()

                                self.yang_name = "laser-bias-current"
                                self.yang_parent_name = "state"

                                self.avg = YLeaf(YType.str, "avg")

                                self.instant = YLeaf(YType.str, "instant")

                                self.max = YLeaf(YType.str, "max")

                                self.min = YLeaf(YType.str, "min")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("avg",
                                                "instant",
                                                "max",
                                                "min") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.avg.is_set or
                                    self.instant.is_set or
                                    self.max.is_set or
                                    self.min.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.avg.yfilter != YFilter.not_set or
                                    self.instant.yfilter != YFilter.not_set or
                                    self.max.yfilter != YFilter.not_set or
                                    self.min.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "laser-bias-current" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.avg.get_name_leafdata())
                                if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.instant.get_name_leafdata())
                                if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.max.get_name_leafdata())
                                if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.min.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "avg"):
                                    self.avg = value
                                    self.avg.value_namespace = name_space
                                    self.avg.value_namespace_prefix = name_space_prefix
                                if(value_path == "instant"):
                                    self.instant = value
                                    self.instant.value_namespace = name_space
                                    self.instant.value_namespace_prefix = name_space_prefix
                                if(value_path == "max"):
                                    self.max = value
                                    self.max.value_namespace = name_space
                                    self.max.value_namespace_prefix = name_space_prefix
                                if(value_path == "min"):
                                    self.min = value
                                    self.min.value_namespace = name_space
                                    self.min.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.description.is_set or
                                self.index.is_set or
                                self.output_frequency.is_set or
                                self.target_output_power.is_set or
                                self.tx_laser.is_set or
                                (self.input_power is not None and self.input_power.has_data()) or
                                (self.laser_bias_current is not None and self.laser_bias_current.has_data()) or
                                (self.output_power is not None and self.output_power.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.description.yfilter != YFilter.not_set or
                                self.index.yfilter != YFilter.not_set or
                                self.output_frequency.yfilter != YFilter.not_set or
                                self.target_output_power.yfilter != YFilter.not_set or
                                self.tx_laser.yfilter != YFilter.not_set or
                                (self.input_power is not None and self.input_power.has_operation()) or
                                (self.laser_bias_current is not None and self.laser_bias_current.has_operation()) or
                                (self.output_power is not None and self.output_power.has_operation()))

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
                            if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index.get_name_leafdata())
                            if (self.output_frequency.is_set or self.output_frequency.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.output_frequency.get_name_leafdata())
                            if (self.target_output_power.is_set or self.target_output_power.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.target_output_power.get_name_leafdata())
                            if (self.tx_laser.is_set or self.tx_laser.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tx_laser.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "input-power"):
                                if (self.input_power is None):
                                    self.input_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower()
                                    self.input_power.parent = self
                                    self._children_name_map["input_power"] = "input-power"
                                return self.input_power

                            if (child_yang_name == "laser-bias-current"):
                                if (self.laser_bias_current is None):
                                    self.laser_bias_current = Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent()
                                    self.laser_bias_current.parent = self
                                    self._children_name_map["laser_bias_current"] = "laser-bias-current"
                                return self.laser_bias_current

                            if (child_yang_name == "output-power"):
                                if (self.output_power is None):
                                    self.output_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower()
                                    self.output_power.parent = self
                                    self._children_name_map["output_power"] = "output-power"
                                return self.output_power

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "input-power" or name == "laser-bias-current" or name == "output-power" or name == "description" or name == "index" or name == "output-frequency" or name == "target-output-power" or name == "tx-laser"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "description"):
                                self.description = value
                                self.description.value_namespace = name_space
                                self.description.value_namespace_prefix = name_space_prefix
                            if(value_path == "index"):
                                self.index = value
                                self.index.value_namespace = name_space
                                self.index.value_namespace_prefix = name_space_prefix
                            if(value_path == "output-frequency"):
                                self.output_frequency = value
                                self.output_frequency.value_namespace = name_space
                                self.output_frequency.value_namespace_prefix = name_space_prefix
                            if(value_path == "target-output-power"):
                                self.target_output_power = value
                                self.target_output_power.value_namespace = name_space
                                self.target_output_power.value_namespace_prefix = name_space_prefix
                            if(value_path == "tx-laser"):
                                self.tx_laser = value
                                self.tx_laser.value_namespace = name_space
                                self.tx_laser.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.index.is_set or
                            (self.config is not None and self.config.has_data()) or
                            (self.state is not None and self.state.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            (self.config is not None and self.config.has_operation()) or
                            (self.state is not None and self.state.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "channel" + "[index='" + self.index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "config"):
                            if (self.config is None):
                                self.config = Components.Component.Transceiver.PhysicalChannels.Channel.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                            return self.config

                        if (child_yang_name == "state"):
                            if (self.state is None):
                                self.state = Components.Component.Transceiver.PhysicalChannels.Channel.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                            return self.state

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "config" or name == "state" or name == "index"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.channel:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.channel:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "physical-channels" + path_buffer

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

                    if (child_yang_name == "channel"):
                        for c in self.channel:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Components.Component.Transceiver.PhysicalChannels.Channel()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.channel.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "channel"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.config is not None and self.config.has_data()) or
                    (self.physical_channels is not None and self.physical_channels.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.physical_channels is not None and self.physical_channels.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "openconfig-platform-transceiver:transceiver" + path_buffer

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

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = Components.Component.Transceiver.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "physical-channels"):
                    if (self.physical_channels is None):
                        self.physical_channels = Components.Component.Transceiver.PhysicalChannels()
                        self.physical_channels.parent = self
                        self._children_name_map["physical_channels"] = "physical-channels"
                    return self.physical_channels

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = Components.Component.Transceiver.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "physical-channels" or name == "state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class OpticalChannel(Entity):
            """
            Enclosing container for the list of optical channels
            
            .. attribute:: config
            
            	Configuration data for optical channels
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.Config>`
            
            .. attribute:: state
            
            	Operational state data for optical channels
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State>`
            
            

            """

            _prefix = 'oc-opt-term'
            _revision = '2016-06-17'

            def __init__(self):
                super(Components.Component.OpticalChannel, self).__init__()

                self.yang_name = "optical-channel"
                self.yang_parent_name = "component"

                self.config = Components.Component.OpticalChannel.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Components.Component.OpticalChannel.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")


            class Config(Entity):
                """
                Configuration data for optical channels
                
                .. attribute:: frequency
                
                	Frequency of the optical channel, expressed in MHz
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: line_port
                
                	Reference to the line\-side physical port that carries this optical channel.  The target port should be a component in the physical inventory data model
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                .. attribute:: operational_mode
                
                	Vendor\-specific mode identifier \-\- sets the operational mode for the channel
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: target_output_power
                
                	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(Components.Component.OpticalChannel.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "optical-channel"

                    self.frequency = YLeaf(YType.uint64, "frequency")

                    self.line_port = YLeaf(YType.str, "line-port")

                    self.operational_mode = YLeaf(YType.uint16, "operational-mode")

                    self.target_output_power = YLeaf(YType.str, "target-output-power")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("frequency",
                                    "line_port",
                                    "operational_mode",
                                    "target_output_power") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.OpticalChannel.Config, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.OpticalChannel.Config, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.frequency.is_set or
                        self.line_port.is_set or
                        self.operational_mode.is_set or
                        self.target_output_power.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.frequency.yfilter != YFilter.not_set or
                        self.line_port.yfilter != YFilter.not_set or
                        self.operational_mode.yfilter != YFilter.not_set or
                        self.target_output_power.yfilter != YFilter.not_set)

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
                    if (self.frequency.is_set or self.frequency.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.frequency.get_name_leafdata())
                    if (self.line_port.is_set or self.line_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.line_port.get_name_leafdata())
                    if (self.operational_mode.is_set or self.operational_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational_mode.get_name_leafdata())
                    if (self.target_output_power.is_set or self.target_output_power.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.target_output_power.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "frequency" or name == "line-port" or name == "operational-mode" or name == "target-output-power"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "frequency"):
                        self.frequency = value
                        self.frequency.value_namespace = name_space
                        self.frequency.value_namespace_prefix = name_space_prefix
                    if(value_path == "line-port"):
                        self.line_port = value
                        self.line_port.value_namespace = name_space
                        self.line_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational-mode"):
                        self.operational_mode = value
                        self.operational_mode.value_namespace = name_space
                        self.operational_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "target-output-power"):
                        self.target_output_power = value
                        self.target_output_power.value_namespace = name_space
                        self.target_output_power.value_namespace_prefix = name_space_prefix


            class State(Entity):
                """
                Operational state data for optical channels
                
                .. attribute:: chromatic_dispersion
                
                	Chromatic Dispersion of an optical channel in ps/nm as reported by receiver
                	**type**\:   :py:class:`ChromaticDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.ChromaticDispersion>`
                
                .. attribute:: frequency
                
                	Frequency of the optical channel, expressed in MHz
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: group_id
                
                	If the device places constraints on which optical channels must be managed together (e.g., transmitted on the same line port), it can indicate that by setting the group\-id to the same value across related optical channels
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_power
                
                	The input optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:   :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.InputPower>`
                
                .. attribute:: laser_bias_current
                
                	The current applied by the system to the transmit laser to achieve the output power.  The current is expressed in mA with up to one decimal precision. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:   :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.LaserBiasCurrent>`
                
                .. attribute:: line_port
                
                	Reference to the line\-side physical port that carries this optical channel.  The target port should be a component in the physical inventory data model
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                .. attribute:: operational_mode
                
                	Vendor\-specific mode identifier \-\- sets the operational mode for the channel
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: output_power
                
                	The output optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:   :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.OutputPower>`
                
                .. attribute:: polarization_dependent_loss
                
                	Polarization Dependent Loss of an optical channel in dB as reported by receiver
                	**type**\:   :py:class:`PolarizationDependentLoss <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.PolarizationDependentLoss>`
                
                .. attribute:: polarization_mode_dispersion
                
                	Polarization Mode Dispersion of an optical channel in ps as reported by receiver
                	**type**\:   :py:class:`PolarizationModeDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.PolarizationModeDispersion>`
                
                .. attribute:: second_order_polarization_mode_dispersion
                
                	Second Order Polarization Mode Dispersion of an optical channel in ps^2 as reported by receiver
                	**type**\:   :py:class:`SecondOrderPolarizationModeDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion>`
                
                .. attribute:: target_output_power
                
                	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(Components.Component.OpticalChannel.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "optical-channel"

                    self.frequency = YLeaf(YType.uint64, "frequency")

                    self.group_id = YLeaf(YType.uint32, "group-id")

                    self.line_port = YLeaf(YType.str, "line-port")

                    self.operational_mode = YLeaf(YType.uint16, "operational-mode")

                    self.target_output_power = YLeaf(YType.str, "target-output-power")

                    self.chromatic_dispersion = Components.Component.OpticalChannel.State.ChromaticDispersion()
                    self.chromatic_dispersion.parent = self
                    self._children_name_map["chromatic_dispersion"] = "chromatic-dispersion"
                    self._children_yang_names.add("chromatic-dispersion")

                    self.input_power = Components.Component.OpticalChannel.State.InputPower()
                    self.input_power.parent = self
                    self._children_name_map["input_power"] = "input-power"
                    self._children_yang_names.add("input-power")

                    self.laser_bias_current = Components.Component.OpticalChannel.State.LaserBiasCurrent()
                    self.laser_bias_current.parent = self
                    self._children_name_map["laser_bias_current"] = "laser-bias-current"
                    self._children_yang_names.add("laser-bias-current")

                    self.output_power = Components.Component.OpticalChannel.State.OutputPower()
                    self.output_power.parent = self
                    self._children_name_map["output_power"] = "output-power"
                    self._children_yang_names.add("output-power")

                    self.polarization_dependent_loss = Components.Component.OpticalChannel.State.PolarizationDependentLoss()
                    self.polarization_dependent_loss.parent = self
                    self._children_name_map["polarization_dependent_loss"] = "polarization-dependent-loss"
                    self._children_yang_names.add("polarization-dependent-loss")

                    self.polarization_mode_dispersion = Components.Component.OpticalChannel.State.PolarizationModeDispersion()
                    self.polarization_mode_dispersion.parent = self
                    self._children_name_map["polarization_mode_dispersion"] = "polarization-mode-dispersion"
                    self._children_yang_names.add("polarization-mode-dispersion")

                    self.second_order_polarization_mode_dispersion = Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion()
                    self.second_order_polarization_mode_dispersion.parent = self
                    self._children_name_map["second_order_polarization_mode_dispersion"] = "second-order-polarization-mode-dispersion"
                    self._children_yang_names.add("second-order-polarization-mode-dispersion")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("frequency",
                                    "group_id",
                                    "line_port",
                                    "operational_mode",
                                    "target_output_power") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Components.Component.OpticalChannel.State, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Components.Component.OpticalChannel.State, self).__setattr__(name, value)


                class OutputPower(Entity):
                    """
                    The output optical power of this port in units of 0.01dBm.
                    If the port is an aggregate of multiple physical channels,
                    this attribute is the total power or sum of all channels. If
                    avg/min/max statistics are not supported, the target is
                    expected to just supply the instant value
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.OutputPower, self).__init__()

                        self.yang_name = "output-power"
                        self.yang_parent_name = "state"

                        self.avg = YLeaf(YType.str, "avg")

                        self.instant = YLeaf(YType.str, "instant")

                        self.max = YLeaf(YType.str, "max")

                        self.min = YLeaf(YType.str, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg",
                                        "instant",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.OpticalChannel.State.OutputPower, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.OpticalChannel.State.OutputPower, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.avg.is_set or
                            self.instant.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.instant.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "output-power" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instant.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "instant"):
                            self.instant = value
                            self.instant.value_namespace = name_space
                            self.instant.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix


                class InputPower(Entity):
                    """
                    The input optical power of this port in units of 0.01dBm.
                    If the port is an aggregate of multiple physical channels,
                    this attribute is the total power or sum of all channels.
                    If avg/min/max statistics are not supported, the target is
                    expected to just supply the instant value
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.InputPower, self).__init__()

                        self.yang_name = "input-power"
                        self.yang_parent_name = "state"

                        self.avg = YLeaf(YType.str, "avg")

                        self.instant = YLeaf(YType.str, "instant")

                        self.max = YLeaf(YType.str, "max")

                        self.min = YLeaf(YType.str, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg",
                                        "instant",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.OpticalChannel.State.InputPower, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.OpticalChannel.State.InputPower, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.avg.is_set or
                            self.instant.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.instant.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "input-power" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instant.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "instant"):
                            self.instant = value
                            self.instant.value_namespace = name_space
                            self.instant.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix


                class LaserBiasCurrent(Entity):
                    """
                    The current applied by the system to the transmit laser to
                    achieve the output power.  The current is expressed in mA
                    with up to one decimal precision. If avg/min/max statistics
                    are not supported, the target is expected to just supply
                    the instant value
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.LaserBiasCurrent, self).__init__()

                        self.yang_name = "laser-bias-current"
                        self.yang_parent_name = "state"

                        self.avg = YLeaf(YType.str, "avg")

                        self.instant = YLeaf(YType.str, "instant")

                        self.max = YLeaf(YType.str, "max")

                        self.min = YLeaf(YType.str, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg",
                                        "instant",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.OpticalChannel.State.LaserBiasCurrent, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.OpticalChannel.State.LaserBiasCurrent, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.avg.is_set or
                            self.instant.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.instant.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "laser-bias-current" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instant.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "instant"):
                            self.instant = value
                            self.instant.value_namespace = name_space
                            self.instant.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix


                class ChromaticDispersion(Entity):
                    """
                    Chromatic Dispersion of an optical channel
                    in ps/nm as reported by receiver
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.ChromaticDispersion, self).__init__()

                        self.yang_name = "chromatic-dispersion"
                        self.yang_parent_name = "state"

                        self.avg = YLeaf(YType.str, "avg")

                        self.instant = YLeaf(YType.str, "instant")

                        self.max = YLeaf(YType.str, "max")

                        self.min = YLeaf(YType.str, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg",
                                        "instant",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.OpticalChannel.State.ChromaticDispersion, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.OpticalChannel.State.ChromaticDispersion, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.avg.is_set or
                            self.instant.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.instant.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "chromatic-dispersion" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instant.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "instant"):
                            self.instant = value
                            self.instant.value_namespace = name_space
                            self.instant.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix


                class PolarizationModeDispersion(Entity):
                    """
                    Polarization Mode Dispersion of an optical channel
                    in ps as reported by receiver
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.PolarizationModeDispersion, self).__init__()

                        self.yang_name = "polarization-mode-dispersion"
                        self.yang_parent_name = "state"

                        self.avg = YLeaf(YType.str, "avg")

                        self.instant = YLeaf(YType.str, "instant")

                        self.max = YLeaf(YType.str, "max")

                        self.min = YLeaf(YType.str, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg",
                                        "instant",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.OpticalChannel.State.PolarizationModeDispersion, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.OpticalChannel.State.PolarizationModeDispersion, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.avg.is_set or
                            self.instant.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.instant.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "polarization-mode-dispersion" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instant.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "instant"):
                            self.instant = value
                            self.instant.value_namespace = name_space
                            self.instant.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix


                class SecondOrderPolarizationModeDispersion(Entity):
                    """
                    Second Order Polarization Mode Dispersion of an optical
                    channel in ps^2 as reported by receiver
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion, self).__init__()

                        self.yang_name = "second-order-polarization-mode-dispersion"
                        self.yang_parent_name = "state"

                        self.avg = YLeaf(YType.str, "avg")

                        self.instant = YLeaf(YType.str, "instant")

                        self.max = YLeaf(YType.str, "max")

                        self.min = YLeaf(YType.str, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg",
                                        "instant",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.avg.is_set or
                            self.instant.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.instant.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "second-order-polarization-mode-dispersion" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instant.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "instant"):
                            self.instant = value
                            self.instant.value_namespace = name_space
                            self.instant.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix


                class PolarizationDependentLoss(Entity):
                    """
                    Polarization Dependent Loss of an optical channel
                    in dB as reported by receiver
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.PolarizationDependentLoss, self).__init__()

                        self.yang_name = "polarization-dependent-loss"
                        self.yang_parent_name = "state"

                        self.avg = YLeaf(YType.str, "avg")

                        self.instant = YLeaf(YType.str, "instant")

                        self.max = YLeaf(YType.str, "max")

                        self.min = YLeaf(YType.str, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg",
                                        "instant",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Components.Component.OpticalChannel.State.PolarizationDependentLoss, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Components.Component.OpticalChannel.State.PolarizationDependentLoss, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.avg.is_set or
                            self.instant.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.instant.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "polarization-dependent-loss" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.instant.is_set or self.instant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instant.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "avg" or name == "instant" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "instant"):
                            self.instant = value
                            self.instant.value_namespace = name_space
                            self.instant.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.frequency.is_set or
                        self.group_id.is_set or
                        self.line_port.is_set or
                        self.operational_mode.is_set or
                        self.target_output_power.is_set or
                        (self.chromatic_dispersion is not None and self.chromatic_dispersion.has_data()) or
                        (self.input_power is not None and self.input_power.has_data()) or
                        (self.laser_bias_current is not None and self.laser_bias_current.has_data()) or
                        (self.output_power is not None and self.output_power.has_data()) or
                        (self.polarization_dependent_loss is not None and self.polarization_dependent_loss.has_data()) or
                        (self.polarization_mode_dispersion is not None and self.polarization_mode_dispersion.has_data()) or
                        (self.second_order_polarization_mode_dispersion is not None and self.second_order_polarization_mode_dispersion.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.frequency.yfilter != YFilter.not_set or
                        self.group_id.yfilter != YFilter.not_set or
                        self.line_port.yfilter != YFilter.not_set or
                        self.operational_mode.yfilter != YFilter.not_set or
                        self.target_output_power.yfilter != YFilter.not_set or
                        (self.chromatic_dispersion is not None and self.chromatic_dispersion.has_operation()) or
                        (self.input_power is not None and self.input_power.has_operation()) or
                        (self.laser_bias_current is not None and self.laser_bias_current.has_operation()) or
                        (self.output_power is not None and self.output_power.has_operation()) or
                        (self.polarization_dependent_loss is not None and self.polarization_dependent_loss.has_operation()) or
                        (self.polarization_mode_dispersion is not None and self.polarization_mode_dispersion.has_operation()) or
                        (self.second_order_polarization_mode_dispersion is not None and self.second_order_polarization_mode_dispersion.has_operation()))

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
                    if (self.frequency.is_set or self.frequency.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.frequency.get_name_leafdata())
                    if (self.group_id.is_set or self.group_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_id.get_name_leafdata())
                    if (self.line_port.is_set or self.line_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.line_port.get_name_leafdata())
                    if (self.operational_mode.is_set or self.operational_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.operational_mode.get_name_leafdata())
                    if (self.target_output_power.is_set or self.target_output_power.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.target_output_power.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "chromatic-dispersion"):
                        if (self.chromatic_dispersion is None):
                            self.chromatic_dispersion = Components.Component.OpticalChannel.State.ChromaticDispersion()
                            self.chromatic_dispersion.parent = self
                            self._children_name_map["chromatic_dispersion"] = "chromatic-dispersion"
                        return self.chromatic_dispersion

                    if (child_yang_name == "input-power"):
                        if (self.input_power is None):
                            self.input_power = Components.Component.OpticalChannel.State.InputPower()
                            self.input_power.parent = self
                            self._children_name_map["input_power"] = "input-power"
                        return self.input_power

                    if (child_yang_name == "laser-bias-current"):
                        if (self.laser_bias_current is None):
                            self.laser_bias_current = Components.Component.OpticalChannel.State.LaserBiasCurrent()
                            self.laser_bias_current.parent = self
                            self._children_name_map["laser_bias_current"] = "laser-bias-current"
                        return self.laser_bias_current

                    if (child_yang_name == "output-power"):
                        if (self.output_power is None):
                            self.output_power = Components.Component.OpticalChannel.State.OutputPower()
                            self.output_power.parent = self
                            self._children_name_map["output_power"] = "output-power"
                        return self.output_power

                    if (child_yang_name == "polarization-dependent-loss"):
                        if (self.polarization_dependent_loss is None):
                            self.polarization_dependent_loss = Components.Component.OpticalChannel.State.PolarizationDependentLoss()
                            self.polarization_dependent_loss.parent = self
                            self._children_name_map["polarization_dependent_loss"] = "polarization-dependent-loss"
                        return self.polarization_dependent_loss

                    if (child_yang_name == "polarization-mode-dispersion"):
                        if (self.polarization_mode_dispersion is None):
                            self.polarization_mode_dispersion = Components.Component.OpticalChannel.State.PolarizationModeDispersion()
                            self.polarization_mode_dispersion.parent = self
                            self._children_name_map["polarization_mode_dispersion"] = "polarization-mode-dispersion"
                        return self.polarization_mode_dispersion

                    if (child_yang_name == "second-order-polarization-mode-dispersion"):
                        if (self.second_order_polarization_mode_dispersion is None):
                            self.second_order_polarization_mode_dispersion = Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion()
                            self.second_order_polarization_mode_dispersion.parent = self
                            self._children_name_map["second_order_polarization_mode_dispersion"] = "second-order-polarization-mode-dispersion"
                        return self.second_order_polarization_mode_dispersion

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "chromatic-dispersion" or name == "input-power" or name == "laser-bias-current" or name == "output-power" or name == "polarization-dependent-loss" or name == "polarization-mode-dispersion" or name == "second-order-polarization-mode-dispersion" or name == "frequency" or name == "group-id" or name == "line-port" or name == "operational-mode" or name == "target-output-power"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "frequency"):
                        self.frequency = value
                        self.frequency.value_namespace = name_space
                        self.frequency.value_namespace_prefix = name_space_prefix
                    if(value_path == "group-id"):
                        self.group_id = value
                        self.group_id.value_namespace = name_space
                        self.group_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "line-port"):
                        self.line_port = value
                        self.line_port.value_namespace = name_space
                        self.line_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "operational-mode"):
                        self.operational_mode = value
                        self.operational_mode.value_namespace = name_space
                        self.operational_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "target-output-power"):
                        self.target_output_power = value
                        self.target_output_power.value_namespace = name_space
                        self.target_output_power.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.config is not None and self.config.has_data()) or
                    (self.state is not None and self.state.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.config is not None and self.config.has_operation()) or
                    (self.state is not None and self.state.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "openconfig-terminal-device:optical-channel" + path_buffer

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

                if (child_yang_name == "config"):
                    if (self.config is None):
                        self.config = Components.Component.OpticalChannel.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                    return self.config

                if (child_yang_name == "state"):
                    if (self.state is None):
                        self.state = Components.Component.OpticalChannel.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                    return self.state

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "config" or name == "state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.name.is_set or
                (self.config is not None and self.config.has_data()) or
                (self.optical_channel is not None and self.optical_channel.has_data()) or
                (self.properties is not None and self.properties.has_data()) or
                (self.state is not None and self.state.has_data()) or
                (self.subcomponents is not None and self.subcomponents.has_data()) or
                (self.transceiver is not None and self.transceiver.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                (self.config is not None and self.config.has_operation()) or
                (self.optical_channel is not None and self.optical_channel.has_operation()) or
                (self.properties is not None and self.properties.has_operation()) or
                (self.state is not None and self.state.has_operation()) or
                (self.subcomponents is not None and self.subcomponents.has_operation()) or
                (self.transceiver is not None and self.transceiver.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "component" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "openconfig-platform:components/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "config"):
                if (self.config is None):
                    self.config = Components.Component.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                return self.config

            if (child_yang_name == "optical-channel"):
                if (self.optical_channel is None):
                    self.optical_channel = Components.Component.OpticalChannel()
                    self.optical_channel.parent = self
                    self._children_name_map["optical_channel"] = "optical-channel"
                return self.optical_channel

            if (child_yang_name == "properties"):
                if (self.properties is None):
                    self.properties = Components.Component.Properties()
                    self.properties.parent = self
                    self._children_name_map["properties"] = "properties"
                return self.properties

            if (child_yang_name == "state"):
                if (self.state is None):
                    self.state = Components.Component.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                return self.state

            if (child_yang_name == "subcomponents"):
                if (self.subcomponents is None):
                    self.subcomponents = Components.Component.Subcomponents()
                    self.subcomponents.parent = self
                    self._children_name_map["subcomponents"] = "subcomponents"
                return self.subcomponents

            if (child_yang_name == "transceiver"):
                if (self.transceiver is None):
                    self.transceiver = Components.Component.Transceiver()
                    self.transceiver.parent = self
                    self._children_name_map["transceiver"] = "transceiver"
                return self.transceiver

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "config" or name == "optical-channel" or name == "properties" or name == "state" or name == "subcomponents" or name == "transceiver" or name == "name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix

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
        path_buffer = "openconfig-platform:components" + path_buffer

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

