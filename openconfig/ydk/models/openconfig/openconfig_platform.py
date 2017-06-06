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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Components(object):
    """
    Enclosing container for the components in the system.
    
    .. attribute:: component
    
    	List of components, keyed by component name
    	**type**\: list of    :py:class:`Component <ydk.models.openconfig.openconfig_platform.Components.Component>`
    
    

    """

    _prefix = 'oc-platform'
    _revision = '2016-06-06'

    def __init__(self):
        self.component = YList()
        self.component.parent = self
        self.component.name = 'component'


    class Component(object):
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
            self.parent = None
            self.name = None
            self.config = Components.Component.Config()
            self.config.parent = self
            self.optical_channel = Components.Component.OpticalChannel()
            self.optical_channel.parent = self
            self.properties = Components.Component.Properties()
            self.properties.parent = self
            self.state = Components.Component.State()
            self.state.parent = self
            self.subcomponents = Components.Component.Subcomponents()
            self.subcomponents.parent = self
            self.transceiver = Components.Component.Transceiver()
            self.transceiver.parent = self


        class Config(object):
            """
            Configuration data for each component
            
            .. attribute:: name
            
            	Device name for the component \-\- this will not be a configurable parameter on many implementations
            	**type**\:  str
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                self.parent = None
                self.name = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-platform:config'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_platform as meta
                return meta._meta_table['Components.Component.Config']['meta_info']


        class State(object):
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
            
            	**type**\:   :py:class:`Openconfig_Hardware_ComponentIdentity <ydk.models.openconfig.openconfig_platform_types.Openconfig_Hardware_ComponentIdentity>`
            
            
            ----
            	**type**\:   :py:class:`Openconfig_Software_ComponentIdentity <ydk.models.openconfig.openconfig_platform_types.Openconfig_Software_ComponentIdentity>`
            
            
            ----
            .. attribute:: version
            
            	System\-defined version string for a hardware, firmware, or software component
            	**type**\:  str
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                self.parent = None
                self.description = None
                self.id = None
                self.mfg_name = None
                self.name = None
                self.part_no = None
                self.serial_no = None
                self.type = None
                self.version = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-platform:state'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.description is not None:
                    return True

                if self.id is not None:
                    return True

                if self.mfg_name is not None:
                    return True

                if self.name is not None:
                    return True

                if self.part_no is not None:
                    return True

                if self.serial_no is not None:
                    return True

                if self.type is not None:
                    return True

                if self.version is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_platform as meta
                return meta._meta_table['Components.Component.State']['meta_info']


        class Properties(object):
            """
            Enclosing container 
            
            .. attribute:: property
            
            	List of system properties for the component
            	**type**\: list of    :py:class:`Property <ydk.models.openconfig.openconfig_platform.Components.Component.Properties.Property>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

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
                        self.parent = None
                        self.name = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-platform:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.Properties.Property.Config']['meta_info']


                class State(object):
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
                        self.parent = None
                        self.configurable = None
                        self.name = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-platform:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.configurable is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.Properties.Property.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/openconfig-platform:property[openconfig-platform:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_platform as meta
                    return meta._meta_table['Components.Component.Properties.Property']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-platform:properties'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.property is not None:
                    for child_ref in self.property:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_platform as meta
                return meta._meta_table['Components.Component.Properties']['meta_info']


        class Subcomponents(object):
            """
            Enclosing container for subcomponent references
            
            .. attribute:: subcomponent
            
            	List of subcomponent references
            	**type**\: list of    :py:class:`Subcomponent <ydk.models.openconfig.openconfig_platform.Components.Component.Subcomponents.Subcomponent>`
            
            

            """

            _prefix = 'oc-platform'
            _revision = '2016-06-06'

            def __init__(self):
                self.parent = None
                self.subcomponent = YList()
                self.subcomponent.parent = self
                self.subcomponent.name = 'subcomponent'


            class Subcomponent(object):
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
                    
                    	Reference to the name of the subcomponent
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component.Config>`
                    
                    

                    """

                    _prefix = 'oc-platform'
                    _revision = '2016-06-06'

                    def __init__(self):
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-platform:config'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.Subcomponents.Subcomponent.Config']['meta_info']


                class State(object):
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
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-platform:state'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.Subcomponents.Subcomponent.State']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/openconfig-platform:subcomponent[openconfig-platform:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.config is not None and self.config._has_data():
                        return True

                    if self.state is not None and self.state._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_platform as meta
                    return meta._meta_table['Components.Component.Subcomponents.Subcomponent']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-platform:subcomponents'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.subcomponent is not None:
                    for child_ref in self.subcomponent:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_platform as meta
                return meta._meta_table['Components.Component.Subcomponents']['meta_info']


        class Transceiver(object):
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
                self.parent = None
                self.config = Components.Component.Transceiver.Config()
                self.config.parent = self
                self.physical_channels = Components.Component.Transceiver.PhysicalChannels()
                self.physical_channels.parent = self
                self.state = Components.Component.Transceiver.State()
                self.state.parent = self


            class Config(object):
                """
                Configuration data for client port transceivers
                
                .. attribute:: enabled
                
                	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                	**type**\:  bool
                
                .. attribute:: form_factor
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not plugable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre\-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system
                	**type**\:   :py:class:`Transceiver_Form_Factor_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Transceiver_Form_Factor_TypeIdentity>`
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2016-05-24'

                def __init__(self):
                    self.parent = None
                    self.enabled = None
                    self.form_factor = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-platform-transceiver:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enabled is not None:
                        return True

                    if self.form_factor is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_platform as meta
                    return meta._meta_table['Components.Component.Transceiver.Config']['meta_info']


            class State(object):
                """
                Operational state data for client port transceivers
                
                .. attribute:: connector_type
                
                	Connector type used on this port
                	**type**\:   :py:class:`Fiber_Connector_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Fiber_Connector_TypeIdentity>`
                
                .. attribute:: date_code
                
                	Representation of the transceiver date code, typically stored as YYMMDD.  The time portion of the value is undefined and not intended to be read
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: enabled
                
                	Turns power on / off to the transceiver \-\- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high\-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
                	**type**\:  bool
                
                .. attribute:: ethernet_compliance_code
                
                	Ethernet PMD that the transceiver supports. The SFF/QSFP MSAs have registers for this and CFP MSA has similar
                	**type**\:   :py:class:`Ethernet_Pmd_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Ethernet_Pmd_TypeIdentity>`
                
                .. attribute:: fault_condition
                
                	Indicates if a fault condition exists in the transceiver
                	**type**\:  bool
                
                .. attribute:: form_factor
                
                	Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not plugable, then non\-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre\-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system
                	**type**\:   :py:class:`Transceiver_Form_Factor_TypeIdentity <ydk.models.openconfig.openconfig_transport_types.Transceiver_Form_Factor_TypeIdentity>`
                
                .. attribute:: internal_temp
                
                	Internally measured temperature in degrees Celsius. MSA valid range is between \-40 and +125C. Accuracy shall be better than +/\- 3 degC over the whole temperature range
                	**type**\:  int
                
                	**range:** \-40..125
                
                .. attribute:: otn_compliance_code
                
                	OTN application code supported by the port
                	**type**\:   :py:class:`Otn_Application_CodeIdentity <ydk.models.openconfig.openconfig_transport_types.Otn_Application_CodeIdentity>`
                
                .. attribute:: present
                
                	Indicates whether a transceiver is present in the specified client port
                	**type**\:   :py:class:`PresentEnum <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.State.PresentEnum>`
                
                .. attribute:: serial_no
                
                	Transceiver serial number. 16\-octet field that contains ASCII characters, left\-aligned and padded on the right with ASCII spaces (20h). If part serial number is undefined, all 16 octets = 0h
                	**type**\:  str
                
                	**length:** 1..16
                
                .. attribute:: sonet_sdh_compliance_code
                
                	SONET/SDH application code supported by the port
                	**type**\:   :py:class:`Sonet_Application_CodeIdentity <ydk.models.openconfig.openconfig_transport_types.Sonet_Application_CodeIdentity>`
                
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
                    self.parent = None
                    self.connector_type = None
                    self.date_code = None
                    self.enabled = None
                    self.ethernet_compliance_code = None
                    self.fault_condition = None
                    self.form_factor = None
                    self.internal_temp = None
                    self.otn_compliance_code = None
                    self.present = None
                    self.serial_no = None
                    self.sonet_sdh_compliance_code = None
                    self.vendor = None
                    self.vendor_part = None
                    self.vendor_rev = None

                class PresentEnum(Enum):
                    """
                    PresentEnum

                    Indicates whether a transceiver is present in

                    the specified client port.

                    .. data:: PRESENT = 0

                    	Transceiver is present on the port

                    .. data:: NOT_PRESENT = 1

                    	Transceiver is not present on the port

                    """

                    PRESENT = 0

                    NOT_PRESENT = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.Transceiver.State.PresentEnum']


                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-platform-transceiver:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.connector_type is not None:
                        return True

                    if self.date_code is not None:
                        return True

                    if self.enabled is not None:
                        return True

                    if self.ethernet_compliance_code is not None:
                        return True

                    if self.fault_condition is not None:
                        return True

                    if self.form_factor is not None:
                        return True

                    if self.internal_temp is not None:
                        return True

                    if self.otn_compliance_code is not None:
                        return True

                    if self.present is not None:
                        return True

                    if self.serial_no is not None:
                        return True

                    if self.sonet_sdh_compliance_code is not None:
                        return True

                    if self.vendor is not None:
                        return True

                    if self.vendor_part is not None:
                        return True

                    if self.vendor_rev is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_platform as meta
                    return meta._meta_table['Components.Component.Transceiver.State']['meta_info']


            class PhysicalChannels(object):
                """
                Enclosing container for client channels
                
                .. attribute:: channel
                
                	List of client channels, keyed by index within a physical client port.  A physical port with a single channel would have a single zero\-indexed element
                	**type**\: list of    :py:class:`Channel <ydk.models.openconfig.openconfig_platform.Components.Component.Transceiver.PhysicalChannels.Channel>`
                
                

                """

                _prefix = 'oc-transceiver'
                _revision = '2016-05-24'

                def __init__(self):
                    self.parent = None
                    self.channel = YList()
                    self.channel.parent = self
                    self.channel.name = 'channel'


                class Channel(object):
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
                        self.parent = None
                        self.index = None
                        self.config = Components.Component.Transceiver.PhysicalChannels.Channel.Config()
                        self.config.parent = self
                        self.state = Components.Component.Transceiver.PhysicalChannels.Channel.State()
                        self.state.parent = self


                    class Config(object):
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
                            self.parent = None
                            self.description = None
                            self.index = None
                            self.target_output_power = None
                            self.tx_laser = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-platform-transceiver:config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.description is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.target_output_power is not None:
                                return True

                            if self.tx_laser is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_platform as meta
                            return meta._meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.Config']['meta_info']


                    class State(object):
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
                            self.parent = None
                            self.description = None
                            self.index = None
                            self.input_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower()
                            self.input_power.parent = self
                            self.laser_bias_current = Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent()
                            self.laser_bias_current.parent = self
                            self.output_frequency = None
                            self.output_power = Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower()
                            self.output_power.parent = self
                            self.target_output_power = None
                            self.tx_laser = None


                        class OutputPower(object):
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
                                self.parent = None
                                self.avg = None
                                self.instant = None
                                self.max = None
                                self.min = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-platform-transceiver:output-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.avg is not None:
                                    return True

                                if self.instant is not None:
                                    return True

                                if self.max is not None:
                                    return True

                                if self.min is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_platform as meta
                                return meta._meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State.OutputPower']['meta_info']


                        class InputPower(object):
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
                                self.parent = None
                                self.avg = None
                                self.instant = None
                                self.max = None
                                self.min = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-platform-transceiver:input-power'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.avg is not None:
                                    return True

                                if self.instant is not None:
                                    return True

                                if self.max is not None:
                                    return True

                                if self.min is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_platform as meta
                                return meta._meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State.InputPower']['meta_info']


                        class LaserBiasCurrent(object):
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
                                self.parent = None
                                self.avg = None
                                self.instant = None
                                self.max = None
                                self.min = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/openconfig-platform-transceiver:laser-bias-current'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.avg is not None:
                                    return True

                                if self.instant is not None:
                                    return True

                                if self.max is not None:
                                    return True

                                if self.min is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.openconfig._meta import _openconfig_platform as meta
                                return meta._meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State.LaserBiasCurrent']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/openconfig-platform-transceiver:state'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.description is not None:
                                return True

                            if self.index is not None:
                                return True

                            if self.input_power is not None and self.input_power._has_data():
                                return True

                            if self.laser_bias_current is not None and self.laser_bias_current._has_data():
                                return True

                            if self.output_frequency is not None:
                                return True

                            if self.output_power is not None and self.output_power._has_data():
                                return True

                            if self.target_output_power is not None:
                                return True

                            if self.tx_laser is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.openconfig._meta import _openconfig_platform as meta
                            return meta._meta_table['Components.Component.Transceiver.PhysicalChannels.Channel.State']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/openconfig-platform-transceiver:channel[openconfig-platform-transceiver:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.index is not None:
                            return True

                        if self.config is not None and self.config._has_data():
                            return True

                        if self.state is not None and self.state._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.Transceiver.PhysicalChannels.Channel']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-platform-transceiver:physical-channels'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.channel is not None:
                        for child_ref in self.channel:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_platform as meta
                    return meta._meta_table['Components.Component.Transceiver.PhysicalChannels']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-platform-transceiver:transceiver'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.config is not None and self.config._has_data():
                    return True

                if self.physical_channels is not None and self.physical_channels._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_platform as meta
                return meta._meta_table['Components.Component.Transceiver']['meta_info']


        class OpticalChannel(object):
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
                self.parent = None
                self.config = Components.Component.OpticalChannel.Config()
                self.config.parent = self
                self.state = Components.Component.OpticalChannel.State()
                self.state.parent = self


            class Config(object):
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
                    self.parent = None
                    self.frequency = None
                    self.line_port = None
                    self.operational_mode = None
                    self.target_output_power = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:config'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.frequency is not None:
                        return True

                    if self.line_port is not None:
                        return True

                    if self.operational_mode is not None:
                        return True

                    if self.target_output_power is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_platform as meta
                    return meta._meta_table['Components.Component.OpticalChannel.Config']['meta_info']


            class State(object):
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
                    self.parent = None
                    self.chromatic_dispersion = Components.Component.OpticalChannel.State.ChromaticDispersion()
                    self.chromatic_dispersion.parent = self
                    self.frequency = None
                    self.group_id = None
                    self.input_power = Components.Component.OpticalChannel.State.InputPower()
                    self.input_power.parent = self
                    self.laser_bias_current = Components.Component.OpticalChannel.State.LaserBiasCurrent()
                    self.laser_bias_current.parent = self
                    self.line_port = None
                    self.operational_mode = None
                    self.output_power = Components.Component.OpticalChannel.State.OutputPower()
                    self.output_power.parent = self
                    self.polarization_dependent_loss = Components.Component.OpticalChannel.State.PolarizationDependentLoss()
                    self.polarization_dependent_loss.parent = self
                    self.polarization_mode_dispersion = Components.Component.OpticalChannel.State.PolarizationModeDispersion()
                    self.polarization_mode_dispersion.parent = self
                    self.second_order_polarization_mode_dispersion = Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion()
                    self.second_order_polarization_mode_dispersion.parent = self
                    self.target_output_power = None


                class OutputPower(object):
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
                        self.parent = None
                        self.avg = None
                        self.instant = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:output-power'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg is not None:
                            return True

                        if self.instant is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.OpticalChannel.State.OutputPower']['meta_info']


                class InputPower(object):
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
                        self.parent = None
                        self.avg = None
                        self.instant = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:input-power'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg is not None:
                            return True

                        if self.instant is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.OpticalChannel.State.InputPower']['meta_info']


                class LaserBiasCurrent(object):
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
                        self.parent = None
                        self.avg = None
                        self.instant = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:laser-bias-current'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg is not None:
                            return True

                        if self.instant is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.OpticalChannel.State.LaserBiasCurrent']['meta_info']


                class ChromaticDispersion(object):
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
                        self.parent = None
                        self.avg = None
                        self.instant = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:chromatic-dispersion'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg is not None:
                            return True

                        if self.instant is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.OpticalChannel.State.ChromaticDispersion']['meta_info']


                class PolarizationModeDispersion(object):
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
                        self.parent = None
                        self.avg = None
                        self.instant = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:polarization-mode-dispersion'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg is not None:
                            return True

                        if self.instant is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.OpticalChannel.State.PolarizationModeDispersion']['meta_info']


                class SecondOrderPolarizationModeDispersion(object):
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
                        self.parent = None
                        self.avg = None
                        self.instant = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:second-order-polarization-mode-dispersion'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg is not None:
                            return True

                        if self.instant is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.OpticalChannel.State.SecondOrderPolarizationModeDispersion']['meta_info']


                class PolarizationDependentLoss(object):
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
                        self.parent = None
                        self.avg = None
                        self.instant = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/openconfig-terminal-device:polarization-dependent-loss'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg is not None:
                            return True

                        if self.instant is not None:
                            return True

                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.openconfig._meta import _openconfig_platform as meta
                        return meta._meta_table['Components.Component.OpticalChannel.State.PolarizationDependentLoss']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/openconfig-terminal-device:state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.chromatic_dispersion is not None and self.chromatic_dispersion._has_data():
                        return True

                    if self.frequency is not None:
                        return True

                    if self.group_id is not None:
                        return True

                    if self.input_power is not None and self.input_power._has_data():
                        return True

                    if self.laser_bias_current is not None and self.laser_bias_current._has_data():
                        return True

                    if self.line_port is not None:
                        return True

                    if self.operational_mode is not None:
                        return True

                    if self.output_power is not None and self.output_power._has_data():
                        return True

                    if self.polarization_dependent_loss is not None and self.polarization_dependent_loss._has_data():
                        return True

                    if self.polarization_mode_dispersion is not None and self.polarization_mode_dispersion._has_data():
                        return True

                    if self.second_order_polarization_mode_dispersion is not None and self.second_order_polarization_mode_dispersion._has_data():
                        return True

                    if self.target_output_power is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.openconfig._meta import _openconfig_platform as meta
                    return meta._meta_table['Components.Component.OpticalChannel.State']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/openconfig-terminal-device:optical-channel'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.config is not None and self.config._has_data():
                    return True

                if self.state is not None and self.state._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.openconfig._meta import _openconfig_platform as meta
                return meta._meta_table['Components.Component.OpticalChannel']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/openconfig-platform:components/openconfig-platform:component[openconfig-platform:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.name is not None:
                return True

            if self.config is not None and self.config._has_data():
                return True

            if self.optical_channel is not None and self.optical_channel._has_data():
                return True

            if self.properties is not None and self.properties._has_data():
                return True

            if self.state is not None and self.state._has_data():
                return True

            if self.subcomponents is not None and self.subcomponents._has_data():
                return True

            if self.transceiver is not None and self.transceiver._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.openconfig._meta import _openconfig_platform as meta
            return meta._meta_table['Components.Component']['meta_info']

    @property
    def _common_path(self):

        return '/openconfig-platform:components'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.component is not None:
            for child_ref in self.component:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_platform as meta
        return meta._meta_table['Components']['meta_info']


