""" openconfig_transport_line_protection 

This model describes configuration and operational state data
for optical line protection elements, deployed as part of a
transport line system. An Automatic Protection Switch (APS)
is typically installed in the same device as the amplifiers
and wave\-router, however an APS can also be a standalone
device. In both scenarios, it serves the same purpose of
providing protection using two dark fiber pairs to ensure the
amplifiers can still receive a signal if one of the two fiber
pairs is broken.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class APSPATHS(Identity):
    """
    Base identity for identifying the line paths on an
    automatic protection switch
    
    

    """

    _prefix = 'oc-line-protect'
    _revision = '2017-03-28'

    def __init__(self):
        super(APSPATHS, self).__init__("http://openconfig.net/yang/optical-transport-line-protection", "openconfig-transport-line-protection", "openconfig-transport-line-protection:APS_PATHS")


class Aps(Entity):
    """
    Top level grouping for automatic protection switch data
    
    .. attribute:: aps_modules
    
    	Enclosing container for list of automatic protection switch modules
    	**type**\:  :py:class:`ApsModules <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules>`
    
    

    """

    _prefix = 'oc-line-protect'
    _revision = '2017-03-28'

    def __init__(self):
        super(Aps, self).__init__()
        self._top_entity = None

        self.yang_name = "aps"
        self.yang_parent_name = "openconfig-transport-line-protection"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("aps-modules", ("aps_modules", Aps.ApsModules))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.aps_modules = Aps.ApsModules()
        self.aps_modules.parent = self
        self._children_name_map["aps_modules"] = "aps-modules"
        self._children_yang_names.add("aps-modules")
        self._segment_path = lambda: "openconfig-transport-line-protection:aps"


    class ApsModules(Entity):
        """
        Enclosing container for list of automatic protection
        switch modules
        
        .. attribute:: aps_module
        
        	List of automatic protection switch modules present in the device
        	**type**\: list of  		 :py:class:`ApsModule <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule>`
        
        

        """

        _prefix = 'oc-line-protect'
        _revision = '2017-03-28'

        def __init__(self):
            super(Aps.ApsModules, self).__init__()

            self.yang_name = "aps-modules"
            self.yang_parent_name = "aps"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("aps-module", ("aps_module", Aps.ApsModules.ApsModule))])
            self._leafs = OrderedDict()

            self.aps_module = YList(self)
            self._segment_path = lambda: "aps-modules"
            self._absolute_path = lambda: "openconfig-transport-line-protection:aps/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aps.ApsModules, [], name, value)


        class ApsModule(Entity):
            """
            List of automatic protection switch modules present
            in the device
            
            .. attribute:: name  (key)
            
            	Reference to the config name list key
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Config>`
            
            .. attribute:: config
            
            	Configuration data for an automatic protection switch module
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Config>`
            
            .. attribute:: state
            
            	Operational state data for an automatic protection switch module
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.State>`
            
            .. attribute:: ports
            
            	Top level grouping for automatic protection switch ports
            	**type**\:  :py:class:`Ports <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports>`
            
            

            """

            _prefix = 'oc-line-protect'
            _revision = '2017-03-28'

            def __init__(self):
                super(Aps.ApsModules.ApsModule, self).__init__()

                self.yang_name = "aps-module"
                self.yang_parent_name = "aps-modules"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Config)), ("state", ("state", Aps.ApsModules.ApsModule.State)), ("ports", ("ports", Aps.ApsModules.ApsModule.Ports))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.name = None

                self.config = Aps.ApsModules.ApsModule.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Aps.ApsModules.ApsModule.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.ports = Aps.ApsModules.ApsModule.Ports()
                self.ports.parent = self
                self._children_name_map["ports"] = "ports"
                self._children_yang_names.add("ports")
                self._segment_path = lambda: "aps-module" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "openconfig-transport-line-protection:aps/aps-modules/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aps.ApsModules.ApsModule, ['name'], name, value)


            class Config(Entity):
                """
                Configuration data for an automatic protection
                switch module
                
                .. attribute:: name
                
                	Reference to the component name (in the platform model) corresponding to this automatic protection switch module in the device
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                .. attribute:: revertive
                
                	Revertive behavior of the module. If True, then automatically revert after protection switch once the fault is restored
                	**type**\: bool
                
                .. attribute:: primary_switch_threshold
                
                	The threshold at which the primary line port will switch to the opposite line port in increments of 0.01 dBm. If the hardware supports only one switch threshold for primary and and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: primary_switch_hysteresis
                
                	The delta in 0.01 dB between the primary\-switch\-threshold and the signal received before initiating a reversion in order to prevent toggling between ports when an input signal is very close to threshold. If the hardware supports only one switch hysteresis for primary and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                .. attribute:: secondary_switch_threshold
                
                	The threshold at which the secondary line port will switch to the opposite line port in increments of 0.01 dBm. If the hardware supports only one switch threshold for primary and and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: secondary_switch_hysteresis
                
                	The delta in 0.01 dB between the secondary\-switch\-threshold and the signal received before initiating a reversion in order to prevent toggling between ports when an input signal is very close to threshold. If the hardware supports only one switch hysteresis for primary and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                

                """

                _prefix = 'oc-line-protect'
                _revision = '2017-03-28'

                def __init__(self):
                    super(Aps.ApsModules.ApsModule.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "aps-module"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('revertive', YLeaf(YType.boolean, 'revertive')),
                        ('primary_switch_threshold', YLeaf(YType.str, 'primary-switch-threshold')),
                        ('primary_switch_hysteresis', YLeaf(YType.str, 'primary-switch-hysteresis')),
                        ('secondary_switch_threshold', YLeaf(YType.str, 'secondary-switch-threshold')),
                        ('secondary_switch_hysteresis', YLeaf(YType.str, 'secondary-switch-hysteresis')),
                    ])
                    self.name = None
                    self.revertive = None
                    self.primary_switch_threshold = None
                    self.primary_switch_hysteresis = None
                    self.secondary_switch_threshold = None
                    self.secondary_switch_hysteresis = None
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Aps.ApsModules.ApsModule.Config, ['name', 'revertive', 'primary_switch_threshold', 'primary_switch_hysteresis', 'secondary_switch_threshold', 'secondary_switch_hysteresis'], name, value)


            class State(Entity):
                """
                Operational state data for an automatic protection
                switch module
                
                .. attribute:: name
                
                	Reference to the component name (in the platform model) corresponding to this automatic protection switch module in the device
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                .. attribute:: revertive
                
                	Revertive behavior of the module. If True, then automatically revert after protection switch once the fault is restored
                	**type**\: bool
                
                .. attribute:: primary_switch_threshold
                
                	The threshold at which the primary line port will switch to the opposite line port in increments of 0.01 dBm. If the hardware supports only one switch threshold for primary and and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: primary_switch_hysteresis
                
                	The delta in 0.01 dB between the primary\-switch\-threshold and the signal received before initiating a reversion in order to prevent toggling between ports when an input signal is very close to threshold. If the hardware supports only one switch hysteresis for primary and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                .. attribute:: secondary_switch_threshold
                
                	The threshold at which the secondary line port will switch to the opposite line port in increments of 0.01 dBm. If the hardware supports only one switch threshold for primary and and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: secondary_switch_hysteresis
                
                	The delta in 0.01 dB between the secondary\-switch\-threshold and the signal received before initiating a reversion in order to prevent toggling between ports when an input signal is very close to threshold. If the hardware supports only one switch hysteresis for primary and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                .. attribute:: active_path
                
                	Indicates which line path on the automatic protection switch is currently the active path connected to the common port
                	**type**\:  :py:class:`APSPATHS <ydk.models.openconfig.openconfig_transport_line_protection.APSPATHS>`
                
                

                """

                _prefix = 'oc-line-protect'
                _revision = '2017-03-28'

                def __init__(self):
                    super(Aps.ApsModules.ApsModule.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "aps-module"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('revertive', YLeaf(YType.boolean, 'revertive')),
                        ('primary_switch_threshold', YLeaf(YType.str, 'primary-switch-threshold')),
                        ('primary_switch_hysteresis', YLeaf(YType.str, 'primary-switch-hysteresis')),
                        ('secondary_switch_threshold', YLeaf(YType.str, 'secondary-switch-threshold')),
                        ('secondary_switch_hysteresis', YLeaf(YType.str, 'secondary-switch-hysteresis')),
                        ('active_path', YLeaf(YType.identityref, 'active-path')),
                    ])
                    self.name = None
                    self.revertive = None
                    self.primary_switch_threshold = None
                    self.primary_switch_hysteresis = None
                    self.secondary_switch_threshold = None
                    self.secondary_switch_hysteresis = None
                    self.active_path = None
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Aps.ApsModules.ApsModule.State, ['name', 'revertive', 'primary_switch_threshold', 'primary_switch_hysteresis', 'secondary_switch_threshold', 'secondary_switch_hysteresis', 'active_path'], name, value)


            class Ports(Entity):
                """
                Top level grouping for automatic protection switch ports
                
                .. attribute:: line_primary_in
                
                	Container for information related to the line primary input port
                	**type**\:  :py:class:`LinePrimaryIn <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryIn>`
                
                .. attribute:: line_primary_out
                
                	Container for information related to the line primary output port
                	**type**\:  :py:class:`LinePrimaryOut <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryOut>`
                
                .. attribute:: line_secondary_in
                
                	Container for information related to the line secondary input port
                	**type**\:  :py:class:`LineSecondaryIn <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryIn>`
                
                .. attribute:: line_secondary_out
                
                	Container for information related to the line secondary output port
                	**type**\:  :py:class:`LineSecondaryOut <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryOut>`
                
                .. attribute:: common_in
                
                	Container for information related to the line common input port
                	**type**\:  :py:class:`CommonIn <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonIn>`
                
                .. attribute:: common_output
                
                	Container for information related to the line common output port
                	**type**\:  :py:class:`CommonOutput <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonOutput>`
                
                

                """

                _prefix = 'oc-line-protect'
                _revision = '2017-03-28'

                def __init__(self):
                    super(Aps.ApsModules.ApsModule.Ports, self).__init__()

                    self.yang_name = "ports"
                    self.yang_parent_name = "aps-module"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("line-primary-in", ("line_primary_in", Aps.ApsModules.ApsModule.Ports.LinePrimaryIn)), ("line-primary-out", ("line_primary_out", Aps.ApsModules.ApsModule.Ports.LinePrimaryOut)), ("line-secondary-in", ("line_secondary_in", Aps.ApsModules.ApsModule.Ports.LineSecondaryIn)), ("line-secondary-out", ("line_secondary_out", Aps.ApsModules.ApsModule.Ports.LineSecondaryOut)), ("common-in", ("common_in", Aps.ApsModules.ApsModule.Ports.CommonIn)), ("common-output", ("common_output", Aps.ApsModules.ApsModule.Ports.CommonOutput))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.line_primary_in = Aps.ApsModules.ApsModule.Ports.LinePrimaryIn()
                    self.line_primary_in.parent = self
                    self._children_name_map["line_primary_in"] = "line-primary-in"
                    self._children_yang_names.add("line-primary-in")

                    self.line_primary_out = Aps.ApsModules.ApsModule.Ports.LinePrimaryOut()
                    self.line_primary_out.parent = self
                    self._children_name_map["line_primary_out"] = "line-primary-out"
                    self._children_yang_names.add("line-primary-out")

                    self.line_secondary_in = Aps.ApsModules.ApsModule.Ports.LineSecondaryIn()
                    self.line_secondary_in.parent = self
                    self._children_name_map["line_secondary_in"] = "line-secondary-in"
                    self._children_yang_names.add("line-secondary-in")

                    self.line_secondary_out = Aps.ApsModules.ApsModule.Ports.LineSecondaryOut()
                    self.line_secondary_out.parent = self
                    self._children_name_map["line_secondary_out"] = "line-secondary-out"
                    self._children_yang_names.add("line-secondary-out")

                    self.common_in = Aps.ApsModules.ApsModule.Ports.CommonIn()
                    self.common_in.parent = self
                    self._children_name_map["common_in"] = "common-in"
                    self._children_yang_names.add("common-in")

                    self.common_output = Aps.ApsModules.ApsModule.Ports.CommonOutput()
                    self.common_output.parent = self
                    self._children_name_map["common_output"] = "common-output"
                    self._children_yang_names.add("common-output")
                    self._segment_path = lambda: "ports"


                class LinePrimaryIn(Entity):
                    """
                    Container for information related to the line primary
                    input port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line primary input port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line primary input port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State>`
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn, self).__init__()

                        self.yang_name = "line-primary-in"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "line-primary-in"


                    class Config(Entity):
                        """
                        Configuration data for the line primary input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "line-primary-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config, ['enabled', 'target_attenuation'], name, value)


                    class State(Entity):
                        """
                        State data for the line primary input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical input power of this port in units of 0.01dBm. Optical input power represents the signal traversing from an external destination into the module. The power is measured before any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower>`
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "line-primary-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                                ('attenuation', YLeaf(YType.str, 'attenuation')),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._children_yang_names.add("optical-power")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State, ['enabled', 'target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(Entity):
                            """
                            The optical input power of this port in units of
                            0.01dBm. Optical input power represents the signal
                            traversing from an external destination into the module.
                            The power is measured before any attenuation. If avg/min/max
                            statistics are not supported, the target is expected to
                            just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', YLeaf(YType.str, 'instant')),
                                    ('avg', YLeaf(YType.str, 'avg')),
                                    ('min', YLeaf(YType.str, 'min')),
                                    ('max', YLeaf(YType.str, 'max')),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "optical-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower, ['instant', 'avg', 'min', 'max'], name, value)


                class LinePrimaryOut(Entity):
                    """
                    Container for information related to the line primary
                    output port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line primary output port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line primary output port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State>`
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut, self).__init__()

                        self.yang_name = "line-primary-out"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "line-primary-out"


                    class Config(Entity):
                        """
                        Configuration data for the line primary output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "line-primary-out"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                            ])
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config, ['target_attenuation'], name, value)


                    class State(Entity):
                        """
                        State data for the line primary output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical output power of this port in units of 0.01dBm. Optical output power represents the signal traversing from the module to an external destination. The power is measured after any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower>`
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "line-primary-out"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                                ('attenuation', YLeaf(YType.str, 'attenuation')),
                            ])
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._children_yang_names.add("optical-power")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State, ['target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(Entity):
                            """
                            The optical output power of this port in units of
                            0.01dBm. Optical output power represents the signal
                            traversing from the module to an external destination. The
                            power is measured after any attenuation. If avg/min/max
                            statistics are not supported, the target is expected to
                            just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', YLeaf(YType.str, 'instant')),
                                    ('avg', YLeaf(YType.str, 'avg')),
                                    ('min', YLeaf(YType.str, 'min')),
                                    ('max', YLeaf(YType.str, 'max')),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "optical-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower, ['instant', 'avg', 'min', 'max'], name, value)


                class LineSecondaryIn(Entity):
                    """
                    Container for information related to the line secondary
                    input port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line secondary input port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line secondary input port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State>`
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn, self).__init__()

                        self.yang_name = "line-secondary-in"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "line-secondary-in"


                    class Config(Entity):
                        """
                        Configuration data for the line secondary input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "line-secondary-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config, ['enabled', 'target_attenuation'], name, value)


                    class State(Entity):
                        """
                        State data for the line secondary input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical input power of this port in units of 0.01dBm. Optical input power represents the signal traversing from an external destination into the module. The power is measured before any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower>`
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "line-secondary-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                                ('attenuation', YLeaf(YType.str, 'attenuation')),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._children_yang_names.add("optical-power")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State, ['enabled', 'target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(Entity):
                            """
                            The optical input power of this port in units of
                            0.01dBm. Optical input power represents the signal
                            traversing from an external destination into the module.
                            The power is measured before any attenuation. If avg/min/max
                            statistics are not supported, the target is expected to
                            just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', YLeaf(YType.str, 'instant')),
                                    ('avg', YLeaf(YType.str, 'avg')),
                                    ('min', YLeaf(YType.str, 'min')),
                                    ('max', YLeaf(YType.str, 'max')),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "optical-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower, ['instant', 'avg', 'min', 'max'], name, value)


                class LineSecondaryOut(Entity):
                    """
                    Container for information related to the line secondary
                    output port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line secondary output port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line secondary output port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State>`
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut, self).__init__()

                        self.yang_name = "line-secondary-out"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "line-secondary-out"


                    class Config(Entity):
                        """
                        Configuration data for the line secondary output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "line-secondary-out"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                            ])
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config, ['target_attenuation'], name, value)


                    class State(Entity):
                        """
                        State data for the line secondary output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical output power of this port in units of 0.01dBm. Optical output power represents the signal traversing from the module to an external destination. The power is measured after any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower>`
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "line-secondary-out"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                                ('attenuation', YLeaf(YType.str, 'attenuation')),
                            ])
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._children_yang_names.add("optical-power")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State, ['target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(Entity):
                            """
                            The optical output power of this port in units of
                            0.01dBm. Optical output power represents the signal
                            traversing from the module to an external destination. The
                            power is measured after any attenuation. If avg/min/max
                            statistics are not supported, the target is expected to
                            just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', YLeaf(YType.str, 'instant')),
                                    ('avg', YLeaf(YType.str, 'avg')),
                                    ('min', YLeaf(YType.str, 'min')),
                                    ('max', YLeaf(YType.str, 'max')),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "optical-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower, ['instant', 'avg', 'min', 'max'], name, value)


                class CommonIn(Entity):
                    """
                    Container for information related to the line common
                    input port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line common input port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonIn.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line common input port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonIn.State>`
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(Aps.ApsModules.ApsModule.Ports.CommonIn, self).__init__()

                        self.yang_name = "common-in"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.CommonIn.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.CommonIn.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.CommonIn.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Aps.ApsModules.ApsModule.Ports.CommonIn.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "common-in"


                    class Config(Entity):
                        """
                        Configuration data for the line common input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.CommonIn.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "common-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonIn.Config, ['enabled', 'target_attenuation'], name, value)


                    class State(Entity):
                        """
                        State data for the line common input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical input power of this port in units of 0.01dBm. Optical input power represents the signal traversing from an external destination into the module. The power is measured before any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower>`
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.CommonIn.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "common-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                                ('attenuation', YLeaf(YType.str, 'attenuation')),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._children_yang_names.add("optical-power")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonIn.State, ['enabled', 'target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(Entity):
                            """
                            The optical input power of this port in units of
                            0.01dBm. Optical input power represents the signal
                            traversing from an external destination into the module.
                            The power is measured before any attenuation. If avg/min/max
                            statistics are not supported, the target is expected to
                            just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', YLeaf(YType.str, 'instant')),
                                    ('avg', YLeaf(YType.str, 'avg')),
                                    ('min', YLeaf(YType.str, 'min')),
                                    ('max', YLeaf(YType.str, 'max')),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "optical-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower, ['instant', 'avg', 'min', 'max'], name, value)


                class CommonOutput(Entity):
                    """
                    Container for information related to the line common
                    output port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line common output port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonOutput.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line common output port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonOutput.State>`
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2017-03-28'

                    def __init__(self):
                        super(Aps.ApsModules.ApsModule.Ports.CommonOutput, self).__init__()

                        self.yang_name = "common-output"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.CommonOutput.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.CommonOutput.State))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.CommonOutput.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Aps.ApsModules.ApsModule.Ports.CommonOutput.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "common-output"


                    class Config(Entity):
                        """
                        Configuration data for the line common output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.CommonOutput.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "common-output"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                            ])
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonOutput.Config, ['target_attenuation'], name, value)


                    class State(Entity):
                        """
                        State data for the line common output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical output power of this port in units of 0.01dBm. Optical output power represents the signal traversing from the module to an external destination. The power is measured after any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower>`
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2017-03-28'

                        def __init__(self):
                            super(Aps.ApsModules.ApsModule.Ports.CommonOutput.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "common-output"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', YLeaf(YType.str, 'target-attenuation')),
                                ('attenuation', YLeaf(YType.str, 'attenuation')),
                            ])
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._children_yang_names.add("optical-power")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonOutput.State, ['target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(Entity):
                            """
                            The optical output power of this port in units of
                            0.01dBm. Optical output power represents the signal
                            traversing from the module to an external destination. The
                            power is measured after any attenuation. If avg/min/max
                            statistics are not supported, the target is expected to
                            just supply the instant value
                            
                            .. attribute:: instant
                            
                            	The instantaneous value of the statistic
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the sampling period
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**units**\: dBm
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2017-03-28'

                            def __init__(self):
                                super(Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('instant', YLeaf(YType.str, 'instant')),
                                    ('avg', YLeaf(YType.str, 'avg')),
                                    ('min', YLeaf(YType.str, 'min')),
                                    ('max', YLeaf(YType.str, 'max')),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self._segment_path = lambda: "optical-power"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower, ['instant', 'avg', 'min', 'max'], name, value)

    def clone_ptr(self):
        self._top_entity = Aps()
        return self._top_entity

class PRIMARY(Identity):
    """
    The primary line path connected to an automatic protection
    switch port indicating the primary/preferred path
    
    

    """

    _prefix = 'oc-line-protect'
    _revision = '2017-03-28'

    def __init__(self):
        super(PRIMARY, self).__init__("http://openconfig.net/yang/optical-transport-line-protection", "openconfig-transport-line-protection", "openconfig-transport-line-protection:PRIMARY")


class SECONDARY(Identity):
    """
    The secondary line path connected to an automatic protection
    switch port indicating the secondary path
    
    

    """

    _prefix = 'oc-line-protect'
    _revision = '2017-03-28'

    def __init__(self):
        super(SECONDARY, self).__init__("http://openconfig.net/yang/optical-transport-line-protection", "openconfig-transport-line-protection", "openconfig-transport-line-protection:SECONDARY")


