""" openconfig_mpls 

This module provides data definitions for configuration of
Multiprotocol Label Switching (MPLS) and associated protocols for
signaling and traffic engineering.

RFC 3031\: Multiprotocol Label Switching Architecture

The MPLS / TE data model consists of several modules and
submodules as shown below.  The top\-level MPLS module describes
the overall framework.  Three types of LSPs are supported\:

i) traffic\-engineered (or constrained\-path)

ii) IGP\-congruent (LSPs that follow the IGP path)

iii) static LSPs which are not signaled

The structure of each of these LSP configurations is defined in
corresponding submodules.  Companion modules define the relevant
configuration and operational data specific to key signaling
protocols used in operational practice.


                         +\-\-\-\-\-\-\-+
       +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\| MPLS  \|<\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
       \|                 +\-\-\-\-\-\-\-+               \|
       \|                     ^                   \|
       \|                     \|                   \|
  +\-\-\-\-+\-\-\-\-\-+      +\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+     +\-\-\-\-\-+\-\-\-\-\-+
  \| TE LSPs  \|      \| IGP\-based LSPs \|     \|static LSPs\|
  \|          \|      \|                \|     \|           \|
  +\-\-\-\-\-\-\-\-\-\-+      +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     +\-\-\-\-\-\-\-\-\-\-\-+
      ^  ^                    ^  ^
      \|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+   \|  +\-\-\-\-\-\-\-\-+
      \|                   \|   \|           \|
      \|   +\-\-\-\-\-\-+      +\-+\-\-\-+\-+      +\-\-+\-\-+
      +\-\-\-+ RSVP \|      \|SEGMENT\|      \| LDP \|
          +\-\-\-\-\-\-+      \|ROUTING\|      +\-\-\-\-\-+
                        +\-\-\-\-\-\-\-+


"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CspfTieBreaking(Enum):
    """
    CspfTieBreaking

    type to indicate the CSPF selection policy when

    multiple equal cost paths are available

    .. data:: RANDOM = 0

    	CSPF calculation selects a random path among

    	multiple equal-cost paths to the destination

    .. data:: LEAST_FILL = 1

    	CSPF calculation selects the path with greatest

    	available bandwidth

    .. data:: MOST_FILL = 2

    	CSPF calculation selects the path with the least

    	available bandwidth

    """

    RANDOM = Enum.YLeaf(0, "RANDOM")

    LEAST_FILL = Enum.YLeaf(1, "LEAST_FILL")

    MOST_FILL = Enum.YLeaf(2, "MOST_FILL")


class MplsHopType(Enum):
    """
    MplsHopType

    enumerated type for specifying loose or strict

    paths

    .. data:: LOOSE = 0

    	loose hop in an explicit path

    .. data:: STRICT = 1

    	strict hop in an explicit path

    """

    LOOSE = Enum.YLeaf(0, "LOOSE")

    STRICT = Enum.YLeaf(1, "STRICT")


class MplsSrlgFloodingType(Enum):
    """
    MplsSrlgFloodingType

    Enumerated bype for specifying how the SRLG is flooded

    .. data:: FLOODED_SRLG = 0

    	SRLG is flooded in the IGP

    .. data:: STATIC_SRLG = 1

    	SRLG is not flooded, the members are

    	statically configured

    """

    FLOODED_SRLG = Enum.YLeaf(0, "FLOODED-SRLG")

    STATIC_SRLG = Enum.YLeaf(1, "STATIC-SRLG")


class TeBandwidthType(Enum):
    """
    TeBandwidthType

    enumerated type for specifying whether bandwidth is

    explicitly specified or automatically computed

    .. data:: SPECIFIED = 0

    	Bandwidth is explicitly specified

    .. data:: AUTO = 1

    	Bandwidth is automatically computed

    """

    SPECIFIED = Enum.YLeaf(0, "SPECIFIED")

    AUTO = Enum.YLeaf(1, "AUTO")


class TeMetricType(Enum):
    """
    TeMetricType

    union type for setting the LSP TE metric to a

    static value, or to track the IGP metric

    .. data:: IGP = 0

    	set the LSP metric to track the underlying

    	IGP metric

    """

    IGP = Enum.YLeaf(0, "IGP")



class Mpls(Entity):
    """
    Anchor point for mpls configuration and operational
    data
    
    .. attribute:: global_
    
    	general mpls configuration applicable to any type of LSP and signaling protocol \- label ranges, entropy label supportmay be added here
    	**type**\:   :py:class:`Global_ <ydk.models.openconfig.openconfig_mpls.Mpls.Global_>`
    
    .. attribute:: lsps
    
    	LSP definitions and configuration
    	**type**\:   :py:class:`Lsps <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps>`
    
    .. attribute:: signaling_protocols
    
    	top\-level signaling protocol configuration
    	**type**\:   :py:class:`SignalingProtocols <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols>`
    
    .. attribute:: te_global_attributes
    
    	traffic\-engineering global attributes
    	**type**\:   :py:class:`TeGlobalAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes>`
    
    .. attribute:: te_interface_attributes
    
    	traffic engineering attributes specific for interfaces
    	**type**\:   :py:class:`TeInterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes>`
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        super(Mpls, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls"
        self.yang_parent_name = "openconfig-mpls"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"global" : ("global_", Mpls.Global_), "lsps" : ("lsps", Mpls.Lsps), "signaling-protocols" : ("signaling_protocols", Mpls.SignalingProtocols), "te-global-attributes" : ("te_global_attributes", Mpls.TeGlobalAttributes), "te-interface-attributes" : ("te_interface_attributes", Mpls.TeInterfaceAttributes)}
        self._child_list_classes = {}
        self.is_presence_container = True

        self.global_ = Mpls.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.lsps = Mpls.Lsps()
        self.lsps.parent = self
        self._children_name_map["lsps"] = "lsps"
        self._children_yang_names.add("lsps")

        self.signaling_protocols = Mpls.SignalingProtocols()
        self.signaling_protocols.parent = self
        self._children_name_map["signaling_protocols"] = "signaling-protocols"
        self._children_yang_names.add("signaling-protocols")

        self.te_global_attributes = Mpls.TeGlobalAttributes()
        self.te_global_attributes.parent = self
        self._children_name_map["te_global_attributes"] = "te-global-attributes"
        self._children_yang_names.add("te-global-attributes")

        self.te_interface_attributes = Mpls.TeInterfaceAttributes()
        self.te_interface_attributes.parent = self
        self._children_name_map["te_interface_attributes"] = "te-interface-attributes"
        self._children_yang_names.add("te-interface-attributes")
        self._segment_path = lambda: "openconfig-mpls:mpls"


    class Global_(Entity):
        """
        general mpls configuration applicable to any
        type of LSP and signaling protocol \- label ranges,
        entropy label supportmay be added here
        
        .. attribute:: config
        
        	Top level global MPLS configuration
        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Global_.Config>`
        
        .. attribute:: mpls_interface_attributes
        
        	Parameters related to MPLS interfaces
        	**type**\:   :py:class:`MplsInterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.Global_.MplsInterfaceAttributes>`
        
        .. attribute:: state
        
        	Top level global MPLS state
        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Global_.State>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            super(Mpls.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"config" : ("config", Mpls.Global_.Config), "mpls-interface-attributes" : ("mpls_interface_attributes", Mpls.Global_.MplsInterfaceAttributes), "state" : ("state", Mpls.Global_.State)}
            self._child_list_classes = {}

            self.config = Mpls.Global_.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"
            self._children_yang_names.add("config")

            self.mpls_interface_attributes = Mpls.Global_.MplsInterfaceAttributes()
            self.mpls_interface_attributes.parent = self
            self._children_name_map["mpls_interface_attributes"] = "mpls-interface-attributes"
            self._children_yang_names.add("mpls-interface-attributes")

            self.state = Mpls.Global_.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"
            self._children_yang_names.add("state")
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()


        class Config(Entity):
            """
            Top level global MPLS configuration
            
            .. attribute:: null_label
            
            	The null\-label type used, implicit or explicit
            	**type**\:   :py:class:`NullLabelType <ydk.models.openconfig.openconfig_mpls_types.NullLabelType>`
            
            	**default value**\: mplst:IMPLICIT
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.Global_.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.null_label = YLeaf(YType.identityref, "null-label")
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-mpls:mpls/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Global_.Config, ['null_label'], name, value)


        class MplsInterfaceAttributes(Entity):
            """
            Parameters related to MPLS interfaces
            
            .. attribute:: interface
            
            	List of TE interfaces
            	**type**\: list of    :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.Global_.MplsInterfaceAttributes.Interface>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.Global_.MplsInterfaceAttributes, self).__init__()

                self.yang_name = "mpls-interface-attributes"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", Mpls.Global_.MplsInterfaceAttributes.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "mpls-interface-attributes"
                self._absolute_path = lambda: "openconfig-mpls:mpls/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Global_.MplsInterfaceAttributes, [], name, value)


            class Interface(Entity):
                """
                List of TE interfaces
                
                .. attribute:: name  <key>
                
                	The interface name
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Global_.MplsInterfaceAttributes.Interface.Config>`
                
                .. attribute:: config
                
                	Configuration parameters related to MPLS interfaces\:
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Global_.MplsInterfaceAttributes.Interface.Config>`
                
                .. attribute:: state
                
                	State parameters related to TE interfaces
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Global_.MplsInterfaceAttributes.Interface.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.Global_.MplsInterfaceAttributes.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "mpls-interface-attributes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"config" : ("config", Mpls.Global_.MplsInterfaceAttributes.Interface.Config), "state" : ("state", Mpls.Global_.MplsInterfaceAttributes.Interface.State)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.config = Mpls.Global_.MplsInterfaceAttributes.Interface.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.Global_.MplsInterfaceAttributes.Interface.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "interface" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/global/mpls-interface-attributes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Global_.MplsInterfaceAttributes.Interface, ['name'], name, value)


                class Config(Entity):
                    """
                    Configuration parameters related to MPLS interfaces\:
                    
                    .. attribute:: mpls_enabled
                    
                    	Enable MPLS forwarding on this interfacek
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: name
                    
                    	reference to interface name
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Global_.MplsInterfaceAttributes.Interface.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.mpls_enabled = YLeaf(YType.boolean, "mpls-enabled")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Global_.MplsInterfaceAttributes.Interface.Config, ['mpls_enabled', 'name'], name, value)


                class State(Entity):
                    """
                    State parameters related to TE interfaces
                    
                    .. attribute:: mpls_enabled
                    
                    	Enable MPLS forwarding on this interfacek
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: name
                    
                    	reference to interface name
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Global_.MplsInterfaceAttributes.Interface.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.mpls_enabled = YLeaf(YType.boolean, "mpls-enabled")

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Global_.MplsInterfaceAttributes.Interface.State, ['mpls_enabled', 'name'], name, value)


        class State(Entity):
            """
            Top level global MPLS state
            
            .. attribute:: null_label
            
            	The null\-label type used, implicit or explicit
            	**type**\:   :py:class:`NullLabelType <ydk.models.openconfig.openconfig_mpls_types.NullLabelType>`
            
            	**default value**\: mplst:IMPLICIT
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.Global_.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.null_label = YLeaf(YType.identityref, "null-label")
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-mpls:mpls/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Global_.State, ['null_label'], name, value)


    class Lsps(Entity):
        """
        LSP definitions and configuration
        
        .. attribute:: constrained_path
        
        	traffic\-engineered LSPs supporting different path computation and signaling methods
        	**type**\:   :py:class:`ConstrainedPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath>`
        
        .. attribute:: static_lsps
        
        	statically configured LSPs, without dynamic signaling
        	**type**\:   :py:class:`StaticLsps <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps>`
        
        .. attribute:: unconstrained_path
        
        	LSPs that use the IGP\-determined path, i.e., non traffic\-engineered, or non constrained\-path
        	**type**\:   :py:class:`UnconstrainedPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            super(Mpls.Lsps, self).__init__()

            self.yang_name = "lsps"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"constrained-path" : ("constrained_path", Mpls.Lsps.ConstrainedPath), "static-lsps" : ("static_lsps", Mpls.Lsps.StaticLsps), "unconstrained-path" : ("unconstrained_path", Mpls.Lsps.UnconstrainedPath)}
            self._child_list_classes = {}

            self.constrained_path = Mpls.Lsps.ConstrainedPath()
            self.constrained_path.parent = self
            self._children_name_map["constrained_path"] = "constrained-path"
            self._children_yang_names.add("constrained-path")

            self.static_lsps = Mpls.Lsps.StaticLsps()
            self.static_lsps.parent = self
            self._children_name_map["static_lsps"] = "static-lsps"
            self._children_yang_names.add("static-lsps")

            self.unconstrained_path = Mpls.Lsps.UnconstrainedPath()
            self.unconstrained_path.parent = self
            self._children_name_map["unconstrained_path"] = "unconstrained-path"
            self._children_yang_names.add("unconstrained-path")
            self._segment_path = lambda: "lsps"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()


        class ConstrainedPath(Entity):
            """
            traffic\-engineered LSPs supporting different
            path computation and signaling methods
            
            .. attribute:: named_explicit_paths
            
            	A list of explicit paths
            	**type**\: list of    :py:class:`NamedExplicitPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths>`
            
            .. attribute:: tunnel
            
            	List of TE tunnels
            	**type**\: list of    :py:class:`Tunnel <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.Lsps.ConstrainedPath, self).__init__()

                self.yang_name = "constrained-path"
                self.yang_parent_name = "lsps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"named-explicit-paths" : ("named_explicit_paths", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths), "tunnel" : ("tunnel", Mpls.Lsps.ConstrainedPath.Tunnel)}

                self.named_explicit_paths = YList(self)
                self.tunnel = YList(self)
                self._segment_path = lambda: "constrained-path"
                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Lsps.ConstrainedPath, [], name, value)


            class NamedExplicitPaths(Entity):
                """
                A list of explicit paths
                
                .. attribute:: name  <key>
                
                	A string name that uniquely identifies an explicit path
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config>`
                
                .. attribute:: config
                
                	Configuration parameters relating to named explicit paths
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config>`
                
                .. attribute:: explicit_route_objects
                
                	List of explicit route objects
                	**type**\: list of    :py:class:`ExplicitRouteObjects <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects>`
                
                .. attribute:: state
                
                	Operational state parameters relating to the named explicit paths
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths, self).__init__()

                    self.yang_name = "named-explicit-paths"
                    self.yang_parent_name = "constrained-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State)}
                    self._child_list_classes = {"explicit-route-objects" : ("explicit_route_objects", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects)}

                    self.name = YLeaf(YType.str, "name")

                    self.config = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.explicit_route_objects = YList(self)
                    self._segment_path = lambda: "named-explicit-paths" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/constrained-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths, ['name'], name, value)


                class Config(Entity):
                    """
                    Configuration parameters relating to named explicit
                    paths
                    
                    .. attribute:: name
                    
                    	A string name that uniquely identifies an explicit path
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "named-explicit-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config, ['name'], name, value)


                class ExplicitRouteObjects(Entity):
                    """
                    List of explicit route objects
                    
                    .. attribute:: index  <key>
                    
                    	Index of this explicit route object, to express the order of hops in path
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to an explicit route
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters relating to an explicit route
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects, self).__init__()

                        self.yang_name = "explicit-route-objects"
                        self.yang_parent_name = "named-explicit-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State)}
                        self._child_list_classes = {}

                        self.index = YLeaf(YType.str, "index")

                        self.config = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "explicit-route-objects" + "[index='" + self.index.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects, ['index'], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters relating to an explicit
                        route
                        
                        .. attribute:: address
                        
                        	router hop for the LSP path
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: hop_type
                        
                        	strict or loose hop
                        	**type**\:   :py:class:`MplsHopType <ydk.models.openconfig.openconfig_mpls.MplsHopType>`
                        
                        .. attribute:: index
                        
                        	Index of this explicit route object to express the order of hops in the path
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "explicit-route-objects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.hop_type = YLeaf(YType.enumeration, "hop-type")

                            self.index = YLeaf(YType.uint8, "index")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config, ['address', 'hop_type', 'index'], name, value)


                    class State(Entity):
                        """
                        State parameters relating to an explicit route
                        
                        .. attribute:: address
                        
                        	router hop for the LSP path
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: hop_type
                        
                        	strict or loose hop
                        	**type**\:   :py:class:`MplsHopType <ydk.models.openconfig.openconfig_mpls.MplsHopType>`
                        
                        .. attribute:: index
                        
                        	Index of this explicit route object to express the order of hops in the path
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "explicit-route-objects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.hop_type = YLeaf(YType.enumeration, "hop-type")

                            self.index = YLeaf(YType.uint8, "index")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State, ['address', 'hop_type', 'index'], name, value)


                class State(Entity):
                    """
                    Operational state parameters relating to the named
                    explicit paths
                    
                    .. attribute:: name
                    
                    	A string name that uniquely identifies an explicit path
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "named-explicit-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State, ['name'], name, value)


            class Tunnel(Entity):
                """
                List of TE tunnels
                
                .. attribute:: name  <key>
                
                	The tunnel name
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Config>`
                
                .. attribute:: type  <key>
                
                	The tunnel type, p2p or p2mp
                	**type**\:   :py:class:`TunnelType <ydk.models.openconfig.openconfig_mpls_types.TunnelType>`
                
                .. attribute:: bandwidth
                
                	Bandwidth configuration for TE LSPs
                	**type**\:   :py:class:`Bandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth>`
                
                .. attribute:: config
                
                	Configuration parameters related to TE tunnels\:
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Config>`
                
                .. attribute:: p2p_tunnel_attributes
                
                	Parameters related to LSPs of type P2P
                	**type**\:   :py:class:`P2PTunnelAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes>`
                
                .. attribute:: state
                
                	State parameters related to TE tunnels
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.Lsps.ConstrainedPath.Tunnel, self).__init__()

                    self.yang_name = "tunnel"
                    self.yang_parent_name = "constrained-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"bandwidth" : ("bandwidth", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth), "config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.Config), "p2p-tunnel-attributes" : ("p2p_tunnel_attributes", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.State)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.type = YLeaf(YType.identityref, "type")

                    self.bandwidth = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth()
                    self.bandwidth.parent = self
                    self._children_name_map["bandwidth"] = "bandwidth"
                    self._children_yang_names.add("bandwidth")

                    self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.p2p_tunnel_attributes = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes()
                    self.p2p_tunnel_attributes.parent = self
                    self._children_name_map["p2p_tunnel_attributes"] = "p2p-tunnel-attributes"
                    self._children_yang_names.add("p2p-tunnel-attributes")

                    self.state = Mpls.Lsps.ConstrainedPath.Tunnel.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "tunnel" + "[name='" + self.name.get() + "']" + "[type='" + self.type.get() + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/constrained-path/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel, ['name', 'type'], name, value)


                class Bandwidth(Entity):
                    """
                    Bandwidth configuration for TE LSPs
                    
                    .. attribute:: auto_bandwidth
                    
                    	Parameters related to auto\-bandwidth
                    	**type**\:   :py:class:`AutoBandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters related to bandwidth on TE tunnels\:
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters related to bandwidth configuration of TE tunnels
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth, self).__init__()

                        self.yang_name = "bandwidth"
                        self.yang_parent_name = "tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"auto-bandwidth" : ("auto_bandwidth", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth), "config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State)}
                        self._child_list_classes = {}

                        self.auto_bandwidth = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth()
                        self.auto_bandwidth.parent = self
                        self._children_name_map["auto_bandwidth"] = "auto-bandwidth"
                        self._children_yang_names.add("auto-bandwidth")

                        self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "bandwidth"


                    class AutoBandwidth(Entity):
                        """
                        Parameters related to auto\-bandwidth
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to MPLS auto\-bandwidth on the tunnel
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config>`
                        
                        .. attribute:: overflow
                        
                        	configuration of MPLS overflow bandwidth adjustement for the LSP
                        	**type**\:   :py:class:`Overflow <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to MPLS auto\-bandwidth on the tunnel
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State>`
                        
                        .. attribute:: underflow
                        
                        	configuration of MPLS underflow bandwidth           adjustement for the LSP
                        	**type**\:   :py:class:`Underflow <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth, self).__init__()

                            self.yang_name = "auto-bandwidth"
                            self.yang_parent_name = "bandwidth"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config), "overflow" : ("overflow", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State), "underflow" : ("underflow", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow)}
                            self._child_list_classes = {}

                            self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.overflow = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow()
                            self.overflow.parent = self
                            self._children_name_map["overflow"] = "overflow"
                            self._children_yang_names.add("overflow")

                            self.state = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")

                            self.underflow = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow()
                            self.underflow.parent = self
                            self._children_name_map["underflow"] = "underflow"
                            self._children_yang_names.add("underflow")
                            self._segment_path = lambda: "auto-bandwidth"


                        class Config(Entity):
                            """
                            Configuration parameters relating to MPLS
                            auto\-bandwidth on the tunnel.
                            
                            .. attribute:: adjust_interval
                            
                            	time in seconds between adjustments to LSP bandwidth
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjust_threshold
                            
                            	percentage difference between the LSP's specified bandwidth and its current bandwidth allocation \-\- if the difference is greater than the specified percentage, auto\-bandwidth adjustment is triggered
                            	**type**\:  int
                            
                            	**range:** 0..100
                            
                            .. attribute:: enabled
                            
                            	enables mpls auto\-bandwidth on the lsp
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            .. attribute:: max_bw
                            
                            	set the maximum bandwidth in Mbps for an auto\-bandwidth LSP
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: min_bw
                            
                            	set the minimum bandwidth in Mbps for an auto\-bandwidth LSP
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "auto-bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.adjust_interval = YLeaf(YType.uint32, "adjust-interval")

                                self.adjust_threshold = YLeaf(YType.uint8, "adjust-threshold")

                                self.enabled = YLeaf(YType.boolean, "enabled")

                                self.max_bw = YLeaf(YType.uint32, "max-bw")

                                self.min_bw = YLeaf(YType.uint32, "min-bw")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config, ['adjust_interval', 'adjust_threshold', 'enabled', 'max_bw', 'min_bw'], name, value)


                        class Overflow(Entity):
                            """
                            configuration of MPLS overflow bandwidth
                            adjustement for the LSP
                            
                            .. attribute:: config
                            
                            	Config information for MPLS overflow bandwidth adjustment
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config>`
                            
                            .. attribute:: state
                            
                            	Config information for MPLS overflow bandwidth adjustment
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow, self).__init__()

                                self.yang_name = "overflow"
                                self.yang_parent_name = "auto-bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State)}
                                self._child_list_classes = {}

                                self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "overflow"


                            class Config(Entity):
                                """
                                Config information for MPLS overflow bandwidth
                                adjustment
                                
                                .. attribute:: enabled
                                
                                	enables mpls lsp bandwidth overflow adjustment on the lsp
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: overflow_threshold
                                
                                	bandwidth percentage change to trigger an overflow event
                                	**type**\:  int
                                
                                	**range:** 0..100
                                
                                .. attribute:: trigger_event_count
                                
                                	number of consecutive overflow sample events needed to trigger an overflow adjustment
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "overflow"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enabled = YLeaf(YType.boolean, "enabled")

                                    self.overflow_threshold = YLeaf(YType.uint8, "overflow-threshold")

                                    self.trigger_event_count = YLeaf(YType.uint16, "trigger-event-count")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config, ['enabled', 'overflow_threshold', 'trigger_event_count'], name, value)


                            class State(Entity):
                                """
                                Config information for MPLS overflow bandwidth
                                adjustment
                                
                                .. attribute:: enabled
                                
                                	enables mpls lsp bandwidth overflow adjustment on the lsp
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: overflow_threshold
                                
                                	bandwidth percentage change to trigger an overflow event
                                	**type**\:  int
                                
                                	**range:** 0..100
                                
                                .. attribute:: trigger_event_count
                                
                                	number of consecutive overflow sample events needed to trigger an overflow adjustment
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "overflow"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enabled = YLeaf(YType.boolean, "enabled")

                                    self.overflow_threshold = YLeaf(YType.uint8, "overflow-threshold")

                                    self.trigger_event_count = YLeaf(YType.uint16, "trigger-event-count")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State, ['enabled', 'overflow_threshold', 'trigger_event_count'], name, value)


                        class State(Entity):
                            """
                            State parameters relating to MPLS
                            auto\-bandwidth on the tunnel.
                            
                            .. attribute:: adjust_interval
                            
                            	time in seconds between adjustments to LSP bandwidth
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adjust_threshold
                            
                            	percentage difference between the LSP's specified bandwidth and its current bandwidth allocation \-\- if the difference is greater than the specified percentage, auto\-bandwidth adjustment is triggered
                            	**type**\:  int
                            
                            	**range:** 0..100
                            
                            .. attribute:: enabled
                            
                            	enables mpls auto\-bandwidth on the lsp
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            .. attribute:: max_bw
                            
                            	set the maximum bandwidth in Mbps for an auto\-bandwidth LSP
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: min_bw
                            
                            	set the minimum bandwidth in Mbps for an auto\-bandwidth LSP
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "auto-bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.adjust_interval = YLeaf(YType.uint32, "adjust-interval")

                                self.adjust_threshold = YLeaf(YType.uint8, "adjust-threshold")

                                self.enabled = YLeaf(YType.boolean, "enabled")

                                self.max_bw = YLeaf(YType.uint32, "max-bw")

                                self.min_bw = YLeaf(YType.uint32, "min-bw")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State, ['adjust_interval', 'adjust_threshold', 'enabled', 'max_bw', 'min_bw'], name, value)


                        class Underflow(Entity):
                            """
                            configuration of MPLS underflow bandwidth
                                      adjustement for the LSP
                            
                            .. attribute:: config
                            
                            	Config information for MPLS underflow bandwidth           adjustment
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config>`
                            
                            .. attribute:: state
                            
                            	State information for MPLS underflow bandwidth           adjustment
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow, self).__init__()

                                self.yang_name = "underflow"
                                self.yang_parent_name = "auto-bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State)}
                                self._child_list_classes = {}

                                self.config = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "underflow"


                            class Config(Entity):
                                """
                                Config information for MPLS underflow bandwidth
                                          adjustment
                                
                                .. attribute:: enabled
                                
                                	enables bandwidth underflow adjustment on the lsp
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: trigger_event_count
                                
                                	number of consecutive underflow sample events needed to trigger an underflow adjustment
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: underflow_threshold
                                
                                	bandwidth percentage change to trigger and underflow event
                                	**type**\:  int
                                
                                	**range:** 0..100
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "underflow"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enabled = YLeaf(YType.boolean, "enabled")

                                    self.trigger_event_count = YLeaf(YType.uint16, "trigger-event-count")

                                    self.underflow_threshold = YLeaf(YType.uint8, "underflow-threshold")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config, ['enabled', 'trigger_event_count', 'underflow_threshold'], name, value)


                            class State(Entity):
                                """
                                State information for MPLS underflow bandwidth
                                          adjustment
                                
                                .. attribute:: enabled
                                
                                	enables bandwidth underflow adjustment on the lsp
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                .. attribute:: trigger_event_count
                                
                                	number of consecutive underflow sample events needed to trigger an underflow adjustment
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: underflow_threshold
                                
                                	bandwidth percentage change to trigger and underflow event
                                	**type**\:  int
                                
                                	**range:** 0..100
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "underflow"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.enabled = YLeaf(YType.boolean, "enabled")

                                    self.trigger_event_count = YLeaf(YType.uint16, "trigger-event-count")

                                    self.underflow_threshold = YLeaf(YType.uint8, "underflow-threshold")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State, ['enabled', 'trigger_event_count', 'underflow_threshold'], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters related to bandwidth on TE
                        tunnels\:
                        
                        .. attribute:: set_bandwidth
                        
                        	set bandwidth explicitly, e.g., using offline calculation
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: specification_type
                        
                        	The method used for settign the bandwidth, either explicitly specified or configured
                        	**type**\:   :py:class:`TeBandwidthType <ydk.models.openconfig.openconfig_mpls.TeBandwidthType>`
                        
                        	**default value**\: SPECIFIED
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "bandwidth"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.set_bandwidth = YLeaf(YType.uint32, "set-bandwidth")

                            self.specification_type = YLeaf(YType.enumeration, "specification-type")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config, ['set_bandwidth', 'specification_type'], name, value)


                    class State(Entity):
                        """
                        State parameters related to bandwidth
                        configuration of TE tunnels
                        
                        .. attribute:: set_bandwidth
                        
                        	set bandwidth explicitly, e.g., using offline calculation
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: specification_type
                        
                        	The method used for settign the bandwidth, either explicitly specified or configured
                        	**type**\:   :py:class:`TeBandwidthType <ydk.models.openconfig.openconfig_mpls.TeBandwidthType>`
                        
                        	**default value**\: SPECIFIED
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "bandwidth"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.set_bandwidth = YLeaf(YType.uint32, "set-bandwidth")

                            self.specification_type = YLeaf(YType.enumeration, "specification-type")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State, ['set_bandwidth', 'specification_type'], name, value)


                class Config(Entity):
                    """
                    Configuration parameters related to TE tunnels\:
                    
                    .. attribute:: admin_status
                    
                    	TE tunnel administrative state
                    	**type**\:   :py:class:`TunnelAdminStatus <ydk.models.openconfig.openconfig_mpls_types.TunnelAdminStatus>`
                    
                    	**default value**\: mplst:ADMIN_UP
                    
                    .. attribute:: description
                    
                    	optional text description for the tunnel
                    	**type**\:  str
                    
                    .. attribute:: hold_priority
                    
                    	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    	**default value**\: 0
                    
                    .. attribute:: local_id
                    
                    	locally signficant optional identifier for the tunnel; may be a numerical or string value
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\:  str
                    
                    
                    ----
                    .. attribute:: metric
                    
                    	LSP metric, either explicit or IGP
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`TeMetricType <ydk.models.openconfig.openconfig_mpls.TeMetricType>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    .. attribute:: name
                    
                    	The tunnel name
                    	**type**\:  str
                    
                    .. attribute:: preference
                    
                    	Specifies a preference for this tunnel. A lower number signifies a better preference
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    .. attribute:: protection_style_requested
                    
                    	style of mpls frr protection desired\: can be link, link\-node or unprotected
                    	**type**\:   :py:class:`ProtectionType <ydk.models.openconfig.openconfig_mpls_types.ProtectionType>`
                    
                    	**default value**\: mplst:unprotected
                    
                    .. attribute:: reoptimize_timer
                    
                    	frequency of reoptimization of a traffic engineered LSP
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**units**\: seconds
                    
                    .. attribute:: setup_priority
                    
                    	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    	**default value**\: 7
                    
                    .. attribute:: signaling_protocol
                    
                    	Signaling protocol used to set up this tunnel
                    	**type**\:   :py:class:`TunnelType <ydk.models.openconfig.openconfig_mpls_types.TunnelType>`
                    
                    .. attribute:: soft_preemption
                    
                    	Enables RSVP soft\-preemption on this LSP
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: source
                    
                    	RSVP\-TE tunnel source address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: type
                    
                    	Tunnel type, p2p or p2mp
                    	**type**\:   :py:class:`TunnelType <ydk.models.openconfig.openconfig_mpls_types.TunnelType>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.ConstrainedPath.Tunnel.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.admin_status = YLeaf(YType.identityref, "admin-status")

                        self.description = YLeaf(YType.str, "description")

                        self.hold_priority = YLeaf(YType.uint8, "hold-priority")

                        self.local_id = YLeaf(YType.str, "local-id")

                        self.metric = YLeaf(YType.str, "metric")

                        self.name = YLeaf(YType.str, "name")

                        self.preference = YLeaf(YType.uint8, "preference")

                        self.protection_style_requested = YLeaf(YType.identityref, "protection-style-requested")

                        self.reoptimize_timer = YLeaf(YType.uint16, "reoptimize-timer")

                        self.setup_priority = YLeaf(YType.uint8, "setup-priority")

                        self.signaling_protocol = YLeaf(YType.identityref, "signaling-protocol")

                        self.soft_preemption = YLeaf(YType.boolean, "soft-preemption")

                        self.source = YLeaf(YType.str, "source")

                        self.type = YLeaf(YType.identityref, "type")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.Config, ['admin_status', 'description', 'hold_priority', 'local_id', 'metric', 'name', 'preference', 'protection_style_requested', 'reoptimize_timer', 'setup_priority', 'signaling_protocol', 'soft_preemption', 'source', 'type'], name, value)


                class P2PTunnelAttributes(Entity):
                    """
                    Parameters related to LSPs of type P2P
                    
                    .. attribute:: config
                    
                    	Configuration parameters for P2P LSPs
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config>`
                    
                    .. attribute:: p2p_primary_paths
                    
                    	List of p2p primary paths for a tunnel
                    	**type**\: list of    :py:class:`P2PPrimaryPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths>`
                    
                    .. attribute:: p2p_secondary_paths
                    
                    	List of p2p primary paths for a tunnel
                    	**type**\: list of    :py:class:`P2PSecondaryPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths>`
                    
                    .. attribute:: state
                    
                    	State parameters for P2P LSPs
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes, self).__init__()

                        self.yang_name = "p2p-tunnel-attributes"
                        self.yang_parent_name = "tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State)}
                        self._child_list_classes = {"p2p-primary-paths" : ("p2p_primary_paths", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths), "p2p-secondary-paths" : ("p2p_secondary_paths", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths)}

                        self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.p2p_primary_paths = YList(self)
                        self.p2p_secondary_paths = YList(self)
                        self._segment_path = lambda: "p2p-tunnel-attributes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes, [], name, value)


                    class Config(Entity):
                        """
                        Configuration parameters for P2P LSPs
                        
                        .. attribute:: destination
                        
                        	P2P tunnel destination address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "p2p-tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.destination = YLeaf(YType.str, "destination")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config, ['destination'], name, value)


                    class P2PPrimaryPaths(Entity):
                        """
                        List of p2p primary paths for a tunnel
                        
                        .. attribute:: name  <key>
                        
                        	Path name
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config>`
                        
                        .. attribute:: admin_groups
                        
                        	Top\-level container for include/exclude constraints for link affinities
                        	**type**\:   :py:class:`AdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups>`
                        
                        .. attribute:: candidate_secondary_paths
                        
                        	The set of candidate secondary paths which may be used for this primary path. When secondary paths are specified in the list the path of the secondary LSP in use must be restricted to those path options referenced. The priority of the secondary paths is specified within the list. Higher priority values are less preferred \- that is to say that a path with priority 0 is the most preferred path. In the case that the list is empty, any secondary path option may be utilised when the current primary path is in use
                        	**type**\:   :py:class:`CandidateSecondaryPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to paths
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters related to paths
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths, self).__init__()

                            self.yang_name = "p2p-primary-paths"
                            self.yang_parent_name = "p2p-tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"admin-groups" : ("admin_groups", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups), "candidate-secondary-paths" : ("candidate_secondary_paths", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths), "config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State)}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.admin_groups = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups()
                            self.admin_groups.parent = self
                            self._children_name_map["admin_groups"] = "admin-groups"
                            self._children_yang_names.add("admin-groups")

                            self.candidate_secondary_paths = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths()
                            self.candidate_secondary_paths.parent = self
                            self._children_name_map["candidate_secondary_paths"] = "candidate-secondary-paths"
                            self._children_yang_names.add("candidate-secondary-paths")

                            self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "p2p-primary-paths" + "[name='" + self.name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths, ['name'], name, value)


                        class AdminGroups(Entity):
                            """
                            Top\-level container for include/exclude constraints for
                            link affinities
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups, self).__init__()

                                self.yang_name = "admin-groups"
                                self.yang_parent_name = "p2p-primary-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State)}
                                self._child_list_classes = {}

                                self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "admin-groups"


                            class Config(Entity):
                                """
                                Configuration data 
                                
                                .. attribute:: exclude_group
                                
                                	list of references to named admin\-groups to exclude in path calculation
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                .. attribute:: include_all_group
                                
                                	list of references to named admin\-groups of which all must be included
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                .. attribute:: include_any_group
                                
                                	list of references to named admin\-groups of which one must be included
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "admin-groups"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.exclude_group = YLeafList(YType.str, "exclude-group")

                                    self.include_all_group = YLeafList(YType.str, "include-all-group")

                                    self.include_any_group = YLeafList(YType.str, "include-any-group")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config, ['exclude_group', 'include_all_group', 'include_any_group'], name, value)


                            class State(Entity):
                                """
                                Operational state data 
                                
                                .. attribute:: exclude_group
                                
                                	list of references to named admin\-groups to exclude in path calculation
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                .. attribute:: include_all_group
                                
                                	list of references to named admin\-groups of which all must be included
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                .. attribute:: include_any_group
                                
                                	list of references to named admin\-groups of which one must be included
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "admin-groups"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.exclude_group = YLeafList(YType.str, "exclude-group")

                                    self.include_all_group = YLeafList(YType.str, "include-all-group")

                                    self.include_any_group = YLeafList(YType.str, "include-any-group")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State, ['exclude_group', 'include_all_group', 'include_any_group'], name, value)


                        class CandidateSecondaryPaths(Entity):
                            """
                            The set of candidate secondary paths which may be used
                            for this primary path. When secondary paths are specified
                            in the list the path of the secondary LSP in use must be
                            restricted to those path options referenced. The
                            priority of the secondary paths is specified within the
                            list. Higher priority values are less preferred \- that is
                            to say that a path with priority 0 is the most preferred
                            path. In the case that the list is empty, any secondary
                            path option may be utilised when the current primary path
                            is in use.
                            
                            .. attribute:: candidate_secondary_path
                            
                            	List of secondary paths which may be utilised when the current primary path is in use
                            	**type**\: list of    :py:class:`CandidateSecondaryPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths, self).__init__()

                                self.yang_name = "candidate-secondary-paths"
                                self.yang_parent_name = "p2p-primary-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"candidate-secondary-path" : ("candidate_secondary_path", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath)}

                                self.candidate_secondary_path = YList(self)
                                self._segment_path = lambda: "candidate-secondary-paths"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths, [], name, value)


                            class CandidateSecondaryPath(Entity):
                                """
                                List of secondary paths which may be utilised when the
                                current primary path is in use
                                
                                .. attribute:: secondary_path  <key>
                                
                                	A reference to the secondary path option reference which acts as the key of the candidate\-secondary\-path list
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`secondary_path <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config>`
                                
                                .. attribute:: config
                                
                                	Configuration parameters relating to the candidate secondary path
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config>`
                                
                                .. attribute:: state
                                
                                	Operational state parameters relating to the candidate secondary path
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State>`
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath, self).__init__()

                                    self.yang_name = "candidate-secondary-path"
                                    self.yang_parent_name = "candidate-secondary-paths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State)}
                                    self._child_list_classes = {}

                                    self.secondary_path = YLeaf(YType.str, "secondary-path")

                                    self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "candidate-secondary-path" + "[secondary-path='" + self.secondary_path.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath, ['secondary_path'], name, value)


                                class Config(Entity):
                                    """
                                    Configuration parameters relating to the candidate
                                    secondary path
                                    
                                    .. attribute:: priority
                                    
                                    	The priority of the specified secondary path option. Higher priority options are less preferable \- such that a secondary path reference with a priority of 0 is the most preferred
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: secondary_path
                                    
                                    	A reference to the secondary path that should be utilised when the containing primary path option is in use
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config>`
                                    
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "candidate-secondary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.priority = YLeaf(YType.uint16, "priority")

                                        self.secondary_path = YLeaf(YType.str, "secondary-path")
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config, ['priority', 'secondary_path'], name, value)


                                class State(Entity):
                                    """
                                    Operational state parameters relating to the candidate
                                    secondary path
                                    
                                    .. attribute:: active
                                    
                                    	Indicates the current active path option that has been selected of the candidate secondary paths
                                    	**type**\:  bool
                                    
                                    .. attribute:: priority
                                    
                                    	The priority of the specified secondary path option. Higher priority options are less preferable \- such that a secondary path reference with a priority of 0 is the most preferred
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: secondary_path
                                    
                                    	A reference to the secondary path that should be utilised when the containing primary path option is in use
                                    	**type**\:  str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config>`
                                    
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "candidate-secondary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.active = YLeaf(YType.boolean, "active")

                                        self.priority = YLeaf(YType.uint16, "priority")

                                        self.secondary_path = YLeaf(YType.str, "secondary-path")
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State, ['active', 'priority', 'secondary_path'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters related to paths
                            
                            .. attribute:: cspf_tiebreaker
                            
                            	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                            	**type**\:   :py:class:`CspfTieBreaking <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking>`
                            
                            .. attribute:: explicit_path_name
                            
                            	reference to a defined path
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config>`
                            
                            .. attribute:: hold_priority
                            
                            	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**default value**\: 0
                            
                            .. attribute:: name
                            
                            	Path name
                            	**type**\:  str
                            
                            .. attribute:: path_computation_method
                            
                            	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                            	**type**\:   :py:class:`PathComputationMethod <ydk.models.openconfig.openconfig_mpls.PathComputationMethod>`
                            
                            	**default value**\: locally-computed
                            
                            .. attribute:: path_computation_server
                            
                            	Address of the external path computation server
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: preference
                            
                            	Specifies a preference for this path. The lower the number higher the preference
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: retry_timer
                            
                            	sets the time between attempts to establish the LSP
                            	**type**\:  int
                            
                            	**range:** 1..600
                            
                            	**units**\: seconds
                            
                            .. attribute:: setup_priority
                            
                            	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**default value**\: 7
                            
                            .. attribute:: use_cspf
                            
                            	Flag to enable CSPF for locally computed LSPs
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "p2p-primary-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.cspf_tiebreaker = YLeaf(YType.enumeration, "cspf-tiebreaker")

                                self.explicit_path_name = YLeaf(YType.str, "explicit-path-name")

                                self.hold_priority = YLeaf(YType.uint8, "hold-priority")

                                self.name = YLeaf(YType.str, "name")

                                self.path_computation_method = YLeaf(YType.identityref, "path-computation-method")

                                self.path_computation_server = YLeaf(YType.str, "path-computation-server")

                                self.preference = YLeaf(YType.uint8, "preference")

                                self.retry_timer = YLeaf(YType.uint16, "retry-timer")

                                self.setup_priority = YLeaf(YType.uint8, "setup-priority")

                                self.use_cspf = YLeaf(YType.boolean, "use-cspf")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config, ['cspf_tiebreaker', 'explicit_path_name', 'hold_priority', 'name', 'path_computation_method', 'path_computation_server', 'preference', 'retry_timer', 'setup_priority', 'use_cspf'], name, value)


                        class State(Entity):
                            """
                            State parameters related to paths
                            
                            .. attribute:: cspf_tiebreaker
                            
                            	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                            	**type**\:   :py:class:`CspfTieBreaking <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking>`
                            
                            .. attribute:: explicit_path_name
                            
                            	reference to a defined path
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config>`
                            
                            .. attribute:: hold_priority
                            
                            	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**default value**\: 0
                            
                            .. attribute:: name
                            
                            	Path name
                            	**type**\:  str
                            
                            .. attribute:: path_computation_method
                            
                            	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                            	**type**\:   :py:class:`PathComputationMethod <ydk.models.openconfig.openconfig_mpls.PathComputationMethod>`
                            
                            	**default value**\: locally-computed
                            
                            .. attribute:: path_computation_server
                            
                            	Address of the external path computation server
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: preference
                            
                            	Specifies a preference for this path. The lower the number higher the preference
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: retry_timer
                            
                            	sets the time between attempts to establish the LSP
                            	**type**\:  int
                            
                            	**range:** 1..600
                            
                            	**units**\: seconds
                            
                            .. attribute:: setup_priority
                            
                            	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**default value**\: 7
                            
                            .. attribute:: use_cspf
                            
                            	Flag to enable CSPF for locally computed LSPs
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "p2p-primary-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.cspf_tiebreaker = YLeaf(YType.enumeration, "cspf-tiebreaker")

                                self.explicit_path_name = YLeaf(YType.str, "explicit-path-name")

                                self.hold_priority = YLeaf(YType.uint8, "hold-priority")

                                self.name = YLeaf(YType.str, "name")

                                self.path_computation_method = YLeaf(YType.identityref, "path-computation-method")

                                self.path_computation_server = YLeaf(YType.str, "path-computation-server")

                                self.preference = YLeaf(YType.uint8, "preference")

                                self.retry_timer = YLeaf(YType.uint16, "retry-timer")

                                self.setup_priority = YLeaf(YType.uint8, "setup-priority")

                                self.use_cspf = YLeaf(YType.boolean, "use-cspf")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State, ['cspf_tiebreaker', 'explicit_path_name', 'hold_priority', 'name', 'path_computation_method', 'path_computation_server', 'preference', 'retry_timer', 'setup_priority', 'use_cspf'], name, value)


                    class P2PSecondaryPaths(Entity):
                        """
                        List of p2p primary paths for a tunnel
                        
                        .. attribute:: name  <key>
                        
                        	Path name
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config>`
                        
                        .. attribute:: admin_groups
                        
                        	Top\-level container for include/exclude constraints for link affinities
                        	**type**\:   :py:class:`AdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to paths
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters related to paths
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths, self).__init__()

                            self.yang_name = "p2p-secondary-paths"
                            self.yang_parent_name = "p2p-tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"admin-groups" : ("admin_groups", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups), "config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State)}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.admin_groups = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups()
                            self.admin_groups.parent = self
                            self._children_name_map["admin_groups"] = "admin-groups"
                            self._children_yang_names.add("admin-groups")

                            self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "p2p-secondary-paths" + "[name='" + self.name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths, ['name'], name, value)


                        class AdminGroups(Entity):
                            """
                            Top\-level container for include/exclude constraints for
                            link affinities
                            
                            .. attribute:: config
                            
                            	Configuration data 
                            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config>`
                            
                            .. attribute:: state
                            
                            	Operational state data 
                            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups, self).__init__()

                                self.yang_name = "admin-groups"
                                self.yang_parent_name = "p2p-secondary-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"config" : ("config", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config), "state" : ("state", Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State)}
                                self._child_list_classes = {}

                                self.config = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"
                                self._children_yang_names.add("config")

                                self.state = Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._children_yang_names.add("state")
                                self._segment_path = lambda: "admin-groups"


                            class Config(Entity):
                                """
                                Configuration data 
                                
                                .. attribute:: exclude_group
                                
                                	list of references to named admin\-groups to exclude in path calculation
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                .. attribute:: include_all_group
                                
                                	list of references to named admin\-groups of which all must be included
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                .. attribute:: include_any_group
                                
                                	list of references to named admin\-groups of which one must be included
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "admin-groups"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.exclude_group = YLeafList(YType.str, "exclude-group")

                                    self.include_all_group = YLeafList(YType.str, "include-all-group")

                                    self.include_any_group = YLeafList(YType.str, "include-any-group")
                                    self._segment_path = lambda: "config"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config, ['exclude_group', 'include_all_group', 'include_any_group'], name, value)


                            class State(Entity):
                                """
                                Operational state data 
                                
                                .. attribute:: exclude_group
                                
                                	list of references to named admin\-groups to exclude in path calculation
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                .. attribute:: include_all_group
                                
                                	list of references to named admin\-groups of which all must be included
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                .. attribute:: include_any_group
                                
                                	list of references to named admin\-groups of which one must be included
                                	**type**\:  list of str
                                
                                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "admin-groups"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.exclude_group = YLeafList(YType.str, "exclude-group")

                                    self.include_all_group = YLeafList(YType.str, "include-all-group")

                                    self.include_any_group = YLeafList(YType.str, "include-any-group")
                                    self._segment_path = lambda: "state"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State, ['exclude_group', 'include_all_group', 'include_any_group'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters related to paths
                            
                            .. attribute:: cspf_tiebreaker
                            
                            	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                            	**type**\:   :py:class:`CspfTieBreaking <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking>`
                            
                            .. attribute:: explicit_path_name
                            
                            	reference to a defined path
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config>`
                            
                            .. attribute:: hold_priority
                            
                            	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**default value**\: 0
                            
                            .. attribute:: name
                            
                            	Path name
                            	**type**\:  str
                            
                            .. attribute:: path_computation_method
                            
                            	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                            	**type**\:   :py:class:`PathComputationMethod <ydk.models.openconfig.openconfig_mpls.PathComputationMethod>`
                            
                            	**default value**\: locally-computed
                            
                            .. attribute:: path_computation_server
                            
                            	Address of the external path computation server
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: preference
                            
                            	Specifies a preference for this path. The lower the number higher the preference
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: retry_timer
                            
                            	sets the time between attempts to establish the LSP
                            	**type**\:  int
                            
                            	**range:** 1..600
                            
                            	**units**\: seconds
                            
                            .. attribute:: setup_priority
                            
                            	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**default value**\: 7
                            
                            .. attribute:: use_cspf
                            
                            	Flag to enable CSPF for locally computed LSPs
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "p2p-secondary-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.cspf_tiebreaker = YLeaf(YType.enumeration, "cspf-tiebreaker")

                                self.explicit_path_name = YLeaf(YType.str, "explicit-path-name")

                                self.hold_priority = YLeaf(YType.uint8, "hold-priority")

                                self.name = YLeaf(YType.str, "name")

                                self.path_computation_method = YLeaf(YType.identityref, "path-computation-method")

                                self.path_computation_server = YLeaf(YType.str, "path-computation-server")

                                self.preference = YLeaf(YType.uint8, "preference")

                                self.retry_timer = YLeaf(YType.uint16, "retry-timer")

                                self.setup_priority = YLeaf(YType.uint8, "setup-priority")

                                self.use_cspf = YLeaf(YType.boolean, "use-cspf")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config, ['cspf_tiebreaker', 'explicit_path_name', 'hold_priority', 'name', 'path_computation_method', 'path_computation_server', 'preference', 'retry_timer', 'setup_priority', 'use_cspf'], name, value)


                        class State(Entity):
                            """
                            State parameters related to paths
                            
                            .. attribute:: cspf_tiebreaker
                            
                            	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                            	**type**\:   :py:class:`CspfTieBreaking <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking>`
                            
                            .. attribute:: explicit_path_name
                            
                            	reference to a defined path
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config>`
                            
                            .. attribute:: hold_priority
                            
                            	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**default value**\: 0
                            
                            .. attribute:: name
                            
                            	Path name
                            	**type**\:  str
                            
                            .. attribute:: path_computation_method
                            
                            	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                            	**type**\:   :py:class:`PathComputationMethod <ydk.models.openconfig.openconfig_mpls.PathComputationMethod>`
                            
                            	**default value**\: locally-computed
                            
                            .. attribute:: path_computation_server
                            
                            	Address of the external path computation server
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: preference
                            
                            	Specifies a preference for this path. The lower the number higher the preference
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            .. attribute:: retry_timer
                            
                            	sets the time between attempts to establish the LSP
                            	**type**\:  int
                            
                            	**range:** 1..600
                            
                            	**units**\: seconds
                            
                            .. attribute:: setup_priority
                            
                            	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            	**default value**\: 7
                            
                            .. attribute:: use_cspf
                            
                            	Flag to enable CSPF for locally computed LSPs
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "p2p-secondary-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.cspf_tiebreaker = YLeaf(YType.enumeration, "cspf-tiebreaker")

                                self.explicit_path_name = YLeaf(YType.str, "explicit-path-name")

                                self.hold_priority = YLeaf(YType.uint8, "hold-priority")

                                self.name = YLeaf(YType.str, "name")

                                self.path_computation_method = YLeaf(YType.identityref, "path-computation-method")

                                self.path_computation_server = YLeaf(YType.str, "path-computation-server")

                                self.preference = YLeaf(YType.uint8, "preference")

                                self.retry_timer = YLeaf(YType.uint16, "retry-timer")

                                self.setup_priority = YLeaf(YType.uint8, "setup-priority")

                                self.use_cspf = YLeaf(YType.boolean, "use-cspf")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State, ['cspf_tiebreaker', 'explicit_path_name', 'hold_priority', 'name', 'path_computation_method', 'path_computation_server', 'preference', 'retry_timer', 'setup_priority', 'use_cspf'], name, value)


                    class State(Entity):
                        """
                        State parameters for P2P LSPs
                        
                        .. attribute:: destination
                        
                        	P2P tunnel destination address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "p2p-tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.destination = YLeaf(YType.str, "destination")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State, ['destination'], name, value)


                class State(Entity):
                    """
                    State parameters related to TE tunnels
                    
                    .. attribute:: admin_status
                    
                    	TE tunnel administrative state
                    	**type**\:   :py:class:`TunnelAdminStatus <ydk.models.openconfig.openconfig_mpls_types.TunnelAdminStatus>`
                    
                    	**default value**\: mplst:ADMIN_UP
                    
                    .. attribute:: counters
                    
                    	State data for MPLS label switched paths. This state data is specific to a single label switched path
                    	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters>`
                    
                    .. attribute:: description
                    
                    	optional text description for the tunnel
                    	**type**\:  str
                    
                    .. attribute:: hold_priority
                    
                    	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    	**default value**\: 0
                    
                    .. attribute:: local_id
                    
                    	locally signficant optional identifier for the tunnel; may be a numerical or string value
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    	**type**\:  str
                    
                    
                    ----
                    .. attribute:: metric
                    
                    	LSP metric, either explicit or IGP
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`TeMetricType <ydk.models.openconfig.openconfig_mpls.TeMetricType>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    .. attribute:: name
                    
                    	The tunnel name
                    	**type**\:  str
                    
                    .. attribute:: oper_status
                    
                    	The operational status of the TE tunnel
                    	**type**\:   :py:class:`LspOperStatus <ydk.models.openconfig.openconfig_mpls_types.LspOperStatus>`
                    
                    .. attribute:: preference
                    
                    	Specifies a preference for this tunnel. A lower number signifies a better preference
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    .. attribute:: protection_style_requested
                    
                    	style of mpls frr protection desired\: can be link, link\-node or unprotected
                    	**type**\:   :py:class:`ProtectionType <ydk.models.openconfig.openconfig_mpls_types.ProtectionType>`
                    
                    	**default value**\: mplst:unprotected
                    
                    .. attribute:: reoptimize_timer
                    
                    	frequency of reoptimization of a traffic engineered LSP
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**units**\: seconds
                    
                    .. attribute:: role
                    
                    	The lsp role at the current node, whether it is headend, transit or tailend
                    	**type**\:   :py:class:`LspRole <ydk.models.openconfig.openconfig_mpls_types.LspRole>`
                    
                    .. attribute:: setup_priority
                    
                    	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    	**default value**\: 7
                    
                    .. attribute:: signaling_protocol
                    
                    	Signaling protocol used to set up this tunnel
                    	**type**\:   :py:class:`TunnelType <ydk.models.openconfig.openconfig_mpls_types.TunnelType>`
                    
                    .. attribute:: soft_preemption
                    
                    	Enables RSVP soft\-preemption on this LSP
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: source
                    
                    	RSVP\-TE tunnel source address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: type
                    
                    	Tunnel type, p2p or p2mp
                    	**type**\:   :py:class:`TunnelType <ydk.models.openconfig.openconfig_mpls_types.TunnelType>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.ConstrainedPath.Tunnel.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"counters" : ("counters", Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters)}
                        self._child_list_classes = {}

                        self.admin_status = YLeaf(YType.identityref, "admin-status")

                        self.description = YLeaf(YType.str, "description")

                        self.hold_priority = YLeaf(YType.uint8, "hold-priority")

                        self.local_id = YLeaf(YType.str, "local-id")

                        self.metric = YLeaf(YType.str, "metric")

                        self.name = YLeaf(YType.str, "name")

                        self.oper_status = YLeaf(YType.identityref, "oper-status")

                        self.preference = YLeaf(YType.uint8, "preference")

                        self.protection_style_requested = YLeaf(YType.identityref, "protection-style-requested")

                        self.reoptimize_timer = YLeaf(YType.uint16, "reoptimize-timer")

                        self.role = YLeaf(YType.identityref, "role")

                        self.setup_priority = YLeaf(YType.uint8, "setup-priority")

                        self.signaling_protocol = YLeaf(YType.identityref, "signaling-protocol")

                        self.soft_preemption = YLeaf(YType.boolean, "soft-preemption")

                        self.source = YLeaf(YType.str, "source")

                        self.type = YLeaf(YType.identityref, "type")

                        self.counters = Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._children_yang_names.add("counters")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.State, ['admin_status', 'description', 'hold_priority', 'local_id', 'metric', 'name', 'oper_status', 'preference', 'protection_style_requested', 'reoptimize_timer', 'role', 'setup_priority', 'signaling_protocol', 'soft_preemption', 'source', 'type'], name, value)


                    class Counters(Entity):
                        """
                        State data for MPLS label switched paths. This state
                        data is specific to a single label switched path.
                        
                        .. attribute:: bytes
                        
                        	Number of bytes that have been forwarded over the label switched path
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: current_path_time
                        
                        	Indicates the time the LSP switched onto its current path. This is reset upon a LSP path change
                        	**type**\:  str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: next_reoptimization_time
                        
                        	Indicates the next scheduled time the LSP will be reoptimized
                        	**type**\:  str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: online_time
                        
                        	Indication of the time the label switched path transitioned to an Oper Up or in\-service state
                        	**type**\:  str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: packets
                        
                        	Number of pacets that have been forwarded over the label switched path
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: path_changes
                        
                        	Number of path changes for the label switched path
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: state_changes
                        
                        	Number of state changes for the label switched path
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bytes = YLeaf(YType.uint64, "bytes")

                            self.current_path_time = YLeaf(YType.str, "current-path-time")

                            self.next_reoptimization_time = YLeaf(YType.str, "next-reoptimization-time")

                            self.online_time = YLeaf(YType.str, "online-time")

                            self.packets = YLeaf(YType.uint64, "packets")

                            self.path_changes = YLeaf(YType.uint64, "path-changes")

                            self.state_changes = YLeaf(YType.uint64, "state-changes")
                            self._segment_path = lambda: "counters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters, ['bytes', 'current_path_time', 'next_reoptimization_time', 'online_time', 'packets', 'path_changes', 'state_changes'], name, value)


        class StaticLsps(Entity):
            """
            statically configured LSPs, without dynamic
            signaling
            
            .. attribute:: label_switched_path
            
            	list of defined static LSPs
            	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.LabelSwitchedPath>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.Lsps.StaticLsps, self).__init__()

                self.yang_name = "static-lsps"
                self.yang_parent_name = "lsps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"label-switched-path" : ("label_switched_path", Mpls.Lsps.StaticLsps.LabelSwitchedPath)}

                self.label_switched_path = YList(self)
                self._segment_path = lambda: "static-lsps"
                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Lsps.StaticLsps, [], name, value)


            class LabelSwitchedPath(Entity):
                """
                list of defined static LSPs
                
                .. attribute:: name  <key>
                
                	name to identify the LSP
                	**type**\:  str
                
                .. attribute:: egress
                
                	static LSPs for which the router is a egress  node
                	**type**\:   :py:class:`Egress <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress>`
                
                .. attribute:: ingress
                
                	Static LSPs for which the router is an ingress node
                	**type**\:   :py:class:`Ingress <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress>`
                
                .. attribute:: transit
                
                	static LSPs for which the router is a transit node
                	**type**\:   :py:class:`Transit <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.Lsps.StaticLsps.LabelSwitchedPath, self).__init__()

                    self.yang_name = "label-switched-path"
                    self.yang_parent_name = "static-lsps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"egress" : ("egress", Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress), "ingress" : ("ingress", Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress), "transit" : ("transit", Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.egress = Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress()
                    self.egress.parent = self
                    self._children_name_map["egress"] = "egress"
                    self._children_yang_names.add("egress")

                    self.ingress = Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress()
                    self.ingress.parent = self
                    self._children_name_map["ingress"] = "ingress"
                    self._children_yang_names.add("ingress")

                    self.transit = Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit()
                    self.transit.parent = self
                    self._children_name_map["transit"] = "transit"
                    self._children_yang_names.add("transit")
                    self._segment_path = lambda: "label-switched-path" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/static-lsps/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Lsps.StaticLsps.LabelSwitchedPath, ['name'], name, value)


                class Egress(Entity):
                    """
                    static LSPs for which the router is a
                    egress  node
                    
                    .. attribute:: incoming_label
                    
                    	label value on the incoming packet
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    
                    ----
                    	**type**\:   :py:class:`MplsLabel <ydk.models.openconfig.openconfig_mpls_types.MplsLabel>`
                    
                    
                    ----
                    .. attribute:: next_hop
                    
                    	next hop IP address for the LSP
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: push_label
                    
                    	label value to push at the current hop for the LSP
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    
                    ----
                    	**type**\:   :py:class:`MplsLabel <ydk.models.openconfig.openconfig_mpls_types.MplsLabel>`
                    
                    
                    ----
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress, self).__init__()

                        self.yang_name = "egress"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.incoming_label = YLeaf(YType.str, "incoming-label")

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.push_label = YLeaf(YType.str, "push-label")
                        self._segment_path = lambda: "egress"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress, ['incoming_label', 'next_hop', 'push_label'], name, value)


                class Ingress(Entity):
                    """
                    Static LSPs for which the router is an
                    ingress node
                    
                    .. attribute:: incoming_label
                    
                    	label value on the incoming packet
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    
                    ----
                    	**type**\:   :py:class:`MplsLabel <ydk.models.openconfig.openconfig_mpls_types.MplsLabel>`
                    
                    
                    ----
                    .. attribute:: next_hop
                    
                    	next hop IP address for the LSP
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: push_label
                    
                    	label value to push at the current hop for the LSP
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    
                    ----
                    	**type**\:   :py:class:`MplsLabel <ydk.models.openconfig.openconfig_mpls_types.MplsLabel>`
                    
                    
                    ----
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress, self).__init__()

                        self.yang_name = "ingress"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.incoming_label = YLeaf(YType.str, "incoming-label")

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.push_label = YLeaf(YType.str, "push-label")
                        self._segment_path = lambda: "ingress"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress, ['incoming_label', 'next_hop', 'push_label'], name, value)


                class Transit(Entity):
                    """
                    static LSPs for which the router is a
                    transit node
                    
                    .. attribute:: incoming_label
                    
                    	label value on the incoming packet
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    
                    ----
                    	**type**\:   :py:class:`MplsLabel <ydk.models.openconfig.openconfig_mpls_types.MplsLabel>`
                    
                    
                    ----
                    .. attribute:: next_hop
                    
                    	next hop IP address for the LSP
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: push_label
                    
                    	label value to push at the current hop for the LSP
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    
                    ----
                    	**type**\:   :py:class:`MplsLabel <ydk.models.openconfig.openconfig_mpls_types.MplsLabel>`
                    
                    
                    ----
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit, self).__init__()

                        self.yang_name = "transit"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.incoming_label = YLeaf(YType.str, "incoming-label")

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.push_label = YLeaf(YType.str, "push-label")
                        self._segment_path = lambda: "transit"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit, ['incoming_label', 'next_hop', 'push_label'], name, value)


        class UnconstrainedPath(Entity):
            """
            LSPs that use the IGP\-determined path, i.e., non
            traffic\-engineered, or non constrained\-path
            
            .. attribute:: path_setup_protocol
            
            	select and configure the signaling method for  the LSP
            	**type**\:   :py:class:`PathSetupProtocol <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.Lsps.UnconstrainedPath, self).__init__()

                self.yang_name = "unconstrained-path"
                self.yang_parent_name = "lsps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"path-setup-protocol" : ("path_setup_protocol", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol)}
                self._child_list_classes = {}

                self.path_setup_protocol = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol()
                self.path_setup_protocol.parent = self
                self._children_name_map["path_setup_protocol"] = "path-setup-protocol"
                self._children_yang_names.add("path-setup-protocol")
                self._segment_path = lambda: "unconstrained-path"
                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/%s" % self._segment_path()


            class PathSetupProtocol(Entity):
                """
                select and configure the signaling method for
                 the LSP
                
                .. attribute:: ldp
                
                	LDP signaling setup for IGP\-congruent LSPs
                	**type**\:   :py:class:`Ldp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp>`
                
                	**presence node**\: True
                
                .. attribute:: segment_routing
                
                	segment routing signaling extensions for IGP\-confgruent LSPs
                	**type**\:   :py:class:`SegmentRouting <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol, self).__init__()

                    self.yang_name = "path-setup-protocol"
                    self.yang_parent_name = "unconstrained-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"ldp" : ("ldp", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp), "segment-routing" : ("segment_routing", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting)}
                    self._child_list_classes = {}

                    self.ldp = None
                    self._children_name_map["ldp"] = "ldp"
                    self._children_yang_names.add("ldp")

                    self.segment_routing = None
                    self._children_name_map["segment_routing"] = "segment-routing"
                    self._children_yang_names.add("segment-routing")
                    self._segment_path = lambda: "path-setup-protocol"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/%s" % self._segment_path()


                class Ldp(Entity):
                    """
                    LDP signaling setup for IGP\-congruent LSPs
                    
                    .. attribute:: tunnel
                    
                    	contains configuration stanzas for different LSP tunnel types (P2P, P2MP, etc.)
                    	**type**\:   :py:class:`Tunnel <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp, self).__init__()

                        self.yang_name = "ldp"
                        self.yang_parent_name = "path-setup-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"tunnel" : ("tunnel", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel)}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.tunnel = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel()
                        self.tunnel.parent = self
                        self._children_name_map["tunnel"] = "tunnel"
                        self._children_yang_names.add("tunnel")
                        self._segment_path = lambda: "ldp"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/%s" % self._segment_path()


                    class Tunnel(Entity):
                        """
                        contains configuration stanzas for different LSP
                        tunnel types (P2P, P2MP, etc.)
                        
                        .. attribute:: ldp_type
                        
                        	specify basic or targeted LDP LSP
                        	**type**\:   :py:class:`LdpType <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.LdpType>`
                        
                        .. attribute:: mp2mp_lsp
                        
                        	properties of multipoint\-to\-multipoint tunnels
                        	**type**\:   :py:class:`Mp2MpLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2MpLsp>`
                        
                        .. attribute:: p2mp_lsp
                        
                        	properties of point\-to\-multipoint tunnels
                        	**type**\:   :py:class:`P2MpLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2MpLsp>`
                        
                        .. attribute:: p2p_lsp
                        
                        	properties of point\-to\-point tunnels
                        	**type**\:   :py:class:`P2PLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp>`
                        
                        .. attribute:: tunnel_type
                        
                        	specifies the type of LSP, e.g., P2P or P2MP
                        	**type**\:   :py:class:`TunnelType <ydk.models.openconfig.openconfig_mpls_types.TunnelType>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel, self).__init__()

                            self.yang_name = "tunnel"
                            self.yang_parent_name = "ldp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"mp2mp-lsp" : ("mp2mp_lsp", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2MpLsp), "p2mp-lsp" : ("p2mp_lsp", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2MpLsp), "p2p-lsp" : ("p2p_lsp", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp)}
                            self._child_list_classes = {}

                            self.ldp_type = YLeaf(YType.enumeration, "ldp-type")

                            self.tunnel_type = YLeaf(YType.enumeration, "tunnel-type")

                            self.mp2mp_lsp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2MpLsp()
                            self.mp2mp_lsp.parent = self
                            self._children_name_map["mp2mp_lsp"] = "mp2mp-lsp"
                            self._children_yang_names.add("mp2mp-lsp")

                            self.p2mp_lsp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2MpLsp()
                            self.p2mp_lsp.parent = self
                            self._children_name_map["p2mp_lsp"] = "p2mp-lsp"
                            self._children_yang_names.add("p2mp-lsp")

                            self.p2p_lsp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp()
                            self.p2p_lsp.parent = self
                            self._children_name_map["p2p_lsp"] = "p2p-lsp"
                            self._children_yang_names.add("p2p-lsp")
                            self._segment_path = lambda: "tunnel"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/ldp/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel, ['ldp_type', 'tunnel_type'], name, value)

                        class LdpType(Enum):
                            """
                            LdpType

                            specify basic or targeted LDP LSP

                            .. data:: BASIC = 0

                            	basic hop-by-hop LSP

                            .. data:: TARGETED = 1

                            	tLDP LSP

                            """

                            BASIC = Enum.YLeaf(0, "BASIC")

                            TARGETED = Enum.YLeaf(1, "TARGETED")



                        class Mp2MpLsp(Entity):
                            """
                            properties of multipoint\-to\-multipoint tunnels
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2MpLsp, self).__init__()

                                self.yang_name = "mp2mp-lsp"
                                self.yang_parent_name = "tunnel"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "mp2mp-lsp"
                                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/ldp/tunnel/%s" % self._segment_path()


                        class P2MpLsp(Entity):
                            """
                            properties of point\-to\-multipoint tunnels
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2MpLsp, self).__init__()

                                self.yang_name = "p2mp-lsp"
                                self.yang_parent_name = "tunnel"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self._segment_path = lambda: "p2mp-lsp"
                                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/ldp/tunnel/%s" % self._segment_path()


                        class P2PLsp(Entity):
                            """
                            properties of point\-to\-point tunnels
                            
                            .. attribute:: fec_address
                            
                            	Address prefix for packets sharing the same forwarding equivalence class for the IGP\-based LSP
                            	**type**\: one of the below types:
                            
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            
                            ----
                            	**type**\:  list of str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            
                            ----
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp, self).__init__()

                                self.yang_name = "p2p-lsp"
                                self.yang_parent_name = "tunnel"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.fec_address = YLeafList(YType.str, "fec-address")
                                self._segment_path = lambda: "p2p-lsp"
                                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/ldp/tunnel/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp, ['fec_address'], name, value)


                class SegmentRouting(Entity):
                    """
                    segment routing signaling extensions for
                    IGP\-confgruent LSPs
                    
                    .. attribute:: tunnel
                    
                    	contains configuration stanzas for different LSP tunnel types (P2P, P2MP, etc.)
                    	**type**\:   :py:class:`Tunnel <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting, self).__init__()

                        self.yang_name = "segment-routing"
                        self.yang_parent_name = "path-setup-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"tunnel" : ("tunnel", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel)}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.tunnel = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel()
                        self.tunnel.parent = self
                        self._children_name_map["tunnel"] = "tunnel"
                        self._children_yang_names.add("tunnel")
                        self._segment_path = lambda: "segment-routing"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/%s" % self._segment_path()


                    class Tunnel(Entity):
                        """
                        contains configuration stanzas for different LSP
                        tunnel types (P2P, P2MP, etc.)
                        
                        .. attribute:: p2p_lsp
                        
                        	properties of point\-to\-point tunnels
                        	**type**\:   :py:class:`P2PLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp>`
                        
                        .. attribute:: tunnel_type
                        
                        	specifies the type of LSP, e.g., P2P or P2MP
                        	**type**\:   :py:class:`TunnelType <ydk.models.openconfig.openconfig_mpls_types.TunnelType>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel, self).__init__()

                            self.yang_name = "tunnel"
                            self.yang_parent_name = "segment-routing"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"p2p-lsp" : ("p2p_lsp", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp)}
                            self._child_list_classes = {}

                            self.tunnel_type = YLeaf(YType.enumeration, "tunnel-type")

                            self.p2p_lsp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp()
                            self.p2p_lsp.parent = self
                            self._children_name_map["p2p_lsp"] = "p2p-lsp"
                            self._children_yang_names.add("p2p-lsp")
                            self._segment_path = lambda: "tunnel"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/segment-routing/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel, ['tunnel_type'], name, value)


                        class P2PLsp(Entity):
                            """
                            properties of point\-to\-point tunnels
                            
                            .. attribute:: fec
                            
                            	List of FECs that are to be originated as SR LSPs
                            	**type**\: list of    :py:class:`Fec <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec>`
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp, self).__init__()

                                self.yang_name = "p2p-lsp"
                                self.yang_parent_name = "tunnel"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {"fec" : ("fec", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec)}

                                self.fec = YList(self)
                                self._segment_path = lambda: "p2p-lsp"
                                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/segment-routing/tunnel/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp, [], name, value)


                            class Fec(Entity):
                                """
                                List of FECs that are to be originated as SR LSPs
                                
                                .. attribute:: fec_address  <key>
                                
                                	FEC that is to be advertised as part of the Prefix\-SID
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: config
                                
                                	Configuration parameters relating to the FEC to be advertised by SR
                                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config>`
                                
                                .. attribute:: prefix_sid
                                
                                	Parameters relating to the Prefix\-SID used for the originated FEC
                                	**type**\:   :py:class:`PrefixSid <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid>`
                                
                                .. attribute:: state
                                
                                	Operational state relating to a FEC advertised by SR
                                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State>`
                                
                                

                                """

                                _prefix = 'mpls'
                                _revision = '2015-11-05'

                                def __init__(self):
                                    super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec, self).__init__()

                                    self.yang_name = "fec"
                                    self.yang_parent_name = "p2p-lsp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self._child_container_classes = {"config" : ("config", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config), "prefix-sid" : ("prefix_sid", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid), "state" : ("state", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State)}
                                    self._child_list_classes = {}

                                    self.fec_address = YLeaf(YType.str, "fec-address")

                                    self.config = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"
                                    self._children_yang_names.add("config")

                                    self.prefix_sid = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid()
                                    self.prefix_sid.parent = self
                                    self._children_name_map["prefix_sid"] = "prefix-sid"
                                    self._children_yang_names.add("prefix-sid")

                                    self.state = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._children_yang_names.add("state")
                                    self._segment_path = lambda: "fec" + "[fec-address='" + self.fec_address.get() + "']"
                                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/segment-routing/tunnel/p2p-lsp/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec, ['fec_address'], name, value)


                                class Config(Entity):
                                    """
                                    Configuration parameters relating to the FEC to be
                                    advertised by SR
                                    
                                    .. attribute:: fec_address
                                    
                                    	FEC that is to be advertised as part of the Prefix\-SID
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "fec"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.fec_address = YLeaf(YType.str, "fec-address")
                                        self._segment_path = lambda: "config"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config, ['fec_address'], name, value)


                                class PrefixSid(Entity):
                                    """
                                    Parameters relating to the Prefix\-SID
                                    used for the originated FEC
                                    
                                    .. attribute:: config
                                    
                                    	Configuration parameters relating to the Prefix\-SID used for the originated FEC
                                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state parameters relating to the Prefix\-SID used for the originated FEC
                                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State>`
                                    
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid, self).__init__()

                                        self.yang_name = "prefix-sid"
                                        self.yang_parent_name = "fec"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"config" : ("config", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config), "state" : ("state", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State)}
                                        self._child_list_classes = {}

                                        self.config = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"
                                        self._children_yang_names.add("config")

                                        self.state = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._children_yang_names.add("state")
                                        self._segment_path = lambda: "prefix-sid"


                                    class Config(Entity):
                                        """
                                        Configuration parameters relating to the Prefix\-SID
                                        used for the originated FEC
                                        
                                        .. attribute:: last_hop_behavior
                                        
                                        	Configuration relating to the LFIB actions for the Prefix\-SID to be used by the penultimate\-hop
                                        	**type**\:   :py:class:`LastHopBehavior <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config.LastHopBehavior>`
                                        
                                        .. attribute:: node_flag
                                        
                                        	Specifies that the Prefix\-SID is to be treated as a Node\-SID by setting the N\-flag in the advertised Prefix\-SID TLV in the IGP
                                        	**type**\:  bool
                                        
                                        .. attribute:: type
                                        
                                        	Specifies how the value of the Prefix\-SID should be interpreted \- whether as an offset to the SRGB, or as an absolute value
                                        	**type**\:   :py:class:`Type <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config.Type>`
                                        
                                        	**default value**\: INDEX
                                        
                                        

                                        """

                                        _prefix = 'mpls'
                                        _revision = '2015-11-05'

                                        def __init__(self):
                                            super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "prefix-sid"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.last_hop_behavior = YLeaf(YType.enumeration, "last-hop-behavior")

                                            self.node_flag = YLeaf(YType.boolean, "node-flag")

                                            self.type = YLeaf(YType.enumeration, "type")
                                            self._segment_path = lambda: "config"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config, ['last_hop_behavior', 'node_flag', 'type'], name, value)

                                        class LastHopBehavior(Enum):
                                            """
                                            LastHopBehavior

                                            Configuration relating to the LFIB actions for the

                                            Prefix\-SID to be used by the penultimate\-hop

                                            .. data:: EXPLICIT_NULL = 0

                                            	Specifies that the explicit null label is to be used

                                            	when the penultimate hop forwards a labelled packet to

                                            	this Prefix-SID

                                            .. data:: UNCHANGED = 1

                                            	Specicies that the Prefix-SID's label value is to be

                                            	left in place when the penultimate hop forwards to this

                                            	Prefix-SID

                                            .. data:: PHP = 2

                                            	Specicies that the penultimate hop should pop the

                                            	Prefix-SID label before forwarding to the eLER

                                            """

                                            EXPLICIT_NULL = Enum.YLeaf(0, "EXPLICIT-NULL")

                                            UNCHANGED = Enum.YLeaf(1, "UNCHANGED")

                                            PHP = Enum.YLeaf(2, "PHP")


                                        class Type(Enum):
                                            """
                                            Type

                                            Specifies how the value of the Prefix\-SID should be

                                            interpreted \- whether as an offset to the SRGB, or as an

                                            absolute value

                                            .. data:: INDEX = 0

                                            	Set when the value of the prefix SID should be specified

                                            	as an off-set from the SRGB's zero-value. When multiple

                                            	SRGBs are specified, the zero-value is the minimum

                                            	of their lower bounds

                                            .. data:: ABSOLUTE = 1

                                            	Set when the value of a prefix SID is specified as the

                                            	absolute value within an SRGB. It is an error to specify

                                            	an absolute value outside of a specified SRGB

                                            """

                                            INDEX = Enum.YLeaf(0, "INDEX")

                                            ABSOLUTE = Enum.YLeaf(1, "ABSOLUTE")



                                    class State(Entity):
                                        """
                                        Operational state parameters relating to the
                                        Prefix\-SID used for the originated FEC
                                        
                                        .. attribute:: last_hop_behavior
                                        
                                        	Configuration relating to the LFIB actions for the Prefix\-SID to be used by the penultimate\-hop
                                        	**type**\:   :py:class:`LastHopBehavior <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State.LastHopBehavior>`
                                        
                                        .. attribute:: node_flag
                                        
                                        	Specifies that the Prefix\-SID is to be treated as a Node\-SID by setting the N\-flag in the advertised Prefix\-SID TLV in the IGP
                                        	**type**\:  bool
                                        
                                        .. attribute:: type
                                        
                                        	Specifies how the value of the Prefix\-SID should be interpreted \- whether as an offset to the SRGB, or as an absolute value
                                        	**type**\:   :py:class:`Type <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State.Type>`
                                        
                                        	**default value**\: INDEX
                                        
                                        

                                        """

                                        _prefix = 'mpls'
                                        _revision = '2015-11-05'

                                        def __init__(self):
                                            super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "prefix-sid"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.last_hop_behavior = YLeaf(YType.enumeration, "last-hop-behavior")

                                            self.node_flag = YLeaf(YType.boolean, "node-flag")

                                            self.type = YLeaf(YType.enumeration, "type")
                                            self._segment_path = lambda: "state"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State, ['last_hop_behavior', 'node_flag', 'type'], name, value)

                                        class LastHopBehavior(Enum):
                                            """
                                            LastHopBehavior

                                            Configuration relating to the LFIB actions for the

                                            Prefix\-SID to be used by the penultimate\-hop

                                            .. data:: EXPLICIT_NULL = 0

                                            	Specifies that the explicit null label is to be used

                                            	when the penultimate hop forwards a labelled packet to

                                            	this Prefix-SID

                                            .. data:: UNCHANGED = 1

                                            	Specicies that the Prefix-SID's label value is to be

                                            	left in place when the penultimate hop forwards to this

                                            	Prefix-SID

                                            .. data:: PHP = 2

                                            	Specicies that the penultimate hop should pop the

                                            	Prefix-SID label before forwarding to the eLER

                                            """

                                            EXPLICIT_NULL = Enum.YLeaf(0, "EXPLICIT-NULL")

                                            UNCHANGED = Enum.YLeaf(1, "UNCHANGED")

                                            PHP = Enum.YLeaf(2, "PHP")


                                        class Type(Enum):
                                            """
                                            Type

                                            Specifies how the value of the Prefix\-SID should be

                                            interpreted \- whether as an offset to the SRGB, or as an

                                            absolute value

                                            .. data:: INDEX = 0

                                            	Set when the value of the prefix SID should be specified

                                            	as an off-set from the SRGB's zero-value. When multiple

                                            	SRGBs are specified, the zero-value is the minimum

                                            	of their lower bounds

                                            .. data:: ABSOLUTE = 1

                                            	Set when the value of a prefix SID is specified as the

                                            	absolute value within an SRGB. It is an error to specify

                                            	an absolute value outside of a specified SRGB

                                            """

                                            INDEX = Enum.YLeaf(0, "INDEX")

                                            ABSOLUTE = Enum.YLeaf(1, "ABSOLUTE")



                                class State(Entity):
                                    """
                                    Operational state relating to a FEC advertised by SR
                                    
                                    .. attribute:: fec_address
                                    
                                    	FEC that is to be advertised as part of the Prefix\-SID
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'mpls'
                                    _revision = '2015-11-05'

                                    def __init__(self):
                                        super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "fec"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.fec_address = YLeaf(YType.str, "fec-address")
                                        self._segment_path = lambda: "state"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State, ['fec_address'], name, value)


    class SignalingProtocols(Entity):
        """
        top\-level signaling protocol configuration
        
        .. attribute:: ldp
        
        	LDP global signaling configuration
        	**type**\:   :py:class:`Ldp <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.Ldp>`
        
        .. attribute:: rsvp_te
        
        	RSVP\-TE global signaling protocol configuration
        	**type**\:   :py:class:`RsvpTe <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe>`
        
        .. attribute:: segment_routing
        
        	SR global signaling config
        	**type**\:   :py:class:`SegmentRouting <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            super(Mpls.SignalingProtocols, self).__init__()

            self.yang_name = "signaling-protocols"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"ldp" : ("ldp", Mpls.SignalingProtocols.Ldp), "rsvp-te" : ("rsvp_te", Mpls.SignalingProtocols.RsvpTe), "segment-routing" : ("segment_routing", Mpls.SignalingProtocols.SegmentRouting)}
            self._child_list_classes = {}

            self.ldp = Mpls.SignalingProtocols.Ldp()
            self.ldp.parent = self
            self._children_name_map["ldp"] = "ldp"
            self._children_yang_names.add("ldp")

            self.rsvp_te = Mpls.SignalingProtocols.RsvpTe()
            self.rsvp_te.parent = self
            self._children_name_map["rsvp_te"] = "rsvp-te"
            self._children_yang_names.add("rsvp-te")

            self.segment_routing = Mpls.SignalingProtocols.SegmentRouting()
            self.segment_routing.parent = self
            self._children_name_map["segment_routing"] = "segment-routing"
            self._children_yang_names.add("segment-routing")
            self._segment_path = lambda: "signaling-protocols"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()


        class Ldp(Entity):
            """
            LDP global signaling configuration
            
            .. attribute:: timers
            
            	LDP timers
            	**type**\:   :py:class:`Timers <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.Ldp.Timers>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.SignalingProtocols.Ldp, self).__init__()

                self.yang_name = "ldp"
                self.yang_parent_name = "signaling-protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"timers" : ("timers", Mpls.SignalingProtocols.Ldp.Timers)}
                self._child_list_classes = {}

                self.timers = Mpls.SignalingProtocols.Ldp.Timers()
                self.timers.parent = self
                self._children_name_map["timers"] = "timers"
                self._children_yang_names.add("timers")
                self._segment_path = lambda: "ldp"
                self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/%s" % self._segment_path()


            class Timers(Entity):
                """
                LDP timers
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.SignalingProtocols.Ldp.Timers, self).__init__()

                    self.yang_name = "timers"
                    self.yang_parent_name = "ldp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self._segment_path = lambda: "timers"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/ldp/%s" % self._segment_path()


        class RsvpTe(Entity):
            """
            RSVP\-TE global signaling protocol configuration
            
            .. attribute:: global_
            
            	Platform wide RSVP configuration and state
            	**type**\:   :py:class:`Global_ <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_>`
            
            .. attribute:: interface_attributes
            
            	Attributes relating to RSVP\-TE enabled interfaces
            	**type**\:   :py:class:`InterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes>`
            
            .. attribute:: neighbors
            
            	Configuration and state for RSVP neighbors connecting to the device
            	**type**\:   :py:class:`Neighbors <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors>`
            
            .. attribute:: sessions
            
            	Configuration and state of RSVP sessions
            	**type**\:   :py:class:`Sessions <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.SignalingProtocols.RsvpTe, self).__init__()

                self.yang_name = "rsvp-te"
                self.yang_parent_name = "signaling-protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"global" : ("global_", Mpls.SignalingProtocols.RsvpTe.Global_), "interface-attributes" : ("interface_attributes", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes), "neighbors" : ("neighbors", Mpls.SignalingProtocols.RsvpTe.Neighbors), "sessions" : ("sessions", Mpls.SignalingProtocols.RsvpTe.Sessions)}
                self._child_list_classes = {}

                self.global_ = Mpls.SignalingProtocols.RsvpTe.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
                self._children_yang_names.add("global")

                self.interface_attributes = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes()
                self.interface_attributes.parent = self
                self._children_name_map["interface_attributes"] = "interface-attributes"
                self._children_yang_names.add("interface-attributes")

                self.neighbors = Mpls.SignalingProtocols.RsvpTe.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
                self._children_yang_names.add("neighbors")

                self.sessions = Mpls.SignalingProtocols.RsvpTe.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")
                self._segment_path = lambda: "rsvp-te"
                self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/%s" % self._segment_path()


            class Global_(Entity):
                """
                Platform wide RSVP configuration and state
                
                .. attribute:: graceful_restart
                
                	Operational state and configuration parameters relating to graceful\-restart for RSVP
                	**type**\:   :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart>`
                
                .. attribute:: hellos
                
                	Top level container for RSVP hello parameters
                	**type**\:   :py:class:`Hellos <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.Hellos>`
                
                .. attribute:: soft_preemption
                
                	Protocol options relating to RSVP soft preemption
                	**type**\:   :py:class:`SoftPreemption <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption>`
                
                .. attribute:: state
                
                	Platform wide RSVP state, including counters
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.SignalingProtocols.RsvpTe.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "rsvp-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"graceful-restart" : ("graceful_restart", Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart), "hellos" : ("hellos", Mpls.SignalingProtocols.RsvpTe.Global_.Hellos), "soft-preemption" : ("soft_preemption", Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.Global_.State)}
                    self._child_list_classes = {}

                    self.graceful_restart = Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart()
                    self.graceful_restart.parent = self
                    self._children_name_map["graceful_restart"] = "graceful-restart"
                    self._children_yang_names.add("graceful-restart")

                    self.hellos = Mpls.SignalingProtocols.RsvpTe.Global_.Hellos()
                    self.hellos.parent = self
                    self._children_name_map["hellos"] = "hellos"
                    self._children_yang_names.add("hellos")

                    self.soft_preemption = Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption()
                    self.soft_preemption.parent = self
                    self._children_name_map["soft_preemption"] = "soft-preemption"
                    self._children_yang_names.add("soft-preemption")

                    self.state = Mpls.SignalingProtocols.RsvpTe.Global_.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "global"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/%s" % self._segment_path()


                class GracefulRestart(Entity):
                    """
                    Operational state and configuration parameters relating to
                    graceful\-restart for RSVP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to graceful\-restart
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with RSVP graceful\-restart
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart, self).__init__()

                        self.yang_name = "graceful-restart"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State)}
                        self._child_list_classes = {}

                        self.config = Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "graceful-restart"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/%s" % self._segment_path()


                    class Config(Entity):
                        """
                        Configuration parameters relating to
                        graceful\-restart
                        
                        .. attribute:: enable
                        
                        	Enables graceful restart on the node
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: recovery_time
                        
                        	RSVP state recovery time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restart_time
                        
                        	Graceful restart time (seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "graceful-restart"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.boolean, "enable")

                            self.recovery_time = YLeaf(YType.uint32, "recovery-time")

                            self.restart_time = YLeaf(YType.uint32, "restart-time")
                            self._segment_path = lambda: "config"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/graceful-restart/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config, ['enable', 'recovery_time', 'restart_time'], name, value)


                    class State(Entity):
                        """
                        State information associated with
                        RSVP graceful\-restart
                        
                        .. attribute:: enable
                        
                        	Enables graceful restart on the node
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: recovery_time
                        
                        	RSVP state recovery time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: restart_time
                        
                        	Graceful restart time (seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "graceful-restart"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.boolean, "enable")

                            self.recovery_time = YLeaf(YType.uint32, "recovery-time")

                            self.restart_time = YLeaf(YType.uint32, "restart-time")
                            self._segment_path = lambda: "state"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/graceful-restart/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State, ['enable', 'recovery_time', 'restart_time'], name, value)


                class Hellos(Entity):
                    """
                    Top level container for RSVP hello parameters
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to RSVP hellos
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with RSVP hellos
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.Global_.Hellos, self).__init__()

                        self.yang_name = "hellos"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State)}
                        self._child_list_classes = {}

                        self.config = Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "hellos"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/%s" % self._segment_path()


                    class Config(Entity):
                        """
                        Configuration parameters relating to RSVP
                        hellos
                        
                        .. attribute:: hello_interval
                        
                        	set the interval in ms between RSVP hello messages
                        	**type**\:  int
                        
                        	**range:** 1000..60000
                        
                        	**units**\: milliseconds
                        
                        	**default value**\: 9000
                        
                        .. attribute:: refresh_reduction
                        
                        	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "hellos"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.hello_interval = YLeaf(YType.uint16, "hello-interval")

                            self.refresh_reduction = YLeaf(YType.boolean, "refresh-reduction")
                            self._segment_path = lambda: "config"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/hellos/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config, ['hello_interval', 'refresh_reduction'], name, value)


                    class State(Entity):
                        """
                        State information associated with RSVP hellos
                        
                        .. attribute:: hello_interval
                        
                        	set the interval in ms between RSVP hello messages
                        	**type**\:  int
                        
                        	**range:** 1000..60000
                        
                        	**units**\: milliseconds
                        
                        	**default value**\: 9000
                        
                        .. attribute:: refresh_reduction
                        
                        	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "hellos"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.hello_interval = YLeaf(YType.uint16, "hello-interval")

                            self.refresh_reduction = YLeaf(YType.boolean, "refresh-reduction")
                            self._segment_path = lambda: "state"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/hellos/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State, ['hello_interval', 'refresh_reduction'], name, value)


                class SoftPreemption(Entity):
                    """
                    Protocol options relating to RSVP
                    soft preemption
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to RSVP soft preemption support
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters relating to RSVP soft preemption support
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption, self).__init__()

                        self.yang_name = "soft-preemption"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State)}
                        self._child_list_classes = {}

                        self.config = Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "soft-preemption"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/%s" % self._segment_path()


                    class Config(Entity):
                        """
                        Configuration parameters relating to RSVP
                        soft preemption support
                        
                        .. attribute:: enable
                        
                        	Enables soft preemption on a node
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: soft_preemption_timeout
                        
                        	Timeout value for soft preemption to revert to hard preemption
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "soft-preemption"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.boolean, "enable")

                            self.soft_preemption_timeout = YLeaf(YType.uint16, "soft-preemption-timeout")
                            self._segment_path = lambda: "config"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/soft-preemption/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config, ['enable', 'soft_preemption_timeout'], name, value)


                    class State(Entity):
                        """
                        State parameters relating to RSVP
                        soft preemption support
                        
                        .. attribute:: enable
                        
                        	Enables soft preemption on a node
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: soft_preemption_timeout
                        
                        	Timeout value for soft preemption to revert to hard preemption
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "soft-preemption"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.boolean, "enable")

                            self.soft_preemption_timeout = YLeaf(YType.uint16, "soft-preemption-timeout")
                            self._segment_path = lambda: "state"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/soft-preemption/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State, ['enable', 'soft_preemption_timeout'], name, value)


                class State(Entity):
                    """
                    Platform wide RSVP state, including counters
                    
                    .. attribute:: counters
                    
                    	Platform wide RSVP statistics and counters
                    	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.Global_.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"counters" : ("counters", Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters)}
                        self._child_list_classes = {}

                        self.counters = Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._children_yang_names.add("counters")
                        self._segment_path = lambda: "state"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/%s" % self._segment_path()


                    class Counters(Entity):
                        """
                        Platform wide RSVP statistics and counters
                        
                        .. attribute:: in_ack_messages
                        
                        	Number of received RSVP refresh reduction ack messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_hello_messages
                        
                        	Number of received RSVP hello messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_path_error_messages
                        
                        	Number of received RSVP Path Error messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_path_messages
                        
                        	Number of received RSVP Path messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_path_tear_messages
                        
                        	Number of received RSVP Path Tear messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_reservation_error_messages
                        
                        	Number of received RSVP Resv Error messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_reservation_messages
                        
                        	Number of received RSVP Resv messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_reservation_tear_messages
                        
                        	Number of received RSVP Resv Tear messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: in_srefresh_messages
                        
                        	Number of received RSVP summary refresh messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_ack_messages
                        
                        	Number of sent RSVP refresh reduction ack messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_hello_messages
                        
                        	Number of sent RSVP hello messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_path_error_messages
                        
                        	Number of sent RSVP Path Error messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_path_messages
                        
                        	Number of sent RSVP PATH messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_path_tear_messages
                        
                        	Number of sent RSVP Path Tear messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_reservation_error_messages
                        
                        	Number of sent RSVP Resv Error messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_reservation_messages
                        
                        	Number of sent RSVP Resv messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_reservation_tear_messages
                        
                        	Number of sent RSVP Resv Tear messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: out_srefresh_messages
                        
                        	Number of sent RSVP summary refresh messages
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: path_timeouts
                        
                        	TODO
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: rate_limited_messages
                        
                        	RSVP messages dropped due to rate limiting
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: reservation_timeouts
                        
                        	TODO
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.in_ack_messages = YLeaf(YType.uint64, "in-ack-messages")

                            self.in_hello_messages = YLeaf(YType.uint64, "in-hello-messages")

                            self.in_path_error_messages = YLeaf(YType.uint64, "in-path-error-messages")

                            self.in_path_messages = YLeaf(YType.uint64, "in-path-messages")

                            self.in_path_tear_messages = YLeaf(YType.uint64, "in-path-tear-messages")

                            self.in_reservation_error_messages = YLeaf(YType.uint64, "in-reservation-error-messages")

                            self.in_reservation_messages = YLeaf(YType.uint64, "in-reservation-messages")

                            self.in_reservation_tear_messages = YLeaf(YType.uint64, "in-reservation-tear-messages")

                            self.in_srefresh_messages = YLeaf(YType.uint64, "in-srefresh-messages")

                            self.out_ack_messages = YLeaf(YType.uint64, "out-ack-messages")

                            self.out_hello_messages = YLeaf(YType.uint64, "out-hello-messages")

                            self.out_path_error_messages = YLeaf(YType.uint64, "out-path-error-messages")

                            self.out_path_messages = YLeaf(YType.uint64, "out-path-messages")

                            self.out_path_tear_messages = YLeaf(YType.uint64, "out-path-tear-messages")

                            self.out_reservation_error_messages = YLeaf(YType.uint64, "out-reservation-error-messages")

                            self.out_reservation_messages = YLeaf(YType.uint64, "out-reservation-messages")

                            self.out_reservation_tear_messages = YLeaf(YType.uint64, "out-reservation-tear-messages")

                            self.out_srefresh_messages = YLeaf(YType.uint64, "out-srefresh-messages")

                            self.path_timeouts = YLeaf(YType.uint64, "path-timeouts")

                            self.rate_limited_messages = YLeaf(YType.uint64, "rate-limited-messages")

                            self.reservation_timeouts = YLeaf(YType.uint64, "reservation-timeouts")
                            self._segment_path = lambda: "counters"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/state/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters, ['in_ack_messages', 'in_hello_messages', 'in_path_error_messages', 'in_path_messages', 'in_path_tear_messages', 'in_reservation_error_messages', 'in_reservation_messages', 'in_reservation_tear_messages', 'in_srefresh_messages', 'out_ack_messages', 'out_hello_messages', 'out_path_error_messages', 'out_path_messages', 'out_path_tear_messages', 'out_reservation_error_messages', 'out_reservation_messages', 'out_reservation_tear_messages', 'out_srefresh_messages', 'path_timeouts', 'rate_limited_messages', 'reservation_timeouts'], name, value)


            class InterfaceAttributes(Entity):
                """
                Attributes relating to RSVP\-TE enabled interfaces
                
                .. attribute:: interface
                
                	list of per\-interface RSVP configurations
                	**type**\: list of    :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes, self).__init__()

                    self.yang_name = "interface-attributes"
                    self.yang_parent_name = "rsvp-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interface-attributes"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes, [], name, value)


                class Interface(Entity):
                    """
                    list of per\-interface RSVP configurations
                    
                    .. attribute:: interface_name  <key>
                    
                    	references a configured IP interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`interface_name <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config>`
                    
                    .. attribute:: authentication
                    
                    	Configuration and state parameters relating to RSVP authentication as per RFC2747
                    	**type**\:   :py:class:`Authentication <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication>`
                    
                    .. attribute:: config
                    
                    	Configuration of per\-interface RSVP parameters
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config>`
                    
                    .. attribute:: hellos
                    
                    	Top level container for RSVP hello parameters
                    	**type**\:   :py:class:`Hellos <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos>`
                    
                    .. attribute:: protection
                    
                    	link\-protection (NHOP) related configuration
                    	**type**\:   :py:class:`Protection <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection>`
                    
                    .. attribute:: state
                    
                    	Per\-interface RSVP protocol and state information
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State>`
                    
                    .. attribute:: subscription
                    
                    	Bandwidth percentage reservable by RSVP on an interface
                    	**type**\:   :py:class:`Subscription <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interface-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"authentication" : ("authentication", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication), "config" : ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config), "hellos" : ("hellos", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos), "protection" : ("protection", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State), "subscription" : ("subscription", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.authentication = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                        self._children_yang_names.add("authentication")

                        self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.hellos = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos()
                        self.hellos.parent = self
                        self._children_name_map["hellos"] = "hellos"
                        self._children_yang_names.add("hellos")

                        self.protection = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection()
                        self.protection.parent = self
                        self._children_name_map["protection"] = "protection"
                        self._children_yang_names.add("protection")

                        self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")

                        self.subscription = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription()
                        self.subscription.parent = self
                        self._children_name_map["subscription"] = "subscription"
                        self._children_yang_names.add("subscription")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/interface-attributes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface, ['interface_name'], name, value)


                    class Authentication(Entity):
                        """
                        Configuration and state parameters relating to RSVP
                        authentication as per RFC2747
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to authentication
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config>`
                        
                        .. attribute:: state
                        
                        	State information associated with authentication
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State)}
                            self._child_list_classes = {}

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "authentication"


                        class Config(Entity):
                            """
                            Configuration parameters relating
                            to authentication
                            
                            .. attribute:: authentication_key
                            
                            	authenticate RSVP signaling messages
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: enable
                            
                            	Enables RSVP authentication on the node
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "authentication"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.authentication_key = YLeaf(YType.str, "authentication-key")

                                self.enable = YLeaf(YType.boolean, "enable")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config, ['authentication_key', 'enable'], name, value)


                        class State(Entity):
                            """
                            State information associated
                            with authentication
                            
                            .. attribute:: authentication_key
                            
                            	authenticate RSVP signaling messages
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: enable
                            
                            	Enables RSVP authentication on the node
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "authentication"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.authentication_key = YLeaf(YType.str, "authentication-key")

                                self.enable = YLeaf(YType.boolean, "enable")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State, ['authentication_key', 'enable'], name, value)


                    class Config(Entity):
                        """
                        Configuration of per\-interface RSVP parameters
                        
                        .. attribute:: interface_name
                        
                        	Name of configured IP interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config, ['interface_name'], name, value)


                    class Hellos(Entity):
                        """
                        Top level container for RSVP hello parameters
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to RSVP hellos
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config>`
                        
                        .. attribute:: state
                        
                        	State information associated with RSVP hellos
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos, self).__init__()

                            self.yang_name = "hellos"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State)}
                            self._child_list_classes = {}

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "hellos"


                        class Config(Entity):
                            """
                            Configuration parameters relating to RSVP
                            hellos
                            
                            .. attribute:: hello_interval
                            
                            	set the interval in ms between RSVP hello messages
                            	**type**\:  int
                            
                            	**range:** 1000..60000
                            
                            	**units**\: milliseconds
                            
                            	**default value**\: 9000
                            
                            .. attribute:: refresh_reduction
                            
                            	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                            	**type**\:  bool
                            
                            	**default value**\: true
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "hellos"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.hello_interval = YLeaf(YType.uint16, "hello-interval")

                                self.refresh_reduction = YLeaf(YType.boolean, "refresh-reduction")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config, ['hello_interval', 'refresh_reduction'], name, value)


                        class State(Entity):
                            """
                            State information associated with RSVP hellos
                            
                            .. attribute:: hello_interval
                            
                            	set the interval in ms between RSVP hello messages
                            	**type**\:  int
                            
                            	**range:** 1000..60000
                            
                            	**units**\: milliseconds
                            
                            	**default value**\: 9000
                            
                            .. attribute:: refresh_reduction
                            
                            	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                            	**type**\:  bool
                            
                            	**default value**\: true
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "hellos"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.hello_interval = YLeaf(YType.uint16, "hello-interval")

                                self.refresh_reduction = YLeaf(YType.boolean, "refresh-reduction")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State, ['hello_interval', 'refresh_reduction'], name, value)


                    class Protection(Entity):
                        """
                        link\-protection (NHOP) related configuration
                        
                        .. attribute:: config
                        
                        	Configuration for link\-protection
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config>`
                        
                        .. attribute:: state
                        
                        	State for link\-protection
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection, self).__init__()

                            self.yang_name = "protection"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State)}
                            self._child_list_classes = {}

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "protection"


                        class Config(Entity):
                            """
                            Configuration for link\-protection
                            
                            .. attribute:: bypass_optimize_interval
                            
                            	interval between periodic optimization of the bypass LSPs
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**units**\: seconds
                            
                            .. attribute:: link_protection_style_requested
                            
                            	Style of mpls frr protection desired\: link, link\-node, or unprotected
                            	**type**\:   :py:class:`ProtectionType <ydk.models.openconfig.openconfig_mpls_types.ProtectionType>`
                            
                            	**default value**\: mplst:link-node-protection-requested
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "protection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bypass_optimize_interval = YLeaf(YType.uint16, "bypass-optimize-interval")

                                self.link_protection_style_requested = YLeaf(YType.identityref, "link-protection-style-requested")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config, ['bypass_optimize_interval', 'link_protection_style_requested'], name, value)


                        class State(Entity):
                            """
                            State for link\-protection
                            
                            .. attribute:: bypass_optimize_interval
                            
                            	interval between periodic optimization of the bypass LSPs
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**units**\: seconds
                            
                            .. attribute:: link_protection_style_requested
                            
                            	Style of mpls frr protection desired\: link, link\-node, or unprotected
                            	**type**\:   :py:class:`ProtectionType <ydk.models.openconfig.openconfig_mpls_types.ProtectionType>`
                            
                            	**default value**\: mplst:link-node-protection-requested
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "protection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.bypass_optimize_interval = YLeaf(YType.uint16, "bypass-optimize-interval")

                                self.link_protection_style_requested = YLeaf(YType.identityref, "link-protection-style-requested")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State, ['bypass_optimize_interval', 'link_protection_style_requested'], name, value)


                    class State(Entity):
                        """
                        Per\-interface RSVP protocol and state information
                        
                        .. attribute:: active_reservation_count
                        
                        	Number of active RSVP reservations
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bandwidth
                        
                        	Available and reserved bandwidth by priority on the interface
                        	**type**\: list of    :py:class:`Bandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth>`
                        
                        .. attribute:: counters
                        
                        	Interface specific RSVP statistics and counters
                        	**type**\:   :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters>`
                        
                        .. attribute:: highwater_mark
                        
                        	Maximum bandwidth ever reserved
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"counters" : ("counters", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters)}
                            self._child_list_classes = {"bandwidth" : ("bandwidth", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth)}

                            self.active_reservation_count = YLeaf(YType.uint64, "active-reservation-count")

                            self.highwater_mark = YLeaf(YType.uint64, "highwater-mark")

                            self.counters = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters()
                            self.counters.parent = self
                            self._children_name_map["counters"] = "counters"
                            self._children_yang_names.add("counters")

                            self.bandwidth = YList(self)
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State, ['active_reservation_count', 'highwater_mark'], name, value)


                        class Bandwidth(Entity):
                            """
                            Available and reserved bandwidth by priority on
                            the interface.
                            
                            .. attribute:: priority  <key>
                            
                            	RSVP priority level for LSPs traversing the interface
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: available_bandwidth
                            
                            	Bandwidth currently available
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: reserved_bandwidth
                            
                            	Bandwidth currently reserved
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth, self).__init__()

                                self.yang_name = "bandwidth"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.priority = YLeaf(YType.uint8, "priority")

                                self.available_bandwidth = YLeaf(YType.uint64, "available-bandwidth")

                                self.reserved_bandwidth = YLeaf(YType.uint64, "reserved-bandwidth")
                                self._segment_path = lambda: "bandwidth" + "[priority='" + self.priority.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth, ['priority', 'available_bandwidth', 'reserved_bandwidth'], name, value)


                        class Counters(Entity):
                            """
                            Interface specific RSVP statistics and counters
                            
                            .. attribute:: in_ack_messages
                            
                            	Number of received RSVP refresh reduction ack messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_hello_messages
                            
                            	Number of received RSVP hello messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_path_error_messages
                            
                            	Number of received RSVP Path Error messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_path_messages
                            
                            	Number of received RSVP Path messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_path_tear_messages
                            
                            	Number of received RSVP Path Tear messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_reservation_error_messages
                            
                            	Number of received RSVP Resv Error messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_reservation_messages
                            
                            	Number of received RSVP Resv messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_reservation_tear_messages
                            
                            	Number of received RSVP Resv Tear messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_srefresh_messages
                            
                            	Number of received RSVP summary refresh messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_ack_messages
                            
                            	Number of sent RSVP refresh reduction ack messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_hello_messages
                            
                            	Number of sent RSVP hello messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path_error_messages
                            
                            	Number of sent RSVP Path Error messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path_messages
                            
                            	Number of sent RSVP PATH messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_path_tear_messages
                            
                            	Number of sent RSVP Path Tear messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_reservation_error_messages
                            
                            	Number of sent RSVP Resv Error messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_reservation_messages
                            
                            	Number of sent RSVP Resv messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_reservation_tear_messages
                            
                            	Number of sent RSVP Resv Tear messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_srefresh_messages
                            
                            	Number of sent RSVP summary refresh messages
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters, self).__init__()

                                self.yang_name = "counters"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.in_ack_messages = YLeaf(YType.uint64, "in-ack-messages")

                                self.in_hello_messages = YLeaf(YType.uint64, "in-hello-messages")

                                self.in_path_error_messages = YLeaf(YType.uint64, "in-path-error-messages")

                                self.in_path_messages = YLeaf(YType.uint64, "in-path-messages")

                                self.in_path_tear_messages = YLeaf(YType.uint64, "in-path-tear-messages")

                                self.in_reservation_error_messages = YLeaf(YType.uint64, "in-reservation-error-messages")

                                self.in_reservation_messages = YLeaf(YType.uint64, "in-reservation-messages")

                                self.in_reservation_tear_messages = YLeaf(YType.uint64, "in-reservation-tear-messages")

                                self.in_srefresh_messages = YLeaf(YType.uint64, "in-srefresh-messages")

                                self.out_ack_messages = YLeaf(YType.uint64, "out-ack-messages")

                                self.out_hello_messages = YLeaf(YType.uint64, "out-hello-messages")

                                self.out_path_error_messages = YLeaf(YType.uint64, "out-path-error-messages")

                                self.out_path_messages = YLeaf(YType.uint64, "out-path-messages")

                                self.out_path_tear_messages = YLeaf(YType.uint64, "out-path-tear-messages")

                                self.out_reservation_error_messages = YLeaf(YType.uint64, "out-reservation-error-messages")

                                self.out_reservation_messages = YLeaf(YType.uint64, "out-reservation-messages")

                                self.out_reservation_tear_messages = YLeaf(YType.uint64, "out-reservation-tear-messages")

                                self.out_srefresh_messages = YLeaf(YType.uint64, "out-srefresh-messages")
                                self._segment_path = lambda: "counters"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters, ['in_ack_messages', 'in_hello_messages', 'in_path_error_messages', 'in_path_messages', 'in_path_tear_messages', 'in_reservation_error_messages', 'in_reservation_messages', 'in_reservation_tear_messages', 'in_srefresh_messages', 'out_ack_messages', 'out_hello_messages', 'out_path_error_messages', 'out_path_messages', 'out_path_tear_messages', 'out_reservation_error_messages', 'out_reservation_messages', 'out_reservation_tear_messages', 'out_srefresh_messages'], name, value)


                    class Subscription(Entity):
                        """
                        Bandwidth percentage reservable by RSVP
                        on an interface
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to RSVP subscription options
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to RSVP subscription options
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription, self).__init__()

                            self.yang_name = "subscription"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State)}
                            self._child_list_classes = {}

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "subscription"


                        class Config(Entity):
                            """
                            Configuration parameters relating to RSVP
                            subscription options
                            
                            .. attribute:: subscription
                            
                            	percentage of the interface bandwidth that RSVP can reserve
                            	**type**\:  int
                            
                            	**range:** 0..100
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "subscription"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.subscription = YLeaf(YType.uint8, "subscription")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config, ['subscription'], name, value)


                        class State(Entity):
                            """
                            State parameters relating to RSVP
                            subscription options
                            
                            .. attribute:: subscription
                            
                            	percentage of the interface bandwidth that RSVP can reserve
                            	**type**\:  int
                            
                            	**range:** 0..100
                            
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "subscription"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.subscription = YLeaf(YType.uint8, "subscription")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State, ['subscription'], name, value)


            class Neighbors(Entity):
                """
                Configuration and state for RSVP neighbors connecting
                to the device
                
                .. attribute:: config
                
                	Configuration of RSVP neighbor information
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.Config>`
                
                .. attribute:: state
                
                	State information relating to RSVP neighbors
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.SignalingProtocols.RsvpTe.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "rsvp-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.Neighbors.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.Neighbors.State)}
                    self._child_list_classes = {}

                    self.config = Mpls.SignalingProtocols.RsvpTe.Neighbors.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.SignalingProtocols.RsvpTe.Neighbors.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "neighbors"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/%s" % self._segment_path()


                class Config(Entity):
                    """
                    Configuration of RSVP neighbor information
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.Neighbors.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self._segment_path = lambda: "config"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/neighbors/%s" % self._segment_path()


                class State(Entity):
                    """
                    State information relating to RSVP neighbors
                    
                    .. attribute:: neighbor
                    
                    	List of RSVP neighbors connecting to the device, keyed by neighbor address
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.Neighbors.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"neighbor" : ("neighbor", Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor)}

                        self.neighbor = YList(self)
                        self._segment_path = lambda: "state"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/neighbors/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Neighbors.State, [], name, value)


                    class Neighbor(Entity):
                        """
                        List of RSVP neighbors connecting to the device,
                        keyed by neighbor address
                        
                        .. attribute:: address  <key>
                        
                        	Address of RSVP neighbor
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: detected_interface
                        
                        	Interface where RSVP neighbor was detected
                        	**type**\:  str
                        
                        .. attribute:: neighbor_status
                        
                        	Enumuration of possible RSVP neighbor states
                        	**type**\:   :py:class:`NeighborStatus <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor.NeighborStatus>`
                        
                        .. attribute:: refresh_reduction
                        
                        	Suppport of neighbor for RSVP refresh reduction
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.detected_interface = YLeaf(YType.str, "detected-interface")

                            self.neighbor_status = YLeaf(YType.enumeration, "neighbor-status")

                            self.refresh_reduction = YLeaf(YType.boolean, "refresh-reduction")
                            self._segment_path = lambda: "neighbor" + "[address='" + self.address.get() + "']"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/neighbors/state/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor, ['address', 'detected_interface', 'neighbor_status', 'refresh_reduction'], name, value)

                        class NeighborStatus(Enum):
                            """
                            NeighborStatus

                            Enumuration of possible RSVP neighbor states

                            .. data:: UP = 0

                            	RSVP hello messages are detected from the neighbor

                            .. data:: DOWN = 1

                            	RSVP neighbor not detected as up, due to a

                            	communication failure or IGP notification

                            	the neighbor is unavailable

                            """

                            UP = Enum.YLeaf(0, "UP")

                            DOWN = Enum.YLeaf(1, "DOWN")



            class Sessions(Entity):
                """
                Configuration and state of RSVP sessions
                
                .. attribute:: config
                
                	Configuration of RSVP sessions on the device
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Config>`
                
                .. attribute:: state
                
                	State information relating to RSVP sessions on the device
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.SignalingProtocols.RsvpTe.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "rsvp-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.RsvpTe.Sessions.Config), "state" : ("state", Mpls.SignalingProtocols.RsvpTe.Sessions.State)}
                    self._child_list_classes = {}

                    self.config = Mpls.SignalingProtocols.RsvpTe.Sessions.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.SignalingProtocols.RsvpTe.Sessions.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/%s" % self._segment_path()


                class Config(Entity):
                    """
                    Configuration of RSVP sessions on the device
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.Sessions.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self._segment_path = lambda: "config"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/sessions/%s" % self._segment_path()


                class State(Entity):
                    """
                    State information relating to RSVP sessions
                    on the device
                    
                    .. attribute:: session
                    
                    	List of RSVP sessions
                    	**type**\: list of    :py:class:`Session <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.RsvpTe.Sessions.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"session" : ("session", Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session)}

                        self.session = YList(self)
                        self._segment_path = lambda: "state"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions.State, [], name, value)


                    class Session(Entity):
                        """
                        List of RSVP sessions
                        
                        .. attribute:: source_port  <key>
                        
                        	RSVP source port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: destination_port  <key>
                        
                        	RSVP source port
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: source_address  <key>
                        
                        	Origin address of RSVP session
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: destination_address  <key>
                        
                        	Destination address of RSVP session
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: associated_lsps
                        
                        	List of label switched paths associated with this RSVP session
                        	**type**\:  list of str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnel.Config>`
                        
                        .. attribute:: label_in
                        
                        	Incoming MPLS label associated with this RSVP session
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        
                        ----
                        	**type**\:   :py:class:`MplsLabel <ydk.models.openconfig.openconfig_mpls_types.MplsLabel>`
                        
                        
                        ----
                        .. attribute:: label_out
                        
                        	Outgoing MPLS label associated with this RSVP session
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        
                        ----
                        	**type**\:   :py:class:`MplsLabel <ydk.models.openconfig.openconfig_mpls_types.MplsLabel>`
                        
                        
                        ----
                        .. attribute:: status
                        
                        	Enumeration of RSVP session states
                        	**type**\:   :py:class:`Status <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.Status>`
                        
                        .. attribute:: tunnel_id
                        
                        	Unique identifier of RSVP session
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: type
                        
                        	Enumeration of possible RSVP session types
                        	**type**\:   :py:class:`Type <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.Type>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session, self).__init__()

                            self.yang_name = "session"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.source_port = YLeaf(YType.uint16, "source-port")

                            self.destination_port = YLeaf(YType.uint16, "destination-port")

                            self.source_address = YLeaf(YType.str, "source-address")

                            self.destination_address = YLeaf(YType.str, "destination-address")

                            self.associated_lsps = YLeafList(YType.str, "associated-lsps")

                            self.label_in = YLeaf(YType.str, "label-in")

                            self.label_out = YLeaf(YType.str, "label-out")

                            self.status = YLeaf(YType.enumeration, "status")

                            self.tunnel_id = YLeaf(YType.uint16, "tunnel-id")

                            self.type = YLeaf(YType.enumeration, "type")
                            self._segment_path = lambda: "session" + "[source-port='" + self.source_port.get() + "']" + "[destination-port='" + self.destination_port.get() + "']" + "[source-address='" + self.source_address.get() + "']" + "[destination-address='" + self.destination_address.get() + "']"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/sessions/state/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session, ['source_port', 'destination_port', 'source_address', 'destination_address', 'associated_lsps', 'label_in', 'label_out', 'status', 'tunnel_id', 'type'], name, value)

                        class Status(Enum):
                            """
                            Status

                            Enumeration of RSVP session states

                            .. data:: UP = 0

                            	RSVP session is up

                            .. data:: DOWN = 1

                            	RSVP session is down

                            """

                            UP = Enum.YLeaf(0, "UP")

                            DOWN = Enum.YLeaf(1, "DOWN")


                        class Type(Enum):
                            """
                            Type

                            Enumeration of possible RSVP session types

                            .. data:: SOURCE = 0

                            	RSVP session originates on this device

                            .. data:: TRANSIT = 1

                            	RSVP session transits this device only

                            .. data:: DESTINATION = 2

                            	RSVP session terminates on this device

                            """

                            SOURCE = Enum.YLeaf(0, "SOURCE")

                            TRANSIT = Enum.YLeaf(1, "TRANSIT")

                            DESTINATION = Enum.YLeaf(2, "DESTINATION")



        class SegmentRouting(Entity):
            """
            SR global signaling config
            
            .. attribute:: interfaces
            
            	List of interfaces with associated segment routing configuration
            	**type**\: list of    :py:class:`Interfaces <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces>`
            
            .. attribute:: srgb
            
            	List of Segment Routing Global Block (SRGB) entries. These label blocks are reserved to be allocated as domain\-wide entries
            	**type**\: list of    :py:class:`Srgb <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Srgb>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.SignalingProtocols.SegmentRouting, self).__init__()

                self.yang_name = "segment-routing"
                self.yang_parent_name = "signaling-protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interfaces" : ("interfaces", Mpls.SignalingProtocols.SegmentRouting.Interfaces), "srgb" : ("srgb", Mpls.SignalingProtocols.SegmentRouting.Srgb)}

                self.interfaces = YList(self)
                self.srgb = YList(self)
                self._segment_path = lambda: "segment-routing"
                self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting, [], name, value)


            class Interfaces(Entity):
                """
                List of interfaces with associated segment routing
                configuration
                
                .. attribute:: interface  <key>
                
                	Reference to the interface for which segment routing configuration is to be applied
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: adjacency_sid
                
                	Configuration for Adjacency SIDs that are related to the specified interface
                	**type**\:   :py:class:`AdjacencySid <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid>`
                
                .. attribute:: config
                
                	Interface configuration parameters for Segment Routing relating to the specified interface
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config>`
                
                .. attribute:: state
                
                	State parameters for Segment Routing features relating to the specified interface
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.SignalingProtocols.SegmentRouting.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "segment-routing"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"adjacency-sid" : ("adjacency_sid", Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid), "config" : ("config", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config), "state" : ("state", Mpls.SignalingProtocols.SegmentRouting.Interfaces.State)}
                    self._child_list_classes = {}

                    self.interface = YLeaf(YType.str, "interface")

                    self.adjacency_sid = Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid()
                    self.adjacency_sid.parent = self
                    self._children_name_map["adjacency_sid"] = "adjacency-sid"
                    self._children_yang_names.add("adjacency-sid")

                    self.config = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.SignalingProtocols.SegmentRouting.Interfaces.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "interfaces" + "[interface='" + self.interface.get() + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/segment-routing/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces, ['interface'], name, value)


                class AdjacencySid(Entity):
                    """
                    Configuration for Adjacency SIDs that are related to
                    the specified interface
                    
                    .. attribute:: config
                    
                    	Configuration parameters for the Adjacency\-SIDs that are related to this interface
                    	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters for the Adjacency\-SIDs that are related to this interface
                    	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config), "state" : ("state", Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State)}
                        self._child_list_classes = {}

                        self.config = Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"
                        self._children_yang_names.add("config")

                        self.state = Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._children_yang_names.add("state")
                        self._segment_path = lambda: "adjacency-sid"


                    class Config(Entity):
                        """
                        Configuration parameters for the Adjacency\-SIDs
                        that are related to this interface
                        
                        .. attribute:: advertise
                        
                        	Specifies the type of adjacency SID which should be advertised for the specified entity
                        	**type**\:  list of   :py:class:`Advertise <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config.Advertise>`
                        
                        .. attribute:: groups
                        
                        	Specifies the groups to which this interface belongs. Setting a value in this list results in an additional AdjSID being advertised, with the S\-bit set to 1. The AdjSID is assumed to be protected
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.advertise = YLeafList(YType.enumeration, "advertise")

                            self.groups = YLeafList(YType.uint32, "groups")
                            self._segment_path = lambda: "config"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config, ['advertise', 'groups'], name, value)

                        class Advertise(Enum):
                            """
                            Advertise

                            Specifies the type of adjacency SID which should be

                            advertised for the specified entity.

                            .. data:: PROTECTED = 0

                            	Advertise an Adjacency-SID for this interface, which is

                            	eligible to be protected using a local protection

                            	mechanism on the local LSR. The local protection

                            	mechanism selected is dependent upon the configuration

                            	of RSVP-TE FRR or LFA elsewhere on the system

                            .. data:: UNPROTECTED = 1

                            	Advertise an Adajcency-SID for this interface, which is

                            	explicitly excluded from being protected by any local

                            	protection mechanism

                            """

                            PROTECTED = Enum.YLeaf(0, "PROTECTED")

                            UNPROTECTED = Enum.YLeaf(1, "UNPROTECTED")



                    class State(Entity):
                        """
                        State parameters for the Adjacency\-SIDs that are
                        related to this interface
                        
                        .. attribute:: advertise
                        
                        	Specifies the type of adjacency SID which should be advertised for the specified entity
                        	**type**\:  list of   :py:class:`Advertise <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State.Advertise>`
                        
                        .. attribute:: groups
                        
                        	Specifies the groups to which this interface belongs. Setting a value in this list results in an additional AdjSID being advertised, with the S\-bit set to 1. The AdjSID is assumed to be protected
                        	**type**\:  list of int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.advertise = YLeafList(YType.enumeration, "advertise")

                            self.groups = YLeafList(YType.uint32, "groups")
                            self._segment_path = lambda: "state"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State, ['advertise', 'groups'], name, value)

                        class Advertise(Enum):
                            """
                            Advertise

                            Specifies the type of adjacency SID which should be

                            advertised for the specified entity.

                            .. data:: PROTECTED = 0

                            	Advertise an Adjacency-SID for this interface, which is

                            	eligible to be protected using a local protection

                            	mechanism on the local LSR. The local protection

                            	mechanism selected is dependent upon the configuration

                            	of RSVP-TE FRR or LFA elsewhere on the system

                            .. data:: UNPROTECTED = 1

                            	Advertise an Adajcency-SID for this interface, which is

                            	explicitly excluded from being protected by any local

                            	protection mechanism

                            """

                            PROTECTED = Enum.YLeaf(0, "PROTECTED")

                            UNPROTECTED = Enum.YLeaf(1, "UNPROTECTED")



                class Config(Entity):
                    """
                    Interface configuration parameters for Segment Routing
                    relating to the specified interface
                    
                    .. attribute:: interface
                    
                    	Reference to the interface for which segment routing configuration is to be applied
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config, ['interface'], name, value)


                class State(Entity):
                    """
                    State parameters for Segment Routing features relating
                    to the specified interface
                    
                    .. attribute:: interface
                    
                    	Reference to the interface for which segment routing configuration is to be applied
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface = YLeaf(YType.str, "interface")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.State, ['interface'], name, value)


            class Srgb(Entity):
                """
                List of Segment Routing Global Block (SRGB) entries. These
                label blocks are reserved to be allocated as domain\-wide
                entries.
                
                .. attribute:: lower_bound  <key>
                
                	Lower value in the block
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: upper_bound  <key>
                
                	Upper value in the block
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: config
                
                	Configuration parameters relating to the Segment Routing Global Block (SRGB)
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Srgb.Config>`
                
                .. attribute:: state
                
                	State parameters relating to the Segment Routing Global Block (SRGB)
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Srgb.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.SignalingProtocols.SegmentRouting.Srgb, self).__init__()

                    self.yang_name = "srgb"
                    self.yang_parent_name = "segment-routing"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"config" : ("config", Mpls.SignalingProtocols.SegmentRouting.Srgb.Config), "state" : ("state", Mpls.SignalingProtocols.SegmentRouting.Srgb.State)}
                    self._child_list_classes = {}

                    self.lower_bound = YLeaf(YType.uint32, "lower-bound")

                    self.upper_bound = YLeaf(YType.uint32, "upper-bound")

                    self.config = Mpls.SignalingProtocols.SegmentRouting.Srgb.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.SignalingProtocols.SegmentRouting.Srgb.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "srgb" + "[lower-bound='" + self.lower_bound.get() + "']" + "[upper-bound='" + self.upper_bound.get() + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/segment-routing/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Srgb, ['lower_bound', 'upper_bound'], name, value)


                class Config(Entity):
                    """
                    Configuration parameters relating to the Segment Routing
                    Global Block (SRGB)
                    
                    .. attribute:: lower_bound
                    
                    	Lower value in the block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: upper_bound
                    
                    	Upper value in the block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.SegmentRouting.Srgb.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "srgb"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.lower_bound = YLeaf(YType.uint32, "lower-bound")

                        self.upper_bound = YLeaf(YType.uint32, "upper-bound")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Srgb.Config, ['lower_bound', 'upper_bound'], name, value)


                class State(Entity):
                    """
                    State parameters relating to the Segment Routing Global
                    Block (SRGB)
                    
                    .. attribute:: free
                    
                    	Number of SRGB indexes that have not yet been allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lower_bound
                    
                    	Lower value in the block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	Number of indexes in the SRGB block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: upper_bound
                    
                    	Upper value in the block
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: used
                    
                    	Number of SRGB indexes that are currently allocated
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.SignalingProtocols.SegmentRouting.Srgb.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "srgb"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.free = YLeaf(YType.uint32, "free")

                        self.lower_bound = YLeaf(YType.uint32, "lower-bound")

                        self.size = YLeaf(YType.uint32, "size")

                        self.upper_bound = YLeaf(YType.uint32, "upper-bound")

                        self.used = YLeaf(YType.uint32, "used")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Srgb.State, ['free', 'lower_bound', 'size', 'upper_bound', 'used'], name, value)


    class TeGlobalAttributes(Entity):
        """
        traffic\-engineering global attributes
        
        .. attribute:: igp_flooding_bandwidth
        
        	Interface bandwidth change percentages that trigger update events into the IGP traffic engineering database (TED)
        	**type**\:   :py:class:`IgpFloodingBandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth>`
        
        .. attribute:: mpls_admin_groups
        
        	Top\-level container for admin\-groups configuration and state
        	**type**\:   :py:class:`MplsAdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups>`
        
        .. attribute:: srlg
        
        	Shared risk link groups attributes
        	**type**\:   :py:class:`Srlg <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg>`
        
        .. attribute:: te_lsp_timers
        
        	Definition for delays associated with setup and cleanup of TE LSPs
        	**type**\:   :py:class:`TeLspTimers <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            super(Mpls.TeGlobalAttributes, self).__init__()

            self.yang_name = "te-global-attributes"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"igp-flooding-bandwidth" : ("igp_flooding_bandwidth", Mpls.TeGlobalAttributes.IgpFloodingBandwidth), "mpls-admin-groups" : ("mpls_admin_groups", Mpls.TeGlobalAttributes.MplsAdminGroups), "srlg" : ("srlg", Mpls.TeGlobalAttributes.Srlg), "te-lsp-timers" : ("te_lsp_timers", Mpls.TeGlobalAttributes.TeLspTimers)}
            self._child_list_classes = {}

            self.igp_flooding_bandwidth = Mpls.TeGlobalAttributes.IgpFloodingBandwidth()
            self.igp_flooding_bandwidth.parent = self
            self._children_name_map["igp_flooding_bandwidth"] = "igp-flooding-bandwidth"
            self._children_yang_names.add("igp-flooding-bandwidth")

            self.mpls_admin_groups = Mpls.TeGlobalAttributes.MplsAdminGroups()
            self.mpls_admin_groups.parent = self
            self._children_name_map["mpls_admin_groups"] = "mpls-admin-groups"
            self._children_yang_names.add("mpls-admin-groups")

            self.srlg = Mpls.TeGlobalAttributes.Srlg()
            self.srlg.parent = self
            self._children_name_map["srlg"] = "srlg"
            self._children_yang_names.add("srlg")

            self.te_lsp_timers = Mpls.TeGlobalAttributes.TeLspTimers()
            self.te_lsp_timers.parent = self
            self._children_name_map["te_lsp_timers"] = "te-lsp-timers"
            self._children_yang_names.add("te-lsp-timers")
            self._segment_path = lambda: "te-global-attributes"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()


        class IgpFloodingBandwidth(Entity):
            """
            Interface bandwidth change percentages
            that trigger update events into the IGP traffic
            engineering database (TED)
            
            .. attribute:: config
            
            	Configuration parameters for TED update threshold 
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config>`
            
            .. attribute:: state
            
            	State parameters for TED update threshold 
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.TeGlobalAttributes.IgpFloodingBandwidth, self).__init__()

                self.yang_name = "igp-flooding-bandwidth"
                self.yang_parent_name = "te-global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"config" : ("config", Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config), "state" : ("state", Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State)}
                self._child_list_classes = {}

                self.config = Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "igp-flooding-bandwidth"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/%s" % self._segment_path()


            class Config(Entity):
                """
                Configuration parameters for TED
                update threshold 
                
                .. attribute:: delta_percentage
                
                	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                	**type**\:  int
                
                	**range:** 0..100
                
                .. attribute:: down_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                	**type**\:  list of int
                
                	**range:** 0..100
                
                .. attribute:: threshold_specification
                
                	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                	**type**\:   :py:class:`ThresholdSpecification <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdSpecification>`
                
                .. attribute:: threshold_type
                
                	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\-CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                	**type**\:   :py:class:`ThresholdType <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdType>`
                
                .. attribute:: up_down_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                	**type**\:  list of int
                
                	**range:** 0..100
                
                .. attribute:: up_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                	**type**\:  list of int
                
                	**range:** 0..100
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "igp-flooding-bandwidth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.delta_percentage = YLeaf(YType.uint8, "delta-percentage")

                    self.down_thresholds = YLeafList(YType.uint8, "down-thresholds")

                    self.threshold_specification = YLeaf(YType.enumeration, "threshold-specification")

                    self.threshold_type = YLeaf(YType.enumeration, "threshold-type")

                    self.up_down_thresholds = YLeafList(YType.uint8, "up-down-thresholds")

                    self.up_thresholds = YLeafList(YType.uint8, "up-thresholds")
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/igp-flooding-bandwidth/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config, ['delta_percentage', 'down_thresholds', 'threshold_specification', 'threshold_type', 'up_down_thresholds', 'up_thresholds'], name, value)

                class ThresholdSpecification(Enum):
                    """
                    ThresholdSpecification

                    This value specifies whether a single set of threshold

                    values should be used for both increasing and decreasing

                    bandwidth when determining whether to trigger updated

                    bandwidth values to be flooded in the IGP TE extensions.

                    MIRRORED\-UP\-DOWN indicates that a single value (or set of

                    values) should be used for both increasing and decreasing

                    values, where SEPARATE\-UP\-DOWN specifies that the increasing

                    and decreasing values will be separately specified

                    .. data:: MIRRORED_UP_DOWN = 0

                    	MIRRORED-UP-DOWN indicates that a single set of

                    	threshold values should be used for both increasing

                    	and decreasing bandwidth when determining whether

                    	to trigger updated bandwidth values to be flooded

                    	in the IGP TE extensions.

                    .. data:: SEPARATE_UP_DOWN = 1

                    	SEPARATE-UP-DOWN indicates that a separate

                    	threshold values should be used for the increasing

                    	and decreasing bandwidth when determining whether

                    	to trigger updated bandwidth values to be flooded

                    	in the IGP TE extensions.

                    """

                    MIRRORED_UP_DOWN = Enum.YLeaf(0, "MIRRORED-UP-DOWN")

                    SEPARATE_UP_DOWN = Enum.YLeaf(1, "SEPARATE-UP-DOWN")


                class ThresholdType(Enum):
                    """
                    ThresholdType

                    The type of threshold that should be used to specify the

                    values at which bandwidth is flooded. DELTA indicates that

                    the local system should flood IGP updates when a change in

                    reserved bandwidth >= the specified delta occurs on the

                    interface. Where THRESHOLD\-CROSSED is specified, the local

                    system should trigger an update (and hence flood) the

                    reserved bandwidth when the reserved bandwidth changes such

                    that it crosses, or becomes equal to one of the threshold

                    values

                    .. data:: DELTA = 0

                    	DELTA indicates that the local

                    	system should flood IGP updates when a

                    	change in reserved bandwidth >= the specified

                    	delta occurs on the interface.

                    .. data:: THRESHOLD_CROSSED = 1

                    	THRESHOLD-CROSSED indicates that

                    	the local system should trigger an update (and

                    	hence flood) the reserved bandwidth when the

                    	reserved bandwidth changes such that it crosses,

                    	or becomes equal to one of the threshold values.

                    """

                    DELTA = Enum.YLeaf(0, "DELTA")

                    THRESHOLD_CROSSED = Enum.YLeaf(1, "THRESHOLD-CROSSED")



            class State(Entity):
                """
                State parameters for TED update threshold 
                
                .. attribute:: delta_percentage
                
                	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                	**type**\:  int
                
                	**range:** 0..100
                
                .. attribute:: down_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                	**type**\:  list of int
                
                	**range:** 0..100
                
                .. attribute:: threshold_specification
                
                	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                	**type**\:   :py:class:`ThresholdSpecification <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdSpecification>`
                
                .. attribute:: threshold_type
                
                	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\-CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                	**type**\:   :py:class:`ThresholdType <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdType>`
                
                .. attribute:: up_down_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                	**type**\:  list of int
                
                	**range:** 0..100
                
                .. attribute:: up_thresholds
                
                	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                	**type**\:  list of int
                
                	**range:** 0..100
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "igp-flooding-bandwidth"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.delta_percentage = YLeaf(YType.uint8, "delta-percentage")

                    self.down_thresholds = YLeafList(YType.uint8, "down-thresholds")

                    self.threshold_specification = YLeaf(YType.enumeration, "threshold-specification")

                    self.threshold_type = YLeaf(YType.enumeration, "threshold-type")

                    self.up_down_thresholds = YLeafList(YType.uint8, "up-down-thresholds")

                    self.up_thresholds = YLeafList(YType.uint8, "up-thresholds")
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/igp-flooding-bandwidth/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State, ['delta_percentage', 'down_thresholds', 'threshold_specification', 'threshold_type', 'up_down_thresholds', 'up_thresholds'], name, value)

                class ThresholdSpecification(Enum):
                    """
                    ThresholdSpecification

                    This value specifies whether a single set of threshold

                    values should be used for both increasing and decreasing

                    bandwidth when determining whether to trigger updated

                    bandwidth values to be flooded in the IGP TE extensions.

                    MIRRORED\-UP\-DOWN indicates that a single value (or set of

                    values) should be used for both increasing and decreasing

                    values, where SEPARATE\-UP\-DOWN specifies that the increasing

                    and decreasing values will be separately specified

                    .. data:: MIRRORED_UP_DOWN = 0

                    	MIRRORED-UP-DOWN indicates that a single set of

                    	threshold values should be used for both increasing

                    	and decreasing bandwidth when determining whether

                    	to trigger updated bandwidth values to be flooded

                    	in the IGP TE extensions.

                    .. data:: SEPARATE_UP_DOWN = 1

                    	SEPARATE-UP-DOWN indicates that a separate

                    	threshold values should be used for the increasing

                    	and decreasing bandwidth when determining whether

                    	to trigger updated bandwidth values to be flooded

                    	in the IGP TE extensions.

                    """

                    MIRRORED_UP_DOWN = Enum.YLeaf(0, "MIRRORED-UP-DOWN")

                    SEPARATE_UP_DOWN = Enum.YLeaf(1, "SEPARATE-UP-DOWN")


                class ThresholdType(Enum):
                    """
                    ThresholdType

                    The type of threshold that should be used to specify the

                    values at which bandwidth is flooded. DELTA indicates that

                    the local system should flood IGP updates when a change in

                    reserved bandwidth >= the specified delta occurs on the

                    interface. Where THRESHOLD\-CROSSED is specified, the local

                    system should trigger an update (and hence flood) the

                    reserved bandwidth when the reserved bandwidth changes such

                    that it crosses, or becomes equal to one of the threshold

                    values

                    .. data:: DELTA = 0

                    	DELTA indicates that the local

                    	system should flood IGP updates when a

                    	change in reserved bandwidth >= the specified

                    	delta occurs on the interface.

                    .. data:: THRESHOLD_CROSSED = 1

                    	THRESHOLD-CROSSED indicates that

                    	the local system should trigger an update (and

                    	hence flood) the reserved bandwidth when the

                    	reserved bandwidth changes such that it crosses,

                    	or becomes equal to one of the threshold values.

                    """

                    DELTA = Enum.YLeaf(0, "DELTA")

                    THRESHOLD_CROSSED = Enum.YLeaf(1, "THRESHOLD-CROSSED")



        class MplsAdminGroups(Entity):
            """
            Top\-level container for admin\-groups configuration
            and state
            
            .. attribute:: admin_group
            
            	configuration of value to name mapping for mpls affinities/admin\-groups
            	**type**\: list of    :py:class:`AdminGroup <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.TeGlobalAttributes.MplsAdminGroups, self).__init__()

                self.yang_name = "mpls-admin-groups"
                self.yang_parent_name = "te-global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"admin-group" : ("admin_group", Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup)}

                self.admin_group = YList(self)
                self._segment_path = lambda: "mpls-admin-groups"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.TeGlobalAttributes.MplsAdminGroups, [], name, value)


            class AdminGroup(Entity):
                """
                configuration of value to name mapping
                for mpls affinities/admin\-groups
                
                .. attribute:: admin_group_name  <key>
                
                	name for mpls admin\-group
                	**type**\:  str
                
                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config>`
                
                .. attribute:: config
                
                	Configurable items for admin\-groups
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config>`
                
                .. attribute:: state
                
                	Operational state for admin\-groups
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup, self).__init__()

                    self.yang_name = "admin-group"
                    self.yang_parent_name = "mpls-admin-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"config" : ("config", Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config), "state" : ("state", Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State)}
                    self._child_list_classes = {}

                    self.admin_group_name = YLeaf(YType.str, "admin-group-name")

                    self.config = Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "admin-group" + "[admin-group-name='" + self.admin_group_name.get() + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/mpls-admin-groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup, ['admin_group_name'], name, value)


                class Config(Entity):
                    """
                    Configurable items for admin\-groups
                    
                    .. attribute:: admin_group_name
                    
                    	name for mpls admin\-group
                    	**type**\:  str
                    
                    .. attribute:: bit_position
                    
                    	bit\-position value for mpls admin\-group. The value for the admin group is an integer that represents one of the bit positions in the admin\-group bitmask. Values between 0 and 31 are interpreted as the original limit of 32 admin groups. Values >=32 are interpreted as extended admin group values as per RFC7308
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "admin-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.admin_group_name = YLeaf(YType.str, "admin-group-name")

                        self.bit_position = YLeaf(YType.uint32, "bit-position")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config, ['admin_group_name', 'bit_position'], name, value)


                class State(Entity):
                    """
                    Operational state for admin\-groups
                    
                    .. attribute:: admin_group_name
                    
                    	name for mpls admin\-group
                    	**type**\:  str
                    
                    .. attribute:: bit_position
                    
                    	bit\-position value for mpls admin\-group. The value for the admin group is an integer that represents one of the bit positions in the admin\-group bitmask. Values between 0 and 31 are interpreted as the original limit of 32 admin groups. Values >=32 are interpreted as extended admin group values as per RFC7308
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "admin-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.admin_group_name = YLeaf(YType.str, "admin-group-name")

                        self.bit_position = YLeaf(YType.uint32, "bit-position")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State, ['admin_group_name', 'bit_position'], name, value)


        class Srlg(Entity):
            """
            Shared risk link groups attributes
            
            .. attribute:: srlg
            
            	List of shared risk link groups
            	**type**\: list of    :py:class:`Srlg <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.TeGlobalAttributes.Srlg, self).__init__()

                self.yang_name = "srlg"
                self.yang_parent_name = "te-global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"srlg" : ("srlg", Mpls.TeGlobalAttributes.Srlg.Srlg)}

                self.srlg = YList(self)
                self._segment_path = lambda: "srlg"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.TeGlobalAttributes.Srlg, [], name, value)


            class Srlg(Entity):
                """
                List of shared risk link groups
                
                .. attribute:: name  <key>
                
                	The SRLG group identifier
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.Config>`
                
                .. attribute:: config
                
                	Configuration parameters related to the SRLG
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.Config>`
                
                .. attribute:: state
                
                	State parameters related to the SRLG
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.State>`
                
                .. attribute:: static_srlg_members
                
                	SRLG members for static (not flooded) SRLGs 
                	**type**\:   :py:class:`StaticSrlgMembers <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeGlobalAttributes.Srlg.Srlg, self).__init__()

                    self.yang_name = "srlg"
                    self.yang_parent_name = "srlg"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"config" : ("config", Mpls.TeGlobalAttributes.Srlg.Srlg.Config), "state" : ("state", Mpls.TeGlobalAttributes.Srlg.Srlg.State), "static-srlg-members" : ("static_srlg_members", Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.config = Mpls.TeGlobalAttributes.Srlg.Srlg.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.TeGlobalAttributes.Srlg.Srlg.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")

                    self.static_srlg_members = Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers()
                    self.static_srlg_members.parent = self
                    self._children_name_map["static_srlg_members"] = "static-srlg-members"
                    self._children_yang_names.add("static-srlg-members")
                    self._segment_path = lambda: "srlg" + "[name='" + self.name.get() + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/srlg/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.Srlg.Srlg, ['name'], name, value)


                class Config(Entity):
                    """
                    Configuration parameters related to the SRLG
                    
                    .. attribute:: cost
                    
                    	The cost of the SRLG to the computation algorithm
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flooding_type
                    
                    	The type of SRLG, either flooded in the IGP or statically configured
                    	**type**\:   :py:class:`MplsSrlgFloodingType <ydk.models.openconfig.openconfig_mpls.MplsSrlgFloodingType>`
                    
                    	**default value**\: FLOODED-SRLG
                    
                    .. attribute:: name
                    
                    	SRLG group identifier
                    	**type**\:  str
                    
                    .. attribute:: value
                    
                    	group ID for the SRLG
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.TeGlobalAttributes.Srlg.Srlg.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "srlg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.cost = YLeaf(YType.uint32, "cost")

                        self.flooding_type = YLeaf(YType.enumeration, "flooding-type")

                        self.name = YLeaf(YType.str, "name")

                        self.value = YLeaf(YType.uint32, "value")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.Srlg.Srlg.Config, ['cost', 'flooding_type', 'name', 'value'], name, value)


                class State(Entity):
                    """
                    State parameters related to the SRLG
                    
                    .. attribute:: cost
                    
                    	The cost of the SRLG to the computation algorithm
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flooding_type
                    
                    	The type of SRLG, either flooded in the IGP or statically configured
                    	**type**\:   :py:class:`MplsSrlgFloodingType <ydk.models.openconfig.openconfig_mpls.MplsSrlgFloodingType>`
                    
                    	**default value**\: FLOODED-SRLG
                    
                    .. attribute:: name
                    
                    	SRLG group identifier
                    	**type**\:  str
                    
                    .. attribute:: value
                    
                    	group ID for the SRLG
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.TeGlobalAttributes.Srlg.Srlg.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "srlg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.cost = YLeaf(YType.uint32, "cost")

                        self.flooding_type = YLeaf(YType.enumeration, "flooding-type")

                        self.name = YLeaf(YType.str, "name")

                        self.value = YLeaf(YType.uint32, "value")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.Srlg.Srlg.State, ['cost', 'flooding_type', 'name', 'value'], name, value)


                class StaticSrlgMembers(Entity):
                    """
                    SRLG members for static (not flooded) SRLGs 
                    
                    .. attribute:: members_list
                    
                    	List of SRLG members, which are expressed as IP address endpoints of links contained in the SRLG
                    	**type**\: list of    :py:class:`MembersList <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList>`
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers, self).__init__()

                        self.yang_name = "static-srlg-members"
                        self.yang_parent_name = "srlg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"members-list" : ("members_list", Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList)}

                        self.members_list = YList(self)
                        self._segment_path = lambda: "static-srlg-members"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers, [], name, value)


                    class MembersList(Entity):
                        """
                        List of SRLG members, which are expressed
                        as IP address endpoints of links contained in the
                        SRLG
                        
                        .. attribute:: from_address  <key>
                        
                        	The from address of the link in the SRLG
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: config
                        
                        	Configuration parameters relating to the SRLG members
                        	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to the SRLG members
                        	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.State>`
                        
                        

                        """

                        _prefix = 'mpls'
                        _revision = '2015-11-05'

                        def __init__(self):
                            super(Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList, self).__init__()

                            self.yang_name = "members-list"
                            self.yang_parent_name = "static-srlg-members"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"config" : ("config", Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.Config), "state" : ("state", Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.State)}
                            self._child_list_classes = {}

                            self.from_address = YLeaf(YType.str, "from-address")

                            self.config = Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.state = Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._children_yang_names.add("state")
                            self._segment_path = lambda: "members-list" + "[from-address='" + self.from_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList, ['from_address'], name, value)


                        class Config(Entity):
                            """
                            Configuration parameters relating to the
                            SRLG members
                            
                            .. attribute:: from_address
                            
                            	IP address of the a\-side of the SRLG link
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: to_address
                            
                            	IP address of the z\-side of the SRLG link
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "members-list"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.from_address = YLeaf(YType.str, "from-address")

                                self.to_address = YLeaf(YType.str, "to-address")
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.Config, ['from_address', 'to_address'], name, value)


                        class State(Entity):
                            """
                            State parameters relating to the SRLG
                            members
                            
                            .. attribute:: from_address
                            
                            	IP address of the a\-side of the SRLG link
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: to_address
                            
                            	IP address of the z\-side of the SRLG link
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            

                            """

                            _prefix = 'mpls'
                            _revision = '2015-11-05'

                            def __init__(self):
                                super(Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "members-list"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.from_address = YLeaf(YType.str, "from-address")

                                self.to_address = YLeaf(YType.str, "to-address")
                                self._segment_path = lambda: "state"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.TeGlobalAttributes.Srlg.Srlg.StaticSrlgMembers.MembersList.State, ['from_address', 'to_address'], name, value)


        class TeLspTimers(Entity):
            """
            Definition for delays associated with setup
            and cleanup of TE LSPs
            
            .. attribute:: config
            
            	Configuration parameters related to timers for TE LSPs
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers.Config>`
            
            .. attribute:: state
            
            	State related to timers for TE LSPs
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers.State>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.TeGlobalAttributes.TeLspTimers, self).__init__()

                self.yang_name = "te-lsp-timers"
                self.yang_parent_name = "te-global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"config" : ("config", Mpls.TeGlobalAttributes.TeLspTimers.Config), "state" : ("state", Mpls.TeGlobalAttributes.TeLspTimers.State)}
                self._child_list_classes = {}

                self.config = Mpls.TeGlobalAttributes.TeLspTimers.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.state = Mpls.TeGlobalAttributes.TeLspTimers.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "te-lsp-timers"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/%s" % self._segment_path()


            class Config(Entity):
                """
                Configuration parameters related
                to timers for TE LSPs
                
                .. attribute:: cleanup_delay
                
                	delay the removal of old te lsp for a specified amount of time
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**units**\: seconds
                
                .. attribute:: install_delay
                
                	delay the use of newly installed te lsp for a specified amount of time
                	**type**\:  int
                
                	**range:** 0..3600
                
                	**units**\: seconds
                
                .. attribute:: reoptimize_timer
                
                	frequency of reoptimization of a traffic engineered LSP
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**units**\: seconds
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeGlobalAttributes.TeLspTimers.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "te-lsp-timers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.cleanup_delay = YLeaf(YType.uint16, "cleanup-delay")

                    self.install_delay = YLeaf(YType.uint16, "install-delay")

                    self.reoptimize_timer = YLeaf(YType.uint16, "reoptimize-timer")
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/te-lsp-timers/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.TeLspTimers.Config, ['cleanup_delay', 'install_delay', 'reoptimize_timer'], name, value)


            class State(Entity):
                """
                State related to timers for TE LSPs
                
                .. attribute:: cleanup_delay
                
                	delay the removal of old te lsp for a specified amount of time
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**units**\: seconds
                
                .. attribute:: install_delay
                
                	delay the use of newly installed te lsp for a specified amount of time
                	**type**\:  int
                
                	**range:** 0..3600
                
                	**units**\: seconds
                
                .. attribute:: reoptimize_timer
                
                	frequency of reoptimization of a traffic engineered LSP
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**units**\: seconds
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeGlobalAttributes.TeLspTimers.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "te-lsp-timers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.cleanup_delay = YLeaf(YType.uint16, "cleanup-delay")

                    self.install_delay = YLeaf(YType.uint16, "install-delay")

                    self.reoptimize_timer = YLeaf(YType.uint16, "reoptimize-timer")
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/te-lsp-timers/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.TeLspTimers.State, ['cleanup_delay', 'install_delay', 'reoptimize_timer'], name, value)


    class TeInterfaceAttributes(Entity):
        """
        traffic engineering attributes specific
        for interfaces
        
        .. attribute:: interface
        
        	List of TE interfaces
        	**type**\: list of    :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface>`
        
        

        """

        _prefix = 'mpls'
        _revision = '2015-11-05'

        def __init__(self):
            super(Mpls.TeInterfaceAttributes, self).__init__()

            self.yang_name = "te-interface-attributes"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", Mpls.TeInterfaceAttributes.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "te-interface-attributes"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mpls.TeInterfaceAttributes, [], name, value)


        class Interface(Entity):
            """
            List of TE interfaces
            
            .. attribute:: name  <key>
            
            	The interface name
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.Config>`
            
            .. attribute:: config
            
            	Configuration parameters related to TE interfaces\:
            	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.Config>`
            
            .. attribute:: igp_flooding_bandwidth
            
            	Interface bandwidth change percentages that trigger update events into the IGP traffic engineering database (TED)
            	**type**\:   :py:class:`IgpFloodingBandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth>`
            
            .. attribute:: state
            
            	State parameters related to TE interfaces
            	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.State>`
            
            

            """

            _prefix = 'mpls'
            _revision = '2015-11-05'

            def __init__(self):
                super(Mpls.TeInterfaceAttributes.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "te-interface-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"config" : ("config", Mpls.TeInterfaceAttributes.Interface.Config), "igp-flooding-bandwidth" : ("igp_flooding_bandwidth", Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth), "state" : ("state", Mpls.TeInterfaceAttributes.Interface.State)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.config = Mpls.TeInterfaceAttributes.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"
                self._children_yang_names.add("config")

                self.igp_flooding_bandwidth = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth()
                self.igp_flooding_bandwidth.parent = self
                self._children_name_map["igp_flooding_bandwidth"] = "igp-flooding-bandwidth"
                self._children_yang_names.add("igp-flooding-bandwidth")

                self.state = Mpls.TeInterfaceAttributes.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._children_yang_names.add("state")
                self._segment_path = lambda: "interface" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-interface-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.TeInterfaceAttributes.Interface, ['name'], name, value)


            class Config(Entity):
                """
                Configuration parameters related to TE interfaces\:
                
                .. attribute:: admin_group
                
                	list of admin groups (by name) on the interface
                	**type**\:  list of str
                
                .. attribute:: name
                
                	reference to interface name
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: srlg_membership
                
                	list of references to named shared risk link groups that the interface belongs to
                	**type**\:  list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg>`
                
                .. attribute:: te_metric
                
                	TE specific metric for the link
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeInterfaceAttributes.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.admin_group = YLeafList(YType.str, "admin-group")

                    self.name = YLeaf(YType.str, "name")

                    self.srlg_membership = YLeafList(YType.str, "srlg-membership")

                    self.te_metric = YLeaf(YType.uint32, "te-metric")
                    self._segment_path = lambda: "config"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.Config, ['admin_group', 'name', 'srlg_membership', 'te_metric'], name, value)


            class IgpFloodingBandwidth(Entity):
                """
                Interface bandwidth change percentages
                that trigger update events into the IGP traffic
                engineering database (TED)
                
                .. attribute:: config
                
                	Configuration parameters for TED update threshold 
                	**type**\:   :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config>`
                
                .. attribute:: state
                
                	State parameters for TED update threshold 
                	**type**\:   :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State>`
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth, self).__init__()

                    self.yang_name = "igp-flooding-bandwidth"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"config" : ("config", Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config), "state" : ("state", Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State)}
                    self._child_list_classes = {}

                    self.config = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"
                    self._children_yang_names.add("config")

                    self.state = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._children_yang_names.add("state")
                    self._segment_path = lambda: "igp-flooding-bandwidth"


                class Config(Entity):
                    """
                    Configuration parameters for TED
                    update threshold 
                    
                    .. attribute:: delta_percentage
                    
                    	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                    	**type**\:  int
                    
                    	**range:** 0..100
                    
                    .. attribute:: down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                    	**type**\:  list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: threshold_specification
                    
                    	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                    	**type**\:   :py:class:`ThresholdSpecification <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdSpecification>`
                    
                    .. attribute:: threshold_type
                    
                    	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\-CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                    	**type**\:   :py:class:`ThresholdType <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdType>`
                    
                    .. attribute:: up_down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                    	**type**\:  list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: up_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                    	**type**\:  list of int
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "igp-flooding-bandwidth"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.delta_percentage = YLeaf(YType.uint8, "delta-percentage")

                        self.down_thresholds = YLeafList(YType.uint8, "down-thresholds")

                        self.threshold_specification = YLeaf(YType.enumeration, "threshold-specification")

                        self.threshold_type = YLeaf(YType.enumeration, "threshold-type")

                        self.up_down_thresholds = YLeafList(YType.uint8, "up-down-thresholds")

                        self.up_thresholds = YLeafList(YType.uint8, "up-thresholds")
                        self._segment_path = lambda: "config"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config, ['delta_percentage', 'down_thresholds', 'threshold_specification', 'threshold_type', 'up_down_thresholds', 'up_thresholds'], name, value)

                    class ThresholdSpecification(Enum):
                        """
                        ThresholdSpecification

                        This value specifies whether a single set of threshold

                        values should be used for both increasing and decreasing

                        bandwidth when determining whether to trigger updated

                        bandwidth values to be flooded in the IGP TE extensions.

                        MIRRORED\-UP\-DOWN indicates that a single value (or set of

                        values) should be used for both increasing and decreasing

                        values, where SEPARATE\-UP\-DOWN specifies that the increasing

                        and decreasing values will be separately specified

                        .. data:: MIRRORED_UP_DOWN = 0

                        	MIRRORED-UP-DOWN indicates that a single set of

                        	threshold values should be used for both increasing

                        	and decreasing bandwidth when determining whether

                        	to trigger updated bandwidth values to be flooded

                        	in the IGP TE extensions.

                        .. data:: SEPARATE_UP_DOWN = 1

                        	SEPARATE-UP-DOWN indicates that a separate

                        	threshold values should be used for the increasing

                        	and decreasing bandwidth when determining whether

                        	to trigger updated bandwidth values to be flooded

                        	in the IGP TE extensions.

                        """

                        MIRRORED_UP_DOWN = Enum.YLeaf(0, "MIRRORED-UP-DOWN")

                        SEPARATE_UP_DOWN = Enum.YLeaf(1, "SEPARATE-UP-DOWN")


                    class ThresholdType(Enum):
                        """
                        ThresholdType

                        The type of threshold that should be used to specify the

                        values at which bandwidth is flooded. DELTA indicates that

                        the local system should flood IGP updates when a change in

                        reserved bandwidth >= the specified delta occurs on the

                        interface. Where THRESHOLD\-CROSSED is specified, the local

                        system should trigger an update (and hence flood) the

                        reserved bandwidth when the reserved bandwidth changes such

                        that it crosses, or becomes equal to one of the threshold

                        values

                        .. data:: DELTA = 0

                        	DELTA indicates that the local

                        	system should flood IGP updates when a

                        	change in reserved bandwidth >= the specified

                        	delta occurs on the interface.

                        .. data:: THRESHOLD_CROSSED = 1

                        	THRESHOLD-CROSSED indicates that

                        	the local system should trigger an update (and

                        	hence flood) the reserved bandwidth when the

                        	reserved bandwidth changes such that it crosses,

                        	or becomes equal to one of the threshold values.

                        """

                        DELTA = Enum.YLeaf(0, "DELTA")

                        THRESHOLD_CROSSED = Enum.YLeaf(1, "THRESHOLD-CROSSED")



                class State(Entity):
                    """
                    State parameters for TED update threshold 
                    
                    .. attribute:: delta_percentage
                    
                    	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                    	**type**\:  int
                    
                    	**range:** 0..100
                    
                    .. attribute:: down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                    	**type**\:  list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: threshold_specification
                    
                    	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                    	**type**\:   :py:class:`ThresholdSpecification <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdSpecification>`
                    
                    .. attribute:: threshold_type
                    
                    	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\-CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                    	**type**\:   :py:class:`ThresholdType <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdType>`
                    
                    .. attribute:: up_down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                    	**type**\:  list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: up_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                    	**type**\:  list of int
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'mpls'
                    _revision = '2015-11-05'

                    def __init__(self):
                        super(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "igp-flooding-bandwidth"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.delta_percentage = YLeaf(YType.uint8, "delta-percentage")

                        self.down_thresholds = YLeafList(YType.uint8, "down-thresholds")

                        self.threshold_specification = YLeaf(YType.enumeration, "threshold-specification")

                        self.threshold_type = YLeaf(YType.enumeration, "threshold-type")

                        self.up_down_thresholds = YLeafList(YType.uint8, "up-down-thresholds")

                        self.up_thresholds = YLeafList(YType.uint8, "up-thresholds")
                        self._segment_path = lambda: "state"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State, ['delta_percentage', 'down_thresholds', 'threshold_specification', 'threshold_type', 'up_down_thresholds', 'up_thresholds'], name, value)

                    class ThresholdSpecification(Enum):
                        """
                        ThresholdSpecification

                        This value specifies whether a single set of threshold

                        values should be used for both increasing and decreasing

                        bandwidth when determining whether to trigger updated

                        bandwidth values to be flooded in the IGP TE extensions.

                        MIRRORED\-UP\-DOWN indicates that a single value (or set of

                        values) should be used for both increasing and decreasing

                        values, where SEPARATE\-UP\-DOWN specifies that the increasing

                        and decreasing values will be separately specified

                        .. data:: MIRRORED_UP_DOWN = 0

                        	MIRRORED-UP-DOWN indicates that a single set of

                        	threshold values should be used for both increasing

                        	and decreasing bandwidth when determining whether

                        	to trigger updated bandwidth values to be flooded

                        	in the IGP TE extensions.

                        .. data:: SEPARATE_UP_DOWN = 1

                        	SEPARATE-UP-DOWN indicates that a separate

                        	threshold values should be used for the increasing

                        	and decreasing bandwidth when determining whether

                        	to trigger updated bandwidth values to be flooded

                        	in the IGP TE extensions.

                        """

                        MIRRORED_UP_DOWN = Enum.YLeaf(0, "MIRRORED-UP-DOWN")

                        SEPARATE_UP_DOWN = Enum.YLeaf(1, "SEPARATE-UP-DOWN")


                    class ThresholdType(Enum):
                        """
                        ThresholdType

                        The type of threshold that should be used to specify the

                        values at which bandwidth is flooded. DELTA indicates that

                        the local system should flood IGP updates when a change in

                        reserved bandwidth >= the specified delta occurs on the

                        interface. Where THRESHOLD\-CROSSED is specified, the local

                        system should trigger an update (and hence flood) the

                        reserved bandwidth when the reserved bandwidth changes such

                        that it crosses, or becomes equal to one of the threshold

                        values

                        .. data:: DELTA = 0

                        	DELTA indicates that the local

                        	system should flood IGP updates when a

                        	change in reserved bandwidth >= the specified

                        	delta occurs on the interface.

                        .. data:: THRESHOLD_CROSSED = 1

                        	THRESHOLD-CROSSED indicates that

                        	the local system should trigger an update (and

                        	hence flood) the reserved bandwidth when the

                        	reserved bandwidth changes such that it crosses,

                        	or becomes equal to one of the threshold values.

                        """

                        DELTA = Enum.YLeaf(0, "DELTA")

                        THRESHOLD_CROSSED = Enum.YLeaf(1, "THRESHOLD-CROSSED")



            class State(Entity):
                """
                State parameters related to TE interfaces
                
                .. attribute:: admin_group
                
                	list of admin groups (by name) on the interface
                	**type**\:  list of str
                
                .. attribute:: name
                
                	reference to interface name
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                
                .. attribute:: srlg_membership
                
                	list of references to named shared risk link groups that the interface belongs to
                	**type**\:  list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlg.Srlg>`
                
                .. attribute:: te_metric
                
                	TE specific metric for the link
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls'
                _revision = '2015-11-05'

                def __init__(self):
                    super(Mpls.TeInterfaceAttributes.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.admin_group = YLeafList(YType.str, "admin-group")

                    self.name = YLeaf(YType.str, "name")

                    self.srlg_membership = YLeafList(YType.str, "srlg-membership")

                    self.te_metric = YLeaf(YType.uint32, "te-metric")
                    self._segment_path = lambda: "state"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.State, ['admin_group', 'name', 'srlg_membership', 'te_metric'], name, value)

    def clone_ptr(self):
        self._top_entity = Mpls()
        return self._top_entity

class PathComputationMethod(Identity):
    """
    base identity for supported path computation
    mechanisms
    
    

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        super(PathComputationMethod, self).__init__("http://openconfig.net/yang/mpls", "openconfig-mpls", "openconfig-mpls:path-computation-method")


class ExplicitlyDefined(Identity):
    """
    constrained\-path LSP in which the path is
    explicitly specified as a collection of strict or/and loose
    hops
    
    

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        super(ExplicitlyDefined, self).__init__("http://openconfig.net/yang/mpls", "openconfig-mpls", "openconfig-mpls:explicitly-defined")


class ExternallyQueried(Identity):
    """
    constrained\-path LSP in which the path is
    obtained by querying an external source, such as a PCE server
    
    

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        super(ExternallyQueried, self).__init__("http://openconfig.net/yang/mpls", "openconfig-mpls", "openconfig-mpls:externally-queried")


class LocallyComputed(Identity):
    """
    indicates a constrained\-path LSP in which the
    path is computed by the local LER
    
    

    """

    _prefix = 'mpls'
    _revision = '2015-11-05'

    def __init__(self):
        super(LocallyComputed, self).__init__("http://openconfig.net/yang/mpls", "openconfig-mpls", "openconfig-mpls:locally-computed")


