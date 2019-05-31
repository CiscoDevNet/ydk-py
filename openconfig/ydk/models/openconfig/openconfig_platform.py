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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Components(Entity):
    """
    Enclosing container for the components in the system.
    
    .. attribute:: component
    
    	List of components, keyed by component name
    	**type**\: list of  		 :py:class:`Component <ydk.models.openconfig.openconfig_platform.Components.Component>`
    
    

    """

    _prefix = 'oc-platform'
    _revision = '2016-06-06'

    def __init__(self):
        super(Components, self).__init__()
        self._top_entity = None

        self.yang_name = "components"
        self.yang_parent_name = "openconfig-platform"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("component", ("component", Components.Component))])
        self._leafs = OrderedDict()

        self.component = YList(self)
        self._segment_path = lambda: "openconfig-platform:components"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Components, [], name, value)


    class Component(Entity):
        """
        List of components, keyed by component name.
        
        .. attribute:: name  (key)
        
        	References the component name
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
        
        .. attribute:: config
        
        	Configuration data for each component
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
        
        .. attribute:: state
        
        	Operational state data for each component
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.State>`
        
        	**config**\: False
        
        .. attribute:: properties
        
        	Enclosing container 
        	**type**\:  :py:class:`Properties <ydk.models.openconfig.openconfig_platform.Components.Component.Properties>`
        
        .. attribute:: subcomponents
        
        	Enclosing container for subcomponent references
        	**type**\:  :py:class:`Subcomponents <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents>`
        
        .. attribute:: optical_port
        
        	Top\-level container 
        	**type**\:  :py:class:`OpticalPort <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort>`
        
        .. attribute:: transceiver
        
        	Top\-level container for client port transceiver data
        	**type**\:  :py:class:`Transceiver <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver>`
        
        .. attribute:: optical_channel
        
        	Enclosing container for the list of optical channels
        	**type**\:  :py:class:`OpticalChannel <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel>`
        
        

        """

        _prefix = 'oc-platform'
        _revision = '2016-06-06'

        def __init__(self):
            super(Components.Component, self).__init__()

            self.yang_name = "component"
            self.yang_parent_name = "components"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([("config", ("config", Components.Component.Config)), ("state", ("state", Components.Component.State)), ("properties", ("properties", Components.Component.Properties)), ("subcomponents", ("subcomponents", Components.Component.Subcomponents)), ("openconfig-transport-line-common:optical-port", ("optical_port", Components.Component.OpticalPort)), ("openconfig-platform-transceiver:transceiver", ("transceiver", Components.Component.Transceiver)), ("openconfig-terminal-device:optical-channel", ("optical_channel", Components.Component.OpticalChannel))])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
            ])
            self.name = None

            self.config = Components.Component.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = Components.Component.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"

            self.properties = Components.Component.Properties()
            self.properties.parent = self
            self._children_name_map["properties"] = "properties"

            self.subcomponents = Components.Component.Subcomponents()
            self.subcomponents.parent = self
            self._children_name_map["subcomponents"] = "subcomponents"

            self.optical_port = Components.Component.OpticalPort()
            self.optical_port.parent = self
            self._children_name_map["optical_port"] = "openconfig-transport-line-common:optical-port"

            self.transceiver = Components.Component.Transceiver()
            self.transceiver.parent = self
            self._children_name_map["transceiver"] = "openconfig-platform-transceiver:transceiver"

            self.optical_channel = Components.Component.OpticalChannel()
            self.optical_channel.parent = self
            self._children_name_map["optical_channel"] = "openconfig-terminal-device:optical-channel"
            self._segment_path = lambda: "component" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "openconfig-platform:components/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Components.Component, ['name'], name, value)


        class Config(Entity):
            """
            Configuration data for each component
            
            .. attribute:: name
            
            	Device name for the component \-\- this will not be a configurable parameter on many implementations
            	**type**\: str
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                super(Components.Component.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None
                self._segment_path = lambda: "config"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Config, ['name'], name, value)



        class State(Entity):
            """
            Operational state data for each component
            
            .. attribute:: name
            
            	Device name for the component \-\- this will not be a configurable parameter on many implementations
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: type
            
            	Type of component as identified by the system
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`OPENCONFIGHARDWARECOMPONENT <ydk.models.openconfig.openconfig_platform_types.OPENCONFIGHARDWARECOMPONENT>`
            
            		**type**\:  :py:class:`OPENCONFIGSOFTWARECOMPONENT <ydk.models.openconfig.openconfig_platform_types.OPENCONFIGSOFTWARECOMPONENT>`
            
            	**config**\: False
            
            .. attribute:: id
            
            	Unique identifier assigned by the system for the component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: description
            
            	System\-supplied description of the component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mfg_name
            
            	System\-supplied identifier for the manufacturer of the component.  This data is particularly useful when a component manufacturer is different than the overall device vendor
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: version
            
            	System\-defined version string for a hardware, firmware, or software component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: serial_no
            
            	System\-assigned serial number of the component
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: part_no
            
            	System\-assigned part number for the component.  This should be present in particular if the component is also an FRU (field replacable unit)
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                super(Components.Component.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('type', (YLeaf(YType.str, 'type'), [('ydk.models.openconfig.openconfig_platform_types', 'OPENCONFIGHARDWARECOMPONENT'),('ydk.models.openconfig.openconfig_platform_types', 'OPENCONFIGSOFTWARECOMPONENT')])),
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('mfg_name', (YLeaf(YType.str, 'mfg-name'), ['str'])),
                    ('version', (YLeaf(YType.str, 'version'), ['str'])),
                    ('serial_no', (YLeaf(YType.str, 'serial-no'), ['str'])),
                    ('part_no', (YLeaf(YType.str, 'part-no'), ['str'])),
                ])
                self.name = None
                self.type = None
                self.id = None
                self.description = None
                self.mfg_name = None
                self.version = None
                self.serial_no = None
                self.part_no = None
                self._segment_path = lambda: "state"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.State, ['name', 'type', 'id', 'description', 'mfg_name', 'version', 'serial_no', 'part_no'], name, value)



        class Properties(Entity):
            """
            Enclosing container 
            
            .. attribute:: property
            
            	List of system properties for the component
            	**type**\: list of  		 :py:class:`Property <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                super(Components.Component.Properties, self).__init__()

                self.yang_name = "properties"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("property", ("property", Components.Component.Properties.Property))])
                self._leafs = OrderedDict()

                self.property = YList(self)
                self._segment_path = lambda: "properties"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Properties, [], name, value)


            class Property(Entity):
                """
                List of system properties for the component
                
                .. attribute:: name  (key)
                
                	Reference to the property name
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.Config>`
                
                .. attribute:: config
                
                	Configuration data for each property
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.Config>`
                
                .. attribute:: state
                
                	Operational state data for each property
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2016-06-06'

                def __init__(self):
                    super(Components.Component.Properties.Property, self).__init__()

                    self.yang_name = "property"
                    self.yang_parent_name = "properties"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("config", ("config", Components.Component.Properties.Property.Config)), ("state", ("state", Components.Component.Properties.Property.State))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.config = Components.Component.Properties.Property.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Components.Component.Properties.Property.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "property" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Properties.Property, ['name'], name, value)


                class Config(Entity):
                    """
                    Configuration data for each property
                    
                    .. attribute:: name
                    
                    	System\-supplied name of the property \-\- this is typically non\-configurable
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	Property values can take on a variety of types.  Signed and unsigned integer types may be provided in smaller sizes, e.g., int8, uint16, etc
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    		**type**\: bool
                    
                    		**type**\: int
                    
                    			**range:** \-9223372036854775808..9223372036854775807
                    
                    		**type**\: int
                    
                    			**range:** 0..18446744073709551615
                    
                    		**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    			**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        super(Components.Component.Properties.Property.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "property"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('value', (YLeaf(YType.str, 'value'), ['str','bool','int','int','Decimal64'])),
                        ])
                        self.name = None
                        self.value = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Properties.Property.Config, ['name', 'value'], name, value)



                class State(Entity):
                    """
                    Operational state data for each property
                    
                    .. attribute:: name
                    
                    	System\-supplied name of the property \-\- this is typically non\-configurable
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: value
                    
                    	Property values can take on a variety of types.  Signed and unsigned integer types may be provided in smaller sizes, e.g., int8, uint16, etc
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    		**type**\: bool
                    
                    		**type**\: int
                    
                    			**range:** \-9223372036854775808..9223372036854775807
                    
                    		**type**\: int
                    
                    			**range:** 0..18446744073709551615
                    
                    		**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    			**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    .. attribute:: configurable
                    
                    	Indication whether the property is user\-configurable
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        super(Components.Component.Properties.Property.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "property"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('value', (YLeaf(YType.str, 'value'), ['str','bool','int','int','Decimal64'])),
                            ('configurable', (YLeaf(YType.boolean, 'configurable'), ['bool'])),
                        ])
                        self.name = None
                        self.value = None
                        self.configurable = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Properties.Property.State, ['name', 'value', 'configurable'], name, value)





        class Subcomponents(Entity):
            """
            Enclosing container for subcomponent references
            
            .. attribute:: subcomponent
            
            	List of subcomponent references
            	**type**\: list of  		 :py:class:`Subcomponent <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                super(Components.Component.Subcomponents, self).__init__()

                self.yang_name = "subcomponents"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("subcomponent", ("subcomponent", Components.Component.Subcomponents.Subcomponent))])
                self._leafs = OrderedDict()

                self.subcomponent = YList(self)
                self._segment_path = lambda: "subcomponents"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Subcomponents, [], name, value)


            class Subcomponent(Entity):
                """
                List of subcomponent references
                
                .. attribute:: name  (key)
                
                	Reference to the name list key
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.Config>`
                
                .. attribute:: config
                
                	Configuration data 
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.Config>`
                
                .. attribute:: state
                
                	Operational state data 
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-platform'
                _revision = '2016-06-06'

                def __init__(self):
                    super(Components.Component.Subcomponents.Subcomponent, self).__init__()

                    self.yang_name = "subcomponent"
                    self.yang_parent_name = "subcomponents"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("config", ("config", Components.Component.Subcomponents.Subcomponent.Config)), ("state", ("state", Components.Component.Subcomponents.Subcomponent.State))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.config = Components.Component.Subcomponents.Subcomponent.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Components.Component.Subcomponents.Subcomponent.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "subcomponent" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Subcomponents.Subcomponent, ['name'], name, value)


                class Config(Entity):
                    """
                    Configuration data 
                    
                    .. attribute:: name
                    
                    	Reference to the name of the subcomponent
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        super(Components.Component.Subcomponents.Subcomponent.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "subcomponent"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Subcomponents.Subcomponent.Config, ['name'], name, value)



                class State(Entity):
                    """
                    Operational state data 
                    
                    .. attribute:: name
                    
                    	Reference to the name of the subcomponent
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        super(Components.Component.Subcomponents.Subcomponent.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "subcomponent"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Subcomponents.Subcomponent.State, ['name'], name, value)





        class OpticalPort(Entity):
            """
            Top\-level container 
            
            .. attribute:: config
            
            	Operational config data for optical line ports
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort.Config>`
            
            .. attribute:: state
            
            	Operational state data for optical line ports
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-line-com'
            _revision = '2017-07-08'

            def __init__(self):
                super(Components.Component.OpticalPort, self).__init__()

                self.yang_name = "optical-port"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.OpticalPort.Config)), ("state", ("state", Components.Component.OpticalPort.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.OpticalPort.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.OpticalPort.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "openconfig-transport-line-common:optical-port"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.OpticalPort, [], name, value)


            class Config(Entity):
                """
                Operational config data for optical line ports
                
                .. attribute:: admin_state
                
                	Sets the admin state of the optical\-port
                	**type**\:  :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                

                """

                _prefix = 'oc-line-com'
                _revision = '2017-07-08'

                def __init__(self):
                    super(Components.Component.OpticalPort.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "optical-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.openconfig.openconfig_transport_types', 'AdminStateType', '')])),
                    ])
                    self.admin_state = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.OpticalPort.Config, ['admin_state'], name, value)



            class State(Entity):
                """
                Operational state data for optical line ports
                
                .. attribute:: admin_state
                
                	Sets the admin state of the optical\-port
                	**type**\:  :py:class:`AdminStateType <ydk.models.openconfig.openconfig_transport_types.AdminStateType>`
                
                	**config**\: False
                
                .. attribute:: optical_port_type
                
                	Indicates the type of transport line port.  This is an informational field that should be made available by the device (e.g., in the openconfig\-platform model)
                	**type**\:  :py:class:`OPTICALLINEPORTTYPE <ydk.models.openconfig.openconfig_transport_line_common.OPTICALLINEPORTTYPE>`
                
                	**config**\: False
                
                .. attribute:: input_power
                
                	The total input optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort.State.InputPower>`
                
                	**config**\: False
                
                .. attribute:: output_power
                
                	The total output optical power of this port in units of 0.01dBm. If avg/min/max statistics are not supported, just supply the instant value
                	**type**\:  :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalPort.State.OutputPower>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-line-com'
                _revision = '2017-07-08'

                def __init__(self):
                    super(Components.Component.OpticalPort.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "optical-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("input-power", ("input_power", Components.Component.OpticalPort.State.InputPower)), ("output-power", ("output_power", Components.Component.OpticalPort.State.OutputPower))])
                    self._leafs = OrderedDict([
                        ('admin_state', (YLeaf(YType.enumeration, 'admin-state'), [('ydk.models.openconfig.openconfig_transport_types', 'AdminStateType', '')])),
                        ('optical_port_type', (YLeaf(YType.identityref, 'optical-port-type'), [('ydk.models.openconfig.openconfig_transport_line_common', 'OPTICALLINEPORTTYPE')])),
                    ])
                    self.admin_state = None
                    self.optical_port_type = None

                    self.input_power = Components.Component.OpticalPort.State.InputPower()
                    self.input_power.parent = self
                    self._children_name_map["input_power"] = "input-power"

                    self.output_power = Components.Component.OpticalPort.State.OutputPower()
                    self.output_power.parent = self
                    self._children_name_map["output_power"] = "output-power"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.OpticalPort.State, ['admin_state', 'optical_port_type'], name, value)


                class InputPower(Entity):
                    """
                    The total input optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-line-com'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(Components.Component.OpticalPort.State.InputPower, self).__init__()

                        self.yang_name = "input-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "input-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalPort.State.InputPower, ['instant', 'avg', 'min', 'max'], name, value)



                class OutputPower(Entity):
                    """
                    The total output optical power of this port in units
                    of 0.01dBm. If avg/min/max statistics are not supported,
                    just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    .. attribute:: max
                    
                    	The maximum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    	**config**\: False
                    
                    	**units**\: dBm
                    
                    

                    """

                    _prefix = 'oc-line-com'
                    _revision = '2017-07-08'

                    def __init__(self):
                        super(Components.Component.OpticalPort.State.OutputPower, self).__init__()

                        self.yang_name = "output-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "output-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalPort.State.OutputPower, ['instant', 'avg', 'min', 'max'], name, value)





        class Transceiver(Entity):
            """
            Top\-level container for client port transceiver data
            
            .. attribute:: config
            
            	Configuration data for client port transceivers
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.Config>`
            
            .. attribute:: state
            
            	Operational state data for client port transceivers
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State>`
            
            	**config**\: False
            
            .. attribute:: physical_channels
            
            	Enclosing container for client channels
            	**type**\:  :py:class:`PhysicalChannels <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels>`
            
            

            """

            _prefix = 'oc-transceiver'
            _revision = '2016-05-24'

            def __init__(self):
                super(Components.Component.Transceiver, self).__init__()

                self.yang_name = "transceiver"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.Transceiver.Config)), ("state", ("state", Components.Component.Transceiver.State)), ("physical-channels", ("physical_channels", Components.Component.Transceiver.PhysicalChannels))])
                self._leafs = OrderedDict()

                self.config = Components.Component.Transceiver.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.Transceiver.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.physical_channels = Components.Component.Transceiver.PhysicalChannels()
                self.physical_channels.parent = self
                self._children_name_map["physical_channels"] = "physical-channels"
                self._segment_path = lambda: "openconfig-platform-transceiver:transceiver"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.Transceiver, [], name, value)


            class Config(Entity):
                """
                Configuration data for client port transceivers
                
                .. attribute:: enabled
                
                	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                	**type**\: bool
                
                .. attribute:: form_factor
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not plugable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre\-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system
                	**type**\:  :py:class:`TRANSCEIVERFORMFACTORTYPE <ydk.models.openconfig.openconfig_transport_types.TRANSCEIVERFORMFACTORTYPE>`
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2016-05-24'

                def __init__(self):
                    super(Components.Component.Transceiver.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "transceiver"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('form_factor', (YLeaf(YType.identityref, 'form-factor'), [('ydk.models.openconfig.openconfig_transport_types', 'TRANSCEIVERFORMFACTORTYPE')])),
                    ])
                    self.enabled = None
                    self.form_factor = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Transceiver.Config, ['enabled', 'form_factor'], name, value)



            class State(Entity):
                """
                Operational state data for client port transceivers
                
                .. attribute:: enabled
                
                	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: form_factor
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not plugable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre\-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system
                	**type**\:  :py:class:`TRANSCEIVERFORMFACTORTYPE <ydk.models.openconfig.openconfig_transport_types.TRANSCEIVERFORMFACTORTYPE>`
                
                	**config**\: False
                
                .. attribute:: present
                
                	Indicates whether a transceiver is present in the specified client port
                	**type**\:  :py:class:`Present <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.Present>`
                
                	**config**\: False
                
                .. attribute:: connector_type
                
                	Connector type used on this port
                	**type**\:  :py:class:`FIBERCONNECTORTYPE <ydk.models.openconfig.openconfig_transport_types.FIBERCONNECTORTYPE>`
                
                	**config**\: False
                
                .. attribute:: internal_temp
                
                	Internally measured temperature in degrees Celsius. MSA valid range is between \-40 and +125C. Accuracy shall be better than +/\- 3 degC over the whole temperature range
                	**type**\: int
                
                	**range:** \-40..125
                
                	**config**\: False
                
                .. attribute:: vendor
                
                	Full name of transceiver vendor. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h)
                	**type**\: str
                
                	**length:** 1..16
                
                	**config**\: False
                
                .. attribute:: vendor_part
                
                	Transceiver vendor's part number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part number is undefined, all 16 octets = 0h
                	**type**\: str
                
                	**length:** 1..16
                
                	**config**\: False
                
                .. attribute:: vendor_rev
                
                	Transceiver vendor's revision number. 2\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h)
                	**type**\: str
                
                	**length:** 1..2
                
                	**config**\: False
                
                .. attribute:: ethernet_compliance_code
                
                	Ethernet PMD that the transceiver supports. The SFF/QSFP MSAs have registers for this and CFP MSA has similar
                	**type**\:  :py:class:`ETHERNETPMDTYPE <ydk.models.openconfig.openconfig_transport_types.ETHERNETPMDTYPE>`
                
                	**config**\: False
                
                .. attribute:: sonet_sdh_compliance_code
                
                	SONET/SDH application code supported by the port
                	**type**\:  :py:class:`SONETAPPLICATIONCODE <ydk.models.openconfig.openconfig_transport_types.SONETAPPLICATIONCODE>`
                
                	**config**\: False
                
                .. attribute:: otn_compliance_code
                
                	OTN application code supported by the port
                	**type**\:  :py:class:`OTNAPPLICATIONCODE <ydk.models.openconfig.openconfig_transport_types.OTNAPPLICATIONCODE>`
                
                	**config**\: False
                
                .. attribute:: serial_no
                
                	Transceiver serial number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part serial number is undefined, all 16 octets = 0h
                	**type**\: str
                
                	**length:** 1..16
                
                	**config**\: False
                
                .. attribute:: date_code
                
                	Representation of the transceiver date code, typically stored as YYMMDD.  The time portion of the value is undefined and not intended to be read
                	**type**\: str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                	**config**\: False
                
                .. attribute:: fault_condition
                
                	Indicates if a fault condition exists in the transceiver
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2016-05-24'

                def __init__(self):
                    super(Components.Component.Transceiver.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "transceiver"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                        ('form_factor', (YLeaf(YType.identityref, 'form-factor'), [('ydk.models.openconfig.openconfig_transport_types', 'TRANSCEIVERFORMFACTORTYPE')])),
                        ('present', (YLeaf(YType.enumeration, 'present'), [('ydk.models.openconfig.openconfig_platform', 'Components', 'Component.Transceiver.State.Present')])),
                        ('connector_type', (YLeaf(YType.identityref, 'connector-type'), [('ydk.models.openconfig.openconfig_transport_types', 'FIBERCONNECTORTYPE')])),
                        ('internal_temp', (YLeaf(YType.int16, 'internal-temp'), ['int'])),
                        ('vendor', (YLeaf(YType.str, 'vendor'), ['str'])),
                        ('vendor_part', (YLeaf(YType.str, 'vendor-part'), ['str'])),
                        ('vendor_rev', (YLeaf(YType.str, 'vendor-rev'), ['str'])),
                        ('ethernet_compliance_code', (YLeaf(YType.identityref, 'ethernet-compliance-code'), [('ydk.models.openconfig.openconfig_transport_types', 'ETHERNETPMDTYPE')])),
                        ('sonet_sdh_compliance_code', (YLeaf(YType.identityref, 'sonet-sdh-compliance-code'), [('ydk.models.openconfig.openconfig_transport_types', 'SONETAPPLICATIONCODE')])),
                        ('otn_compliance_code', (YLeaf(YType.identityref, 'otn-compliance-code'), [('ydk.models.openconfig.openconfig_transport_types', 'OTNAPPLICATIONCODE')])),
                        ('serial_no', (YLeaf(YType.str, 'serial-no'), ['str'])),
                        ('date_code', (YLeaf(YType.str, 'date-code'), ['str'])),
                        ('fault_condition', (YLeaf(YType.boolean, 'fault-condition'), ['bool'])),
                    ])
                    self.enabled = None
                    self.form_factor = None
                    self.present = None
                    self.connector_type = None
                    self.internal_temp = None
                    self.vendor = None
                    self.vendor_part = None
                    self.vendor_rev = None
                    self.ethernet_compliance_code = None
                    self.sonet_sdh_compliance_code = None
                    self.otn_compliance_code = None
                    self.serial_no = None
                    self.date_code = None
                    self.fault_condition = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Transceiver.State, ['enabled', 'form_factor', 'present', 'connector_type', 'internal_temp', 'vendor', 'vendor_part', 'vendor_rev', 'ethernet_compliance_code', 'sonet_sdh_compliance_code', 'otn_compliance_code', 'serial_no', 'date_code', 'fault_condition'], name, value)

                class Present(Enum):
                    """
                    Present (Enum Class)

                    Indicates whether a transceiver is present in

                    the specified client port.

                    .. data:: PRESENT = 0

                    	Transceiver is present on the port

                    .. data:: NOT_PRESENT = 1

                    	Transceiver is not present on the port

                    """

                    PRESENT = Enum.YLeaf(0, "PRESENT")

                    NOT_PRESENT = Enum.YLeaf(1, "NOT_PRESENT")




            class PhysicalChannels(Entity):
                """
                Enclosing container for client channels
                
                .. attribute:: channel
                
                	List of client channels, keyed by index within a physical client port.  A physical port with a single channel would have a single zero\-indexed element
                	**type**\: list of  		 :py:class:`Channel <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2016-05-24'

                def __init__(self):
                    super(Components.Component.Transceiver.PhysicalChannels, self).__init__()

                    self.yang_name = "physical-channels"
                    self.yang_parent_name = "transceiver"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("channel", ("channel", Components.Component.Transceiver.PhysicalChannels.Channel))])
                    self._leafs = OrderedDict()

                    self.channel = YList(self)
                    self._segment_path = lambda: "physical-channels"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.Transceiver.PhysicalChannels, [], name, value)


                class Channel(Entity):
                    """
                    List of client channels, keyed by index within a physical
                    client port.  A physical port with a single channel would
                    have a single zero\-indexed element
                    
                    .. attribute:: index  (key)
                    
                    	Reference to the index number of the channel
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration data for physical channels
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for channels
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-transceiver'
                    _revision = '2016-05-24'

                    def __init__(self):
                        super(Components.Component.Transceiver.PhysicalChannels.Channel, self).__init__()

                        self.yang_name = "channel"
                        self.yang_parent_name = "physical-channels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['index']
                        self._child_classes = OrderedDict([("config", ("config", Components.Component.Transceiver.PhysicalChannels.Channel.Config)), ("state", ("state", Components.Component.Transceiver.PhysicalChannels.Channel.State))])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.str, 'index'), ['int'])),
                        ])
                        self.index = None

                        self.config = Components.Component.Transceiver.PhysicalChannels.Channel.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Components.Component.Transceiver.PhysicalChannels.Channel.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "channel" + "[index='" + str(self.index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel, ['index'], name, value)


                    class Config(Entity):
                        """
                        Configuration data for physical channels
                        
                        .. attribute:: index
                        
                        	Index of the physical channnel or lane within a physical client port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: description
                        
                        	Text description for the client physical channel
                        	**type**\: str
                        
                        .. attribute:: tx_laser
                        
                        	Enable (true) or disable (false) the transmit label for the channel
                        	**type**\: bool
                        
                        .. attribute:: target_output_power
                        
                        	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dBm
                        
                        

                        """

                        _prefix = 'oc-transceiver'
                        _revision = '2016-05-24'

                        def __init__(self):
                            super(Components.Component.Transceiver.PhysicalChannels.Channel.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "channel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('tx_laser', (YLeaf(YType.boolean, 'tx-laser'), ['bool'])),
                                ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                            ])
                            self.index = None
                            self.description = None
                            self.tx_laser = None
                            self.target_output_power = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.Config, ['index', 'description', 'tx_laser', 'target_output_power'], name, value)



                    class State(Entity):
                        """
                        Operational state data for channels
                        
                        .. attribute:: index
                        
                        	Index of the physical channnel or lane within a physical client port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: description
                        
                        	Text description for the client physical channel
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: tx_laser
                        
                        	Enable (true) or disable (false) the transmit label for the channel
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: target_output_power
                        
                        	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dBm
                        
                        .. attribute:: output_frequency
                        
                        	The frequency in MHz of the individual physical channel (e.g. ITU C50 \- 195.0THz and would be reported as 195,000,000 MHz in this model). This attribute is not configurable on most client ports
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: output_power
                        
                        	The output optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower>`
                        
                        	**config**\: False
                        
                        .. attribute:: input_power
                        
                        	The input optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower>`
                        
                        	**config**\: False
                        
                        .. attribute:: laser_bias_current
                        
                        	The current applied by the system to the transmit laser to achieve the output power.  The current is expressed in mA with up to one decimal precision. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-transceiver'
                        _revision = '2016-05-24'

                        def __init__(self):
                            super(Components.Component.Transceiver.PhysicalChannels.Channel.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "channel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("output-power", ("output_power", Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower)), ("input-power", ("input_power", Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower)), ("laser-bias-current", ("laser_bias_current", Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent))])
                            self._leafs = OrderedDict([
                                ('index', (YLeaf(YType.uint16, 'index'), ['int'])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('tx_laser', (YLeaf(YType.boolean, 'tx-laser'), ['bool'])),
                                ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                                ('output_frequency', (YLeaf(YType.uint64, 'output-frequency'), ['int'])),
                            ])
                            self.index = None
                            self.description = None
                            self.tx_laser = None
                            self.target_output_power = None
                            self.output_frequency = None

                            self.output_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower()
                            self.output_power.parent = self
                            self._children_name_map["output_power"] = "output-power"

                            self.input_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower()
                            self.input_power.parent = self
                            self._children_name_map["input_power"] = "input-power"

                            self.laser_bias_current = Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent()
                            self.laser_bias_current.parent = self
                            self._children_name_map["laser_bias_current"] = "laser-bias-current"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.State, ['index', 'description', 'tx_laser', 'target_output_power', 'output_frequency'], name, value)


                        class OutputPower(Entity):
                            """
                            The output optical power of this port in units of 0.01dBm.
                            If the port is an aggregate of multiple physical channels,
                            this attribute is the total power or sum of all channels. If
                            avg/min/max statistics are not supported, the target is
                            expected to just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: max
                            
                            	The maximum value of the statitic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2016-05-24'

                            def __init__(self):
                                super(Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower, self).__init__()

                                self.yang_name = "output-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "output-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower, ['instant', 'avg', 'min', 'max'], name, value)



                        class InputPower(Entity):
                            """
                            The input optical power of this port in units of 0.01dBm.
                            If the port is an aggregate of multiple physical channels,
                            this attribute is the total power or sum of all channels.
                            If avg/min/max statistics are not supported, the target is
                            expected to just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: max
                            
                            	The maximum value of the statitic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2016-05-24'

                            def __init__(self):
                                super(Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower, self).__init__()

                                self.yang_name = "input-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "input-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower, ['instant', 'avg', 'min', 'max'], name, value)



                        class LaserBiasCurrent(Entity):
                            """
                            The current applied by the system to the transmit laser to
                            achieve the output power.  The current is expressed in mA
                            with up to one decimal precision. If avg/min/max statistics
                            are not supported, the target is expected to just supply
                            the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            .. attribute:: max
                            
                            	The maximum value of the statitic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-922337203685477580.8..922337203685477580.7
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-transceiver'
                            _revision = '2016-05-24'

                            def __init__(self):
                                super(Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent, self).__init__()

                                self.yang_name = "laser-bias-current"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                                    ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                                    ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                                    ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "laser-bias-current"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent, ['instant', 'avg', 'min', 'max'], name, value)







        class OpticalChannel(Entity):
            """
            Enclosing container for the list of optical channels
            
            .. attribute:: config
            
            	Configuration data for optical channels
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.Config>`
            
            .. attribute:: state
            
            	Operational state data for optical channels
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-opt-term'
            _revision = '2016-06-17'

            def __init__(self):
                super(Components.Component.OpticalChannel, self).__init__()

                self.yang_name = "optical-channel"
                self.yang_parent_name = "component"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Components.Component.OpticalChannel.Config)), ("state", ("state", Components.Component.OpticalChannel.State))])
                self._leafs = OrderedDict()

                self.config = Components.Component.OpticalChannel.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Components.Component.OpticalChannel.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "openconfig-terminal-device:optical-channel"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Components.Component.OpticalChannel, [], name, value)


            class Config(Entity):
                """
                Configuration data for optical channels
                
                .. attribute:: frequency
                
                	Frequency of the optical channel, expressed in MHz
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: target_output_power
                
                	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: operational_mode
                
                	Vendor\-specific mode identifier \-\- sets the operational mode for the channel
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: line_port
                
                	Reference to the line\-side physical port that carries this optical channel.  The target port should be a component in the physical inventory data model
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(Components.Component.OpticalChannel.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "optical-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('frequency', (YLeaf(YType.uint64, 'frequency'), ['int'])),
                        ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                        ('operational_mode', (YLeaf(YType.uint16, 'operational-mode'), ['int'])),
                        ('line_port', (YLeaf(YType.str, 'line-port'), ['str'])),
                    ])
                    self.frequency = None
                    self.target_output_power = None
                    self.operational_mode = None
                    self.line_port = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.OpticalChannel.Config, ['frequency', 'target_output_power', 'operational_mode', 'line_port'], name, value)



            class State(Entity):
                """
                Operational state data for optical channels
                
                .. attribute:: frequency
                
                	Frequency of the optical channel, expressed in MHz
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: target_output_power
                
                	Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel\-milliwats)
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                	**units**\: dBm
                
                .. attribute:: operational_mode
                
                	Vendor\-specific mode identifier \-\- sets the operational mode for the channel
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: line_port
                
                	Reference to the line\-side physical port that carries this optical channel.  The target port should be a component in the physical inventory data model
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                	**config**\: False
                
                .. attribute:: group_id
                
                	If the device places constraints on which optical channels must be managed together (e.g., transmitted on the same line port), it can indicate that by setting the group\-id to the same value across related optical channels
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: output_power
                
                	The output optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`OutputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.OutputPower>`
                
                	**config**\: False
                
                .. attribute:: input_power
                
                	The input optical power of this port in units of 0.01dBm. If the port is an aggregate of multiple physical channels, this attribute is the total power or sum of all channels. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`InputPower <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.InputPower>`
                
                	**config**\: False
                
                .. attribute:: laser_bias_current
                
                	The current applied by the system to the transmit laser to achieve the output power.  The current is expressed in mA with up to one decimal precision. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                	**type**\:  :py:class:`LaserBiasCurrent <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.LaserBiasCurrent>`
                
                	**config**\: False
                
                .. attribute:: chromatic_dispersion
                
                	Chromatic Dispersion of an optical channel in ps/nm as reported by receiver
                	**type**\:  :py:class:`ChromaticDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.ChromaticDispersion>`
                
                	**config**\: False
                
                .. attribute:: polarization_mode_dispersion
                
                	Polarization Mode Dispersion of an optical channel in ps as reported by receiver
                	**type**\:  :py:class:`PolarizationModeDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.PolarizationModeDispersion>`
                
                	**config**\: False
                
                .. attribute:: second_order_polarization_mode_dispersion
                
                	Second Order Polarization Mode Dispersion of an optical channel in ps^2 as reported by receiver
                	**type**\:  :py:class:`SecondOrderPolarizationModeDispersion <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion>`
                
                	**config**\: False
                
                .. attribute:: polarization_dependent_loss
                
                	Polarization Dependent Loss of an optical channel in dB as reported by receiver
                	**type**\:  :py:class:`PolarizationDependentLoss <ydk.models.openconfig.openconfig_platform.Components.Component.OpticalChannel.State.PolarizationDependentLoss>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-opt-term'
                _revision = '2016-06-17'

                def __init__(self):
                    super(Components.Component.OpticalChannel.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "optical-channel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("output-power", ("output_power", Components.Component.OpticalChannel.State.OutputPower)), ("input-power", ("input_power", Components.Component.OpticalChannel.State.InputPower)), ("laser-bias-current", ("laser_bias_current", Components.Component.OpticalChannel.State.LaserBiasCurrent)), ("chromatic-dispersion", ("chromatic_dispersion", Components.Component.OpticalChannel.State.ChromaticDispersion)), ("polarization-mode-dispersion", ("polarization_mode_dispersion", Components.Component.OpticalChannel.State.PolarizationModeDispersion)), ("second-order-polarization-mode-dispersion", ("second_order_polarization_mode_dispersion", Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion)), ("polarization-dependent-loss", ("polarization_dependent_loss", Components.Component.OpticalChannel.State.PolarizationDependentLoss))])
                    self._leafs = OrderedDict([
                        ('frequency', (YLeaf(YType.uint64, 'frequency'), ['int'])),
                        ('target_output_power', (YLeaf(YType.str, 'target-output-power'), ['Decimal64'])),
                        ('operational_mode', (YLeaf(YType.uint16, 'operational-mode'), ['int'])),
                        ('line_port', (YLeaf(YType.str, 'line-port'), ['str'])),
                        ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                    ])
                    self.frequency = None
                    self.target_output_power = None
                    self.operational_mode = None
                    self.line_port = None
                    self.group_id = None

                    self.output_power = Components.Component.OpticalChannel.State.OutputPower()
                    self.output_power.parent = self
                    self._children_name_map["output_power"] = "output-power"

                    self.input_power = Components.Component.OpticalChannel.State.InputPower()
                    self.input_power.parent = self
                    self._children_name_map["input_power"] = "input-power"

                    self.laser_bias_current = Components.Component.OpticalChannel.State.LaserBiasCurrent()
                    self.laser_bias_current.parent = self
                    self._children_name_map["laser_bias_current"] = "laser-bias-current"

                    self.chromatic_dispersion = Components.Component.OpticalChannel.State.ChromaticDispersion()
                    self.chromatic_dispersion.parent = self
                    self._children_name_map["chromatic_dispersion"] = "chromatic-dispersion"

                    self.polarization_mode_dispersion = Components.Component.OpticalChannel.State.PolarizationModeDispersion()
                    self.polarization_mode_dispersion.parent = self
                    self._children_name_map["polarization_mode_dispersion"] = "polarization-mode-dispersion"

                    self.second_order_polarization_mode_dispersion = Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion()
                    self.second_order_polarization_mode_dispersion.parent = self
                    self._children_name_map["second_order_polarization_mode_dispersion"] = "second-order-polarization-mode-dispersion"

                    self.polarization_dependent_loss = Components.Component.OpticalChannel.State.PolarizationDependentLoss()
                    self.polarization_dependent_loss.parent = self
                    self._children_name_map["polarization_dependent_loss"] = "polarization-dependent-loss"
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Components.Component.OpticalChannel.State, ['frequency', 'target_output_power', 'operational_mode', 'line_port', 'group_id'], name, value)


                class OutputPower(Entity):
                    """
                    The output optical power of this port in units of 0.01dBm.
                    If the port is an aggregate of multiple physical channels,
                    this attribute is the total power or sum of all channels. If
                    avg/min/max statistics are not supported, the target is
                    expected to just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.OutputPower, self).__init__()

                        self.yang_name = "output-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "output-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.OutputPower, ['instant', 'avg', 'min', 'max'], name, value)



                class InputPower(Entity):
                    """
                    The input optical power of this port in units of 0.01dBm.
                    If the port is an aggregate of multiple physical channels,
                    this attribute is the total power or sum of all channels.
                    If avg/min/max statistics are not supported, the target is
                    expected to just supply the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.InputPower, self).__init__()

                        self.yang_name = "input-power"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "input-power"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.InputPower, ['instant', 'avg', 'min', 'max'], name, value)



                class LaserBiasCurrent(Entity):
                    """
                    The current applied by the system to the transmit laser to
                    achieve the output power.  The current is expressed in mA
                    with up to one decimal precision. If avg/min/max statistics
                    are not supported, the target is expected to just supply
                    the instant value
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.LaserBiasCurrent, self).__init__()

                        self.yang_name = "laser-bias-current"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "laser-bias-current"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.LaserBiasCurrent, ['instant', 'avg', 'min', 'max'], name, value)



                class ChromaticDispersion(Entity):
                    """
                    Chromatic Dispersion of an optical channel
                    in ps/nm as reported by receiver
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.ChromaticDispersion, self).__init__()

                        self.yang_name = "chromatic-dispersion"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "chromatic-dispersion"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.ChromaticDispersion, ['instant', 'avg', 'min', 'max'], name, value)



                class PolarizationModeDispersion(Entity):
                    """
                    Polarization Mode Dispersion of an optical channel
                    in ps as reported by receiver
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.PolarizationModeDispersion, self).__init__()

                        self.yang_name = "polarization-mode-dispersion"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "polarization-mode-dispersion"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.PolarizationModeDispersion, ['instant', 'avg', 'min', 'max'], name, value)



                class SecondOrderPolarizationModeDispersion(Entity):
                    """
                    Second Order Polarization Mode Dispersion of an optical
                    channel in ps^2 as reported by receiver
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion, self).__init__()

                        self.yang_name = "second-order-polarization-mode-dispersion"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "second-order-polarization-mode-dispersion"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion, ['instant', 'avg', 'min', 'max'], name, value)



                class PolarizationDependentLoss(Entity):
                    """
                    Polarization Dependent Loss of an optical channel
                    in dB as reported by receiver
                    
                    .. attribute:: instant
                    
                    	The instantaneous value of the statistic
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: avg
                    
                    	The arithmetic mean value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: min
                    
                    	The minimum value of the statistic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    .. attribute:: max
                    
                    	The maximum value of the statitic over the sampling period
                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-922337203685477580.8..922337203685477580.7
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-opt-term'
                    _revision = '2016-06-17'

                    def __init__(self):
                        super(Components.Component.OpticalChannel.State.PolarizationDependentLoss, self).__init__()

                        self.yang_name = "polarization-dependent-loss"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('instant', (YLeaf(YType.str, 'instant'), ['Decimal64'])),
                            ('avg', (YLeaf(YType.str, 'avg'), ['Decimal64'])),
                            ('min', (YLeaf(YType.str, 'min'), ['Decimal64'])),
                            ('max', (YLeaf(YType.str, 'max'), ['Decimal64'])),
                        ])
                        self.instant = None
                        self.avg = None
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "polarization-dependent-loss"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Components.Component.OpticalChannel.State.PolarizationDependentLoss, ['instant', 'avg', 'min', 'max'], name, value)





    def clone_ptr(self):
        self._top_entity = Components()
        return self._top_entity



