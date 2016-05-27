""" openconfig_inventory 

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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class Components(object):
    """
    Enclosing container for the components in the system.
    
    .. attribute:: component
    
    	List of components, keyed by component name
    	**type**\: list of :py:class:`Component <ydk.models.openconfig.openconfig_inventory.Components.Component>`
    
    

    """

    _prefix = 'oc-inv'
    _revision = '2015-12-18'

    def __init__(self):
        self.component = YList()
        self.component.parent = self
        self.component.name = 'component'


    class Component(object):
        """
        List of components, keyed by component name.
        
        .. attribute:: name  <key>
        
        	References the component name
        	**type**\: str
        
        .. attribute:: config
        
        	Configuration data for each component
        	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_inventory.Components.Component.Config>`
        
        .. attribute:: state
        
        	Operational state data for each component
        	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_inventory.Components.Component.State>`
        
        .. attribute:: properties
        
        	Enclosing container 
        	**type**\: :py:class:`Properties <ydk.models.openconfig.openconfig_inventory.Components.Component.Properties>`
        
        .. attribute:: subcomponents
        
        	Enclosing container for subcomponent references
        	**type**\: :py:class:`Subcomponents <ydk.models.openconfig.openconfig_inventory.Components.Component.Subcomponents>`
        
        

        """

        _prefix = 'oc-inv'
        _revision = '2015-12-18'

        def __init__(self):
            self.parent = None
            self.name = None
            self.config = Components.Component.Config()
            self.config.parent = self
            self.state = Components.Component.State()
            self.state.parent = self
            self.properties = Components.Component.Properties()
            self.properties.parent = self
            self.subcomponents = Components.Component.Subcomponents()
            self.subcomponents.parent = self


        class Config(object):
            """
            Configuration data for each component
            
            .. attribute:: name
            
            	Device name for the component \-\- this may not be a configurable parameter on many implementations
            	**type**\: str
            
            

            """

            _prefix = 'oc-inv'
            _revision = '2015-12-18'

            def __init__(self):
                self.parent = None
                self.name = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-inventory:config'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_inventory as meta
                return meta._meta_table['Components.Component.Config']['meta_info']


        class State(object):
            """
            Operational state data for each component
            
            .. attribute:: name
            
            	Device name for the component \-\- this may not be a configurable parameter on many implementations
            	**type**\: str
            
            .. attribute:: type
            
            	Type of component as identified by the system
            	**type**\: one of the below types:
            
            	**type**\: :py:class:`OpenconfigHardwareComponent_Identity <ydk.models.openconfig.openconfig_inventory_types.OpenconfigHardwareComponent_Identity>`
            
            
            ----
            	**type**\: :py:class:`OpenconfigSoftwareComponent_Identity <ydk.models.openconfig.openconfig_inventory_types.OpenconfigSoftwareComponent_Identity>`
            
            
            ----
            .. attribute:: id
            
            	Unique identifier assigned by the system for the component
            	**type**\: str
            
            .. attribute:: description
            
            	System\-supplied description of the component
            	**type**\: str
            
            .. attribute:: serial_no
            
            	System\-assigned serial number of the component
            	**type**\: str
            
            .. attribute:: part_no
            
            	System\-assigned part number for the component.  This should be present in particular if the component is also an FRU (field replacable unit)
            	**type**\: str
            
            

            """

            _prefix = 'oc-inv'
            _revision = '2015-12-18'

            def __init__(self):
                self.parent = None
                self.name = None
                self.type = None
                self.id = None
                self.description = None
                self.serial_no = None
                self.part_no = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-inventory:state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.type is not None:
                    return True

                if self.id is not None:
                    return True

                if self.description is not None:
                    return True

                if self.serial_no is not None:
                    return True

                if self.part_no is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_inventory as meta
                return meta._meta_table['Components.Component.State']['meta_info']


        class Properties(object):
            """
            Enclosing container 
            
            .. attribute:: property
            
            	List of system properties for the component
            	**type**\: list of :py:class:`Property <ydk.models.openconfig.openconfig_inventory.Components.Component.Properties.Property>`
            
            

            """

            _prefix = 'oc-inv'
            _revision = '2015-12-18'

            def __init__(self):
                self.parent = None
                self.property = YList()
                self.property.parent = self
                self.property.name = 'property'


            class Property(object):
                """
                List of system properties for the component
                
                .. attribute:: name  <key>
                
                	Reference to the property name
                	**type**\: str
                
                .. attribute:: config
                
                	Configuration data for each property
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_inventory.Components.Component.Properties.Property.Config>`
                
                .. attribute:: state
                
                	Operational state data for each property
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_inventory.Components.Component.Properties.Property.State>`
                
                

                """

                _prefix = 'oc-inv'
                _revision = '2015-12-18'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.config = Components.Component.Properties.Property.Config()
                    self.config.parent = self
                    self.state = Components.Component.Properties.Property.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration data for each property
                    
                    .. attribute:: name
                    
                    	System\-supplied name of the property \-\- this is typically non\-configurable
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	Property values can take on a variety of types.  Signed and unsigned integer types may be provided in smaller sizes, e.g., int8, uint16, etc
                    	**type**\: one of the below types:
                    
                    	**type**\: str
                    
                    
                    ----
                    	**type**\: bool
                    
                    
                    ----
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    
                    ----
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    
                    ----
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    
                    ----
                    

                    """

                    _prefix = 'oc-inv'
                    _revision = '2015-12-18'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-inventory:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_inventory as meta
                        return meta._meta_table['Components.Component.Properties.Property.Config']['meta_info']


                class State(object):
                    """
                    Operational state data for each property
                    
                    .. attribute:: name
                    
                    	System\-supplied name of the property \-\- this is typically non\-configurable
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	Property values can take on a variety of types.  Signed and unsigned integer types may be provided in smaller sizes, e.g., int8, uint16, etc
                    	**type**\: one of the below types:
                    
                    	**type**\: str
                    
                    
                    ----
                    	**type**\: bool
                    
                    
                    ----
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    
                    ----
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    
                    ----
                    	**type**\: :py:class:`Decimal64 <ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    
                    ----
                    .. attribute:: configurable
                    
                    	Indication whether the property is user\-configurable
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'oc-inv'
                    _revision = '2015-12-18'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.value = None
                        self.configurable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-inventory:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.value is not None:
                            return True

                        if self.configurable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_inventory as meta
                        return meta._meta_table['Components.Component.Properties.Property.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return self.parent._common_path +'/openconfig-inventory:property[openconfig-inventory:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_inventory as meta
                    return meta._meta_table['Components.Component.Properties.Property']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-inventory:properties'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.property is not None:
                    for child_ref in self.property:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_inventory as meta
                return meta._meta_table['Components.Component.Properties']['meta_info']


        class Subcomponents(object):
            """
            Enclosing container for subcomponent references
            
            .. attribute:: subcomponent
            
            	List of subcomponent references
            	**type**\: list of :py:class:`Subcomponent <ydk.models.openconfig.openconfig_inventory.Components.Component.Subcomponents.Subcomponent>`
            
            

            """

            _prefix = 'oc-inv'
            _revision = '2015-12-18'

            def __init__(self):
                self.parent = None
                self.subcomponent = YList()
                self.subcomponent.parent = self
                self.subcomponent.name = 'subcomponent'


            class Subcomponent(object):
                """
                List of subcomponent references
                
                .. attribute:: name  <key>
                
                	Reference to the subcomponent name
                	**type**\: str
                
                .. attribute:: config
                
                	Configuration data 
                	**type**\: :py:class:`Config <ydk.models.openconfig.openconfig_inventory.Components.Component.Subcomponents.Subcomponent.Config>`
                
                .. attribute:: state
                
                	Operational state data 
                	**type**\: :py:class:`State <ydk.models.openconfig.openconfig_inventory.Components.Component.Subcomponents.Subcomponent.State>`
                
                

                """

                _prefix = 'oc-inv'
                _revision = '2015-12-18'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.config = Components.Component.Subcomponents.Subcomponent.Config()
                    self.config.parent = self
                    self.state = Components.Component.Subcomponents.Subcomponent.State()
                    self.state.parent = self


                class Config(object):
                    """
                    Configuration data 
                    
                    .. attribute:: name
                    
                    	Name of the subcomponent \-\- should reflect the name of the referenced component
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'oc-inv'
                    _revision = '2015-12-18'

                    def __init__(self):
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-inventory:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_inventory as meta
                        return meta._meta_table['Components.Component.Subcomponents.Subcomponent.Config']['meta_info']


                class State(object):
                    """
                    Operational state data 
                    
                    .. attribute:: name
                    
                    	Name of the subcomponent \-\- should reflect the name of the referenced component
                    	**type**\: str
                    
                    .. attribute:: reference
                    
                    	References the corresponding component in the overall list of inventory components
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'oc-inv'
                    _revision = '2015-12-18'

                    def __init__(self):
                        self.parent = None
                        self.name = None
                        self.reference = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-inventory:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        if self.reference is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_inventory as meta
                        return meta._meta_table['Components.Component.Subcomponents.Subcomponent.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return self.parent._common_path +'/openconfig-inventory:subcomponent[openconfig-inventory:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_inventory as meta
                    return meta._meta_table['Components.Component.Subcomponents.Subcomponent']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-inventory:subcomponents'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.subcomponent is not None:
                    for child_ref in self.subcomponent:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_inventory as meta
                return meta._meta_table['Components.Component.Subcomponents']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYDataValidationError('Key property name is None')

            return '/openconfig-inventory:components/openconfig-inventory:component[openconfig-inventory:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.config is not None and self.config._has_data():
                return True

            if self.state is not None and self.state._has_data():
                return True

            if self.properties is not None and self.properties._has_data():
                return True

            if self.subcomponents is not None and self.subcomponents._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_inventory as meta
            return meta._meta_table['Components.Component']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-inventory:components'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.component is not None:
            for child_ref in self.component:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_inventory as meta
        return meta._meta_table['Components']['meta_info']


