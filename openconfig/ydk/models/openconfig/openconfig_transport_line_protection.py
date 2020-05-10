""" openconfig_transport_line_protection 

This model describes configuration and operational state data
for optical line protection elements, deployed as part of a
transport line system. An Automatic Protection Switch (APS)
is typically installed in the same device as the amplifiers
and wave\-router, however an APS can also be a standalone
device. In both scenarios, it serves the same purpose of
providing protection using two dark fiber pairs to ensure the
amplifiers can still receive a signal if one of the two fiber
pairs is broken. The APS port details and directionality are
shown below. The three major attributes, together with their
modifiers, define the behavior of the APS and can be prioritized
in the descending order as shown in the following table

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/optical-transport-line-protection", pref="openconfig-transport-line-protection", tag="openconfig-transport-line-protection:APS_PATHS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(APSPATHS, self).__init__(ns, pref, tag)



class Aps(_Entity_):
    """
    Top level grouping for automatic protection switch data
    
    .. attribute:: aps_modules
    
    	Enclosing container for list of automatic protection switch modules
    	**type**\:  :py:class:`ApsModules <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules>`
    
    

    """

    _prefix = 'oc-line-protect'
    _revision = '2018-11-21'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Aps, self).__init__()
        self._top_entity = None

        self.yang_name = "aps"
        self.yang_parent_name = "openconfig-transport-line-protection"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("aps-modules", ("aps_modules", Aps.ApsModules))])
        self._leafs = OrderedDict()

        self.aps_modules = Aps.ApsModules()
        self.aps_modules.parent = self
        self._children_name_map["aps_modules"] = "aps-modules"
        self._segment_path = lambda: "openconfig-transport-line-protection:aps"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Aps, [], name, value)


    class ApsModules(_Entity_):
        """
        Enclosing container for list of automatic protection
        switch modules
        
        .. attribute:: aps_module
        
        	List of automatic protection switch modules present in the device
        	**type**\: list of  		 :py:class:`ApsModule <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule>`
        
        

        """

        _prefix = 'oc-line-protect'
        _revision = '2018-11-21'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Aps.ApsModules, self).__init__()

            self.yang_name = "aps-modules"
            self.yang_parent_name = "aps"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("aps-module", ("aps_module", Aps.ApsModules.ApsModule))])
            self._leafs = OrderedDict()

            self.aps_module = YList(self)
            self._segment_path = lambda: "aps-modules"
            self._absolute_path = lambda: "openconfig-transport-line-protection:aps/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aps.ApsModules, [], name, value)


        class ApsModule(_Entity_):
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
            
            	**config**\: False
            
            .. attribute:: ports
            
            	Top level grouping for automatic protection switch ports
            	**type**\:  :py:class:`Ports <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports>`
            
            

            """

            _prefix = 'oc-line-protect'
            _revision = '2018-11-21'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Aps.ApsModules.ApsModule, self).__init__()

                self.yang_name = "aps-module"
                self.yang_parent_name = "aps-modules"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Config)), ("state", ("state", Aps.ApsModules.ApsModule.State)), ("ports", ("ports", Aps.ApsModules.ApsModule.Ports))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.config = Aps.ApsModules.ApsModule.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Aps.ApsModules.ApsModule.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.ports = Aps.ApsModules.ApsModule.Ports()
                self.ports.parent = self
                self._children_name_map["ports"] = "ports"
                self._segment_path = lambda: "aps-module" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "openconfig-transport-line-protection:aps/aps-modules/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aps.ApsModules.ApsModule, ['name'], name, value)


            class Config(_Entity_):
                """
                Configuration data for an automatic protection
                switch module
                
                .. attribute:: name
                
                	Reference to the component name (in the platform model) corresponding to this automatic protection switch module in the device
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                .. attribute:: revertive
                
                	Revertive behavior of the module. If True, then automatically revert after protection switch once the fault is restored. This leaf is not valid when the relative\-switch\-threshold is in effect
                	**type**\: bool
                
                .. attribute:: wait_to_restore_time
                
                	The time that must elapse before an APS path that has recovered from an signal failure (SF) or signal degradation (SD) condition can be used again to transport the normal traffic signal. During this time period, an SF or SD condition shall override the wait\-to\-restore time period. This leaf can only take effect when the revertive leaf equals true
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                .. attribute:: hold_off_time
                
                	The time delay between the declaration of an SF or SD condition and the initiation of the protection switching algorithm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                .. attribute:: primary_switch_threshold
                
                	The threshold at which the primary line port will switch to the opposite line port in increments of 0.01 dBm. If the hardware supports only one switch threshold for primary and and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit. When the relative switch threshold is enabled, i.e. set to a non\-zero value, the primary switch threshold will be overridden
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: primary_switch_hysteresis
                
                	The delta in dB between the primary\-switch\-threshold and the signal received on the primary APS\_PATH before initiating a switch from the secondary APS\_PATH to the primary APS\_PATH, in order to prevent toggling between ports when an input signal is very close to the threshold. A zero value means the switch hysteresis is disabled
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                	**default value**\: 0
                
                .. attribute:: secondary_switch_threshold
                
                	The threshold at which the secondary line port will switch to the opposite line port in increments of 0.01 dBm. If the hardware supports only one switch threshold for primary and and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit. When the relative switch threshold is enabled, i.e. set to a non\-zero value, the secondary switch threshold will be overridden
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dBm
                
                .. attribute:: relative_switch_threshold
                
                	The delta threshold in dB at which the current line port will switch to the opposite line port. It can be set to the value of 0dB. When set to 0dB, the threshold is ignored and the system automatically applies the primary and secondary switch thresholds. When set to a non\-zero value, it overrides the primary and secondary switch thresholds
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                	**default value**\: 0
                
                .. attribute:: relative_switch_threshold_offset
                
                	The offset of the relative switch threshold that compensates the normal difference of receiving power between the primary and secondary line ports. A negative offset corresponds to the situation where the secondary line port receives a higher power than the primary line port in normal condition, and a positive offset means the opposite. The offset will only work when the relative switch threshold is set to a non\-zero value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: dB
                
                	**default value**\: 0
                
                .. attribute:: force_to_port
                
                	Explicitly set the switch to stay on a port regardless of its operational condition
                	**type**\:  :py:class:`ForceToPort <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Config.ForceToPort>`
                
                	**default value**\: NONE
                
                

                """

                _prefix = 'oc-line-protect'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Aps.ApsModules.ApsModule.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "aps-module"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('revertive', (YLeaf(YType.boolean, 'revertive'), ['bool'])),
                        ('wait_to_restore_time', (YLeaf(YType.uint32, 'wait-to-restore-time'), ['int'])),
                        ('hold_off_time', (YLeaf(YType.uint32, 'hold-off-time'), ['int'])),
                        ('primary_switch_threshold', (YLeaf(YType.str, 'primary-switch-threshold'), ['Decimal64'])),
                        ('primary_switch_hysteresis', (YLeaf(YType.str, 'primary-switch-hysteresis'), ['Decimal64'])),
                        ('secondary_switch_threshold', (YLeaf(YType.str, 'secondary-switch-threshold'), ['Decimal64'])),
                        ('relative_switch_threshold', (YLeaf(YType.str, 'relative-switch-threshold'), ['Decimal64'])),
                        ('relative_switch_threshold_offset', (YLeaf(YType.str, 'relative-switch-threshold-offset'), ['Decimal64'])),
                        ('force_to_port', (YLeaf(YType.enumeration, 'force-to-port'), [('ydk.models.openconfig.openconfig_transport_line_protection', 'Aps', 'ApsModules.ApsModule.Config.ForceToPort')])),
                    ])
                    self.name = None
                    self.revertive = None
                    self.wait_to_restore_time = None
                    self.hold_off_time = None
                    self.primary_switch_threshold = None
                    self.primary_switch_hysteresis = None
                    self.secondary_switch_threshold = None
                    self.relative_switch_threshold = None
                    self.relative_switch_threshold_offset = None
                    self.force_to_port = None
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aps.ApsModules.ApsModule.Config, ['name', 'revertive', 'wait_to_restore_time', 'hold_off_time', 'primary_switch_threshold', 'primary_switch_hysteresis', 'secondary_switch_threshold', 'relative_switch_threshold', 'relative_switch_threshold_offset', 'force_to_port'], name, value)

                class ForceToPort(Enum):
                    """
                    ForceToPort (Enum Class)

                    Explicitly set the switch to stay on a port regardless of

                    its operational condition

                    .. data:: NONE = 0

                    	Do not force the switch to stay on any line port

                    .. data:: PRIMARY = 1

                    	Force the switch to stay on the primary line port

                    .. data:: SECONDARY = 2

                    	Force the switch to stay on the secondary line port

                    """

                    NONE = Enum.YLeaf(0, "NONE")

                    PRIMARY = Enum.YLeaf(1, "PRIMARY")

                    SECONDARY = Enum.YLeaf(2, "SECONDARY")




            class State(_Entity_):
                """
                Operational state data for an automatic protection
                switch module
                
                .. attribute:: name
                
                	Reference to the component name (in the platform model) corresponding to this automatic protection switch module in the device
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
                
                	**config**\: False
                
                .. attribute:: revertive
                
                	Revertive behavior of the module. If True, then automatically revert after protection switch once the fault is restored. This leaf is not valid when the relative\-switch\-threshold is in effect
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: wait_to_restore_time
                
                	The time that must elapse before an APS path that has recovered from an signal failure (SF) or signal degradation (SD) condition can be used again to transport the normal traffic signal. During this time period, an SF or SD condition shall override the wait\-to\-restore time period. This leaf can only take effect when the revertive leaf equals true
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: milliseconds
                
                .. attribute:: hold_off_time
                
                	The time delay between the declaration of an SF or SD condition and the initiation of the protection switching algorithm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: milliseconds
                
                .. attribute:: primary_switch_threshold
                
                	The threshold at which the primary line port will switch to the opposite line port in increments of 0.01 dBm. If the hardware supports only one switch threshold for primary and and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit. When the relative switch threshold is enabled, i.e. set to a non\-zero value, the primary switch threshold will be overridden
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                	**units**\: dBm
                
                .. attribute:: primary_switch_hysteresis
                
                	The delta in dB between the primary\-switch\-threshold and the signal received on the primary APS\_PATH before initiating a switch from the secondary APS\_PATH to the primary APS\_PATH, in order to prevent toggling between ports when an input signal is very close to the threshold. A zero value means the switch hysteresis is disabled
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                	**units**\: dB
                
                	**default value**\: 0
                
                .. attribute:: secondary_switch_threshold
                
                	The threshold at which the secondary line port will switch to the opposite line port in increments of 0.01 dBm. If the hardware supports only one switch threshold for primary and and secondary ports then it is recommended to set both primary\-switch\-threshold and secondary\-switch\-threshold to the same value to be explicit. When the relative switch threshold is enabled, i.e. set to a non\-zero value, the secondary switch threshold will be overridden
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                	**units**\: dBm
                
                .. attribute:: relative_switch_threshold
                
                	The delta threshold in dB at which the current line port will switch to the opposite line port. It can be set to the value of 0dB. When set to 0dB, the threshold is ignored and the system automatically applies the primary and secondary switch thresholds. When set to a non\-zero value, it overrides the primary and secondary switch thresholds
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                	**units**\: dB
                
                	**default value**\: 0
                
                .. attribute:: relative_switch_threshold_offset
                
                	The offset of the relative switch threshold that compensates the normal difference of receiving power between the primary and secondary line ports. A negative offset corresponds to the situation where the secondary line port receives a higher power than the primary line port in normal condition, and a positive offset means the opposite. The offset will only work when the relative switch threshold is set to a non\-zero value
                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**config**\: False
                
                	**units**\: dB
                
                	**default value**\: 0
                
                .. attribute:: force_to_port
                
                	Explicitly set the switch to stay on a port regardless of its operational condition
                	**type**\:  :py:class:`ForceToPort <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.State.ForceToPort>`
                
                	**config**\: False
                
                	**default value**\: NONE
                
                .. attribute:: active_path
                
                	Indicates which line path on the protection switch is currently the active path connected to the common port
                	**type**\:  :py:class:`APSPATHS <ydk.models.openconfig.openconfig_transport_line_protection.APSPATHS>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-line-protect'
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Aps.ApsModules.ApsModule.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "aps-module"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('revertive', (YLeaf(YType.boolean, 'revertive'), ['bool'])),
                        ('wait_to_restore_time', (YLeaf(YType.uint32, 'wait-to-restore-time'), ['int'])),
                        ('hold_off_time', (YLeaf(YType.uint32, 'hold-off-time'), ['int'])),
                        ('primary_switch_threshold', (YLeaf(YType.str, 'primary-switch-threshold'), ['Decimal64'])),
                        ('primary_switch_hysteresis', (YLeaf(YType.str, 'primary-switch-hysteresis'), ['Decimal64'])),
                        ('secondary_switch_threshold', (YLeaf(YType.str, 'secondary-switch-threshold'), ['Decimal64'])),
                        ('relative_switch_threshold', (YLeaf(YType.str, 'relative-switch-threshold'), ['Decimal64'])),
                        ('relative_switch_threshold_offset', (YLeaf(YType.str, 'relative-switch-threshold-offset'), ['Decimal64'])),
                        ('force_to_port', (YLeaf(YType.enumeration, 'force-to-port'), [('ydk.models.openconfig.openconfig_transport_line_protection', 'Aps', 'ApsModules.ApsModule.State.ForceToPort')])),
                        ('active_path', (YLeaf(YType.identityref, 'active-path'), [('ydk.models.openconfig.openconfig_transport_line_protection', 'APSPATHS')])),
                    ])
                    self.name = None
                    self.revertive = None
                    self.wait_to_restore_time = None
                    self.hold_off_time = None
                    self.primary_switch_threshold = None
                    self.primary_switch_hysteresis = None
                    self.secondary_switch_threshold = None
                    self.relative_switch_threshold = None
                    self.relative_switch_threshold_offset = None
                    self.force_to_port = None
                    self.active_path = None
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aps.ApsModules.ApsModule.State, ['name', 'revertive', 'wait_to_restore_time', 'hold_off_time', 'primary_switch_threshold', 'primary_switch_hysteresis', 'secondary_switch_threshold', 'relative_switch_threshold', 'relative_switch_threshold_offset', 'force_to_port', 'active_path'], name, value)

                class ForceToPort(Enum):
                    """
                    ForceToPort (Enum Class)

                    Explicitly set the switch to stay on a port regardless of

                    its operational condition

                    .. data:: NONE = 0

                    	Do not force the switch to stay on any line port

                    .. data:: PRIMARY = 1

                    	Force the switch to stay on the primary line port

                    .. data:: SECONDARY = 2

                    	Force the switch to stay on the secondary line port

                    """

                    NONE = Enum.YLeaf(0, "NONE")

                    PRIMARY = Enum.YLeaf(1, "PRIMARY")

                    SECONDARY = Enum.YLeaf(2, "SECONDARY")




            class Ports(_Entity_):
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
                _revision = '2018-11-21'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Aps.ApsModules.ApsModule.Ports, self).__init__()

                    self.yang_name = "ports"
                    self.yang_parent_name = "aps-module"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("line-primary-in", ("line_primary_in", Aps.ApsModules.ApsModule.Ports.LinePrimaryIn)), ("line-primary-out", ("line_primary_out", Aps.ApsModules.ApsModule.Ports.LinePrimaryOut)), ("line-secondary-in", ("line_secondary_in", Aps.ApsModules.ApsModule.Ports.LineSecondaryIn)), ("line-secondary-out", ("line_secondary_out", Aps.ApsModules.ApsModule.Ports.LineSecondaryOut)), ("common-in", ("common_in", Aps.ApsModules.ApsModule.Ports.CommonIn)), ("common-output", ("common_output", Aps.ApsModules.ApsModule.Ports.CommonOutput))])
                    self._leafs = OrderedDict()

                    self.line_primary_in = Aps.ApsModules.ApsModule.Ports.LinePrimaryIn()
                    self.line_primary_in.parent = self
                    self._children_name_map["line_primary_in"] = "line-primary-in"

                    self.line_primary_out = Aps.ApsModules.ApsModule.Ports.LinePrimaryOut()
                    self.line_primary_out.parent = self
                    self._children_name_map["line_primary_out"] = "line-primary-out"

                    self.line_secondary_in = Aps.ApsModules.ApsModule.Ports.LineSecondaryIn()
                    self.line_secondary_in.parent = self
                    self._children_name_map["line_secondary_in"] = "line-secondary-in"

                    self.line_secondary_out = Aps.ApsModules.ApsModule.Ports.LineSecondaryOut()
                    self.line_secondary_out.parent = self
                    self._children_name_map["line_secondary_out"] = "line-secondary-out"

                    self.common_in = Aps.ApsModules.ApsModule.Ports.CommonIn()
                    self.common_in.parent = self
                    self._children_name_map["common_in"] = "common-in"

                    self.common_output = Aps.ApsModules.ApsModule.Ports.CommonOutput()
                    self.common_output.parent = self
                    self._children_name_map["common_output"] = "common-output"
                    self._segment_path = lambda: "ports"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aps.ApsModules.ApsModule.Ports, [], name, value)


                class LinePrimaryIn(_Entity_):
                    """
                    Container for information related to the line primary
                    input port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line primary input port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line primary input port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn, self).__init__()

                        self.yang_name = "line-primary-in"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State))])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "line-primary-in"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn, [], name, value)


                    class Config(_Entity_):
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
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "line-primary-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.Config, ['enabled', 'target_attenuation'], name, value)



                    class State(_Entity_):
                        """
                        State data for the line primary input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical input power of this port in units of 0.01dBm. Optical input power represents the signal traversing from an external destination into the module. The power is measured before any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "line-primary-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower))])
                            self._leafs = OrderedDict([
                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                                ('attenuation', (YLeaf(YType.str, 'attenuation'), ['Decimal64'])),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State, ['enabled', 'target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(_Entity_):
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
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
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
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "optical-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryIn.State.OpticalPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





                class LinePrimaryOut(_Entity_):
                    """
                    Container for information related to the line primary
                    output port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line primary output port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line primary output port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut, self).__init__()

                        self.yang_name = "line-primary-out"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State))])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "line-primary-out"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for the line primary output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "line-primary-out"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                            ])
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.Config, ['target_attenuation'], name, value)



                    class State(_Entity_):
                        """
                        State data for the line primary output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical output power of this port in units of 0.01dBm. Optical output power represents the signal traversing from the module to an external destination. The power is measured after any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "line-primary-out"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower))])
                            self._leafs = OrderedDict([
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                                ('attenuation', (YLeaf(YType.str, 'attenuation'), ['Decimal64'])),
                            ])
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State, ['target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(_Entity_):
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
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
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
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "optical-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LinePrimaryOut.State.OpticalPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





                class LineSecondaryIn(_Entity_):
                    """
                    Container for information related to the line secondary
                    input port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line secondary input port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line secondary input port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn, self).__init__()

                        self.yang_name = "line-secondary-in"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State))])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "line-secondary-in"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn, [], name, value)


                    class Config(_Entity_):
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
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "line-secondary-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.Config, ['enabled', 'target_attenuation'], name, value)



                    class State(_Entity_):
                        """
                        State data for the line secondary input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical input power of this port in units of 0.01dBm. Optical input power represents the signal traversing from an external destination into the module. The power is measured before any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "line-secondary-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower))])
                            self._leafs = OrderedDict([
                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                                ('attenuation', (YLeaf(YType.str, 'attenuation'), ['Decimal64'])),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State, ['enabled', 'target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(_Entity_):
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
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
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
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "optical-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryIn.State.OpticalPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





                class LineSecondaryOut(_Entity_):
                    """
                    Container for information related to the line secondary
                    output port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line secondary output port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line secondary output port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut, self).__init__()

                        self.yang_name = "line-secondary-out"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State))])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "line-secondary-out"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for the line secondary output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "line-secondary-out"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                            ])
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.Config, ['target_attenuation'], name, value)



                    class State(_Entity_):
                        """
                        State data for the line secondary output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical output power of this port in units of 0.01dBm. Optical output power represents the signal traversing from the module to an external destination. The power is measured after any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "line-secondary-out"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower))])
                            self._leafs = OrderedDict([
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                                ('attenuation', (YLeaf(YType.str, 'attenuation'), ['Decimal64'])),
                            ])
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State, ['target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(_Entity_):
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
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
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
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "optical-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.LineSecondaryOut.State.OpticalPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





                class CommonIn(_Entity_):
                    """
                    Container for information related to the line common
                    input port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line common input port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonIn.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line common input port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonIn.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Aps.ApsModules.ApsModule.Ports.CommonIn, self).__init__()

                        self.yang_name = "common-in"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.CommonIn.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.CommonIn.State))])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.CommonIn.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Aps.ApsModules.ApsModule.Ports.CommonIn.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "common-in"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonIn, [], name, value)


                    class Config(_Entity_):
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
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.CommonIn.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "common-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonIn.Config, ['enabled', 'target_attenuation'], name, value)



                    class State(_Entity_):
                        """
                        State data for the line common input port
                        
                        .. attribute:: enabled
                        
                        	This leaf contains the configured, desired state of the port. Disabling the port turns off alarm reporting for the port
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: true
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical input power of this port in units of 0.01dBm. Optical input power represents the signal traversing from an external destination into the module. The power is measured before any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.CommonIn.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "common-in"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower))])
                            self._leafs = OrderedDict([
                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                                ('attenuation', (YLeaf(YType.str, 'attenuation'), ['Decimal64'])),
                            ])
                            self.enabled = None
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonIn.State, ['enabled', 'target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(_Entity_):
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
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
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
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "optical-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonIn.State.OpticalPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)





                class CommonOutput(_Entity_):
                    """
                    Container for information related to the line common
                    output port
                    
                    .. attribute:: config
                    
                    	Configuration data for the line common output port
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonOutput.Config>`
                    
                    .. attribute:: state
                    
                    	State data for the line common output port
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonOutput.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-line-protect'
                    _revision = '2018-11-21'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Aps.ApsModules.ApsModule.Ports.CommonOutput, self).__init__()

                        self.yang_name = "common-output"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Aps.ApsModules.ApsModule.Ports.CommonOutput.Config)), ("state", ("state", Aps.ApsModules.ApsModule.Ports.CommonOutput.State))])
                        self._leafs = OrderedDict()

                        self.config = Aps.ApsModules.ApsModule.Ports.CommonOutput.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Aps.ApsModules.ApsModule.Ports.CommonOutput.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "common-output"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonOutput, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for the line common output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**units**\: dB
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.CommonOutput.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "common-output"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                            ])
                            self.target_attenuation = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonOutput.Config, ['target_attenuation'], name, value)



                    class State(_Entity_):
                        """
                        State data for the line common output port
                        
                        .. attribute:: target_attenuation
                        
                        	Target attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: attenuation
                        
                        	The attenuation of the variable optical attenuator associated with the port in increments of 0.01 dB
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        	**config**\: False
                        
                        	**units**\: dB
                        
                        .. attribute:: optical_power
                        
                        	The optical output power of this port in units of 0.01dBm. Optical output power represents the signal traversing from the module to an external destination. The power is measured after any attenuation. If avg/min/max statistics are not supported, the target is expected to just supply the instant value
                        	**type**\:  :py:class:`OpticalPower <ydk.models.openconfig.openconfig_transport_line_protection.Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-line-protect'
                        _revision = '2018-11-21'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Aps.ApsModules.ApsModule.Ports.CommonOutput.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "common-output"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("optical-power", ("optical_power", Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower))])
                            self._leafs = OrderedDict([
                                ('target_attenuation', (YLeaf(YType.str, 'target-attenuation'), ['Decimal64'])),
                                ('attenuation', (YLeaf(YType.str, 'attenuation'), ['Decimal64'])),
                            ])
                            self.target_attenuation = None
                            self.attenuation = None

                            self.optical_power = Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower()
                            self.optical_power.parent = self
                            self._children_name_map["optical_power"] = "optical-power"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonOutput.State, ['target_attenuation', 'attenuation'], name, value)


                        class OpticalPower(_Entity_):
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
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: avg
                            
                            	The arithmetic mean value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: min
                            
                            	The minimum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: max
                            
                            	The maximum value of the statistic over the time interval
                            	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                            
                            	**range:** \-92233720368547758.08..92233720368547758.07
                            
                            	**config**\: False
                            
                            	**units**\: dBm
                            
                            .. attribute:: interval
                            
                            	If supported by the system, this reports the time interval over which the min/max/average statistics are computed by the system
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: min_time
                            
                            	The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: max_time
                            
                            	The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to  the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-line-protect'
                            _revision = '2018-11-21'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower, self).__init__()

                                self.yang_name = "optical-power"
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
                                    ('interval', (YLeaf(YType.uint64, 'interval'), ['int'])),
                                    ('min_time', (YLeaf(YType.uint64, 'min-time'), ['int'])),
                                    ('max_time', (YLeaf(YType.uint64, 'max-time'), ['int'])),
                                ])
                                self.instant = None
                                self.avg = None
                                self.min = None
                                self.max = None
                                self.interval = None
                                self.min_time = None
                                self.max_time = None
                                self._segment_path = lambda: "optical-power"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aps.ApsModules.ApsModule.Ports.CommonOutput.State.OpticalPower, ['instant', 'avg', 'min', 'max', 'interval', 'min_time', 'max_time'], name, value)







    def clone_ptr(self):
        self._top_entity = Aps()
        return self._top_entity



class PRIMARY(APSPATHS):
    """
    The primary line path connected to an automatic protection
    switch port indicating the primary/preferred path
    
    

    """

    _prefix = 'oc-line-protect'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/optical-transport-line-protection", pref="openconfig-transport-line-protection", tag="openconfig-transport-line-protection:PRIMARY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(PRIMARY, self).__init__(ns, pref, tag)



class SECONDARY(APSPATHS):
    """
    The secondary line path connected to an automatic protection
    switch port indicating the secondary path
    
    

    """

    _prefix = 'oc-line-protect'
    _revision = '2018-11-21'

    def __init__(self, ns="http://openconfig.net/yang/optical-transport-line-protection", pref="openconfig-transport-line-protection", tag="openconfig-transport-line-protection:SECONDARY"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(SECONDARY, self).__init__(ns, pref, tag)



