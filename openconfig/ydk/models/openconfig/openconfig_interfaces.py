""" openconfig_interfaces 

Model for managing network interfaces and subinterfaces.  This
module also defines convenience types / groupings for other
models to create references to interfaces\:

 base\-interface\-ref (type) \-  reference to a base interface
 interface\-ref (grouping) \-  container for reference to a
   interface + subinterface
 interface\-ref\-state (grouping) \- container for read\-only
   (opstate) reference to interface + subinterface

This model reuses data items defined in the IETF YANG model for
interfaces described by RFC 7223 with an alternate structure
(particularly for operational state data) and and with
additional configuration items.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Interfaces(Entity):
    """
    Top level container for interfaces, including configuration
    and state data.
    
    .. attribute:: interface
    
    	The list of named interfaces on the device
    	**type**\: list of    :py:class:`Interface <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
    
    

    """

    _prefix = 'oc-if'
    _revision = '2016-05-26'

    def __init__(self):
        super(Interfaces, self).__init__()
        self._top_entity = None

        self.yang_name = "interfaces"
        self.yang_parent_name = "openconfig-interfaces"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"interface" : ("interface", Interfaces.Interface)}

        self.interface = YList(self)
        self._segment_path = lambda: "openconfig-interfaces:interfaces"

    def __setattr__(self, name, value):
        self._perform_setattr(Interfaces, [], name, value)


    class Interface(Entity):
        """
        The list of named interfaces on the device.
        
        .. attribute:: name  <key>
        
        	References the configured name of the interface
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Config>`
        
        .. attribute:: aggregation
        
        	Options for logical interfaces representing aggregates
        	**type**\:   :py:class:`Aggregation <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation>`
        
        .. attribute:: config
        
        	Configurable items at the global, physical interface level
        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Config>`
        
        .. attribute:: ethernet
        
        	Top\-level container for ethernet configuration and state
        	**type**\:   :py:class:`Ethernet <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet>`
        
        .. attribute:: hold_time
        
        	Top\-level container for hold\-time settings to enable dampening advertisements of interface transitions
        	**type**\:   :py:class:`HoldTime <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.HoldTime>`
        
        .. attribute:: routed_vlan
        
        	Top\-level container for routed vlan interfaces.  These logical interfaces are also known as SVI (switched virtual interface), IRB (integrated routing and bridging), RVI (routed VLAN interface)
        	**type**\:   :py:class:`RoutedVlan <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan>`
        
        .. attribute:: sonet
        
        	Data related to SONET/SDH interfaces
        	**type**\:   :py:class:`Sonet <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Sonet>`
        
        .. attribute:: state
        
        	Operational state data at the global interface level
        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.State>`
        
        .. attribute:: subinterfaces
        
        	Enclosing container for the list of subinterfaces associated with a physical interface
        	**type**\:   :py:class:`Subinterfaces <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces>`
        
        

        """

        _prefix = 'oc-if'
        _revision = '2016-05-26'

        def __init__(self):
            super(Interfaces.Interface, self).__init__()

            self.yang_name = "interface"
            self.yang_parent_name = "interfaces"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"aggregation" : ("aggregation", Interfaces.Interface.Aggregation), "config" : ("config", Interfaces.Interface.Config), "ethernet" : ("ethernet", Interfaces.Interface.Ethernet), "hold-time" : ("hold_time", Interfaces.Interface.HoldTime), "routed-vlan" : ("routed_vlan", Interfaces.Interface.RoutedVlan), "sonet" : ("sonet", Interfaces.Interface.Sonet), "state" : ("state", Interfaces.Interface.State), "subinterfaces" : ("subinterfaces", Interfaces.Interface.Subinterfaces)}
            self._child_list_classes = {}

            self.name = YLeaf(YType.str, "name")

            self.aggregation = Interfaces.Interface.Aggregation()
            self.aggregation.parent = self
            self._children_name_map["aggregation"] = "aggregation"
            self._children_yang_names.add("aggregation")

            self.config = Interfaces.Interface.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"
            self._children_yang_names.add("config")

            self.ethernet = Interfaces.Interface.Ethernet()
            self.ethernet.parent = self
            self._children_name_map["ethernet"] = "ethernet"
            self._children_yang_names.add("ethernet")

            self.hold_time = Interfaces.Interface.HoldTime()
            self.hold_time.parent = self
            self._children_name_map["hold_time"] = "hold-time"
            self._children_yang_names.add("hold-time")

            self.routed_vlan = Interfaces.Interface.RoutedVlan()
            self.routed_vlan.parent = self
            self._children_name_map["routed_vlan"] = "routed-vlan"
            self._children_yang_names.add("routed-vlan")

            self.sonet = Interfaces.Interface.Sonet()
            self.sonet.parent = self
            self._children_name_map["sonet"] = "sonet"
            self._children_yang_names.add("sonet")

            self.state = Interfaces.Interface.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._children_yang_names.add("state")

            self.subinterfaces = Interfaces.Interface.Subinterfaces()
            self.subinterfaces.parent = self
            self._children_name_map["subinterfaces"] = "subinterfaces"
            self._children_yang_names.add("subinterfaces")
            self._segment_path = lambda: "interface" + "[name='" + self.name.get() + "']"
            self._absolute_path = lambda: "openconfig-interfaces:interfaces/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Interfaces.Interface, ['name'], name, value)


        class Aggregation(Entity):
            """
            Options for logical interfaces representing
            aggregates
            
            .. attribute:: config
            
            	Configuration variables for logical aggregate / LAG interfaces
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.Config>`
            
            .. attribute:: state
            
            	Operational state variables for logical aggregate / LAG interfaces
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.State>`
            
            .. attribute:: switched_vlan
            
            	Enclosing container for VLAN interface\-specific data on Ethernet interfaces.  These are for standard L2, switched\-style VLANs
            	**type**\:   :py:class:`SwitchedVlan <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.SwitchedVlan>`
            
            

            """

            _prefix = 'oc-lag'
            _revision = '2016-05-26'

            def __init__(self):
                super(Interfaces.Interface.Aggregation, self).__init__()

                self.yang_name = "aggregation"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"config" : ("config", Interfaces.Interface.Aggregation.Config), "state" : ("state", Interfaces.Interface.Aggregation.State), "switched-vlan" : ("switched_vlan", Interfaces.Interface.Aggregation.SwitchedVlan)}
                self._child_list_classes = {}

                self.config = Interfaces.Interface.Aggregation.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Interfaces.Interface.Aggregation.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.switched_vlan = Interfaces.Interface.Aggregation.SwitchedVlan()
                self.switched_vlan.parent = self
                self._children_name_map["switched_vlan"] = "switched-vlan"
                self._children_yang_names.add("switched-vlan")
                self._segment_path = lambda: "openconfig-if-aggregate:aggregation"


            class Config(Entity):
                """
                Configuration variables for logical aggregate /
                LAG interfaces
                
                .. attribute:: lag_type
                
                	Sets the type of LAG, i.e., how it is configured / maintained
                	**type**\:   :py:class:`AggregationType <ydk.models.openconfig.openconfig_if_aggregate.AggregationType>`
                
                .. attribute:: min_links
                
                	Specifies the mininum number of member interfaces that must be active for the aggregate interface to be available
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'oc-lag'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.Aggregation.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "aggregation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.lag_type = YLeaf(YType.enumeration, "lag-type")

                    self.min_links = YLeaf(YType.uint16, "min-links")
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Aggregation.Config, ['lag_type', 'min_links'], name, value)


            class State(Entity):
                """
                Operational state variables for logical
                aggregate / LAG interfaces
                
                .. attribute:: lag_speed
                
                	Reports effective speed of the aggregate interface, based on speed of active member interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: Mbps
                
                .. attribute:: lag_type
                
                	Sets the type of LAG, i.e., how it is configured / maintained
                	**type**\:   :py:class:`AggregationType <ydk.models.openconfig.openconfig_if_aggregate.AggregationType>`
                
                .. attribute:: member
                
                	List of current member interfaces for the aggregate, expressed as references to existing interfaces
                	**type**\:  list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: min_links
                
                	Specifies the mininum number of member interfaces that must be active for the aggregate interface to be available
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'oc-lag'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.Aggregation.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "aggregation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.lag_speed = YLeaf(YType.uint32, "lag-speed")

                    self.lag_type = YLeaf(YType.enumeration, "lag-type")

                    self.member = YLeafList(YType.str, "member")

                    self.min_links = YLeaf(YType.uint16, "min-links")
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Aggregation.State, ['lag_speed', 'lag_type', 'member', 'min_links'], name, value)


            class SwitchedVlan(Entity):
                """
                Enclosing container for VLAN interface\-specific
                data on Ethernet interfaces.  These are for standard
                L2, switched\-style VLANs.
                
                .. attribute:: config
                
                	Configuration parameters for VLANs
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.SwitchedVlan.Config>`
                
                .. attribute:: state
                
                	State variables for VLANs
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Aggregation.SwitchedVlan.State>`
                
                

                """

                _prefix = 'oc-vlan'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.Aggregation.SwitchedVlan, self).__init__()

                    self.yang_name = "switched-vlan"
                    self.yang_parent_name = "aggregation"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"config" : ("config", Interfaces.Interface.Aggregation.SwitchedVlan.Config), "state" : ("state", Interfaces.Interface.Aggregation.SwitchedVlan.State)}
                    self._child_list_classes = {}

                    self.config = Interfaces.Interface.Aggregation.SwitchedVlan.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Interfaces.Interface.Aggregation.SwitchedVlan.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "openconfig-vlan:switched-vlan"


                class Config(Entity):
                    """
                    Configuration parameters for VLANs
                    
                    .. attribute:: access_vlan
                    
                    	Assign the access vlan to the access port
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: interface_mode
                    
                    	Set the interface to access or trunk mode for VLANs
                    	**type**\:   :py:class:`VlanModeType <ydk.models.openconfig.openconfig_vlan_types.VlanModeType>`
                    
                    .. attribute:: native_vlan
                    
                    	Set the native VLAN id for untagged frames arriving on a trunk interface.  This configuration is only valid on a trunk interface
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: trunk_vlans
                    
                    	Specify VLANs, or ranges thereof, that the interface may carry when in trunk mode.  If not specified, all VLANs are allowed on the interface. Ranges are specified in the form x..y, where x<y \- ranges are assumed to be inclusive (such that the VLAN range is x <= range <= y
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (\\\*\|(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9]))\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    
                    ----
                    

                    """

                    _prefix = 'oc-vlan'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Aggregation.SwitchedVlan.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "switched-vlan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.access_vlan = YLeaf(YType.str, "access-vlan")

                        self.interface_mode = YLeaf(YType.enumeration, "interface-mode")

                        self.native_vlan = YLeaf(YType.str, "native-vlan")

                        self.trunk_vlans = YLeafList(YType.str, "trunk-vlans")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.Aggregation.SwitchedVlan.Config, ['access_vlan', 'interface_mode', 'native_vlan', 'trunk_vlans'], name, value)


                class State(Entity):
                    """
                    State variables for VLANs
                    
                    .. attribute:: access_vlan
                    
                    	Assign the access vlan to the access port
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: interface_mode
                    
                    	Set the interface to access or trunk mode for VLANs
                    	**type**\:   :py:class:`VlanModeType <ydk.models.openconfig.openconfig_vlan_types.VlanModeType>`
                    
                    .. attribute:: native_vlan
                    
                    	Set the native VLAN id for untagged frames arriving on a trunk interface.  This configuration is only valid on a trunk interface
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: trunk_vlans
                    
                    	Specify VLANs, or ranges thereof, that the interface may carry when in trunk mode.  If not specified, all VLANs are allowed on the interface. Ranges are specified in the form x..y, where x<y \- ranges are assumed to be inclusive (such that the VLAN range is x <= range <= y
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (\\\*\|(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9]))\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    
                    ----
                    

                    """

                    _prefix = 'oc-vlan'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Aggregation.SwitchedVlan.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "switched-vlan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.access_vlan = YLeaf(YType.str, "access-vlan")

                        self.interface_mode = YLeaf(YType.enumeration, "interface-mode")

                        self.native_vlan = YLeaf(YType.str, "native-vlan")

                        self.trunk_vlans = YLeafList(YType.str, "trunk-vlans")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.Aggregation.SwitchedVlan.State, ['access_vlan', 'interface_mode', 'native_vlan', 'trunk_vlans'], name, value)


        class Config(Entity):
            """
            Configurable items at the global, physical interface
            level
            
            .. attribute:: description
            
            	[adapted from IETF interfaces model (RFC 7223)]  A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
            	**type**\:  str
            
            .. attribute:: enabled
            
            	[adapted from IETF interfaces model (RFC 7223)]  This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: mtu
            
            	Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default \-\- e.g., 1514 bytes on an Ethernet interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: name
            
            	[adapted from IETF interfaces model (RFC 7223)]  The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list interfaces/interface[name]/state contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the corresponding state list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  The IETF model in RFC 7223 provides YANG features for the following (i.e., pre\-provisioning and arbitrary\-names), however they are omitted here\:   If the device supports pre\-provisioning of interface  configuration, the 'pre\-provisioning' feature is  advertised.   If the device allows arbitrarily named user\-controlled  interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interfaces/interface[name]/state list
            	**type**\:  str
            
            .. attribute:: type
            
            	[adapted from IETF interfaces model (RFC 7223)]  The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case
            	**type**\:   :py:class:`InterfaceType <ydk.models.ietf.ietf_interfaces.InterfaceType>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'oc-if'
            _revision = '2016-05-26'

            def __init__(self):
                super(Interfaces.Interface.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.description = YLeaf(YType.str, "description")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.mtu = YLeaf(YType.uint16, "mtu")

                self.name = YLeaf(YType.str, "name")

                self.type = YLeaf(YType.identityref, "type")
                self._segment_path = lambda: "config"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.Config, ['description', 'enabled', 'mtu', 'name', 'type'], name, value)


        class Ethernet(Entity):
            """
            Top\-level container for ethernet configuration
            and state
            
            .. attribute:: config
            
            	Configuration data for ethernet interfaces
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.Config>`
            
            .. attribute:: state
            
            	State variables for Ethernet interfaces
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.State>`
            
            .. attribute:: switched_vlan
            
            	Enclosing container for VLAN interface\-specific data on Ethernet interfaces.  These are for standard L2, switched\-style VLANs
            	**type**\:   :py:class:`SwitchedVlan <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.SwitchedVlan>`
            
            

            """

            _prefix = 'oc-eth'
            _revision = '2016-05-26'

            def __init__(self):
                super(Interfaces.Interface.Ethernet, self).__init__()

                self.yang_name = "ethernet"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"config" : ("config", Interfaces.Interface.Ethernet.Config), "state" : ("state", Interfaces.Interface.Ethernet.State), "switched-vlan" : ("switched_vlan", Interfaces.Interface.Ethernet.SwitchedVlan)}
                self._child_list_classes = {}

                self.config = Interfaces.Interface.Ethernet.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Interfaces.Interface.Ethernet.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")

                self.switched_vlan = Interfaces.Interface.Ethernet.SwitchedVlan()
                self.switched_vlan.parent = self
                self._children_name_map["switched_vlan"] = "switched-vlan"
                self._children_yang_names.add("switched-vlan")
                self._segment_path = lambda: "openconfig-if-ethernet:ethernet"


            class Config(Entity):
                """
                Configuration data for ethernet interfaces
                
                .. attribute:: aggregate_id
                
                	Specify the logical aggregate interface to which this interface belongs
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: auto_negotiate
                
                	Set to TRUE to request the interface to auto\-negotiate transmission parameters with its peer interface.  When set to FALSE, the transmission parameters are specified manually
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: duplex_mode
                
                	When auto\-negotiate is TRUE, this optionally sets the duplex mode that will be advertised to the peer.  If unspecified, the interface should negotiate the duplex mode directly (typically full\-duplex).  When auto\-negotiate is FALSE, this sets the duplex mode on the interface directly
                	**type**\:   :py:class:`DuplexMode <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.Config.DuplexMode>`
                
                .. attribute:: enable_flow_control
                
                	Enable or disable flow control for this interface. Ethernet flow control is a mechanism by which a receiver may send PAUSE frames to a sender to stop transmission for a specified time.  This setting should override auto\-negotiated flow control settings.  If left unspecified, and auto\-negotiate is TRUE, flow control mode is negotiated with the peer interface
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: mac_address
                
                	Assigns a MAC address to the Ethernet interface.  If not specified, the corresponding operational state leaf is expected to show the system\-assigned MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: port_speed
                
                	When auto\-negotiate is TRUE, this optionally sets the port\-speed mode that will be advertised to the peer for negotiation.  If unspecified, it is expected that the interface will select the highest speed available based on negotiation.  When auto\-negotiate is set to FALSE, sets the link speed to a fixed value \-\- supported values are defined by ETHERNET\_SPEED identities
                	**type**\:   :py:class:`ETHERNETSPEED <ydk.models.openconfig.openconfig_if_ethernet.ETHERNETSPEED>`
                
                

                """

                _prefix = 'oc-eth'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.Ethernet.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.aggregate_id = YLeaf(YType.str, "openconfig-if-aggregate:aggregate-id")

                    self.auto_negotiate = YLeaf(YType.boolean, "auto-negotiate")

                    self.duplex_mode = YLeaf(YType.enumeration, "duplex-mode")

                    self.enable_flow_control = YLeaf(YType.boolean, "enable-flow-control")

                    self.mac_address = YLeaf(YType.str, "mac-address")

                    self.port_speed = YLeaf(YType.identityref, "port-speed")
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Ethernet.Config, ['aggregate_id', 'auto_negotiate', 'duplex_mode', 'enable_flow_control', 'mac_address', 'port_speed'], name, value)

                class DuplexMode(Enum):
                    """
                    DuplexMode

                    When auto\-negotiate is TRUE, this optionally sets the

                    duplex mode that will be advertised to the peer.  If

                    unspecified, the interface should negotiate the duplex mode

                    directly (typically full\-duplex).  When auto\-negotiate is

                    FALSE, this sets the duplex mode on the interface directly.

                    .. data:: FULL = 0

                    	Full duplex mode

                    .. data:: HALF = 1

                    	Half duplex mode

                    """

                    FULL = Enum.YLeaf(0, "FULL")

                    HALF = Enum.YLeaf(1, "HALF")



            class State(Entity):
                """
                State variables for Ethernet interfaces
                
                .. attribute:: aggregate_id
                
                	Specify the logical aggregate interface to which this interface belongs
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: auto_negotiate
                
                	Set to TRUE to request the interface to auto\-negotiate transmission parameters with its peer interface.  When set to FALSE, the transmission parameters are specified manually
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: counters
                
                	Ethernet interface counters
                	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.State.Counters>`
                
                .. attribute:: duplex_mode
                
                	When auto\-negotiate is TRUE, this optionally sets the duplex mode that will be advertised to the peer.  If unspecified, the interface should negotiate the duplex mode directly (typically full\-duplex).  When auto\-negotiate is FALSE, this sets the duplex mode on the interface directly
                	**type**\:   :py:class:`DuplexMode <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.State.DuplexMode>`
                
                .. attribute:: effective_speed
                
                	Reports the effective speed of the interface, e.g., the negotiated speed if auto\-negotiate is enabled
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: Mbps
                
                .. attribute:: enable_flow_control
                
                	Enable or disable flow control for this interface. Ethernet flow control is a mechanism by which a receiver may send PAUSE frames to a sender to stop transmission for a specified time.  This setting should override auto\-negotiated flow control settings.  If left unspecified, and auto\-negotiate is TRUE, flow control mode is negotiated with the peer interface
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: hw_mac_address
                
                	Represenets the 'burned\-in',  or system\-assigned, MAC address for the Ethernet interface
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: mac_address
                
                	Assigns a MAC address to the Ethernet interface.  If not specified, the corresponding operational state leaf is expected to show the system\-assigned MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: port_speed
                
                	When auto\-negotiate is TRUE, this optionally sets the port\-speed mode that will be advertised to the peer for negotiation.  If unspecified, it is expected that the interface will select the highest speed available based on negotiation.  When auto\-negotiate is set to FALSE, sets the link speed to a fixed value \-\- supported values are defined by ETHERNET\_SPEED identities
                	**type**\:   :py:class:`ETHERNETSPEED <ydk.models.openconfig.openconfig_if_ethernet.ETHERNETSPEED>`
                
                

                """

                _prefix = 'oc-eth'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.Ethernet.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"counters" : ("counters", Interfaces.Interface.Ethernet.State.Counters)}
                    self._child_list_classes = {}

                    self.aggregate_id = YLeaf(YType.str, "openconfig-if-aggregate:aggregate-id")

                    self.auto_negotiate = YLeaf(YType.boolean, "auto-negotiate")

                    self.duplex_mode = YLeaf(YType.enumeration, "duplex-mode")

                    self.effective_speed = YLeaf(YType.uint32, "effective-speed")

                    self.enable_flow_control = YLeaf(YType.boolean, "enable-flow-control")

                    self.hw_mac_address = YLeaf(YType.str, "hw-mac-address")

                    self.mac_address = YLeaf(YType.str, "mac-address")

                    self.port_speed = YLeaf(YType.identityref, "port-speed")

                    self.counters = Interfaces.Interface.Ethernet.State.Counters()
                    self.counters.parent = self
                    self._children_name_map["counters"] = "counters"
                    self._children_yang_names.add("counters")
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Ethernet.State, ['aggregate_id', 'auto_negotiate', 'duplex_mode', 'effective_speed', 'enable_flow_control', 'hw_mac_address', 'mac_address', 'port_speed'], name, value)

                class DuplexMode(Enum):
                    """
                    DuplexMode

                    When auto\-negotiate is TRUE, this optionally sets the

                    duplex mode that will be advertised to the peer.  If

                    unspecified, the interface should negotiate the duplex mode

                    directly (typically full\-duplex).  When auto\-negotiate is

                    FALSE, this sets the duplex mode on the interface directly.

                    .. data:: FULL = 0

                    	Full duplex mode

                    .. data:: HALF = 1

                    	Half duplex mode

                    """

                    FULL = Enum.YLeaf(0, "FULL")

                    HALF = Enum.YLeaf(1, "HALF")



                class Counters(Entity):
                    """
                    Ethernet interface counters
                    
                    .. attribute:: in_8021q_frames
                    
                    	Number of 802.1q tagged frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_crc_errors
                    
                    	Number of receive error events due to FCS/CRC check failure
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_fragment_frames
                    
                    	Number of fragment frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_jabber_frames
                    
                    	Number of jabber frames received on the interface.  Jabber frames are typically defined as oversize frames which also have a bad CRC.  Implementations may use slightly different definitions of what constitutes a jabber frame.  Often indicative of a NIC hardware problem
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_mac_control_frames
                    
                    	MAC layer control frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_mac_pause_frames
                    
                    	MAC layer PAUSE frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: in_oversize_frames
                    
                    	Number of oversize frames received on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_8021q_frames
                    
                    	Number of 802.1q tagged frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_mac_control_frames
                    
                    	MAC layer control frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: out_mac_pause_frames
                    
                    	MAC layer PAUSE frames sent on the interface
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'oc-eth'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Ethernet.State.Counters, self).__init__()

                        self.yang_name = "counters"
                        self.yang_parent_name = "state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.in_8021q_frames = YLeaf(YType.uint64, "in-8021q-frames")

                        self.in_crc_errors = YLeaf(YType.uint64, "in-crc-errors")

                        self.in_fragment_frames = YLeaf(YType.uint64, "in-fragment-frames")

                        self.in_jabber_frames = YLeaf(YType.uint64, "in-jabber-frames")

                        self.in_mac_control_frames = YLeaf(YType.uint64, "in-mac-control-frames")

                        self.in_mac_pause_frames = YLeaf(YType.uint64, "in-mac-pause-frames")

                        self.in_oversize_frames = YLeaf(YType.uint64, "in-oversize-frames")

                        self.out_8021q_frames = YLeaf(YType.uint64, "out-8021q-frames")

                        self.out_mac_control_frames = YLeaf(YType.uint64, "out-mac-control-frames")

                        self.out_mac_pause_frames = YLeaf(YType.uint64, "out-mac-pause-frames")
                        self._segment_path = lambda: "counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.Ethernet.State.Counters, ['in_8021q_frames', 'in_crc_errors', 'in_fragment_frames', 'in_jabber_frames', 'in_mac_control_frames', 'in_mac_pause_frames', 'in_oversize_frames', 'out_8021q_frames', 'out_mac_control_frames', 'out_mac_pause_frames'], name, value)


            class SwitchedVlan(Entity):
                """
                Enclosing container for VLAN interface\-specific
                data on Ethernet interfaces.  These are for standard
                L2, switched\-style VLANs.
                
                .. attribute:: config
                
                	Configuration parameters for VLANs
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.SwitchedVlan.Config>`
                
                .. attribute:: state
                
                	State variables for VLANs
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Ethernet.SwitchedVlan.State>`
                
                

                """

                _prefix = 'oc-vlan'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.Ethernet.SwitchedVlan, self).__init__()

                    self.yang_name = "switched-vlan"
                    self.yang_parent_name = "ethernet"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"config" : ("config", Interfaces.Interface.Ethernet.SwitchedVlan.Config), "state" : ("state", Interfaces.Interface.Ethernet.SwitchedVlan.State)}
                    self._child_list_classes = {}

                    self.config = Interfaces.Interface.Ethernet.SwitchedVlan.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Interfaces.Interface.Ethernet.SwitchedVlan.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "openconfig-vlan:switched-vlan"


                class Config(Entity):
                    """
                    Configuration parameters for VLANs
                    
                    .. attribute:: access_vlan
                    
                    	Assign the access vlan to the access port
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: interface_mode
                    
                    	Set the interface to access or trunk mode for VLANs
                    	**type**\:   :py:class:`VlanModeType <ydk.models.openconfig.openconfig_vlan_types.VlanModeType>`
                    
                    .. attribute:: native_vlan
                    
                    	Set the native VLAN id for untagged frames arriving on a trunk interface.  This configuration is only valid on a trunk interface
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: trunk_vlans
                    
                    	Specify VLANs, or ranges thereof, that the interface may carry when in trunk mode.  If not specified, all VLANs are allowed on the interface. Ranges are specified in the form x..y, where x<y \- ranges are assumed to be inclusive (such that the VLAN range is x <= range <= y
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (\\\*\|(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9]))\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    
                    ----
                    

                    """

                    _prefix = 'oc-vlan'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Ethernet.SwitchedVlan.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "switched-vlan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.access_vlan = YLeaf(YType.str, "access-vlan")

                        self.interface_mode = YLeaf(YType.enumeration, "interface-mode")

                        self.native_vlan = YLeaf(YType.str, "native-vlan")

                        self.trunk_vlans = YLeafList(YType.str, "trunk-vlans")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.Ethernet.SwitchedVlan.Config, ['access_vlan', 'interface_mode', 'native_vlan', 'trunk_vlans'], name, value)


                class State(Entity):
                    """
                    State variables for VLANs
                    
                    .. attribute:: access_vlan
                    
                    	Assign the access vlan to the access port
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: interface_mode
                    
                    	Set the interface to access or trunk mode for VLANs
                    	**type**\:   :py:class:`VlanModeType <ydk.models.openconfig.openconfig_vlan_types.VlanModeType>`
                    
                    .. attribute:: native_vlan
                    
                    	Set the native VLAN id for untagged frames arriving on a trunk interface.  This configuration is only valid on a trunk interface
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    .. attribute:: trunk_vlans
                    
                    	Specify VLANs, or ranges thereof, that the interface may carry when in trunk mode.  If not specified, all VLANs are allowed on the interface. Ranges are specified in the form x..y, where x<y \- ranges are assumed to be inclusive (such that the VLAN range is x <= range <= y
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 1..4094
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (\\\*\|(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9]))\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.\\.(409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])
                    
                    
                    ----
                    
                    ----
                    

                    """

                    _prefix = 'oc-vlan'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Ethernet.SwitchedVlan.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "switched-vlan"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.access_vlan = YLeaf(YType.str, "access-vlan")

                        self.interface_mode = YLeaf(YType.enumeration, "interface-mode")

                        self.native_vlan = YLeaf(YType.str, "native-vlan")

                        self.trunk_vlans = YLeafList(YType.str, "trunk-vlans")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.Ethernet.SwitchedVlan.State, ['access_vlan', 'interface_mode', 'native_vlan', 'trunk_vlans'], name, value)


        class HoldTime(Entity):
            """
            Top\-level container for hold\-time settings to enable
            dampening advertisements of interface transitions.
            
            .. attribute:: config
            
            	Configuration data for interface hold\-time settings
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.HoldTime.Config>`
            
            .. attribute:: state
            
            	Operational state data for interface hold\-time
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.HoldTime.State>`
            
            

            """

            _prefix = 'oc-if'
            _revision = '2016-05-26'

            def __init__(self):
                super(Interfaces.Interface.HoldTime, self).__init__()

                self.yang_name = "hold-time"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"config" : ("config", Interfaces.Interface.HoldTime.Config), "state" : ("state", Interfaces.Interface.HoldTime.State)}
                self._child_list_classes = {}

                self.config = Interfaces.Interface.HoldTime.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Interfaces.Interface.HoldTime.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "hold-time"


            class Config(Entity):
                """
                Configuration data for interface hold\-time settings.
                
                .. attribute:: down
                
                	Dampens advertisement when the interface transitions from up to down.  A zero value means dampening is turned off, i.e., immediate notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                .. attribute:: up
                
                	Dampens advertisement when the interface transitions from down to up.  A zero value means dampening is turned off, i.e., immediate notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                

                """

                _prefix = 'oc-if'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.HoldTime.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "hold-time"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.down = YLeaf(YType.uint32, "down")

                    self.up = YLeaf(YType.uint32, "up")
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.HoldTime.Config, ['down', 'up'], name, value)


            class State(Entity):
                """
                Operational state data for interface hold\-time.
                
                .. attribute:: down
                
                	Dampens advertisement when the interface transitions from up to down.  A zero value means dampening is turned off, i.e., immediate notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                .. attribute:: up
                
                	Dampens advertisement when the interface transitions from down to up.  A zero value means dampening is turned off, i.e., immediate notification
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: milliseconds
                
                	**default value**\: 0
                
                

                """

                _prefix = 'oc-if'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.HoldTime.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "hold-time"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.down = YLeaf(YType.uint32, "down")

                    self.up = YLeaf(YType.uint32, "up")
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.HoldTime.State, ['down', 'up'], name, value)


        class RoutedVlan(Entity):
            """
            Top\-level container for routed vlan interfaces.  These
            logical interfaces are also known as SVI (switched virtual
            interface), IRB (integrated routing and bridging), RVI
            (routed VLAN interface)
            
            .. attribute:: config
            
            	Configuration data for routed vlan interfaces
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Config>`
            
            .. attribute:: ipv4
            
            	Parameters for the IPv4 address family
            	**type**\:   :py:class:`Ipv4 <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4>`
            
            .. attribute:: ipv6
            
            	Parameters for the IPv6 address family
            	**type**\:   :py:class:`Ipv6 <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6>`
            
            .. attribute:: state
            
            	Operational state data 
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.State>`
            
            

            """

            _prefix = 'oc-vlan'
            _revision = '2016-05-26'

            def __init__(self):
                super(Interfaces.Interface.RoutedVlan, self).__init__()

                self.yang_name = "routed-vlan"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Config), "ipv4" : ("ipv4", Interfaces.Interface.RoutedVlan.Ipv4), "ipv6" : ("ipv6", Interfaces.Interface.RoutedVlan.Ipv6), "state" : ("state", Interfaces.Interface.RoutedVlan.State)}
                self._child_list_classes = {}

                self.config = Interfaces.Interface.RoutedVlan.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.ipv4 = Interfaces.Interface.RoutedVlan.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Interfaces.Interface.RoutedVlan.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")

                self.state = Interfaces.Interface.RoutedVlan.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "openconfig-vlan:routed-vlan"


            class Config(Entity):
                """
                Configuration data for routed vlan interfaces
                
                .. attribute:: vlan
                
                	References the VLAN for which this IP interface provides routing services \-\- similar to a switch virtual interface (SVI), or integrated routing and bridging interface (IRB) in some implementations
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..65535
                
                
                ----
                	**type**\:  str
                
                
                ----
                

                """

                _prefix = 'oc-vlan'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.RoutedVlan.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "routed-vlan"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.vlan = YLeaf(YType.str, "vlan")
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.RoutedVlan.Config, ['vlan'], name, value)


            class Ipv4(Entity):
                """
                Parameters for the IPv4 address family.
                
                .. attribute:: addresses
                
                	Enclosing container for address list
                	**type**\:   :py:class:`Addresses <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses>`
                
                .. attribute:: config
                
                	Top\-level IPv4 configuration data for the interface
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Config>`
                
                .. attribute:: neighbors
                
                	Enclosing container for neighbor list
                	**type**\:   :py:class:`Neighbors <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbors>`
                
                .. attribute:: state
                
                	Top level IPv4 operational state data
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.State>`
                
                .. attribute:: unnumbered
                
                	Top\-level container for setting unnumbered interfaces. Includes reference the interface that provides the address information
                	**type**\:   :py:class:`Unnumbered <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered>`
                
                

                """

                _prefix = 'oc-ip'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.RoutedVlan.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "routed-vlan"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"addresses" : ("addresses", Interfaces.Interface.RoutedVlan.Ipv4.Addresses), "config" : ("config", Interfaces.Interface.RoutedVlan.Ipv4.Config), "neighbors" : ("neighbors", Interfaces.Interface.RoutedVlan.Ipv4.Neighbors), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv4.State), "unnumbered" : ("unnumbered", Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered)}
                    self._child_list_classes = {}

                    self.addresses = Interfaces.Interface.RoutedVlan.Ipv4.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._children_yang_names.add("addresses")

                    self.config = Interfaces.Interface.RoutedVlan.Ipv4.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.neighbors = Interfaces.Interface.RoutedVlan.Ipv4.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._children_yang_names.add("neighbors")

                    self.state = Interfaces.Interface.RoutedVlan.Ipv4.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.unnumbered = Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered()
                    self.unnumbered.parent = self
                    self._children_name_map["unnumbered"] = "unnumbered"
                    self._children_yang_names.add("unnumbered")
                    self._segment_path = lambda: "openconfig-if-ip:ipv4"


                class Addresses(Entity):
                    """
                    Enclosing container for address list
                    
                    .. attribute:: address
                    
                    	The list of configured IPv4 addresses on the interface
                    	**type**\: list of    :py:class:`Address <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address>`
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"address" : ("address", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address)}

                        self.address = YList(self)
                        self._segment_path = lambda: "addresses"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses, [], name, value)


                    class Address(Entity):
                        """
                        The list of configured IPv4 addresses on the interface.
                        
                        .. attribute:: ip  <key>
                        
                        	References the configured IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for each configured IPv4 address on the interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for each IPv4 address configured on the interface
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.State>`
                        
                        .. attribute:: vrrp
                        
                        	Enclosing container for VRRP groups handled by this IP interface
                        	**type**\:   :py:class:`Vrrp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Config), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.State), "vrrp" : ("vrrp", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp)}
                            self._child_list_classes = {}

                            self.ip = YLeaf(YType.str, "ip")

                            self.config = Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                            self.vrrp = Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp()
                            self.vrrp.parent = self
                            self._children_name_map["vrrp"] = "vrrp"
                            self._children_yang_names.add("vrrp")
                            self._segment_path = lambda: "address" + "[ip='" + self.ip.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address, ['ip'], name, value)


                        class Config(Entity):
                            """
                            Configuration data for each configured IPv4
                            address on the interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277]  The IPv4 address on the interface
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	[adapted from IETF IP model RFC 7277]  The length of the subnet prefix
                            	**type**\:  int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Config, ['ip', 'prefix_length'], name, value)


                        class State(Entity):
                            """
                            Operational state data for each IPv4 address
                            configured on the interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277]  The IPv4 address on the interface
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: origin
                            
                            	The origin of this address, e.g., statically configured, assigned by DHCP, etc.
                            	**type**\:   :py:class:`IpAddressOrigin <ydk.models.openconfig.openconfig_if_ip.IpAddressOrigin>`
                            
                            .. attribute:: prefix_length
                            
                            	[adapted from IETF IP model RFC 7277]  The length of the subnet prefix
                            	**type**\:  int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.origin = YLeaf(YType.enumeration, "origin")

                                self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.State, ['ip', 'origin', 'prefix_length'], name, value)


                        class Vrrp(Entity):
                            """
                            Enclosing container for VRRP groups handled by this
                            IP interface
                            
                            .. attribute:: vrrp_group
                            
                            	List of VRRP groups, keyed by virtual router id
                            	**type**\: list of    :py:class:`VrrpGroup <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp, self).__init__()

                                self.yang_name = "vrrp"
                                self.yang_parent_name = "address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"vrrp-group" : ("vrrp_group", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup)}

                                self.vrrp_group = YList(self)
                                self._segment_path = lambda: "vrrp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp, [], name, value)


                            class VrrpGroup(Entity):
                                """
                                List of VRRP groups, keyed by virtual router id
                                
                                .. attribute:: virtual_router_id  <key>
                                
                                	References the configured virtual router id for this VRRP group
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**refers to**\:  :py:class:`virtual_router_id <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config>`
                                
                                .. attribute:: config
                                
                                	Configuration data for the VRRP group
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config>`
                                
                                .. attribute:: interface_tracking
                                
                                	Top\-level container for VRRP interface tracking
                                	**type**\:   :py:class:`InterfaceTracking <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the VRRP group
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup, self).__init__()

                                    self.yang_name = "vrrp-group"
                                    self.yang_parent_name = "vrrp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config), "interface-tracking" : ("interface_tracking", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State)}
                                    self._child_list_classes = {}

                                    self.virtual_router_id = YLeaf(YType.str, "virtual-router-id")

                                    self.config = Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.interface_tracking = Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking()
                                    self.interface_tracking.parent = self
                                    self._children_name_map["interface_tracking"] = "interface-tracking"
                                    self._children_yang_names.add("interface-tracking")

                                    self.state = Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "vrrp-group" + "[virtual-router-id='" + self.virtual_router_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup, ['virtual_router_id'], name, value)


                                class Config(Entity):
                                    """
                                    Configuration data for the VRRP group
                                    
                                    .. attribute:: accept_mode
                                    
                                    	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                    	**type**\:  bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: advertisement_interval
                                    
                                    	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                    	**type**\:  int
                                    
                                    	**range:** 1..4095
                                    
                                    	**units**\: centiseconds
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: preempt
                                    
                                    	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                    	**type**\:  bool
                                    
                                    	**default value**\: true
                                    
                                    .. attribute:: preempt_delay
                                    
                                    	Set the delay the higher priority router waits before preempting
                                    	**type**\:  int
                                    
                                    	**range:** 0..3600
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: priority
                                    
                                    	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: virtual_address
                                    
                                    	Configure one or more virtual addresses for the VRRP group
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  list of str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_router_id
                                    
                                    	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'oc-ip'
                                    _revision = '2016-05-26'

                                    def __init__(self):
                                        super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "vrrp-group"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.accept_mode = YLeaf(YType.boolean, "accept-mode")

                                        self.advertisement_interval = YLeaf(YType.uint16, "advertisement-interval")

                                        self.preempt = YLeaf(YType.boolean, "preempt")

                                        self.preempt_delay = YLeaf(YType.uint16, "preempt-delay")

                                        self.priority = YLeaf(YType.uint8, "priority")

                                        self.virtual_address = YLeafList(YType.str, "virtual-address")

                                        self.virtual_router_id = YLeaf(YType.uint8, "virtual-router-id")
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config, ['accept_mode', 'advertisement_interval', 'preempt', 'preempt_delay', 'priority', 'virtual_address', 'virtual_router_id'], name, value)


                                class InterfaceTracking(Entity):
                                    """
                                    Top\-level container for VRRP interface tracking
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for VRRP interface tracking
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for VRRP interface tracking
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-ip'
                                    _revision = '2016-05-26'

                                    def __init__(self):
                                        super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking, self).__init__()

                                        self.yang_name = "interface-tracking"
                                        self.yang_parent_name = "vrrp-group"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State)}
                                        self._child_list_classes = {}

                                        self.config = Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "interface-tracking"


                                    class Config(Entity):
                                        """
                                        Configuration data for VRRP interface tracking
                                        
                                        .. attribute:: priority_decrement
                                        
                                        	Set the value to subtract from priority when the tracked interface goes down
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: track_interface
                                        
                                        	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "interface-tracking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.priority_decrement = YLeaf(YType.uint8, "priority-decrement")

                                            self.track_interface = YLeaf(YType.str, "track-interface")
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config, ['priority_decrement', 'track_interface'], name, value)


                                    class State(Entity):
                                        """
                                        Operational state data for VRRP interface tracking
                                        
                                        .. attribute:: priority_decrement
                                        
                                        	Set the value to subtract from priority when the tracked interface goes down
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: track_interface
                                        
                                        	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "interface-tracking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.priority_decrement = YLeaf(YType.uint8, "priority-decrement")

                                            self.track_interface = YLeaf(YType.str, "track-interface")
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State, ['priority_decrement', 'track_interface'], name, value)


                                class State(Entity):
                                    """
                                    Operational state data for the VRRP group
                                    
                                    .. attribute:: accept_mode
                                    
                                    	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                    	**type**\:  bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: advertisement_interval
                                    
                                    	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                    	**type**\:  int
                                    
                                    	**range:** 1..4095
                                    
                                    	**units**\: centiseconds
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: current_priority
                                    
                                    	Operational value of the priority for the interface in the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: preempt
                                    
                                    	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                    	**type**\:  bool
                                    
                                    	**default value**\: true
                                    
                                    .. attribute:: preempt_delay
                                    
                                    	Set the delay the higher priority router waits before preempting
                                    	**type**\:  int
                                    
                                    	**range:** 0..3600
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: priority
                                    
                                    	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: virtual_address
                                    
                                    	Configure one or more virtual addresses for the VRRP group
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  list of str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_router_id
                                    
                                    	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'oc-ip'
                                    _revision = '2016-05-26'

                                    def __init__(self):
                                        super(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "vrrp-group"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.accept_mode = YLeaf(YType.boolean, "accept-mode")

                                        self.advertisement_interval = YLeaf(YType.uint16, "advertisement-interval")

                                        self.current_priority = YLeaf(YType.uint8, "current-priority")

                                        self.preempt = YLeaf(YType.boolean, "preempt")

                                        self.preempt_delay = YLeaf(YType.uint16, "preempt-delay")

                                        self.priority = YLeaf(YType.uint8, "priority")

                                        self.virtual_address = YLeafList(YType.str, "virtual-address")

                                        self.virtual_router_id = YLeaf(YType.uint8, "virtual-router-id")
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State, ['accept_mode', 'advertisement_interval', 'current_priority', 'preempt', 'preempt_delay', 'priority', 'virtual_address', 'virtual_router_id'], name, value)


                class Config(Entity):
                    """
                    Top\-level IPv4 configuration data for the interface
                    
                    .. attribute:: enabled
                    
                    	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: mtu
                    
                    	The size, in octets, of the largest IPv4 packet that the interface will send and receive.  The server may restrict the allowed values for this leaf, depending on the interface's type.  If this leaf is not configured, the operationally used MTU depends on the interface's type
                    	**type**\:  int
                    
                    	**range:** 68..65535
                    
                    	**units**\: octets
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv4.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.mtu = YLeaf(YType.uint16, "mtu")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Config, ['enabled', 'mtu'], name, value)


                class Neighbors(Entity):
                    """
                    Enclosing container for neighbor list
                    
                    .. attribute:: neighbor
                    
                    	A list of mappings from IPv4 addresses to link\-layer addresses.  Entries in this list are used as static entries in the ARP Cache
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv4.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"neighbor" : ("neighbor", Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor)}

                        self.neighbor = YList(self)
                        self._segment_path = lambda: "neighbors"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Neighbors, [], name, value)


                    class Neighbor(Entity):
                        """
                        A list of mappings from IPv4 addresses to
                        link\-layer addresses.
                        
                        Entries in this list are used as static entries in the
                        ARP Cache.
                        
                        .. attribute:: ip  <key>
                        
                        	References the configured IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for each configured IPv4 address on the interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state data for each IPv4 address configured on the interface
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.State>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.Config), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.State)}
                            self._child_list_classes = {}

                            self.ip = YLeaf(YType.str, "ip")

                            self.config = Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "neighbor" + "[ip='" + self.ip.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor, ['ip'], name, value)


                        class Config(Entity):
                            """
                            Configuration data for each configured IPv4
                            address on the interface
                            
                            .. attribute:: ip
                            
                            	The IPv4 address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: link_layer_address
                            
                            	The link\-layer address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.link_layer_address = YLeaf(YType.str, "link-layer-address")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.Config, ['ip', 'link_layer_address'], name, value)


                        class State(Entity):
                            """
                            Operational state data for each IPv4 address
                            configured on the interface
                            
                            .. attribute:: ip
                            
                            	The IPv4 address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: link_layer_address
                            
                            	The link\-layer address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: origin
                            
                            	The origin of this neighbor entry, static or dynamic
                            	**type**\:   :py:class:`NeighborOrigin <ydk.models.openconfig.openconfig_if_ip.NeighborOrigin>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                                self.origin = YLeaf(YType.enumeration, "origin")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Neighbors.Neighbor.State, ['ip', 'link_layer_address', 'origin'], name, value)


                class State(Entity):
                    """
                    Top level IPv4 operational state data
                    
                    .. attribute:: enabled
                    
                    	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: mtu
                    
                    	The size, in octets, of the largest IPv4 packet that the interface will send and receive.  The server may restrict the allowed values for this leaf, depending on the interface's type.  If this leaf is not configured, the operationally used MTU depends on the interface's type
                    	**type**\:  int
                    
                    	**range:** 68..65535
                    
                    	**units**\: octets
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv4.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.mtu = YLeaf(YType.uint16, "mtu")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.State, ['enabled', 'mtu'], name, value)


                class Unnumbered(Entity):
                    """
                    Top\-level container for setting unnumbered interfaces.
                    Includes reference the interface that provides the
                    address information
                    
                    .. attribute:: config
                    
                    	Configuration data for unnumbered interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.Config>`
                    
                    .. attribute:: interface_ref
                    
                    	Reference to an interface or subinterface
                    	**type**\:   :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef>`
                    
                    .. attribute:: state
                    
                    	Operational state data for unnumbered interfaces
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.State>`
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered, self).__init__()

                        self.yang_name = "unnumbered"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.Config), "interface-ref" : ("interface_ref", Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.State)}
                        self._child_list_classes = {}

                        self.config = Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.interface_ref = Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef()
                        self.interface_ref.parent = self
                        self._children_name_map["interface_ref"] = "interface-ref"
                        self._children_yang_names.add("interface-ref")

                        self.state = Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "unnumbered"


                    class Config(Entity):
                        """
                        Configuration data for unnumbered interface
                        
                        .. attribute:: enabled
                        
                        	Indicates that the subinterface is unnumbered.  By default the subinterface is numbered, i.e., expected to have an IP address configuration
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "unnumbered"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enabled = YLeaf(YType.boolean, "enabled")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.Config, ['enabled'], name, value)


                    class InterfaceRef(Entity):
                        """
                        Reference to an interface or subinterface
                        
                        .. attribute:: config
                        
                        	Configured reference to interface / subinterface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for interface\-ref
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.State>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef, self).__init__()

                            self.yang_name = "interface-ref"
                            self.yang_parent_name = "unnumbered"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.Config), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.State)}
                            self._child_list_classes = {}

                            self.config = Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "interface-ref"


                        class Config(Entity):
                            """
                            Configured reference to interface / subinterface
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface = YLeaf(YType.str, "interface")

                                self.subinterface = YLeaf(YType.str, "subinterface")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.Config, ['interface', 'subinterface'], name, value)


                        class State(Entity):
                            """
                            Operational state for interface\-ref
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface = YLeaf(YType.str, "interface")

                                self.subinterface = YLeaf(YType.str, "subinterface")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.InterfaceRef.State, ['interface', 'subinterface'], name, value)


                    class State(Entity):
                        """
                        Operational state data for unnumbered interfaces
                        
                        .. attribute:: enabled
                        
                        	Indicates that the subinterface is unnumbered.  By default the subinterface is numbered, i.e., expected to have an IP address configuration
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "unnumbered"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enabled = YLeaf(YType.boolean, "enabled")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv4.Unnumbered.State, ['enabled'], name, value)


            class Ipv6(Entity):
                """
                Parameters for the IPv6 address family.
                
                .. attribute:: addresses
                
                	Enclosing container for address list
                	**type**\:   :py:class:`Addresses <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses>`
                
                .. attribute:: config
                
                	Top\-level config data for the IPv6 interface
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Config>`
                
                .. attribute:: neighbors
                
                	Enclosing container for list of IPv6 neighbors
                	**type**\:   :py:class:`Neighbors <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbors>`
                
                .. attribute:: state
                
                	Top\-level operational state data for the IPv6 interface
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.State>`
                
                .. attribute:: unnumbered
                
                	Top\-level container for setting unnumbered interfaces. Includes reference the interface that provides the address information
                	**type**\:   :py:class:`Unnumbered <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered>`
                
                

                """

                _prefix = 'oc-ip'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.RoutedVlan.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "routed-vlan"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"addresses" : ("addresses", Interfaces.Interface.RoutedVlan.Ipv6.Addresses), "config" : ("config", Interfaces.Interface.RoutedVlan.Ipv6.Config), "neighbors" : ("neighbors", Interfaces.Interface.RoutedVlan.Ipv6.Neighbors), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv6.State), "unnumbered" : ("unnumbered", Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered)}
                    self._child_list_classes = {}

                    self.addresses = Interfaces.Interface.RoutedVlan.Ipv6.Addresses()
                    self.addresses.parent = self
                    self._children_name_map["addresses"] = "addresses"
                    self._children_yang_names.add("addresses")

                    self.config = Interfaces.Interface.RoutedVlan.Ipv6.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.neighbors = Interfaces.Interface.RoutedVlan.Ipv6.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._children_yang_names.add("neighbors")

                    self.state = Interfaces.Interface.RoutedVlan.Ipv6.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.unnumbered = Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered()
                    self.unnumbered.parent = self
                    self._children_name_map["unnumbered"] = "unnumbered"
                    self._children_yang_names.add("unnumbered")
                    self._segment_path = lambda: "openconfig-if-ip:ipv6"


                class Addresses(Entity):
                    """
                    Enclosing container for address list
                    
                    .. attribute:: address
                    
                    	The list of configured IPv6 addresses on the interface
                    	**type**\: list of    :py:class:`Address <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address>`
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses, self).__init__()

                        self.yang_name = "addresses"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"address" : ("address", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address)}

                        self.address = YList(self)
                        self._segment_path = lambda: "addresses"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses, [], name, value)


                    class Address(Entity):
                        """
                        The list of configured IPv6 addresses on the interface.
                        
                        .. attribute:: ip  <key>
                        
                        	References the configured IP address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for each IPv6 address on the interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Config>`
                        
                        .. attribute:: state
                        
                        	State data for each IPv6 address on the interface
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.State>`
                        
                        .. attribute:: vrrp
                        
                        	Enclosing container for VRRP groups handled by this IP interface
                        	**type**\:   :py:class:`Vrrp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Config), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.State), "vrrp" : ("vrrp", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp)}
                            self._child_list_classes = {}

                            self.ip = YLeaf(YType.str, "ip")

                            self.config = Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                            self.vrrp = Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp()
                            self.vrrp.parent = self
                            self._children_name_map["vrrp"] = "vrrp"
                            self._children_yang_names.add("vrrp")
                            self._segment_path = lambda: "address" + "[ip='" + self.ip.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address, ['ip'], name, value)


                        class Config(Entity):
                            """
                            Configuration data for each IPv6 address on
                            the interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277]  The IPv6 address on the interface
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	[adapted from IETF IP model RFC 7277]  The length of the subnet prefix
                            	**type**\:  int
                            
                            	**range:** 0..128
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Config, ['ip', 'prefix_length'], name, value)


                        class State(Entity):
                            """
                            State data for each IPv6 address on the
                            interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277]  The IPv6 address on the interface
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: origin
                            
                            	[adapted from IETF IP model RFC 7277]  The origin of this address, e.g., static, dhcp, etc
                            	**type**\:   :py:class:`IpAddressOrigin <ydk.models.openconfig.openconfig_if_ip.IpAddressOrigin>`
                            
                            .. attribute:: prefix_length
                            
                            	[adapted from IETF IP model RFC 7277]  The length of the subnet prefix
                            	**type**\:  int
                            
                            	**range:** 0..128
                            
                            	**mandatory**\: True
                            
                            .. attribute:: status
                            
                            	[adapted from IETF IP model RFC 7277]  The status of an address.  Most of the states correspond to states from the IPv6 Stateless Address Autoconfiguration protocol
                            	**type**\:   :py:class:`Status <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.State.Status>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.origin = YLeaf(YType.enumeration, "origin")

                                self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                                self.status = YLeaf(YType.enumeration, "status")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.State, ['ip', 'origin', 'prefix_length', 'status'], name, value)

                            class Status(Enum):
                                """
                                Status

                                [adapted from IETF IP model RFC 7277]

                                The status of an address.  Most of the states correspond

                                to states from the IPv6 Stateless Address

                                Autoconfiguration protocol.

                                .. data:: PREFERRED = 0

                                	This is a valid address that can appear as the

                                	destination or source address of a packet.

                                .. data:: DEPRECATED = 1

                                	This is a valid but deprecated address that should

                                	no longer be used as a source address in new

                                	communications, but packets addressed to such an

                                	address are processed as expected.

                                .. data:: INVALID = 2

                                	This isn't a valid address, and it shouldn't appear

                                	as the destination or source address of a packet.

                                .. data:: INACCESSIBLE = 3

                                	The address is not accessible because the interface

                                	to which this address is assigned is not

                                	operational.

                                .. data:: UNKNOWN = 4

                                	The status cannot be determined for some reason.

                                .. data:: TENTATIVE = 5

                                	The uniqueness of the address on the link is being

                                	verified.  Addresses in this state should not be

                                	used for general communication and should only be

                                	used to determine the uniqueness of the address.

                                .. data:: DUPLICATE = 6

                                	The address has been determined to be non-unique on

                                	the link and so must not be used.

                                .. data:: OPTIMISTIC = 7

                                	The address is available for use, subject to

                                	restrictions, while its uniqueness on a link is

                                	being verified.

                                """

                                PREFERRED = Enum.YLeaf(0, "PREFERRED")

                                DEPRECATED = Enum.YLeaf(1, "DEPRECATED")

                                INVALID = Enum.YLeaf(2, "INVALID")

                                INACCESSIBLE = Enum.YLeaf(3, "INACCESSIBLE")

                                UNKNOWN = Enum.YLeaf(4, "UNKNOWN")

                                TENTATIVE = Enum.YLeaf(5, "TENTATIVE")

                                DUPLICATE = Enum.YLeaf(6, "DUPLICATE")

                                OPTIMISTIC = Enum.YLeaf(7, "OPTIMISTIC")



                        class Vrrp(Entity):
                            """
                            Enclosing container for VRRP groups handled by this
                            IP interface
                            
                            .. attribute:: vrrp_group
                            
                            	List of VRRP groups, keyed by virtual router id
                            	**type**\: list of    :py:class:`VrrpGroup <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp, self).__init__()

                                self.yang_name = "vrrp"
                                self.yang_parent_name = "address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"vrrp-group" : ("vrrp_group", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup)}

                                self.vrrp_group = YList(self)
                                self._segment_path = lambda: "vrrp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp, [], name, value)


                            class VrrpGroup(Entity):
                                """
                                List of VRRP groups, keyed by virtual router id
                                
                                .. attribute:: virtual_router_id  <key>
                                
                                	References the configured virtual router id for this VRRP group
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**refers to**\:  :py:class:`virtual_router_id <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config>`
                                
                                .. attribute:: config
                                
                                	Configuration data for the VRRP group
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config>`
                                
                                .. attribute:: interface_tracking
                                
                                	Top\-level container for VRRP interface tracking
                                	**type**\:   :py:class:`InterfaceTracking <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking>`
                                
                                .. attribute:: state
                                
                                	Operational state data for the VRRP group
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup, self).__init__()

                                    self.yang_name = "vrrp-group"
                                    self.yang_parent_name = "vrrp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config), "interface-tracking" : ("interface_tracking", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State)}
                                    self._child_list_classes = {}

                                    self.virtual_router_id = YLeaf(YType.str, "virtual-router-id")

                                    self.config = Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.interface_tracking = Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking()
                                    self.interface_tracking.parent = self
                                    self._children_name_map["interface_tracking"] = "interface-tracking"
                                    self._children_yang_names.add("interface-tracking")

                                    self.state = Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "vrrp-group" + "[virtual-router-id='" + self.virtual_router_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup, ['virtual_router_id'], name, value)


                                class Config(Entity):
                                    """
                                    Configuration data for the VRRP group
                                    
                                    .. attribute:: accept_mode
                                    
                                    	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                    	**type**\:  bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: advertisement_interval
                                    
                                    	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                    	**type**\:  int
                                    
                                    	**range:** 1..4095
                                    
                                    	**units**\: centiseconds
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: preempt
                                    
                                    	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                    	**type**\:  bool
                                    
                                    	**default value**\: true
                                    
                                    .. attribute:: preempt_delay
                                    
                                    	Set the delay the higher priority router waits before preempting
                                    	**type**\:  int
                                    
                                    	**range:** 0..3600
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: priority
                                    
                                    	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: virtual_address
                                    
                                    	Configure one or more virtual addresses for the VRRP group
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  list of str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_link_local
                                    
                                    	For VRRP on IPv6 interfaces, sets the virtual link local address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_router_id
                                    
                                    	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'oc-ip'
                                    _revision = '2016-05-26'

                                    def __init__(self):
                                        super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "vrrp-group"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.accept_mode = YLeaf(YType.boolean, "accept-mode")

                                        self.advertisement_interval = YLeaf(YType.uint16, "advertisement-interval")

                                        self.preempt = YLeaf(YType.boolean, "preempt")

                                        self.preempt_delay = YLeaf(YType.uint16, "preempt-delay")

                                        self.priority = YLeaf(YType.uint8, "priority")

                                        self.virtual_address = YLeafList(YType.str, "virtual-address")

                                        self.virtual_link_local = YLeaf(YType.str, "virtual-link-local")

                                        self.virtual_router_id = YLeaf(YType.uint8, "virtual-router-id")
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config, ['accept_mode', 'advertisement_interval', 'preempt', 'preempt_delay', 'priority', 'virtual_address', 'virtual_link_local', 'virtual_router_id'], name, value)


                                class InterfaceTracking(Entity):
                                    """
                                    Top\-level container for VRRP interface tracking
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for VRRP interface tracking
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for VRRP interface tracking
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-ip'
                                    _revision = '2016-05-26'

                                    def __init__(self):
                                        super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking, self).__init__()

                                        self.yang_name = "interface-tracking"
                                        self.yang_parent_name = "vrrp-group"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State)}
                                        self._child_list_classes = {}

                                        self.config = Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "interface-tracking"


                                    class Config(Entity):
                                        """
                                        Configuration data for VRRP interface tracking
                                        
                                        .. attribute:: priority_decrement
                                        
                                        	Set the value to subtract from priority when the tracked interface goes down
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: track_interface
                                        
                                        	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "interface-tracking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.priority_decrement = YLeaf(YType.uint8, "priority-decrement")

                                            self.track_interface = YLeaf(YType.str, "track-interface")
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config, ['priority_decrement', 'track_interface'], name, value)


                                    class State(Entity):
                                        """
                                        Operational state data for VRRP interface tracking
                                        
                                        .. attribute:: priority_decrement
                                        
                                        	Set the value to subtract from priority when the tracked interface goes down
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: track_interface
                                        
                                        	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                        	**type**\:  str
                                        
                                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "interface-tracking"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.priority_decrement = YLeaf(YType.uint8, "priority-decrement")

                                            self.track_interface = YLeaf(YType.str, "track-interface")
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State, ['priority_decrement', 'track_interface'], name, value)


                                class State(Entity):
                                    """
                                    Operational state data for the VRRP group
                                    
                                    .. attribute:: accept_mode
                                    
                                    	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                    	**type**\:  bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: advertisement_interval
                                    
                                    	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                    	**type**\:  int
                                    
                                    	**range:** 1..4095
                                    
                                    	**units**\: centiseconds
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: current_priority
                                    
                                    	Operational value of the priority for the interface in the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: preempt
                                    
                                    	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                    	**type**\:  bool
                                    
                                    	**default value**\: true
                                    
                                    .. attribute:: preempt_delay
                                    
                                    	Set the delay the higher priority router waits before preempting
                                    	**type**\:  int
                                    
                                    	**range:** 0..3600
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: priority
                                    
                                    	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                    	**type**\:  int
                                    
                                    	**range:** 1..254
                                    
                                    	**default value**\: 100
                                    
                                    .. attribute:: virtual_address
                                    
                                    	Configure one or more virtual addresses for the VRRP group
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  list of str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_link_local
                                    
                                    	For VRRP on IPv6 interfaces, sets the virtual link local address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: virtual_router_id
                                    
                                    	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'oc-ip'
                                    _revision = '2016-05-26'

                                    def __init__(self):
                                        super(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "vrrp-group"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.accept_mode = YLeaf(YType.boolean, "accept-mode")

                                        self.advertisement_interval = YLeaf(YType.uint16, "advertisement-interval")

                                        self.current_priority = YLeaf(YType.uint8, "current-priority")

                                        self.preempt = YLeaf(YType.boolean, "preempt")

                                        self.preempt_delay = YLeaf(YType.uint16, "preempt-delay")

                                        self.priority = YLeaf(YType.uint8, "priority")

                                        self.virtual_address = YLeafList(YType.str, "virtual-address")

                                        self.virtual_link_local = YLeaf(YType.str, "virtual-link-local")

                                        self.virtual_router_id = YLeaf(YType.uint8, "virtual-router-id")
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State, ['accept_mode', 'advertisement_interval', 'current_priority', 'preempt', 'preempt_delay', 'priority', 'virtual_address', 'virtual_link_local', 'virtual_router_id'], name, value)


                class Config(Entity):
                    """
                    Top\-level config data for the IPv6 interface
                    
                    .. attribute:: dup_addr_detect_transmits
                    
                    	[adapted from IETF IP model RFC 7277]  The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    .. attribute:: enabled
                    
                    	[adapted from IETF IP model RFC 7277]  Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: mtu
                    
                    	[adapted from IETF IP model RFC 7277]  The size, in octets, of the largest IPv6 packet that the interface will send and receive.  The server may restrict the allowed values for this leaf, depending on the interface's type.  If this leaf is not configured, the operationally used MTU depends on the interface's type
                    	**type**\:  int
                    
                    	**range:** 1280..4294967295
                    
                    	**units**\: octets
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv6.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dup_addr_detect_transmits = YLeaf(YType.uint32, "dup-addr-detect-transmits")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.mtu = YLeaf(YType.uint32, "mtu")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Config, ['dup_addr_detect_transmits', 'enabled', 'mtu'], name, value)


                class Neighbors(Entity):
                    """
                    Enclosing container for list of IPv6 neighbors
                    
                    .. attribute:: neighbor
                    
                    	List of IPv6 neighbors
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv6.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"neighbor" : ("neighbor", Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor)}

                        self.neighbor = YList(self)
                        self._segment_path = lambda: "neighbors"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Neighbors, [], name, value)


                    class Neighbor(Entity):
                        """
                        List of IPv6 neighbors
                        
                        .. attribute:: ip  <key>
                        
                        	References the configured IP neighbor address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration data for each IPv6 address on the interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.Config>`
                        
                        .. attribute:: state
                        
                        	State data for each IPv6 address on the interface
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.State>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.Config), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.State)}
                            self._child_list_classes = {}

                            self.ip = YLeaf(YType.str, "ip")

                            self.config = Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "neighbor" + "[ip='" + self.ip.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor, ['ip'], name, value)


                        class Config(Entity):
                            """
                            Configuration data for each IPv6 address on
                            the interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277]  The IPv6 address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: link_layer_address
                            
                            	[adapted from IETF IP model RFC 7277]  The link\-layer address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.link_layer_address = YLeaf(YType.str, "link-layer-address")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.Config, ['ip', 'link_layer_address'], name, value)


                        class State(Entity):
                            """
                            State data for each IPv6 address on the
                            interface
                            
                            .. attribute:: ip
                            
                            	[adapted from IETF IP model RFC 7277]  The IPv6 address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: is_router
                            
                            	[adapted from IETF IP model RFC 7277]  Indicates that the neighbor node acts as a router
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: link_layer_address
                            
                            	[adapted from IETF IP model RFC 7277]  The link\-layer address of the neighbor node
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: neighbor_state
                            
                            	[adapted from IETF IP model RFC 7277]  The Neighbor Unreachability Detection state of this entry
                            	**type**\:   :py:class:`NeighborState <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.State.NeighborState>`
                            
                            .. attribute:: origin
                            
                            	[adapted from IETF IP model RFC 7277]  The origin of this neighbor entry
                            	**type**\:   :py:class:`NeighborOrigin <ydk.models.openconfig.openconfig_if_ip.NeighborOrigin>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.is_router = YLeaf(YType.empty, "is-router")

                                self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                                self.neighbor_state = YLeaf(YType.enumeration, "neighbor-state")

                                self.origin = YLeaf(YType.enumeration, "origin")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Neighbors.Neighbor.State, ['ip', 'is_router', 'link_layer_address', 'neighbor_state', 'origin'], name, value)

                            class NeighborState(Enum):
                                """
                                NeighborState

                                [adapted from IETF IP model RFC 7277]

                                The Neighbor Unreachability Detection state of this

                                entry.

                                .. data:: INCOMPLETE = 0

                                	Address resolution is in progress, and the link-layer

                                	     address of the neighbor has not yet been

                                	     determined.

                                .. data:: REACHABLE = 1

                                	Roughly speaking, the neighbor is known to have been

                                	     reachable recently (within tens of seconds ago).

                                .. data:: STALE = 2

                                	The neighbor is no longer known to be reachable, but

                                	     until traffic is sent to the neighbor no attempt

                                	     should be made to verify its reachability.

                                .. data:: DELAY = 3

                                	The neighbor is no longer known to be reachable, and

                                	     traffic has recently been sent to the neighbor.

                                	     Rather than probe the neighbor immediately, however,

                                	     delay sending probes for a short while in order to

                                	     give upper-layer protocols a chance to provide

                                	     reachability confirmation.

                                .. data:: PROBE = 4

                                	The neighbor is no longer known to be reachable, and

                                	     unicast Neighbor Solicitation probes are being sent

                                	     to verify reachability.

                                """

                                INCOMPLETE = Enum.YLeaf(0, "INCOMPLETE")

                                REACHABLE = Enum.YLeaf(1, "REACHABLE")

                                STALE = Enum.YLeaf(2, "STALE")

                                DELAY = Enum.YLeaf(3, "DELAY")

                                PROBE = Enum.YLeaf(4, "PROBE")



                class State(Entity):
                    """
                    Top\-level operational state data for the IPv6 interface
                    
                    .. attribute:: dup_addr_detect_transmits
                    
                    	[adapted from IETF IP model RFC 7277]  The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 1
                    
                    .. attribute:: enabled
                    
                    	[adapted from IETF IP model RFC 7277]  Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: mtu
                    
                    	[adapted from IETF IP model RFC 7277]  The size, in octets, of the largest IPv6 packet that the interface will send and receive.  The server may restrict the allowed values for this leaf, depending on the interface's type.  If this leaf is not configured, the operationally used MTU depends on the interface's type
                    	**type**\:  int
                    
                    	**range:** 1280..4294967295
                    
                    	**units**\: octets
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv6.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.dup_addr_detect_transmits = YLeaf(YType.uint32, "dup-addr-detect-transmits")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.mtu = YLeaf(YType.uint32, "mtu")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.State, ['dup_addr_detect_transmits', 'enabled', 'mtu'], name, value)


                class Unnumbered(Entity):
                    """
                    Top\-level container for setting unnumbered interfaces.
                    Includes reference the interface that provides the
                    address information
                    
                    .. attribute:: config
                    
                    	Configuration data for unnumbered interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.Config>`
                    
                    .. attribute:: interface_ref
                    
                    	Reference to an interface or subinterface
                    	**type**\:   :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef>`
                    
                    .. attribute:: state
                    
                    	Operational state data for unnumbered interfaces
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.State>`
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered, self).__init__()

                        self.yang_name = "unnumbered"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.Config), "interface-ref" : ("interface_ref", Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.State)}
                        self._child_list_classes = {}

                        self.config = Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.interface_ref = Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef()
                        self.interface_ref.parent = self
                        self._children_name_map["interface_ref"] = "interface-ref"
                        self._children_yang_names.add("interface-ref")

                        self.state = Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "unnumbered"


                    class Config(Entity):
                        """
                        Configuration data for unnumbered interface
                        
                        .. attribute:: enabled
                        
                        	Indicates that the subinterface is unnumbered.  By default the subinterface is numbered, i.e., expected to have an IP address configuration
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "unnumbered"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enabled = YLeaf(YType.boolean, "enabled")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.Config, ['enabled'], name, value)


                    class InterfaceRef(Entity):
                        """
                        Reference to an interface or subinterface
                        
                        .. attribute:: config
                        
                        	Configured reference to interface / subinterface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for interface\-ref
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.State>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef, self).__init__()

                            self.yang_name = "interface-ref"
                            self.yang_parent_name = "unnumbered"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.Config), "state" : ("state", Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.State)}
                            self._child_list_classes = {}

                            self.config = Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "interface-ref"


                        class Config(Entity):
                            """
                            Configured reference to interface / subinterface
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface = YLeaf(YType.str, "interface")

                                self.subinterface = YLeaf(YType.str, "subinterface")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.Config, ['interface', 'subinterface'], name, value)


                        class State(Entity):
                            """
                            Operational state for interface\-ref
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface = YLeaf(YType.str, "interface")

                                self.subinterface = YLeaf(YType.str, "subinterface")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.InterfaceRef.State, ['interface', 'subinterface'], name, value)


                    class State(Entity):
                        """
                        Operational state data for unnumbered interfaces
                        
                        .. attribute:: enabled
                        
                        	Indicates that the subinterface is unnumbered.  By default the subinterface is numbered, i.e., expected to have an IP address configuration
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "unnumbered"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enabled = YLeaf(YType.boolean, "enabled")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.RoutedVlan.Ipv6.Unnumbered.State, ['enabled'], name, value)


            class State(Entity):
                """
                Operational state data 
                
                .. attribute:: vlan
                
                	References the VLAN for which this IP interface provides routing services \-\- similar to a switch virtual interface (SVI), or integrated routing and bridging interface (IRB) in some implementations
                	**type**\: one of the below types:
                
                	**type**\:  int
                
                	**range:** 0..65535
                
                
                ----
                	**type**\:  str
                
                
                ----
                

                """

                _prefix = 'oc-vlan'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.RoutedVlan.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "routed-vlan"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.vlan = YLeaf(YType.str, "vlan")
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.RoutedVlan.State, ['vlan'], name, value)


        class Sonet(Entity):
            """
            Data related to SONET/SDH interfaces
            
            

            """

            _prefix = 'oc-line-com'
            _revision = '2017-07-08'

            def __init__(self):
                super(Interfaces.Interface.Sonet, self).__init__()

                self.yang_name = "sonet"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}
                self._segment_path = lambda: "openconfig-transport-line-common:sonet"


        class State(Entity):
            """
            Operational state data at the global interface level
            
            .. attribute:: admin_status
            
            	[adapted from IETF interfaces model (RFC 7223)]  The desired state of the interface.  In RFC 7223 this leaf has the same read semantics as ifAdminStatus.  Here, it reflects the administrative state as set by enabling or disabling the interface
            	**type**\:   :py:class:`AdminStatus <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.State.AdminStatus>`
            
            	**mandatory**\: True
            
            .. attribute:: counters
            
            	A collection of interface\-related statistics objects
            	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.State.Counters>`
            
            .. attribute:: description
            
            	[adapted from IETF interfaces model (RFC 7223)]  A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
            	**type**\:  str
            
            .. attribute:: enabled
            
            	[adapted from IETF interfaces model (RFC 7223)]  This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: hardware_port
            
            	References the hardware port in the device inventory
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_platform.Components.Component>`
            
            .. attribute:: ifindex
            
            	System assigned number for each interface.  Corresponds to ifIndex object in SNMP Interface MIB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_change
            
            	Date and time of the last state change of the interface (e.g., up\-to\-down transition).   This corresponds to the ifLastChange object in the standard interface MIB
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mtu
            
            	Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default \-\- e.g., 1514 bytes on an Ethernet interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: name
            
            	[adapted from IETF interfaces model (RFC 7223)]  The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list interfaces/interface[name]/state contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the corresponding state list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  The IETF model in RFC 7223 provides YANG features for the following (i.e., pre\-provisioning and arbitrary\-names), however they are omitted here\:   If the device supports pre\-provisioning of interface  configuration, the 'pre\-provisioning' feature is  advertised.   If the device allows arbitrarily named user\-controlled  interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interfaces/interface[name]/state list
            	**type**\:  str
            
            .. attribute:: oper_status
            
            	[adapted from IETF interfaces model (RFC 7223)]  The current operational state of the interface.  This leaf has the same semantics as ifOperStatus
            	**type**\:   :py:class:`OperStatus <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.State.OperStatus>`
            
            	**mandatory**\: True
            
            .. attribute:: type
            
            	[adapted from IETF interfaces model (RFC 7223)]  The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case
            	**type**\:   :py:class:`InterfaceType <ydk.models.ietf.ietf_interfaces.InterfaceType>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'oc-if'
            _revision = '2016-05-26'

            def __init__(self):
                super(Interfaces.Interface.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"counters" : ("counters", Interfaces.Interface.State.Counters)}
                self._child_list_classes = {}

                self.admin_status = YLeaf(YType.enumeration, "admin-status")

                self.description = YLeaf(YType.str, "description")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.hardware_port = YLeaf(YType.str, "openconfig-platform:hardware-port")

                self.ifindex = YLeaf(YType.uint32, "ifindex")

                self.last_change = YLeaf(YType.uint32, "last-change")

                self.mtu = YLeaf(YType.uint16, "mtu")

                self.name = YLeaf(YType.str, "name")

                self.oper_status = YLeaf(YType.enumeration, "oper-status")

                self.type = YLeaf(YType.identityref, "type")

                self.counters = Interfaces.Interface.State.Counters()
                self.counters.parent = self
                self._children_name_map["counters"] = "counters"
                self._children_yang_names.add("counters")
                self._segment_path = lambda: "state"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.State, ['admin_status', 'description', 'enabled', 'hardware_port', 'ifindex', 'last_change', 'mtu', 'name', 'oper_status', 'type'], name, value)

            class AdminStatus(Enum):
                """
                AdminStatus

                [adapted from IETF interfaces model (RFC 7223)]

                The desired state of the interface.  In RFC 7223 this leaf

                has the same read semantics as ifAdminStatus.  Here, it

                reflects the administrative state as set by enabling or

                disabling the interface.

                .. data:: UP = 0

                	Ready to pass packets.

                .. data:: DOWN = 1

                	Not ready to pass packets and not in some test mode.

                .. data:: TESTING = 2

                	In some test mode.

                """

                UP = Enum.YLeaf(0, "UP")

                DOWN = Enum.YLeaf(1, "DOWN")

                TESTING = Enum.YLeaf(2, "TESTING")


            class OperStatus(Enum):
                """
                OperStatus

                [adapted from IETF interfaces model (RFC 7223)]

                The current operational state of the interface.

                This leaf has the same semantics as ifOperStatus.

                .. data:: UP = 1

                	Ready to pass packets.

                .. data:: DOWN = 2

                	The interface does not pass any packets.

                .. data:: TESTING = 3

                	In some test mode.  No operational packets can

                	be passed.

                .. data:: UNKNOWN = 4

                	Status cannot be determined for some reason.

                .. data:: DORMANT = 5

                	Waiting for some external event.

                .. data:: NOT_PRESENT = 6

                	Some component (typically hardware) is missing.

                .. data:: LOWER_LAYER_DOWN = 7

                	Down due to state of lower-layer interface(s).

                """

                UP = Enum.YLeaf(1, "UP")

                DOWN = Enum.YLeaf(2, "DOWN")

                TESTING = Enum.YLeaf(3, "TESTING")

                UNKNOWN = Enum.YLeaf(4, "UNKNOWN")

                DORMANT = Enum.YLeaf(5, "DORMANT")

                NOT_PRESENT = Enum.YLeaf(6, "NOT_PRESENT")

                LOWER_LAYER_DOWN = Enum.YLeaf(7, "LOWER_LAYER_DOWN")



            class Counters(Entity):
                """
                A collection of interface\-related statistics objects.
                
                .. attribute:: in_broadcast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]  The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_discards
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_errors
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_multicast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]   The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a multicast address at this sub\-layer.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_octets
                
                	[adapted from IETF interfaces model (RFC 7223)]  The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_unicast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]  The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: in_unknown_protos
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_clear
                
                	Indicates the last time the interface counters were cleared
                	**type**\:  str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: out_broadcast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]  The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_discards
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_errors
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_multicast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_octets
                
                	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: out_unicast_pkts
                
                	[adapted from IETF interfaces model (RFC 7223)]  The total number of packets that higher\-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'oc-if'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.State.Counters, self).__init__()

                    self.yang_name = "counters"
                    self.yang_parent_name = "state"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.in_broadcast_pkts = YLeaf(YType.uint64, "in-broadcast-pkts")

                    self.in_discards = YLeaf(YType.uint64, "in-discards")

                    self.in_errors = YLeaf(YType.uint64, "in-errors")

                    self.in_multicast_pkts = YLeaf(YType.uint64, "in-multicast-pkts")

                    self.in_octets = YLeaf(YType.uint64, "in-octets")

                    self.in_unicast_pkts = YLeaf(YType.uint64, "in-unicast-pkts")

                    self.in_unknown_protos = YLeaf(YType.uint32, "in-unknown-protos")

                    self.last_clear = YLeaf(YType.str, "last-clear")

                    self.out_broadcast_pkts = YLeaf(YType.uint64, "out-broadcast-pkts")

                    self.out_discards = YLeaf(YType.uint64, "out-discards")

                    self.out_errors = YLeaf(YType.uint64, "out-errors")

                    self.out_multicast_pkts = YLeaf(YType.uint64, "out-multicast-pkts")

                    self.out_octets = YLeaf(YType.uint64, "out-octets")

                    self.out_unicast_pkts = YLeaf(YType.uint64, "out-unicast-pkts")
                    self._segment_path = lambda: "counters"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.State.Counters, ['in_broadcast_pkts', 'in_discards', 'in_errors', 'in_multicast_pkts', 'in_octets', 'in_unicast_pkts', 'in_unknown_protos', 'last_clear', 'out_broadcast_pkts', 'out_discards', 'out_errors', 'out_multicast_pkts', 'out_octets', 'out_unicast_pkts'], name, value)


        class Subinterfaces(Entity):
            """
            Enclosing container for the list of subinterfaces associated
            with a physical interface
            
            .. attribute:: subinterface
            
            	The list of subinterfaces (logical interfaces) associated with a physical interface
            	**type**\: list of    :py:class:`Subinterface <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
            
            

            """

            _prefix = 'oc-if'
            _revision = '2016-05-26'

            def __init__(self):
                super(Interfaces.Interface.Subinterfaces, self).__init__()

                self.yang_name = "subinterfaces"
                self.yang_parent_name = "interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"subinterface" : ("subinterface", Interfaces.Interface.Subinterfaces.Subinterface)}

                self.subinterface = YList(self)
                self._segment_path = lambda: "subinterfaces"

            def __setattr__(self, name, value):
                self._perform_setattr(Interfaces.Interface.Subinterfaces, [], name, value)


            class Subinterface(Entity):
                """
                The list of subinterfaces (logical interfaces) associated
                with a physical interface
                
                .. attribute:: index  <key>
                
                	The index number of the subinterface \-\- used to address the logical interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Config>`
                
                .. attribute:: config
                
                	Configurable items at the subinterface level
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Config>`
                
                .. attribute:: ipv4
                
                	Parameters for the IPv4 address family
                	**type**\:   :py:class:`Ipv4 <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4>`
                
                .. attribute:: ipv6
                
                	Parameters for the IPv6 address family
                	**type**\:   :py:class:`Ipv6 <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6>`
                
                .. attribute:: state
                
                	Operational state data for logical interfaces
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.State>`
                
                .. attribute:: vlan
                
                	Enclosing container for VLAN interface\-specific data on subinterfaces
                	**type**\:   :py:class:`Vlan <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Vlan>`
                
                

                """

                _prefix = 'oc-if'
                _revision = '2016-05-26'

                def __init__(self):
                    super(Interfaces.Interface.Subinterfaces.Subinterface, self).__init__()

                    self.yang_name = "subinterface"
                    self.yang_parent_name = "subinterfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Config), "ipv4" : ("ipv4", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4), "ipv6" : ("ipv6", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.State), "vlan" : ("vlan", Interfaces.Interface.Subinterfaces.Subinterface.Vlan)}
                    self._child_list_classes = {}

                    self.index = YLeaf(YType.str, "index")

                    self.config = Interfaces.Interface.Subinterfaces.Subinterface.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.ipv4 = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                    self._children_yang_names.add("ipv4")

                    self.ipv6 = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                    self._children_yang_names.add("ipv6")

                    self.state = Interfaces.Interface.Subinterfaces.Subinterface.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.vlan = Interfaces.Interface.Subinterfaces.Subinterface.Vlan()
                    self.vlan.parent = self
                    self._children_name_map["vlan"] = "vlan"
                    self._children_yang_names.add("vlan")
                    self._segment_path = lambda: "subinterface" + "[index='" + self.index.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface, ['index'], name, value)


                class Config(Entity):
                    """
                    Configurable items at the subinterface level
                    
                    .. attribute:: description
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
                    	**type**\:  str
                    
                    .. attribute:: enabled
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: index
                    
                    	The index of the subinterface, or logical interface number. On systems with no support for subinterfaces, or not using subinterfaces, this value should default to 0, i.e., the default subinterface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    .. attribute:: name
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list interfaces/interface[name]/state contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the corresponding state list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  The IETF model in RFC 7223 provides YANG features for the following (i.e., pre\-provisioning and arbitrary\-names), however they are omitted here\:   If the device supports pre\-provisioning of interface  configuration, the 'pre\-provisioning' feature is  advertised.   If the device allows arbitrarily named user\-controlled  interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interfaces/interface[name]/state list
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'oc-if'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Subinterfaces.Subinterface.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "subinterface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.description = YLeaf(YType.str, "description")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.index = YLeaf(YType.uint32, "index")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Config, ['description', 'enabled', 'index', 'name'], name, value)


                class Ipv4(Entity):
                    """
                    Parameters for the IPv4 address family.
                    
                    .. attribute:: addresses
                    
                    	Enclosing container for address list
                    	**type**\:   :py:class:`Addresses <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses>`
                    
                    .. attribute:: config
                    
                    	Top\-level IPv4 configuration data for the interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config>`
                    
                    .. attribute:: neighbors
                    
                    	Enclosing container for neighbor list
                    	**type**\:   :py:class:`Neighbors <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors>`
                    
                    .. attribute:: state
                    
                    	Top level IPv4 operational state data
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State>`
                    
                    .. attribute:: unnumbered
                    
                    	Top\-level container for setting unnumbered interfaces. Includes reference the interface that provides the address information
                    	**type**\:   :py:class:`Unnumbered <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered>`
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4, self).__init__()

                        self.yang_name = "ipv4"
                        self.yang_parent_name = "subinterface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"addresses" : ("addresses", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses), "config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config), "neighbors" : ("neighbors", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State), "unnumbered" : ("unnumbered", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered)}
                        self._child_list_classes = {}

                        self.addresses = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"
                        self._children_yang_names.add("addresses")

                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.neighbors = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors()
                        self.neighbors.parent = self
                        self._children_name_map["neighbors"] = "neighbors"
                        self._children_yang_names.add("neighbors")

                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.unnumbered = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered()
                        self.unnumbered.parent = self
                        self._children_name_map["unnumbered"] = "unnumbered"
                        self._children_yang_names.add("unnumbered")
                        self._segment_path = lambda: "openconfig-if-ip:ipv4"


                    class Addresses(Entity):
                        """
                        Enclosing container for address list
                        
                        .. attribute:: address
                        
                        	The list of configured IPv4 addresses on the interface
                        	**type**\: list of    :py:class:`Address <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"address" : ("address", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address)}

                            self.address = YList(self)
                            self._segment_path = lambda: "addresses"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses, [], name, value)


                        class Address(Entity):
                            """
                            The list of configured IPv4 addresses on the interface.
                            
                            .. attribute:: ip  <key>
                            
                            	References the configured IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Config>`
                            
                            .. attribute:: config
                            
                            	Configuration data for each configured IPv4 address on the interface
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for each IPv4 address configured on the interface
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.State>`
                            
                            .. attribute:: vrrp
                            
                            	Enclosing container for VRRP groups handled by this IP interface
                            	**type**\:   :py:class:`Vrrp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.State), "vrrp" : ("vrrp", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp)}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")

                                self.vrrp = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp()
                                self.vrrp.parent = self
                                self._children_name_map["vrrp"] = "vrrp"
                                self._children_yang_names.add("vrrp")
                                self._segment_path = lambda: "address" + "[ip='" + self.ip.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address, ['ip'], name, value)


                            class Config(Entity):
                                """
                                Configuration data for each configured IPv4
                                address on the interface
                                
                                .. attribute:: ip
                                
                                	[adapted from IETF IP model RFC 7277]  The IPv4 address on the interface
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: prefix_length
                                
                                	[adapted from IETF IP model RFC 7277]  The length of the subnet prefix
                                	**type**\:  int
                                
                                	**range:** 0..32
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip = YLeaf(YType.str, "ip")

                                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Config, ['ip', 'prefix_length'], name, value)


                            class State(Entity):
                                """
                                Operational state data for each IPv4 address
                                configured on the interface
                                
                                .. attribute:: ip
                                
                                	[adapted from IETF IP model RFC 7277]  The IPv4 address on the interface
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: origin
                                
                                	The origin of this address, e.g., statically configured, assigned by DHCP, etc.
                                	**type**\:   :py:class:`IpAddressOrigin <ydk.models.openconfig.openconfig_if_ip.IpAddressOrigin>`
                                
                                .. attribute:: prefix_length
                                
                                	[adapted from IETF IP model RFC 7277]  The length of the subnet prefix
                                	**type**\:  int
                                
                                	**range:** 0..32
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip = YLeaf(YType.str, "ip")

                                    self.origin = YLeaf(YType.enumeration, "origin")

                                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.State, ['ip', 'origin', 'prefix_length'], name, value)


                            class Vrrp(Entity):
                                """
                                Enclosing container for VRRP groups handled by this
                                IP interface
                                
                                .. attribute:: vrrp_group
                                
                                	List of VRRP groups, keyed by virtual router id
                                	**type**\: list of    :py:class:`VrrpGroup <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp, self).__init__()

                                    self.yang_name = "vrrp"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"vrrp-group" : ("vrrp_group", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup)}

                                    self.vrrp_group = YList(self)
                                    self._segment_path = lambda: "vrrp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp, [], name, value)


                                class VrrpGroup(Entity):
                                    """
                                    List of VRRP groups, keyed by virtual router id
                                    
                                    .. attribute:: virtual_router_id  <key>
                                    
                                    	References the configured virtual router id for this VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**refers to**\:  :py:class:`virtual_router_id <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config>`
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for the VRRP group
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config>`
                                    
                                    .. attribute:: interface_tracking
                                    
                                    	Top\-level container for VRRP interface tracking
                                    	**type**\:   :py:class:`InterfaceTracking <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for the VRRP group
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-ip'
                                    _revision = '2016-05-26'

                                    def __init__(self):
                                        super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup, self).__init__()

                                        self.yang_name = "vrrp-group"
                                        self.yang_parent_name = "vrrp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config), "interface-tracking" : ("interface_tracking", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State)}
                                        self._child_list_classes = {}

                                        self.virtual_router_id = YLeaf(YType.str, "virtual-router-id")

                                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.interface_tracking = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking()
                                        self.interface_tracking.parent = self
                                        self._children_name_map["interface_tracking"] = "interface-tracking"
                                        self._children_yang_names.add("interface-tracking")

                                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "vrrp-group" + "[virtual-router-id='" + self.virtual_router_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup, ['virtual_router_id'], name, value)


                                    class Config(Entity):
                                        """
                                        Configuration data for the VRRP group
                                        
                                        .. attribute:: accept_mode
                                        
                                        	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                        	**type**\:  bool
                                        
                                        	**default value**\: false
                                        
                                        .. attribute:: advertisement_interval
                                        
                                        	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                        	**type**\:  int
                                        
                                        	**range:** 1..4095
                                        
                                        	**units**\: centiseconds
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: preempt
                                        
                                        	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                        	**type**\:  bool
                                        
                                        	**default value**\: true
                                        
                                        .. attribute:: preempt_delay
                                        
                                        	Set the delay the higher priority router waits before preempting
                                        	**type**\:  int
                                        
                                        	**range:** 0..3600
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: priority
                                        
                                        	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                        	**type**\:  int
                                        
                                        	**range:** 1..254
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: virtual_address
                                        
                                        	Configure one or more virtual addresses for the VRRP group
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: virtual_router_id
                                        
                                        	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                        	**type**\:  int
                                        
                                        	**range:** 1..255
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "vrrp-group"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.accept_mode = YLeaf(YType.boolean, "accept-mode")

                                            self.advertisement_interval = YLeaf(YType.uint16, "advertisement-interval")

                                            self.preempt = YLeaf(YType.boolean, "preempt")

                                            self.preempt_delay = YLeaf(YType.uint16, "preempt-delay")

                                            self.priority = YLeaf(YType.uint8, "priority")

                                            self.virtual_address = YLeafList(YType.str, "virtual-address")

                                            self.virtual_router_id = YLeaf(YType.uint8, "virtual-router-id")
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.Config, ['accept_mode', 'advertisement_interval', 'preempt', 'preempt_delay', 'priority', 'virtual_address', 'virtual_router_id'], name, value)


                                    class InterfaceTracking(Entity):
                                        """
                                        Top\-level container for VRRP interface tracking
                                        
                                        .. attribute:: config
                                        
                                        	Configuration data for VRRP interface tracking
                                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config>`
                                        
                                        .. attribute:: state
                                        
                                        	Operational state data for VRRP interface tracking
                                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State>`
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking, self).__init__()

                                            self.yang_name = "interface-tracking"
                                            self.yang_parent_name = "vrrp-group"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State)}
                                            self._child_list_classes = {}

                                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                            self._children_yang_names.add("config")

                                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State()
                                            self.state.parent = self
                                            self._children_name_map["state"] = "state"
                                            self._children_yang_names.add("state")
                                            self._segment_path = lambda: "interface-tracking"


                                        class Config(Entity):
                                            """
                                            Configuration data for VRRP interface tracking
                                            
                                            .. attribute:: priority_decrement
                                            
                                            	Set the value to subtract from priority when the tracked interface goes down
                                            	**type**\:  int
                                            
                                            	**range:** 0..254
                                            
                                            	**default value**\: 0
                                            
                                            .. attribute:: track_interface
                                            
                                            	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                            	**type**\:  str
                                            
                                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                            
                                            

                                            """

                                            _prefix = 'oc-ip'
                                            _revision = '2016-05-26'

                                            def __init__(self):
                                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config, self).__init__()

                                                self.yang_name = "config"
                                                self.yang_parent_name = "interface-tracking"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.priority_decrement = YLeaf(YType.uint8, "priority-decrement")

                                                self.track_interface = YLeaf(YType.str, "track-interface")
                                                self._segment_path = lambda: "config"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config, ['priority_decrement', 'track_interface'], name, value)


                                        class State(Entity):
                                            """
                                            Operational state data for VRRP interface tracking
                                            
                                            .. attribute:: priority_decrement
                                            
                                            	Set the value to subtract from priority when the tracked interface goes down
                                            	**type**\:  int
                                            
                                            	**range:** 0..254
                                            
                                            	**default value**\: 0
                                            
                                            .. attribute:: track_interface
                                            
                                            	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                            	**type**\:  str
                                            
                                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                            
                                            

                                            """

                                            _prefix = 'oc-ip'
                                            _revision = '2016-05-26'

                                            def __init__(self):
                                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State, self).__init__()

                                                self.yang_name = "state"
                                                self.yang_parent_name = "interface-tracking"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.priority_decrement = YLeaf(YType.uint8, "priority-decrement")

                                                self.track_interface = YLeaf(YType.str, "track-interface")
                                                self._segment_path = lambda: "state"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State, ['priority_decrement', 'track_interface'], name, value)


                                    class State(Entity):
                                        """
                                        Operational state data for the VRRP group
                                        
                                        .. attribute:: accept_mode
                                        
                                        	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                        	**type**\:  bool
                                        
                                        	**default value**\: false
                                        
                                        .. attribute:: advertisement_interval
                                        
                                        	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                        	**type**\:  int
                                        
                                        	**range:** 1..4095
                                        
                                        	**units**\: centiseconds
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: current_priority
                                        
                                        	Operational value of the priority for the interface in the VRRP group
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: preempt
                                        
                                        	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                        	**type**\:  bool
                                        
                                        	**default value**\: true
                                        
                                        .. attribute:: preempt_delay
                                        
                                        	Set the delay the higher priority router waits before preempting
                                        	**type**\:  int
                                        
                                        	**range:** 0..3600
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: priority
                                        
                                        	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                        	**type**\:  int
                                        
                                        	**range:** 1..254
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: virtual_address
                                        
                                        	Configure one or more virtual addresses for the VRRP group
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: virtual_router_id
                                        
                                        	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                        	**type**\:  int
                                        
                                        	**range:** 1..255
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "vrrp-group"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.accept_mode = YLeaf(YType.boolean, "accept-mode")

                                            self.advertisement_interval = YLeaf(YType.uint16, "advertisement-interval")

                                            self.current_priority = YLeaf(YType.uint8, "current-priority")

                                            self.preempt = YLeaf(YType.boolean, "preempt")

                                            self.preempt_delay = YLeaf(YType.uint16, "preempt-delay")

                                            self.priority = YLeaf(YType.uint8, "priority")

                                            self.virtual_address = YLeafList(YType.str, "virtual-address")

                                            self.virtual_router_id = YLeaf(YType.uint8, "virtual-router-id")
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Addresses.Address.Vrrp.VrrpGroup.State, ['accept_mode', 'advertisement_interval', 'current_priority', 'preempt', 'preempt_delay', 'priority', 'virtual_address', 'virtual_router_id'], name, value)


                    class Config(Entity):
                        """
                        Top\-level IPv4 configuration data for the interface
                        
                        .. attribute:: enabled
                        
                        	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: mtu
                        
                        	The size, in octets, of the largest IPv4 packet that the interface will send and receive.  The server may restrict the allowed values for this leaf, depending on the interface's type.  If this leaf is not configured, the operationally used MTU depends on the interface's type
                        	**type**\:  int
                        
                        	**range:** 68..65535
                        
                        	**units**\: octets
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enabled = YLeaf(YType.boolean, "enabled")

                            self.mtu = YLeaf(YType.uint16, "mtu")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Config, ['enabled', 'mtu'], name, value)


                    class Neighbors(Entity):
                        """
                        Enclosing container for neighbor list
                        
                        .. attribute:: neighbor
                        
                        	A list of mappings from IPv4 addresses to link\-layer addresses.  Entries in this list are used as static entries in the ARP Cache
                        	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors, self).__init__()

                            self.yang_name = "neighbors"
                            self.yang_parent_name = "ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"neighbor" : ("neighbor", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor)}

                            self.neighbor = YList(self)
                            self._segment_path = lambda: "neighbors"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors, [], name, value)


                        class Neighbor(Entity):
                            """
                            A list of mappings from IPv4 addresses to
                            link\-layer addresses.
                            
                            Entries in this list are used as static entries in the
                            ARP Cache.
                            
                            .. attribute:: ip  <key>
                            
                            	References the configured IP address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.Config>`
                            
                            .. attribute:: config
                            
                            	Configuration data for each configured IPv4 address on the interface
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data for each IPv4 address configured on the interface
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.State>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor, self).__init__()

                                self.yang_name = "neighbor"
                                self.yang_parent_name = "neighbors"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.State)}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "neighbor" + "[ip='" + self.ip.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor, ['ip'], name, value)


                            class Config(Entity):
                                """
                                Configuration data for each configured IPv4
                                address on the interface
                                
                                .. attribute:: ip
                                
                                	The IPv4 address of the neighbor node
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: link_layer_address
                                
                                	The link\-layer address of the neighbor node
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip = YLeaf(YType.str, "ip")

                                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.Config, ['ip', 'link_layer_address'], name, value)


                            class State(Entity):
                                """
                                Operational state data for each IPv4 address
                                configured on the interface
                                
                                .. attribute:: ip
                                
                                	The IPv4 address of the neighbor node
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: link_layer_address
                                
                                	The link\-layer address of the neighbor node
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                	**mandatory**\: True
                                
                                .. attribute:: origin
                                
                                	The origin of this neighbor entry, static or dynamic
                                	**type**\:   :py:class:`NeighborOrigin <ydk.models.openconfig.openconfig_if_ip.NeighborOrigin>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip = YLeaf(YType.str, "ip")

                                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                                    self.origin = YLeaf(YType.enumeration, "origin")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Neighbors.Neighbor.State, ['ip', 'link_layer_address', 'origin'], name, value)


                    class State(Entity):
                        """
                        Top level IPv4 operational state data
                        
                        .. attribute:: enabled
                        
                        	Controls whether IPv4 is enabled or disabled on this interface.  When IPv4 is enabled, this interface is connected to an IPv4 stack, and the interface can send and receive IPv4 packets
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: mtu
                        
                        	The size, in octets, of the largest IPv4 packet that the interface will send and receive.  The server may restrict the allowed values for this leaf, depending on the interface's type.  If this leaf is not configured, the operationally used MTU depends on the interface's type
                        	**type**\:  int
                        
                        	**range:** 68..65535
                        
                        	**units**\: octets
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enabled = YLeaf(YType.boolean, "enabled")

                            self.mtu = YLeaf(YType.uint16, "mtu")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.State, ['enabled', 'mtu'], name, value)


                    class Unnumbered(Entity):
                        """
                        Top\-level container for setting unnumbered interfaces.
                        Includes reference the interface that provides the
                        address information
                        
                        .. attribute:: config
                        
                        	Configuration data for unnumbered interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.Config>`
                        
                        .. attribute:: interface_ref
                        
                        	Reference to an interface or subinterface
                        	**type**\:   :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef>`
                        
                        .. attribute:: state
                        
                        	Operational state data for unnumbered interfaces
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.State>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered, self).__init__()

                            self.yang_name = "unnumbered"
                            self.yang_parent_name = "ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.Config), "interface-ref" : ("interface_ref", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.State)}
                            self._child_list_classes = {}

                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.interface_ref = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef()
                            self.interface_ref.parent = self
                            self._children_name_map["interface_ref"] = "interface-ref"
                            self._children_yang_names.add("interface-ref")

                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "unnumbered"


                        class Config(Entity):
                            """
                            Configuration data for unnumbered interface
                            
                            .. attribute:: enabled
                            
                            	Indicates that the subinterface is unnumbered.  By default the subinterface is numbered, i.e., expected to have an IP address configuration
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "unnumbered"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enabled = YLeaf(YType.boolean, "enabled")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.Config, ['enabled'], name, value)


                        class InterfaceRef(Entity):
                            """
                            Reference to an interface or subinterface
                            
                            .. attribute:: config
                            
                            	Configured reference to interface / subinterface
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state for interface\-ref
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.State>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef, self).__init__()

                                self.yang_name = "interface-ref"
                                self.yang_parent_name = "unnumbered"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.State)}
                                self._child_list_classes = {}

                                self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "interface-ref"


                            class Config(Entity):
                                """
                                Configured reference to interface / subinterface
                                
                                .. attribute:: interface
                                
                                	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: subinterface
                                
                                	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "interface-ref"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.interface = YLeaf(YType.str, "interface")

                                    self.subinterface = YLeaf(YType.str, "subinterface")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.Config, ['interface', 'subinterface'], name, value)


                            class State(Entity):
                                """
                                Operational state for interface\-ref
                                
                                .. attribute:: interface
                                
                                	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: subinterface
                                
                                	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "interface-ref"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.interface = YLeaf(YType.str, "interface")

                                    self.subinterface = YLeaf(YType.str, "subinterface")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.InterfaceRef.State, ['interface', 'subinterface'], name, value)


                        class State(Entity):
                            """
                            Operational state data for unnumbered interfaces
                            
                            .. attribute:: enabled
                            
                            	Indicates that the subinterface is unnumbered.  By default the subinterface is numbered, i.e., expected to have an IP address configuration
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "unnumbered"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enabled = YLeaf(YType.boolean, "enabled")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv4.Unnumbered.State, ['enabled'], name, value)


                class Ipv6(Entity):
                    """
                    Parameters for the IPv6 address family.
                    
                    .. attribute:: addresses
                    
                    	Enclosing container for address list
                    	**type**\:   :py:class:`Addresses <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses>`
                    
                    .. attribute:: config
                    
                    	Top\-level config data for the IPv6 interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config>`
                    
                    .. attribute:: neighbors
                    
                    	Enclosing container for list of IPv6 neighbors
                    	**type**\:   :py:class:`Neighbors <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors>`
                    
                    .. attribute:: state
                    
                    	Top\-level operational state data for the IPv6 interface
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State>`
                    
                    .. attribute:: unnumbered
                    
                    	Top\-level container for setting unnumbered interfaces. Includes reference the interface that provides the address information
                    	**type**\:   :py:class:`Unnumbered <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered>`
                    
                    

                    """

                    _prefix = 'oc-ip'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6, self).__init__()

                        self.yang_name = "ipv6"
                        self.yang_parent_name = "subinterface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"addresses" : ("addresses", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses), "config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config), "neighbors" : ("neighbors", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State), "unnumbered" : ("unnumbered", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered)}
                        self._child_list_classes = {}

                        self.addresses = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"
                        self._children_yang_names.add("addresses")

                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.neighbors = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors()
                        self.neighbors.parent = self
                        self._children_name_map["neighbors"] = "neighbors"
                        self._children_yang_names.add("neighbors")

                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.unnumbered = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered()
                        self.unnumbered.parent = self
                        self._children_name_map["unnumbered"] = "unnumbered"
                        self._children_yang_names.add("unnumbered")
                        self._segment_path = lambda: "openconfig-if-ip:ipv6"


                    class Addresses(Entity):
                        """
                        Enclosing container for address list
                        
                        .. attribute:: address
                        
                        	The list of configured IPv6 addresses on the interface
                        	**type**\: list of    :py:class:`Address <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"address" : ("address", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address)}

                            self.address = YList(self)
                            self._segment_path = lambda: "addresses"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses, [], name, value)


                        class Address(Entity):
                            """
                            The list of configured IPv6 addresses on the interface.
                            
                            .. attribute:: ip  <key>
                            
                            	References the configured IP address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Config>`
                            
                            .. attribute:: config
                            
                            	Configuration data for each IPv6 address on the interface
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Config>`
                            
                            .. attribute:: state
                            
                            	State data for each IPv6 address on the interface
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.State>`
                            
                            .. attribute:: vrrp
                            
                            	Enclosing container for VRRP groups handled by this IP interface
                            	**type**\:   :py:class:`Vrrp <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.State), "vrrp" : ("vrrp", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp)}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")

                                self.vrrp = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp()
                                self.vrrp.parent = self
                                self._children_name_map["vrrp"] = "vrrp"
                                self._children_yang_names.add("vrrp")
                                self._segment_path = lambda: "address" + "[ip='" + self.ip.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address, ['ip'], name, value)


                            class Config(Entity):
                                """
                                Configuration data for each IPv6 address on
                                the interface
                                
                                .. attribute:: ip
                                
                                	[adapted from IETF IP model RFC 7277]  The IPv6 address on the interface
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: prefix_length
                                
                                	[adapted from IETF IP model RFC 7277]  The length of the subnet prefix
                                	**type**\:  int
                                
                                	**range:** 0..128
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip = YLeaf(YType.str, "ip")

                                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Config, ['ip', 'prefix_length'], name, value)


                            class State(Entity):
                                """
                                State data for each IPv6 address on the
                                interface
                                
                                .. attribute:: ip
                                
                                	[adapted from IETF IP model RFC 7277]  The IPv6 address on the interface
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: origin
                                
                                	[adapted from IETF IP model RFC 7277]  The origin of this address, e.g., static, dhcp, etc
                                	**type**\:   :py:class:`IpAddressOrigin <ydk.models.openconfig.openconfig_if_ip.IpAddressOrigin>`
                                
                                .. attribute:: prefix_length
                                
                                	[adapted from IETF IP model RFC 7277]  The length of the subnet prefix
                                	**type**\:  int
                                
                                	**range:** 0..128
                                
                                	**mandatory**\: True
                                
                                .. attribute:: status
                                
                                	[adapted from IETF IP model RFC 7277]  The status of an address.  Most of the states correspond to states from the IPv6 Stateless Address Autoconfiguration protocol
                                	**type**\:   :py:class:`Status <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.State.Status>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip = YLeaf(YType.str, "ip")

                                    self.origin = YLeaf(YType.enumeration, "origin")

                                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                                    self.status = YLeaf(YType.enumeration, "status")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.State, ['ip', 'origin', 'prefix_length', 'status'], name, value)

                                class Status(Enum):
                                    """
                                    Status

                                    [adapted from IETF IP model RFC 7277]

                                    The status of an address.  Most of the states correspond

                                    to states from the IPv6 Stateless Address

                                    Autoconfiguration protocol.

                                    .. data:: PREFERRED = 0

                                    	This is a valid address that can appear as the

                                    	destination or source address of a packet.

                                    .. data:: DEPRECATED = 1

                                    	This is a valid but deprecated address that should

                                    	no longer be used as a source address in new

                                    	communications, but packets addressed to such an

                                    	address are processed as expected.

                                    .. data:: INVALID = 2

                                    	This isn't a valid address, and it shouldn't appear

                                    	as the destination or source address of a packet.

                                    .. data:: INACCESSIBLE = 3

                                    	The address is not accessible because the interface

                                    	to which this address is assigned is not

                                    	operational.

                                    .. data:: UNKNOWN = 4

                                    	The status cannot be determined for some reason.

                                    .. data:: TENTATIVE = 5

                                    	The uniqueness of the address on the link is being

                                    	verified.  Addresses in this state should not be

                                    	used for general communication and should only be

                                    	used to determine the uniqueness of the address.

                                    .. data:: DUPLICATE = 6

                                    	The address has been determined to be non-unique on

                                    	the link and so must not be used.

                                    .. data:: OPTIMISTIC = 7

                                    	The address is available for use, subject to

                                    	restrictions, while its uniqueness on a link is

                                    	being verified.

                                    """

                                    PREFERRED = Enum.YLeaf(0, "PREFERRED")

                                    DEPRECATED = Enum.YLeaf(1, "DEPRECATED")

                                    INVALID = Enum.YLeaf(2, "INVALID")

                                    INACCESSIBLE = Enum.YLeaf(3, "INACCESSIBLE")

                                    UNKNOWN = Enum.YLeaf(4, "UNKNOWN")

                                    TENTATIVE = Enum.YLeaf(5, "TENTATIVE")

                                    DUPLICATE = Enum.YLeaf(6, "DUPLICATE")

                                    OPTIMISTIC = Enum.YLeaf(7, "OPTIMISTIC")



                            class Vrrp(Entity):
                                """
                                Enclosing container for VRRP groups handled by this
                                IP interface
                                
                                .. attribute:: vrrp_group
                                
                                	List of VRRP groups, keyed by virtual router id
                                	**type**\: list of    :py:class:`VrrpGroup <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp, self).__init__()

                                    self.yang_name = "vrrp"
                                    self.yang_parent_name = "address"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"vrrp-group" : ("vrrp_group", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup)}

                                    self.vrrp_group = YList(self)
                                    self._segment_path = lambda: "vrrp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp, [], name, value)


                                class VrrpGroup(Entity):
                                    """
                                    List of VRRP groups, keyed by virtual router id
                                    
                                    .. attribute:: virtual_router_id  <key>
                                    
                                    	References the configured virtual router id for this VRRP group
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**refers to**\:  :py:class:`virtual_router_id <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config>`
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data for the VRRP group
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config>`
                                    
                                    .. attribute:: interface_tracking
                                    
                                    	Top\-level container for VRRP interface tracking
                                    	**type**\:   :py:class:`InterfaceTracking <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data for the VRRP group
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State>`
                                    
                                    

                                    """

                                    _prefix = 'oc-ip'
                                    _revision = '2016-05-26'

                                    def __init__(self):
                                        super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup, self).__init__()

                                        self.yang_name = "vrrp-group"
                                        self.yang_parent_name = "vrrp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config), "interface-tracking" : ("interface_tracking", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State)}
                                        self._child_list_classes = {}

                                        self.virtual_router_id = YLeaf(YType.str, "virtual-router-id")

                                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.interface_tracking = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking()
                                        self.interface_tracking.parent = self
                                        self._children_name_map["interface_tracking"] = "interface-tracking"
                                        self._children_yang_names.add("interface-tracking")

                                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "vrrp-group" + "[virtual-router-id='" + self.virtual_router_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup, ['virtual_router_id'], name, value)


                                    class Config(Entity):
                                        """
                                        Configuration data for the VRRP group
                                        
                                        .. attribute:: accept_mode
                                        
                                        	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                        	**type**\:  bool
                                        
                                        	**default value**\: false
                                        
                                        .. attribute:: advertisement_interval
                                        
                                        	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                        	**type**\:  int
                                        
                                        	**range:** 1..4095
                                        
                                        	**units**\: centiseconds
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: preempt
                                        
                                        	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                        	**type**\:  bool
                                        
                                        	**default value**\: true
                                        
                                        .. attribute:: preempt_delay
                                        
                                        	Set the delay the higher priority router waits before preempting
                                        	**type**\:  int
                                        
                                        	**range:** 0..3600
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: priority
                                        
                                        	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                        	**type**\:  int
                                        
                                        	**range:** 1..254
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: virtual_address
                                        
                                        	Configure one or more virtual addresses for the VRRP group
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: virtual_link_local
                                        
                                        	For VRRP on IPv6 interfaces, sets the virtual link local address
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: virtual_router_id
                                        
                                        	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                        	**type**\:  int
                                        
                                        	**range:** 1..255
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "vrrp-group"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.accept_mode = YLeaf(YType.boolean, "accept-mode")

                                            self.advertisement_interval = YLeaf(YType.uint16, "advertisement-interval")

                                            self.preempt = YLeaf(YType.boolean, "preempt")

                                            self.preempt_delay = YLeaf(YType.uint16, "preempt-delay")

                                            self.priority = YLeaf(YType.uint8, "priority")

                                            self.virtual_address = YLeafList(YType.str, "virtual-address")

                                            self.virtual_link_local = YLeaf(YType.str, "virtual-link-local")

                                            self.virtual_router_id = YLeaf(YType.uint8, "virtual-router-id")
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.Config, ['accept_mode', 'advertisement_interval', 'preempt', 'preempt_delay', 'priority', 'virtual_address', 'virtual_link_local', 'virtual_router_id'], name, value)


                                    class InterfaceTracking(Entity):
                                        """
                                        Top\-level container for VRRP interface tracking
                                        
                                        .. attribute:: config
                                        
                                        	Configuration data for VRRP interface tracking
                                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config>`
                                        
                                        .. attribute:: state
                                        
                                        	Operational state data for VRRP interface tracking
                                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State>`
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking, self).__init__()

                                            self.yang_name = "interface-tracking"
                                            self.yang_parent_name = "vrrp-group"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State)}
                                            self._child_list_classes = {}

                                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"
                                            self._children_yang_names.add("config")

                                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State()
                                            self.state.parent = self
                                            self._children_name_map["state"] = "state"
                                            self._children_yang_names.add("state")
                                            self._segment_path = lambda: "interface-tracking"


                                        class Config(Entity):
                                            """
                                            Configuration data for VRRP interface tracking
                                            
                                            .. attribute:: priority_decrement
                                            
                                            	Set the value to subtract from priority when the tracked interface goes down
                                            	**type**\:  int
                                            
                                            	**range:** 0..254
                                            
                                            	**default value**\: 0
                                            
                                            .. attribute:: track_interface
                                            
                                            	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                            	**type**\:  str
                                            
                                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                            
                                            

                                            """

                                            _prefix = 'oc-ip'
                                            _revision = '2016-05-26'

                                            def __init__(self):
                                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config, self).__init__()

                                                self.yang_name = "config"
                                                self.yang_parent_name = "interface-tracking"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.priority_decrement = YLeaf(YType.uint8, "priority-decrement")

                                                self.track_interface = YLeaf(YType.str, "track-interface")
                                                self._segment_path = lambda: "config"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.Config, ['priority_decrement', 'track_interface'], name, value)


                                        class State(Entity):
                                            """
                                            Operational state data for VRRP interface tracking
                                            
                                            .. attribute:: priority_decrement
                                            
                                            	Set the value to subtract from priority when the tracked interface goes down
                                            	**type**\:  int
                                            
                                            	**range:** 0..254
                                            
                                            	**default value**\: 0
                                            
                                            .. attribute:: track_interface
                                            
                                            	Sets an interface that should be tracked for up/down events to dynamically change the priority state of the VRRP group, and potentially change the mastership if the tracked interface going down lowers the priority sufficiently
                                            	**type**\:  str
                                            
                                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                            
                                            

                                            """

                                            _prefix = 'oc-ip'
                                            _revision = '2016-05-26'

                                            def __init__(self):
                                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State, self).__init__()

                                                self.yang_name = "state"
                                                self.yang_parent_name = "interface-tracking"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.priority_decrement = YLeaf(YType.uint8, "priority-decrement")

                                                self.track_interface = YLeaf(YType.str, "track-interface")
                                                self._segment_path = lambda: "state"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.InterfaceTracking.State, ['priority_decrement', 'track_interface'], name, value)


                                    class State(Entity):
                                        """
                                        Operational state data for the VRRP group
                                        
                                        .. attribute:: accept_mode
                                        
                                        	Configure whether packets destined for virtual addresses are accepted even when the virtual address is not owned by the router interface
                                        	**type**\:  bool
                                        
                                        	**default value**\: false
                                        
                                        .. attribute:: advertisement_interval
                                        
                                        	Sets the interval between successive VRRP advertisements \-\- RFC 5798 defines this as a 12\-bit value expressed as 0.1 seconds, with default 100, i.e., 1 second.  Several implementation express this in units of seconds
                                        	**type**\:  int
                                        
                                        	**range:** 1..4095
                                        
                                        	**units**\: centiseconds
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: current_priority
                                        
                                        	Operational value of the priority for the interface in the VRRP group
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: preempt
                                        
                                        	When set to true, enables preemption by a higher priority backup router of a lower priority master router
                                        	**type**\:  bool
                                        
                                        	**default value**\: true
                                        
                                        .. attribute:: preempt_delay
                                        
                                        	Set the delay the higher priority router waits before preempting
                                        	**type**\:  int
                                        
                                        	**range:** 0..3600
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: priority
                                        
                                        	Specifies the sending VRRP interface's priority for the virtual router.  Higher values equal higher priority
                                        	**type**\:  int
                                        
                                        	**range:** 1..254
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: virtual_address
                                        
                                        	Configure one or more virtual addresses for the VRRP group
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  list of str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: virtual_link_local
                                        
                                        	For VRRP on IPv6 interfaces, sets the virtual link local address
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        
                                        ----
                                        .. attribute:: virtual_router_id
                                        
                                        	Set the virtual router id for use by the VRRP group.  This usually also determines the virtual MAC address that is generated for the VRRP group
                                        	**type**\:  int
                                        
                                        	**range:** 1..255
                                        
                                        

                                        """

                                        _prefix = 'oc-ip'
                                        _revision = '2016-05-26'

                                        def __init__(self):
                                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "vrrp-group"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.accept_mode = YLeaf(YType.boolean, "accept-mode")

                                            self.advertisement_interval = YLeaf(YType.uint16, "advertisement-interval")

                                            self.current_priority = YLeaf(YType.uint8, "current-priority")

                                            self.preempt = YLeaf(YType.boolean, "preempt")

                                            self.preempt_delay = YLeaf(YType.uint16, "preempt-delay")

                                            self.priority = YLeaf(YType.uint8, "priority")

                                            self.virtual_address = YLeafList(YType.str, "virtual-address")

                                            self.virtual_link_local = YLeaf(YType.str, "virtual-link-local")

                                            self.virtual_router_id = YLeaf(YType.uint8, "virtual-router-id")
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Addresses.Address.Vrrp.VrrpGroup.State, ['accept_mode', 'advertisement_interval', 'current_priority', 'preempt', 'preempt_delay', 'priority', 'virtual_address', 'virtual_link_local', 'virtual_router_id'], name, value)


                    class Config(Entity):
                        """
                        Top\-level config data for the IPv6 interface
                        
                        .. attribute:: dup_addr_detect_transmits
                        
                        	[adapted from IETF IP model RFC 7277]  The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 1
                        
                        .. attribute:: enabled
                        
                        	[adapted from IETF IP model RFC 7277]  Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: mtu
                        
                        	[adapted from IETF IP model RFC 7277]  The size, in octets, of the largest IPv6 packet that the interface will send and receive.  The server may restrict the allowed values for this leaf, depending on the interface's type.  If this leaf is not configured, the operationally used MTU depends on the interface's type
                        	**type**\:  int
                        
                        	**range:** 1280..4294967295
                        
                        	**units**\: octets
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.dup_addr_detect_transmits = YLeaf(YType.uint32, "dup-addr-detect-transmits")

                            self.enabled = YLeaf(YType.boolean, "enabled")

                            self.mtu = YLeaf(YType.uint32, "mtu")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Config, ['dup_addr_detect_transmits', 'enabled', 'mtu'], name, value)


                    class Neighbors(Entity):
                        """
                        Enclosing container for list of IPv6 neighbors
                        
                        .. attribute:: neighbor
                        
                        	List of IPv6 neighbors
                        	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors, self).__init__()

                            self.yang_name = "neighbors"
                            self.yang_parent_name = "ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"neighbor" : ("neighbor", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor)}

                            self.neighbor = YList(self)
                            self._segment_path = lambda: "neighbors"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors, [], name, value)


                        class Neighbor(Entity):
                            """
                            List of IPv6 neighbors
                            
                            .. attribute:: ip  <key>
                            
                            	References the configured IP neighbor address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**refers to**\:  :py:class:`ip <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.Config>`
                            
                            .. attribute:: config
                            
                            	Configuration data for each IPv6 address on the interface
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.Config>`
                            
                            .. attribute:: state
                            
                            	State data for each IPv6 address on the interface
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.State>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor, self).__init__()

                                self.yang_name = "neighbor"
                                self.yang_parent_name = "neighbors"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.State)}
                                self._child_list_classes = {}

                                self.ip = YLeaf(YType.str, "ip")

                                self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "neighbor" + "[ip='" + self.ip.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor, ['ip'], name, value)


                            class Config(Entity):
                                """
                                Configuration data for each IPv6 address on
                                the interface
                                
                                .. attribute:: ip
                                
                                	[adapted from IETF IP model RFC 7277]  The IPv6 address of the neighbor node
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: link_layer_address
                                
                                	[adapted from IETF IP model RFC 7277]  The link\-layer address of the neighbor node
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip = YLeaf(YType.str, "ip")

                                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.Config, ['ip', 'link_layer_address'], name, value)


                            class State(Entity):
                                """
                                State data for each IPv6 address on the
                                interface
                                
                                .. attribute:: ip
                                
                                	[adapted from IETF IP model RFC 7277]  The IPv6 address of the neighbor node
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: is_router
                                
                                	[adapted from IETF IP model RFC 7277]  Indicates that the neighbor node acts as a router
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: link_layer_address
                                
                                	[adapted from IETF IP model RFC 7277]  The link\-layer address of the neighbor node
                                	**type**\:  str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                	**mandatory**\: True
                                
                                .. attribute:: neighbor_state
                                
                                	[adapted from IETF IP model RFC 7277]  The Neighbor Unreachability Detection state of this entry
                                	**type**\:   :py:class:`NeighborState <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.State.NeighborState>`
                                
                                .. attribute:: origin
                                
                                	[adapted from IETF IP model RFC 7277]  The origin of this neighbor entry
                                	**type**\:   :py:class:`NeighborOrigin <ydk.models.openconfig.openconfig_if_ip.NeighborOrigin>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ip = YLeaf(YType.str, "ip")

                                    self.is_router = YLeaf(YType.empty, "is-router")

                                    self.link_layer_address = YLeaf(YType.str, "link-layer-address")

                                    self.neighbor_state = YLeaf(YType.enumeration, "neighbor-state")

                                    self.origin = YLeaf(YType.enumeration, "origin")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Neighbors.Neighbor.State, ['ip', 'is_router', 'link_layer_address', 'neighbor_state', 'origin'], name, value)

                                class NeighborState(Enum):
                                    """
                                    NeighborState

                                    [adapted from IETF IP model RFC 7277]

                                    The Neighbor Unreachability Detection state of this

                                    entry.

                                    .. data:: INCOMPLETE = 0

                                    	Address resolution is in progress, and the link-layer

                                    	     address of the neighbor has not yet been

                                    	     determined.

                                    .. data:: REACHABLE = 1

                                    	Roughly speaking, the neighbor is known to have been

                                    	     reachable recently (within tens of seconds ago).

                                    .. data:: STALE = 2

                                    	The neighbor is no longer known to be reachable, but

                                    	     until traffic is sent to the neighbor no attempt

                                    	     should be made to verify its reachability.

                                    .. data:: DELAY = 3

                                    	The neighbor is no longer known to be reachable, and

                                    	     traffic has recently been sent to the neighbor.

                                    	     Rather than probe the neighbor immediately, however,

                                    	     delay sending probes for a short while in order to

                                    	     give upper-layer protocols a chance to provide

                                    	     reachability confirmation.

                                    .. data:: PROBE = 4

                                    	The neighbor is no longer known to be reachable, and

                                    	     unicast Neighbor Solicitation probes are being sent

                                    	     to verify reachability.

                                    """

                                    INCOMPLETE = Enum.YLeaf(0, "INCOMPLETE")

                                    REACHABLE = Enum.YLeaf(1, "REACHABLE")

                                    STALE = Enum.YLeaf(2, "STALE")

                                    DELAY = Enum.YLeaf(3, "DELAY")

                                    PROBE = Enum.YLeaf(4, "PROBE")



                    class State(Entity):
                        """
                        Top\-level operational state data for the IPv6 interface
                        
                        .. attribute:: dup_addr_detect_transmits
                        
                        	[adapted from IETF IP model RFC 7277]  The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address.  A value of zero indicates that Duplicate Address Detection is not performed on tentative addresses.  A value of one indicates a single transmission with no follow\-up retransmissions
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 1
                        
                        .. attribute:: enabled
                        
                        	[adapted from IETF IP model RFC 7277]  Controls whether IPv6 is enabled or disabled on this interface.  When IPv6 is enabled, this interface is connected to an IPv6 stack, and the interface can send and receive IPv6 packets
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: mtu
                        
                        	[adapted from IETF IP model RFC 7277]  The size, in octets, of the largest IPv6 packet that the interface will send and receive.  The server may restrict the allowed values for this leaf, depending on the interface's type.  If this leaf is not configured, the operationally used MTU depends on the interface's type
                        	**type**\:  int
                        
                        	**range:** 1280..4294967295
                        
                        	**units**\: octets
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.dup_addr_detect_transmits = YLeaf(YType.uint32, "dup-addr-detect-transmits")

                            self.enabled = YLeaf(YType.boolean, "enabled")

                            self.mtu = YLeaf(YType.uint32, "mtu")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.State, ['dup_addr_detect_transmits', 'enabled', 'mtu'], name, value)


                    class Unnumbered(Entity):
                        """
                        Top\-level container for setting unnumbered interfaces.
                        Includes reference the interface that provides the
                        address information
                        
                        .. attribute:: config
                        
                        	Configuration data for unnumbered interface
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.Config>`
                        
                        .. attribute:: interface_ref
                        
                        	Reference to an interface or subinterface
                        	**type**\:   :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef>`
                        
                        .. attribute:: state
                        
                        	Operational state data for unnumbered interfaces
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.State>`
                        
                        

                        """

                        _prefix = 'oc-ip'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered, self).__init__()

                            self.yang_name = "unnumbered"
                            self.yang_parent_name = "ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.Config), "interface-ref" : ("interface_ref", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.State)}
                            self._child_list_classes = {}

                            self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.interface_ref = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef()
                            self.interface_ref.parent = self
                            self._children_name_map["interface_ref"] = "interface-ref"
                            self._children_yang_names.add("interface-ref")

                            self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "unnumbered"


                        class Config(Entity):
                            """
                            Configuration data for unnumbered interface
                            
                            .. attribute:: enabled
                            
                            	Indicates that the subinterface is unnumbered.  By default the subinterface is numbered, i.e., expected to have an IP address configuration
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "unnumbered"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enabled = YLeaf(YType.boolean, "enabled")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.Config, ['enabled'], name, value)


                        class InterfaceRef(Entity):
                            """
                            Reference to an interface or subinterface
                            
                            .. attribute:: config
                            
                            	Configured reference to interface / subinterface
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state for interface\-ref
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.State>`
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef, self).__init__()

                                self.yang_name = "interface-ref"
                                self.yang_parent_name = "unnumbered"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.State)}
                                self._child_list_classes = {}

                                self.config = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "interface-ref"


                            class Config(Entity):
                                """
                                Configured reference to interface / subinterface
                                
                                .. attribute:: interface
                                
                                	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: subinterface
                                
                                	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "interface-ref"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.interface = YLeaf(YType.str, "interface")

                                    self.subinterface = YLeaf(YType.str, "subinterface")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.Config, ['interface', 'subinterface'], name, value)


                            class State(Entity):
                                """
                                Operational state for interface\-ref
                                
                                .. attribute:: interface
                                
                                	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: subinterface
                                
                                	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                                
                                

                                """

                                _prefix = 'oc-ip'
                                _revision = '2016-05-26'

                                def __init__(self):
                                    super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "interface-ref"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.interface = YLeaf(YType.str, "interface")

                                    self.subinterface = YLeaf(YType.str, "subinterface")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.InterfaceRef.State, ['interface', 'subinterface'], name, value)


                        class State(Entity):
                            """
                            Operational state data for unnumbered interfaces
                            
                            .. attribute:: enabled
                            
                            	Indicates that the subinterface is unnumbered.  By default the subinterface is numbered, i.e., expected to have an IP address configuration
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'oc-ip'
                            _revision = '2016-05-26'

                            def __init__(self):
                                super(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "unnumbered"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enabled = YLeaf(YType.boolean, "enabled")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Ipv6.Unnumbered.State, ['enabled'], name, value)


                class State(Entity):
                    """
                    Operational state data for logical interfaces
                    
                    .. attribute:: admin_status
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  The desired state of the interface.  In RFC 7223 this leaf has the same read semantics as ifAdminStatus.  Here, it reflects the administrative state as set by enabling or disabling the interface
                    	**type**\:   :py:class:`AdminStatus <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.State.AdminStatus>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: counters
                    
                    	A collection of interface\-related statistics objects
                    	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.State.Counters>`
                    
                    .. attribute:: description
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non\-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports '\:startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy\-config from 'running' to 'startup'.  If the device does not support '\:startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore
                    	**type**\:  str
                    
                    .. attribute:: enabled
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  This leaf contains the configured, desired state of the interface.  Systems that implement the IF\-MIB use the value of this leaf in the 'running' datastore to set IF\-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    .. attribute:: ifindex
                    
                    	System assigned number for each interface.  Corresponds to ifIndex object in SNMP Interface MIB
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: index
                    
                    	The index of the subinterface, or logical interface number. On systems with no support for subinterfaces, or not using subinterfaces, this value should default to 0, i.e., the default subinterface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**default value**\: 0
                    
                    .. attribute:: last_change
                    
                    	Date and time of the last state change of the interface (e.g., up\-to\-down transition).   This corresponds to the ifLastChange object in the standard interface MIB
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  The name of the interface.  A device MAY restrict the allowed values for this leaf, possibly depending on the type of the interface. For system\-controlled interfaces, this leaf is the device\-specific name of the interface.  The 'config false' list interfaces/interface[name]/state contains the currently existing interfaces on the device.  If a client tries to create configuration for a system\-controlled interface that is not present in the corresponding state list, the server MAY reject the request if the implementation does not support pre\-provisioning of interfaces or if the name refers to an interface that can never exist in the system.  A NETCONF server MUST reply with an rpc\-error with the error\-tag 'invalid\-value' in this case.  The IETF model in RFC 7223 provides YANG features for the following (i.e., pre\-provisioning and arbitrary\-names), however they are omitted here\:   If the device supports pre\-provisioning of interface  configuration, the 'pre\-provisioning' feature is  advertised.   If the device allows arbitrarily named user\-controlled  interfaces, the 'arbitrary\-names' feature is advertised.  When a configured user\-controlled interface is created by the system, it is instantiated with the same name in the /interfaces/interface[name]/state list
                    	**type**\:  str
                    
                    .. attribute:: oper_status
                    
                    	[adapted from IETF interfaces model (RFC 7223)]  The current operational state of the interface.  This leaf has the same semantics as ifOperStatus
                    	**type**\:   :py:class:`OperStatus <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.State.OperStatus>`
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'oc-if'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Subinterfaces.Subinterface.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "subinterface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"counters" : ("counters", Interfaces.Interface.Subinterfaces.Subinterface.State.Counters)}
                        self._child_list_classes = {}

                        self.admin_status = YLeaf(YType.enumeration, "admin-status")

                        self.description = YLeaf(YType.str, "description")

                        self.enabled = YLeaf(YType.boolean, "enabled")

                        self.ifindex = YLeaf(YType.uint32, "ifindex")

                        self.index = YLeaf(YType.uint32, "index")

                        self.last_change = YLeaf(YType.uint32, "last-change")

                        self.name = YLeaf(YType.str, "name")

                        self.oper_status = YLeaf(YType.enumeration, "oper-status")

                        self.counters = Interfaces.Interface.Subinterfaces.Subinterface.State.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._children_yang_names.add("counters")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.State, ['admin_status', 'description', 'enabled', 'ifindex', 'index', 'last_change', 'name', 'oper_status'], name, value)

                    class AdminStatus(Enum):
                        """
                        AdminStatus

                        [adapted from IETF interfaces model (RFC 7223)]

                        The desired state of the interface.  In RFC 7223 this leaf

                        has the same read semantics as ifAdminStatus.  Here, it

                        reflects the administrative state as set by enabling or

                        disabling the interface.

                        .. data:: UP = 0

                        	Ready to pass packets.

                        .. data:: DOWN = 1

                        	Not ready to pass packets and not in some test mode.

                        .. data:: TESTING = 2

                        	In some test mode.

                        """

                        UP = Enum.YLeaf(0, "UP")

                        DOWN = Enum.YLeaf(1, "DOWN")

                        TESTING = Enum.YLeaf(2, "TESTING")


                    class OperStatus(Enum):
                        """
                        OperStatus

                        [adapted from IETF interfaces model (RFC 7223)]

                        The current operational state of the interface.

                        This leaf has the same semantics as ifOperStatus.

                        .. data:: UP = 1

                        	Ready to pass packets.

                        .. data:: DOWN = 2

                        	The interface does not pass any packets.

                        .. data:: TESTING = 3

                        	In some test mode.  No operational packets can

                        	be passed.

                        .. data:: UNKNOWN = 4

                        	Status cannot be determined for some reason.

                        .. data:: DORMANT = 5

                        	Waiting for some external event.

                        .. data:: NOT_PRESENT = 6

                        	Some component (typically hardware) is missing.

                        .. data:: LOWER_LAYER_DOWN = 7

                        	Down due to state of lower-layer interface(s).

                        """

                        UP = Enum.YLeaf(1, "UP")

                        DOWN = Enum.YLeaf(2, "DOWN")

                        TESTING = Enum.YLeaf(3, "TESTING")

                        UNKNOWN = Enum.YLeaf(4, "UNKNOWN")

                        DORMANT = Enum.YLeaf(5, "DORMANT")

                        NOT_PRESENT = Enum.YLeaf(6, "NOT_PRESENT")

                        LOWER_LAYER_DOWN = Enum.YLeaf(7, "LOWER_LAYER_DOWN")



                    class Counters(Entity):
                        """
                        A collection of interface\-related statistics objects.
                        
                        .. attribute:: in_broadcast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_discards
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The number of inbound packets that were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher\-layer protocol.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_errors
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher\-layer protocol.  For character\- oriented or fixed\-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher\-layer protocol.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_multicast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]   The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were addressed to a multicast address at this sub\-layer.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_octets
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The total number of octets received on the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_unicast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The number of packets, delivered by this sub\-layer to a higher (sub\-)layer, that were not addressed to a multicast or broadcast address at this sub\-layer.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_unknown_protos
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of packets received via the interface that were discarded because of an unknown or unsupported protocol.  For character\-oriented or fixed\-length interfaces that support protocol multiplexing, the number of transmission units received via the interface that were discarded because of an unknown or unsupported protocol. For any interface that does not support protocol multiplexing, this counter is not present.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_clear
                        
                        	Indicates the last time the interface counters were cleared
                        	**type**\:  str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: out_broadcast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_discards
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The number of outbound packets that were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a packet could be to free up buffer space.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_errors
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  For packet\-oriented interfaces, the number of outbound packets that could not be transmitted because of errors. For character\-oriented or fixed\-length interfaces, the number of outbound transmission units that could not be transmitted because of errors.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_multicast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The total number of packets that higher\-level protocols requested be transmitted, and that were addressed to a multicast address at this sub\-layer, including those that were discarded or not sent.  For a MAC\-layer protocol, this includes both Group and Functional addresses.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_octets
                        
                        	[adapted from IETF interfaces model (RFC 7223)] Changed the counter type to counter64.  The total number of octets transmitted out of the interface, including framing characters.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_unicast_pkts
                        
                        	[adapted from IETF interfaces model (RFC 7223)]  The total number of packets that higher\-level protocols requested be transmitted, and that were not addressed to a multicast or broadcast address at this sub\-layer, including those that were discarded or not sent.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of 'discontinuity\-time'
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'oc-if'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.State.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.in_broadcast_pkts = YLeaf(YType.uint64, "in-broadcast-pkts")

                            self.in_discards = YLeaf(YType.uint64, "in-discards")

                            self.in_errors = YLeaf(YType.uint64, "in-errors")

                            self.in_multicast_pkts = YLeaf(YType.uint64, "in-multicast-pkts")

                            self.in_octets = YLeaf(YType.uint64, "in-octets")

                            self.in_unicast_pkts = YLeaf(YType.uint64, "in-unicast-pkts")

                            self.in_unknown_protos = YLeaf(YType.uint32, "in-unknown-protos")

                            self.last_clear = YLeaf(YType.str, "last-clear")

                            self.out_broadcast_pkts = YLeaf(YType.uint64, "out-broadcast-pkts")

                            self.out_discards = YLeaf(YType.uint64, "out-discards")

                            self.out_errors = YLeaf(YType.uint64, "out-errors")

                            self.out_multicast_pkts = YLeaf(YType.uint64, "out-multicast-pkts")

                            self.out_octets = YLeaf(YType.uint64, "out-octets")

                            self.out_unicast_pkts = YLeaf(YType.uint64, "out-unicast-pkts")
                            self._segment_path = lambda: "counters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.State.Counters, ['in_broadcast_pkts', 'in_discards', 'in_errors', 'in_multicast_pkts', 'in_octets', 'in_unicast_pkts', 'in_unknown_protos', 'last_clear', 'out_broadcast_pkts', 'out_discards', 'out_errors', 'out_multicast_pkts', 'out_octets', 'out_unicast_pkts'], name, value)


                class Vlan(Entity):
                    """
                    Enclosing container for VLAN interface\-specific
                    data on subinterfaces
                    
                    .. attribute:: config
                    
                    	Configuration parameters for VLANs
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config>`
                    
                    .. attribute:: state
                    
                    	State variables for VLANs
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State>`
                    
                    

                    """

                    _prefix = 'oc-vlan'
                    _revision = '2016-05-26'

                    def __init__(self):
                        super(Interfaces.Interface.Subinterfaces.Subinterface.Vlan, self).__init__()

                        self.yang_name = "vlan"
                        self.yang_parent_name = "subinterface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"config" : ("config", Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config), "state" : ("state", Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State)}
                        self._child_list_classes = {}

                        self.config = Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "openconfig-vlan:vlan"


                    class Config(Entity):
                        """
                        Configuration parameters for VLANs
                        
                        .. attribute:: vlan_id
                        
                        	VLAN id for the subinterface \-\- specified inline for the case of a local VLAN.  The id is scoped to the subinterface, and could be repeated on different subinterfaces
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 1..4094
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                        
                        
                        ----
                        

                        """

                        _prefix = 'oc-vlan'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "vlan"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.vlan_id = YLeaf(YType.str, "vlan-id")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Vlan.Config, ['vlan_id'], name, value)


                    class State(Entity):
                        """
                        State variables for VLANs
                        
                        .. attribute:: vlan_id
                        
                        	VLAN id for the subinterface \-\- specified inline for the case of a local VLAN.  The id is scoped to the subinterface, and could be repeated on different subinterfaces
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 1..4094
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** (409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\\.((409[0\-4]\|40[0\-8][0\-9]\|[1\-3][0\-9]{3}\|[1\-9][0\-9]{1,2}\|[1\-9])\|\\\*)
                        
                        
                        ----
                        

                        """

                        _prefix = 'oc-vlan'
                        _revision = '2016-05-26'

                        def __init__(self):
                            super(Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "vlan"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.vlan_id = YLeaf(YType.str, "vlan-id")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Interfaces.Interface.Subinterfaces.Subinterface.Vlan.State, ['vlan_id'], name, value)

    def clone_ptr(self):
        self._top_entity = Interfaces()
        return self._top_entity

