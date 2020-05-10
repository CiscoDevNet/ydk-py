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
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CspfTieBreaking(Enum):
    """
    CspfTieBreaking (Enum Class)

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
    MplsHopType (Enum Class)

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
    MplsSrlgFloodingType (Enum Class)

    Enumerated bype for specifying how the SRLG is flooded

    .. data:: FLOODED_SRLG = 0

    	SRLG is flooded in the IGP

    .. data:: STATIC_SRLG = 1

    	SRLG is not flooded, the members are

    	statically configured

    """

    FLOODED_SRLG = Enum.YLeaf(0, "FLOODED_SRLG")

    STATIC_SRLG = Enum.YLeaf(1, "STATIC_SRLG")


class TeBandwidthType(Enum):
    """
    TeBandwidthType (Enum Class)

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
    TeMetricType (Enum Class)

    union type for setting the LSP TE metric to a

    static value, or to track the IGP metric

    .. data:: IGP = 0

    	set the LSP metric to track the underlying

    	IGP metric

    """

    IGP = Enum.YLeaf(0, "IGP")



class Mpls(_Entity_):
    """
    Anchor point for mpls configuration and operational
    data
    
    .. attribute:: global_
    
    	general mpls configuration applicable to any type of LSP and signaling protocol \- label ranges, entropy label supportmay be added here
    	**type**\:  :py:class:`Global <ydk.models.openconfig.openconfig_mpls.Mpls.Global>`
    
    .. attribute:: te_global_attributes
    
    	traffic\-engineering global attributes
    	**type**\:  :py:class:`TeGlobalAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes>`
    
    .. attribute:: te_interface_attributes
    
    	traffic engineering attributes specific for interfaces
    	**type**\:  :py:class:`TeInterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes>`
    
    .. attribute:: signaling_protocols
    
    	top\-level signaling protocol configuration
    	**type**\:  :py:class:`SignalingProtocols <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols>`
    
    .. attribute:: lsps
    
    	LSP definitions and configuration
    	**type**\:  :py:class:`Lsps <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps>`
    
    

    """

    _prefix = 'oc-mpls'
    _revision = '2017-03-22'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Mpls, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls"
        self.yang_parent_name = "openconfig-mpls"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("global", ("global_", Mpls.Global)), ("te-global-attributes", ("te_global_attributes", Mpls.TeGlobalAttributes)), ("te-interface-attributes", ("te_interface_attributes", Mpls.TeInterfaceAttributes)), ("signaling-protocols", ("signaling_protocols", Mpls.SignalingProtocols)), ("lsps", ("lsps", Mpls.Lsps))])
        self._leafs = OrderedDict()

        self.global_ = Mpls.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"

        self.te_global_attributes = Mpls.TeGlobalAttributes()
        self.te_global_attributes.parent = self
        self._children_name_map["te_global_attributes"] = "te-global-attributes"

        self.te_interface_attributes = Mpls.TeInterfaceAttributes()
        self.te_interface_attributes.parent = self
        self._children_name_map["te_interface_attributes"] = "te-interface-attributes"

        self.signaling_protocols = Mpls.SignalingProtocols()
        self.signaling_protocols.parent = self
        self._children_name_map["signaling_protocols"] = "signaling-protocols"

        self.lsps = Mpls.Lsps()
        self.lsps.parent = self
        self._children_name_map["lsps"] = "lsps"
        self._segment_path = lambda: "openconfig-mpls:mpls"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Mpls, [], name, value)


    class Global(_Entity_):
        """
        general mpls configuration applicable to any
        type of LSP and signaling protocol \- label ranges,
        entropy label supportmay be added here
        
        .. attribute:: config
        
        	Top level global MPLS configuration
        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Global.Config>`
        
        .. attribute:: state
        
        	Top level global MPLS state
        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Global.State>`
        
        	**config**\: False
        
        .. attribute:: interface_attributes
        
        	Parameters related to MPLS interfaces
        	**type**\:  :py:class:`InterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.Global.InterfaceAttributes>`
        
        .. attribute:: reserved_label_blocks
        
        	A range of labels starting with the start\-label and up\-to and including the end label that should be allocated as reserved. These labels should not be utilised by any dynamic label allocation on the local system unless the allocating protocol is explicitly configured to specify that allocation of labels should be out of the label block specified
        	**type**\:  :py:class:`ReservedLabelBlocks <ydk.models.openconfig.openconfig_mpls.Mpls.Global.ReservedLabelBlocks>`
        
        

        """

        _prefix = 'oc-mpls'
        _revision = '2017-03-22'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mpls.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("config", ("config", Mpls.Global.Config)), ("state", ("state", Mpls.Global.State)), ("interface-attributes", ("interface_attributes", Mpls.Global.InterfaceAttributes)), ("reserved-label-blocks", ("reserved_label_blocks", Mpls.Global.ReservedLabelBlocks))])
            self._leafs = OrderedDict()

            self.config = Mpls.Global.Config()
            self.config.parent = self
            self._children_name_map["config"] = "config"

            self.state = Mpls.Global.State()
            self.state.parent = self
            self._children_name_map["state"] = "state"

            self.interface_attributes = Mpls.Global.InterfaceAttributes()
            self.interface_attributes.parent = self
            self._children_name_map["interface_attributes"] = "interface-attributes"

            self.reserved_label_blocks = Mpls.Global.ReservedLabelBlocks()
            self.reserved_label_blocks.parent = self
            self._children_name_map["reserved_label_blocks"] = "reserved-label-blocks"
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mpls.Global, [], name, value)


        class Config(_Entity_):
            """
            Top level global MPLS configuration
            
            .. attribute:: null_label
            
            	The null\-label type used, implicit or explicit
            	**type**\:  :py:class:`NULLLABELTYPE <ydk.models.openconfig.openconfig_mpls_types.NULLLABELTYPE>`
            
            	**default value**\: oc-mplst:IMPLICIT
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.Global.Config, self).__init__()

                self.yang_name = "config"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('null_label', (YLeaf(YType.identityref, 'null-label'), [('ydk.models.openconfig.openconfig_mpls_types', 'NULLLABELTYPE')])),
                ])
                self.null_label = None
                self._segment_path = lambda: "config"
                self._absolute_path = lambda: "openconfig-mpls:mpls/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Global.Config, ['null_label'], name, value)



        class State(_Entity_):
            """
            Top level global MPLS state
            
            .. attribute:: null_label
            
            	The null\-label type used, implicit or explicit
            	**type**\:  :py:class:`NULLLABELTYPE <ydk.models.openconfig.openconfig_mpls_types.NULLLABELTYPE>`
            
            	**config**\: False
            
            	**default value**\: oc-mplst:IMPLICIT
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.Global.State, self).__init__()

                self.yang_name = "state"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('null_label', (YLeaf(YType.identityref, 'null-label'), [('ydk.models.openconfig.openconfig_mpls_types', 'NULLLABELTYPE')])),
                ])
                self.null_label = None
                self._segment_path = lambda: "state"
                self._absolute_path = lambda: "openconfig-mpls:mpls/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Global.State, ['null_label'], name, value)



        class InterfaceAttributes(_Entity_):
            """
            Parameters related to MPLS interfaces
            
            .. attribute:: interface
            
            	List of TE interfaces
            	**type**\: list of  		 :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.Global.InterfaceAttributes.Interface>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.Global.InterfaceAttributes, self).__init__()

                self.yang_name = "interface-attributes"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", Mpls.Global.InterfaceAttributes.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interface-attributes"
                self._absolute_path = lambda: "openconfig-mpls:mpls/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Global.InterfaceAttributes, [], name, value)


            class Interface(_Entity_):
                """
                List of TE interfaces
                
                .. attribute:: interface_id  (key)
                
                	Reference to the interface id list key
                	**type**\: str
                
                	**refers to**\:  :py:class:`interface_id <ydk.models.openconfig.openconfig_mpls.Mpls.Global.InterfaceAttributes.Interface.Config>`
                
                .. attribute:: config
                
                	Configuration parameters related to MPLS interfaces\:
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Global.InterfaceAttributes.Interface.Config>`
                
                .. attribute:: state
                
                	State parameters related to TE interfaces
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Global.InterfaceAttributes.Interface.State>`
                
                	**config**\: False
                
                .. attribute:: interface_ref
                
                	Reference to an interface or subinterface
                	**type**\:  :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_mpls.Mpls.Global.InterfaceAttributes.Interface.InterfaceRef>`
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.Global.InterfaceAttributes.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interface-attributes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_id']
                    self._child_classes = OrderedDict([("config", ("config", Mpls.Global.InterfaceAttributes.Interface.Config)), ("state", ("state", Mpls.Global.InterfaceAttributes.Interface.State)), ("interface-ref", ("interface_ref", Mpls.Global.InterfaceAttributes.Interface.InterfaceRef))])
                    self._leafs = OrderedDict([
                        ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                    ])
                    self.interface_id = None

                    self.config = Mpls.Global.InterfaceAttributes.Interface.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Mpls.Global.InterfaceAttributes.Interface.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.interface_ref = Mpls.Global.InterfaceAttributes.Interface.InterfaceRef()
                    self.interface_ref.parent = self
                    self._children_name_map["interface_ref"] = "interface-ref"
                    self._segment_path = lambda: "interface" + "[interface-id='" + str(self.interface_id) + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/global/interface-attributes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Global.InterfaceAttributes.Interface, ['interface_id'], name, value)


                class Config(_Entity_):
                    """
                    Configuration parameters related to MPLS interfaces\:
                    
                    .. attribute:: interface_id
                    
                    	Indentifier for the MPLS interface
                    	**type**\: str
                    
                    .. attribute:: mpls_enabled
                    
                    	Enable MPLS forwarding on this interface
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Global.InterfaceAttributes.Interface.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                            ('mpls_enabled', (YLeaf(YType.boolean, 'mpls-enabled'), ['bool'])),
                        ])
                        self.interface_id = None
                        self.mpls_enabled = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Global.InterfaceAttributes.Interface.Config, ['interface_id', 'mpls_enabled'], name, value)



                class State(_Entity_):
                    """
                    State parameters related to TE interfaces
                    
                    .. attribute:: interface_id
                    
                    	Indentifier for the MPLS interface
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: mpls_enabled
                    
                    	Enable MPLS forwarding on this interface
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    	**default value**\: false
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Global.InterfaceAttributes.Interface.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                            ('mpls_enabled', (YLeaf(YType.boolean, 'mpls-enabled'), ['bool'])),
                        ])
                        self.interface_id = None
                        self.mpls_enabled = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Global.InterfaceAttributes.Interface.State, ['interface_id', 'mpls_enabled'], name, value)



                class InterfaceRef(_Entity_):
                    """
                    Reference to an interface or subinterface
                    
                    .. attribute:: config
                    
                    	Configured reference to interface / subinterface
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state for interface\-ref
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Global.InterfaceAttributes.Interface.InterfaceRef, self).__init__()

                        self.yang_name = "interface-ref"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.Config)), ("state", ("state", Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.State))])
                        self._leafs = OrderedDict()

                        self.config = Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "interface-ref"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Global.InterfaceAttributes.Interface.InterfaceRef, [], name, value)


                    class Config(_Entity_):
                        """
                        Configured reference to interface / subinterface
                        
                        .. attribute:: interface
                        
                        	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: subinterface
                        
                        	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "interface-ref"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                            ])
                            self.interface = None
                            self.subinterface = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.Config, ['interface', 'subinterface'], name, value)



                    class State(_Entity_):
                        """
                        Operational state for interface\-ref
                        
                        .. attribute:: interface
                        
                        	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                        
                        	**config**\: False
                        
                        .. attribute:: subinterface
                        
                        	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "interface-ref"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                            ])
                            self.interface = None
                            self.subinterface = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Global.InterfaceAttributes.Interface.InterfaceRef.State, ['interface', 'subinterface'], name, value)






        class ReservedLabelBlocks(_Entity_):
            """
            A range of labels starting with the start\-label and up\-to and including
            the end label that should be allocated as reserved. These labels should
            not be utilised by any dynamic label allocation on the local system unless
            the allocating protocol is explicitly configured to specify that
            allocation of labels should be out of the label block specified.
            
            .. attribute:: reserved_label_block
            
            	A range of labels starting with the start\-label up to and including the end label that should be allocated for use by a specific protocol
            	**type**\: list of  		 :py:class:`ReservedLabelBlock <ydk.models.openconfig.openconfig_mpls.Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.Global.ReservedLabelBlocks, self).__init__()

                self.yang_name = "reserved-label-blocks"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("reserved-label-block", ("reserved_label_block", Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock))])
                self._leafs = OrderedDict()

                self.reserved_label_block = YList(self)
                self._segment_path = lambda: "reserved-label-blocks"
                self._absolute_path = lambda: "openconfig-mpls:mpls/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Global.ReservedLabelBlocks, [], name, value)


            class ReservedLabelBlock(_Entity_):
                """
                A range of labels starting with the start\-label up to and including
                the end label that should be allocated for use by a specific protocol.
                
                .. attribute:: local_id  (key)
                
                	A reference to a unique local identifier for this label block
                	**type**\: str
                
                	**refers to**\:  :py:class:`local_id <ydk.models.openconfig.openconfig_mpls.Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.Config>`
                
                .. attribute:: config
                
                	Configuration parameters relating to the label block
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.Config>`
                
                .. attribute:: state
                
                	State parameters relating to the label block
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock, self).__init__()

                    self.yang_name = "reserved-label-block"
                    self.yang_parent_name = "reserved-label-blocks"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['local_id']
                    self._child_classes = OrderedDict([("config", ("config", Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.Config)), ("state", ("state", Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.State))])
                    self._leafs = OrderedDict([
                        ('local_id', (YLeaf(YType.str, 'local-id'), ['str'])),
                    ])
                    self.local_id = None

                    self.config = Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "reserved-label-block" + "[local-id='" + str(self.local_id) + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/global/reserved-label-blocks/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock, ['local_id'], name, value)


                class Config(_Entity_):
                    """
                    Configuration parameters relating to the label block.
                    
                    .. attribute:: local_id
                    
                    	A local identifier for the global label block allocation
                    	**type**\: str
                    
                    .. attribute:: lower_bound
                    
                    	Lower bound of the global label block. The block is defined to include this label
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 16..1048575
                    
                    		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                    
                    .. attribute:: upper_bound
                    
                    	Upper bound for the global label block. The block is defined to include this label
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 16..1048575
                    
                    		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "reserved-label-block"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('local_id', (YLeaf(YType.str, 'local-id'), ['str'])),
                            ('lower_bound', (YLeaf(YType.str, 'lower-bound'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ('upper_bound', (YLeaf(YType.str, 'upper-bound'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                        ])
                        self.local_id = None
                        self.lower_bound = None
                        self.upper_bound = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.Config, ['local_id', 'lower_bound', 'upper_bound'], name, value)



                class State(_Entity_):
                    """
                    State parameters relating to the label block.
                    
                    .. attribute:: local_id
                    
                    	A local identifier for the global label block allocation
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: lower_bound
                    
                    	Lower bound of the global label block. The block is defined to include this label
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 16..1048575
                    
                    		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                    
                    	**config**\: False
                    
                    .. attribute:: upper_bound
                    
                    	Upper bound for the global label block. The block is defined to include this label
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 16..1048575
                    
                    		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "reserved-label-block"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('local_id', (YLeaf(YType.str, 'local-id'), ['str'])),
                            ('lower_bound', (YLeaf(YType.str, 'lower-bound'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ('upper_bound', (YLeaf(YType.str, 'upper-bound'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                        ])
                        self.local_id = None
                        self.lower_bound = None
                        self.upper_bound = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Global.ReservedLabelBlocks.ReservedLabelBlock.State, ['local_id', 'lower_bound', 'upper_bound'], name, value)






    class TeGlobalAttributes(_Entity_):
        """
        traffic\-engineering global attributes
        
        .. attribute:: srlgs
        
        	Shared risk link groups attributes
        	**type**\:  :py:class:`Srlgs <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs>`
        
        .. attribute:: mpls_admin_groups
        
        	Top\-level container for admin\-groups configuration and state
        	**type**\:  :py:class:`MplsAdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups>`
        
        .. attribute:: te_lsp_timers
        
        	Definition for delays associated with setup and cleanup of TE LSPs
        	**type**\:  :py:class:`TeLspTimers <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers>`
        
        

        """

        _prefix = 'oc-mpls'
        _revision = '2017-03-22'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mpls.TeGlobalAttributes, self).__init__()

            self.yang_name = "te-global-attributes"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("srlgs", ("srlgs", Mpls.TeGlobalAttributes.Srlgs)), ("mpls-admin-groups", ("mpls_admin_groups", Mpls.TeGlobalAttributes.MplsAdminGroups)), ("te-lsp-timers", ("te_lsp_timers", Mpls.TeGlobalAttributes.TeLspTimers))])
            self._leafs = OrderedDict()

            self.srlgs = Mpls.TeGlobalAttributes.Srlgs()
            self.srlgs.parent = self
            self._children_name_map["srlgs"] = "srlgs"

            self.mpls_admin_groups = Mpls.TeGlobalAttributes.MplsAdminGroups()
            self.mpls_admin_groups.parent = self
            self._children_name_map["mpls_admin_groups"] = "mpls-admin-groups"

            self.te_lsp_timers = Mpls.TeGlobalAttributes.TeLspTimers()
            self.te_lsp_timers.parent = self
            self._children_name_map["te_lsp_timers"] = "te-lsp-timers"
            self._segment_path = lambda: "te-global-attributes"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mpls.TeGlobalAttributes, [], name, value)


        class Srlgs(_Entity_):
            """
            Shared risk link groups attributes
            
            .. attribute:: srlg
            
            	List of shared risk link groups
            	**type**\: list of  		 :py:class:`Srlg <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.TeGlobalAttributes.Srlgs, self).__init__()

                self.yang_name = "srlgs"
                self.yang_parent_name = "te-global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("srlg", ("srlg", Mpls.TeGlobalAttributes.Srlgs.Srlg))])
                self._leafs = OrderedDict()

                self.srlg = YList(self)
                self._segment_path = lambda: "srlgs"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.TeGlobalAttributes.Srlgs, [], name, value)


            class Srlg(_Entity_):
                """
                List of shared risk link groups
                
                .. attribute:: name  (key)
                
                	The SRLG group identifier
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg.Config>`
                
                .. attribute:: config
                
                	Configuration parameters related to the SRLG
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg.Config>`
                
                .. attribute:: state
                
                	State parameters related to the SRLG
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg.State>`
                
                	**config**\: False
                
                .. attribute:: static_srlg_members
                
                	SRLG members for static (not flooded) SRLGs 
                	**type**\:  :py:class:`StaticSrlgMembers <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers>`
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.TeGlobalAttributes.Srlgs.Srlg, self).__init__()

                    self.yang_name = "srlg"
                    self.yang_parent_name = "srlgs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("config", ("config", Mpls.TeGlobalAttributes.Srlgs.Srlg.Config)), ("state", ("state", Mpls.TeGlobalAttributes.Srlgs.Srlg.State)), ("static-srlg-members", ("static_srlg_members", Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.config = Mpls.TeGlobalAttributes.Srlgs.Srlg.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Mpls.TeGlobalAttributes.Srlgs.Srlg.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.static_srlg_members = Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers()
                    self.static_srlg_members.parent = self
                    self._children_name_map["static_srlg_members"] = "static-srlg-members"
                    self._segment_path = lambda: "srlg" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/srlgs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.Srlgs.Srlg, ['name'], name, value)


                class Config(_Entity_):
                    """
                    Configuration parameters related to the SRLG
                    
                    .. attribute:: name
                    
                    	SRLG group identifier
                    	**type**\: str
                    
                    .. attribute:: value
                    
                    	group ID for the SRLG
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cost
                    
                    	The cost of the SRLG to the computation algorithm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flooding_type
                    
                    	The type of SRLG, either flooded in the IGP or statically configured
                    	**type**\:  :py:class:`MplsSrlgFloodingType <ydk.models.openconfig.openconfig_mpls.MplsSrlgFloodingType>`
                    
                    	**default value**\: FLOODED_SRLG
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeGlobalAttributes.Srlgs.Srlg.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "srlg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                            ('cost', (YLeaf(YType.uint32, 'cost'), ['int'])),
                            ('flooding_type', (YLeaf(YType.enumeration, 'flooding-type'), [('ydk.models.openconfig.openconfig_mpls', 'MplsSrlgFloodingType', '')])),
                        ])
                        self.name = None
                        self.value = None
                        self.cost = None
                        self.flooding_type = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.Srlgs.Srlg.Config, ['name', 'value', 'cost', 'flooding_type'], name, value)



                class State(_Entity_):
                    """
                    State parameters related to the SRLG
                    
                    .. attribute:: name
                    
                    	SRLG group identifier
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: value
                    
                    	group ID for the SRLG
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: cost
                    
                    	The cost of the SRLG to the computation algorithm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: flooding_type
                    
                    	The type of SRLG, either flooded in the IGP or statically configured
                    	**type**\:  :py:class:`MplsSrlgFloodingType <ydk.models.openconfig.openconfig_mpls.MplsSrlgFloodingType>`
                    
                    	**config**\: False
                    
                    	**default value**\: FLOODED_SRLG
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeGlobalAttributes.Srlgs.Srlg.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "srlg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                            ('cost', (YLeaf(YType.uint32, 'cost'), ['int'])),
                            ('flooding_type', (YLeaf(YType.enumeration, 'flooding-type'), [('ydk.models.openconfig.openconfig_mpls', 'MplsSrlgFloodingType', '')])),
                        ])
                        self.name = None
                        self.value = None
                        self.cost = None
                        self.flooding_type = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.Srlgs.Srlg.State, ['name', 'value', 'cost', 'flooding_type'], name, value)



                class StaticSrlgMembers(_Entity_):
                    """
                    SRLG members for static (not flooded) SRLGs 
                    
                    .. attribute:: members_list
                    
                    	List of SRLG members, which are expressed as IP address endpoints of links contained in the SRLG
                    	**type**\: list of  		 :py:class:`MembersList <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList>`
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers, self).__init__()

                        self.yang_name = "static-srlg-members"
                        self.yang_parent_name = "srlg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("members-list", ("members_list", Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList))])
                        self._leafs = OrderedDict()

                        self.members_list = YList(self)
                        self._segment_path = lambda: "static-srlg-members"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers, [], name, value)


                    class MembersList(_Entity_):
                        """
                        List of SRLG members, which are expressed
                        as IP address endpoints of links contained in the
                        SRLG
                        
                        .. attribute:: from_address  (key)
                        
                        	The from address of the link in the SRLG
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**refers to**\:  :py:class:`from_address <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.Config>`
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to the SRLG members
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to the SRLG members
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList, self).__init__()

                            self.yang_name = "members-list"
                            self.yang_parent_name = "static-srlg-members"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['from_address']
                            self._child_classes = OrderedDict([("config", ("config", Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.Config)), ("state", ("state", Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.State))])
                            self._leafs = OrderedDict([
                                ('from_address', (YLeaf(YType.str, 'from-address'), ['str'])),
                            ])
                            self.from_address = None

                            self.config = Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "members-list" + "[from-address='" + str(self.from_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList, ['from_address'], name, value)


                        class Config(_Entity_):
                            """
                            Configuration parameters relating to the
                            SRLG members
                            
                            .. attribute:: from_address
                            
                            	IP address of the a\-side of the SRLG link
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                            
                            .. attribute:: to_address
                            
                            	IP address of the z\-side of the SRLG link
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "members-list"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('from_address', (YLeaf(YType.str, 'from-address'), ['str','str'])),
                                    ('to_address', (YLeaf(YType.str, 'to-address'), ['str','str'])),
                                ])
                                self.from_address = None
                                self.to_address = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.Config, ['from_address', 'to_address'], name, value)



                        class State(_Entity_):
                            """
                            State parameters relating to the SRLG
                            members
                            
                            .. attribute:: from_address
                            
                            	IP address of the a\-side of the SRLG link
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                            
                            	**config**\: False
                            
                            .. attribute:: to_address
                            
                            	IP address of the z\-side of the SRLG link
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "members-list"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('from_address', (YLeaf(YType.str, 'from-address'), ['str','str'])),
                                    ('to_address', (YLeaf(YType.str, 'to-address'), ['str','str'])),
                                ])
                                self.from_address = None
                                self.to_address = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.TeGlobalAttributes.Srlgs.Srlg.StaticSrlgMembers.MembersList.State, ['from_address', 'to_address'], name, value)







        class MplsAdminGroups(_Entity_):
            """
            Top\-level container for admin\-groups configuration
            and state
            
            .. attribute:: admin_group
            
            	configuration of value to name mapping for mpls affinities/admin\-groups
            	**type**\: list of  		 :py:class:`AdminGroup <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.TeGlobalAttributes.MplsAdminGroups, self).__init__()

                self.yang_name = "mpls-admin-groups"
                self.yang_parent_name = "te-global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("admin-group", ("admin_group", Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup))])
                self._leafs = OrderedDict()

                self.admin_group = YList(self)
                self._segment_path = lambda: "mpls-admin-groups"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.TeGlobalAttributes.MplsAdminGroups, [], name, value)


            class AdminGroup(_Entity_):
                """
                configuration of value to name mapping
                for mpls affinities/admin\-groups
                
                .. attribute:: admin_group_name  (key)
                
                	name for mpls admin\-group
                	**type**\: str
                
                	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config>`
                
                .. attribute:: config
                
                	Configurable items for admin\-groups
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config>`
                
                .. attribute:: state
                
                	Operational state for admin\-groups
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup, self).__init__()

                    self.yang_name = "admin-group"
                    self.yang_parent_name = "mpls-admin-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['admin_group_name']
                    self._child_classes = OrderedDict([("config", ("config", Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config)), ("state", ("state", Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State))])
                    self._leafs = OrderedDict([
                        ('admin_group_name', (YLeaf(YType.str, 'admin-group-name'), ['str'])),
                    ])
                    self.admin_group_name = None

                    self.config = Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "admin-group" + "[admin-group-name='" + str(self.admin_group_name) + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/mpls-admin-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup, ['admin_group_name'], name, value)


                class Config(_Entity_):
                    """
                    Configurable items for admin\-groups
                    
                    .. attribute:: admin_group_name
                    
                    	name for mpls admin\-group
                    	**type**\: str
                    
                    .. attribute:: bit_position
                    
                    	bit\-position value for mpls admin\-group. The value for the admin group is an integer that represents one of the bit positions in the admin\-group bitmask. Values between 0 and 31 are interpreted as the original limit of 32 admin groups. Values >=32 are interpreted as extended admin group values as per RFC7308
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "admin-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('admin_group_name', (YLeaf(YType.str, 'admin-group-name'), ['str'])),
                            ('bit_position', (YLeaf(YType.uint32, 'bit-position'), ['int'])),
                        ])
                        self.admin_group_name = None
                        self.bit_position = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config, ['admin_group_name', 'bit_position'], name, value)



                class State(_Entity_):
                    """
                    Operational state for admin\-groups
                    
                    .. attribute:: admin_group_name
                    
                    	name for mpls admin\-group
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: bit_position
                    
                    	bit\-position value for mpls admin\-group. The value for the admin group is an integer that represents one of the bit positions in the admin\-group bitmask. Values between 0 and 31 are interpreted as the original limit of 32 admin groups. Values >=32 are interpreted as extended admin group values as per RFC7308
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "admin-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('admin_group_name', (YLeaf(YType.str, 'admin-group-name'), ['str'])),
                            ('bit_position', (YLeaf(YType.uint32, 'bit-position'), ['int'])),
                        ])
                        self.admin_group_name = None
                        self.bit_position = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State, ['admin_group_name', 'bit_position'], name, value)





        class TeLspTimers(_Entity_):
            """
            Definition for delays associated with setup
            and cleanup of TE LSPs
            
            .. attribute:: config
            
            	Configuration parameters related to timers for TE LSPs
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers.Config>`
            
            .. attribute:: state
            
            	State related to timers for TE LSPs
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.TeLspTimers.State>`
            
            	**config**\: False
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.TeGlobalAttributes.TeLspTimers, self).__init__()

                self.yang_name = "te-lsp-timers"
                self.yang_parent_name = "te-global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("config", ("config", Mpls.TeGlobalAttributes.TeLspTimers.Config)), ("state", ("state", Mpls.TeGlobalAttributes.TeLspTimers.State))])
                self._leafs = OrderedDict()

                self.config = Mpls.TeGlobalAttributes.TeLspTimers.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Mpls.TeGlobalAttributes.TeLspTimers.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"
                self._segment_path = lambda: "te-lsp-timers"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.TeGlobalAttributes.TeLspTimers, [], name, value)


            class Config(_Entity_):
                """
                Configuration parameters related
                to timers for TE LSPs
                
                .. attribute:: install_delay
                
                	delay the use of newly installed te lsp for a specified amount of time
                	**type**\: int
                
                	**range:** 0..3600
                
                	**units**\: seconds
                
                .. attribute:: cleanup_delay
                
                	delay the removal of old te lsp for a specified amount of time
                	**type**\: int
                
                	**range:** 0..65535
                
                	**units**\: seconds
                
                .. attribute:: reoptimize_timer
                
                	frequency of reoptimization of a traffic engineered LSP
                	**type**\: int
                
                	**range:** 0..65535
                
                	**units**\: seconds
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.TeGlobalAttributes.TeLspTimers.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "te-lsp-timers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('install_delay', (YLeaf(YType.uint16, 'install-delay'), ['int'])),
                        ('cleanup_delay', (YLeaf(YType.uint16, 'cleanup-delay'), ['int'])),
                        ('reoptimize_timer', (YLeaf(YType.uint16, 'reoptimize-timer'), ['int'])),
                    ])
                    self.install_delay = None
                    self.cleanup_delay = None
                    self.reoptimize_timer = None
                    self._segment_path = lambda: "config"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/te-lsp-timers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.TeLspTimers.Config, ['install_delay', 'cleanup_delay', 'reoptimize_timer'], name, value)



            class State(_Entity_):
                """
                State related to timers for TE LSPs
                
                .. attribute:: install_delay
                
                	delay the use of newly installed te lsp for a specified amount of time
                	**type**\: int
                
                	**range:** 0..3600
                
                	**config**\: False
                
                	**units**\: seconds
                
                .. attribute:: cleanup_delay
                
                	delay the removal of old te lsp for a specified amount of time
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                	**units**\: seconds
                
                .. attribute:: reoptimize_timer
                
                	frequency of reoptimization of a traffic engineered LSP
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                	**units**\: seconds
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.TeGlobalAttributes.TeLspTimers.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "te-lsp-timers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('install_delay', (YLeaf(YType.uint16, 'install-delay'), ['int'])),
                        ('cleanup_delay', (YLeaf(YType.uint16, 'cleanup-delay'), ['int'])),
                        ('reoptimize_timer', (YLeaf(YType.uint16, 'reoptimize-timer'), ['int'])),
                    ])
                    self.install_delay = None
                    self.cleanup_delay = None
                    self.reoptimize_timer = None
                    self._segment_path = lambda: "state"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/te-global-attributes/te-lsp-timers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeGlobalAttributes.TeLspTimers.State, ['install_delay', 'cleanup_delay', 'reoptimize_timer'], name, value)





    class TeInterfaceAttributes(_Entity_):
        """
        traffic engineering attributes specific
        for interfaces
        
        .. attribute:: interface
        
        	List of TE interfaces
        	**type**\: list of  		 :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface>`
        
        

        """

        _prefix = 'oc-mpls'
        _revision = '2017-03-22'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mpls.TeInterfaceAttributes, self).__init__()

            self.yang_name = "te-interface-attributes"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Mpls.TeInterfaceAttributes.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "te-interface-attributes"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mpls.TeInterfaceAttributes, [], name, value)


        class Interface(_Entity_):
            """
            List of TE interfaces
            
            .. attribute:: interface_id  (key)
            
            	Reference to the interface id list key
            	**type**\: str
            
            	**refers to**\:  :py:class:`interface_id <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.Config>`
            
            .. attribute:: config
            
            	Configuration parameters related to TE interfaces\:
            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.Config>`
            
            .. attribute:: state
            
            	State parameters related to TE interfaces
            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.State>`
            
            	**config**\: False
            
            .. attribute:: interface_ref
            
            	Reference to an interface or subinterface
            	**type**\:  :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.InterfaceRef>`
            
            .. attribute:: igp_flooding_bandwidth
            
            	Interface bandwidth change percentages that trigger update events into the IGP traffic engineering database (TED)
            	**type**\:  :py:class:`IgpFloodingBandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.TeInterfaceAttributes.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "te-interface-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_id']
                self._child_classes = OrderedDict([("config", ("config", Mpls.TeInterfaceAttributes.Interface.Config)), ("state", ("state", Mpls.TeInterfaceAttributes.Interface.State)), ("interface-ref", ("interface_ref", Mpls.TeInterfaceAttributes.Interface.InterfaceRef)), ("igp-flooding-bandwidth", ("igp_flooding_bandwidth", Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth))])
                self._leafs = OrderedDict([
                    ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                ])
                self.interface_id = None

                self.config = Mpls.TeInterfaceAttributes.Interface.Config()
                self.config.parent = self
                self._children_name_map["config"] = "config"

                self.state = Mpls.TeInterfaceAttributes.Interface.State()
                self.state.parent = self
                self._children_name_map["state"] = "state"

                self.interface_ref = Mpls.TeInterfaceAttributes.Interface.InterfaceRef()
                self.interface_ref.parent = self
                self._children_name_map["interface_ref"] = "interface-ref"

                self.igp_flooding_bandwidth = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth()
                self.igp_flooding_bandwidth.parent = self
                self._children_name_map["igp_flooding_bandwidth"] = "igp-flooding-bandwidth"
                self._segment_path = lambda: "interface" + "[interface-id='" + str(self.interface_id) + "']"
                self._absolute_path = lambda: "openconfig-mpls:mpls/te-interface-attributes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.TeInterfaceAttributes.Interface, ['interface_id'], name, value)


            class Config(_Entity_):
                """
                Configuration parameters related to TE interfaces\:
                
                .. attribute:: interface_id
                
                	Id of the interface
                	**type**\: str
                
                .. attribute:: te_metric
                
                	TE specific metric for the link
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: srlg_membership
                
                	list of references to named shared risk link groups that the interface belongs to
                	**type**\: list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg>`
                
                .. attribute:: admin_group
                
                	list of admin groups (by name) on the interface
                	**type**\: list of str
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.TeInterfaceAttributes.Interface.Config, self).__init__()

                    self.yang_name = "config"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                        ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                        ('srlg_membership', (YLeafList(YType.str, 'srlg-membership'), ['str'])),
                        ('admin_group', (YLeafList(YType.str, 'admin-group'), ['str'])),
                    ])
                    self.interface_id = None
                    self.te_metric = None
                    self.srlg_membership = []
                    self.admin_group = []
                    self._segment_path = lambda: "config"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.Config, ['interface_id', 'te_metric', 'srlg_membership', 'admin_group'], name, value)



            class State(_Entity_):
                """
                State parameters related to TE interfaces
                
                .. attribute:: interface_id
                
                	Id of the interface
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: te_metric
                
                	TE specific metric for the link
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: srlg_membership
                
                	list of references to named shared risk link groups that the interface belongs to
                	**type**\: list of str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.Srlgs.Srlg>`
                
                	**config**\: False
                
                .. attribute:: admin_group
                
                	list of admin groups (by name) on the interface
                	**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.TeInterfaceAttributes.Interface.State, self).__init__()

                    self.yang_name = "state"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                        ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                        ('srlg_membership', (YLeafList(YType.str, 'srlg-membership'), ['str'])),
                        ('admin_group', (YLeafList(YType.str, 'admin-group'), ['str'])),
                    ])
                    self.interface_id = None
                    self.te_metric = None
                    self.srlg_membership = []
                    self.admin_group = []
                    self._segment_path = lambda: "state"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.State, ['interface_id', 'te_metric', 'srlg_membership', 'admin_group'], name, value)



            class InterfaceRef(_Entity_):
                """
                Reference to an interface or subinterface
                
                .. attribute:: config
                
                	Configured reference to interface / subinterface
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.InterfaceRef.Config>`
                
                .. attribute:: state
                
                	Operational state for interface\-ref
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.InterfaceRef.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.TeInterfaceAttributes.Interface.InterfaceRef, self).__init__()

                    self.yang_name = "interface-ref"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", Mpls.TeInterfaceAttributes.Interface.InterfaceRef.Config)), ("state", ("state", Mpls.TeInterfaceAttributes.Interface.InterfaceRef.State))])
                    self._leafs = OrderedDict()

                    self.config = Mpls.TeInterfaceAttributes.Interface.InterfaceRef.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Mpls.TeInterfaceAttributes.Interface.InterfaceRef.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "interface-ref"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.InterfaceRef, [], name, value)


                class Config(_Entity_):
                    """
                    Configured reference to interface / subinterface
                    
                    .. attribute:: interface
                    
                    	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: subinterface
                    
                    	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeInterfaceAttributes.Interface.InterfaceRef.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "interface-ref"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                        ])
                        self.interface = None
                        self.subinterface = None
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.InterfaceRef.Config, ['interface', 'subinterface'], name, value)



                class State(_Entity_):
                    """
                    Operational state for interface\-ref
                    
                    .. attribute:: interface
                    
                    	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                    
                    	**config**\: False
                    
                    .. attribute:: subinterface
                    
                    	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeInterfaceAttributes.Interface.InterfaceRef.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "interface-ref"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                        ])
                        self.interface = None
                        self.subinterface = None
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.InterfaceRef.State, ['interface', 'subinterface'], name, value)




            class IgpFloodingBandwidth(_Entity_):
                """
                Interface bandwidth change percentages
                that trigger update events into the IGP traffic
                engineering database (TED)
                
                .. attribute:: config
                
                	Configuration parameters for TED update threshold 
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config>`
                
                .. attribute:: state
                
                	State parameters for TED update threshold 
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth, self).__init__()

                    self.yang_name = "igp-flooding-bandwidth"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("config", ("config", Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config)), ("state", ("state", Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State))])
                    self._leafs = OrderedDict()

                    self.config = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "igp-flooding-bandwidth"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth, [], name, value)


                class Config(_Entity_):
                    """
                    Configuration parameters for TED
                    update threshold 
                    
                    .. attribute:: threshold_type
                    
                    	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\_CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                    	**type**\:  :py:class:`ThresholdType <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdType>`
                    
                    .. attribute:: delta_percentage
                    
                    	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    .. attribute:: threshold_specification
                    
                    	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                    	**type**\:  :py:class:`ThresholdSpecification <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdSpecification>`
                    
                    .. attribute:: up_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    .. attribute:: up_down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "igp-flooding-bandwidth"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('threshold_type', (YLeaf(YType.enumeration, 'threshold-type'), [('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdType')])),
                            ('delta_percentage', (YLeaf(YType.uint8, 'delta-percentage'), ['int'])),
                            ('threshold_specification', (YLeaf(YType.enumeration, 'threshold-specification'), [('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdSpecification')])),
                            ('up_thresholds', (YLeafList(YType.uint8, 'up-thresholds'), ['int'])),
                            ('down_thresholds', (YLeafList(YType.uint8, 'down-thresholds'), ['int'])),
                            ('up_down_thresholds', (YLeafList(YType.uint8, 'up-down-thresholds'), ['int'])),
                        ])
                        self.threshold_type = None
                        self.delta_percentage = None
                        self.threshold_specification = None
                        self.up_thresholds = []
                        self.down_thresholds = []
                        self.up_down_thresholds = []
                        self._segment_path = lambda: "config"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config, ['threshold_type', 'delta_percentage', 'threshold_specification', 'up_thresholds', 'down_thresholds', 'up_down_thresholds'], name, value)

                    class ThresholdSpecification(Enum):
                        """
                        ThresholdSpecification (Enum Class)

                        This value specifies whether a single set of threshold

                        values should be used for both increasing and decreasing

                        bandwidth when determining whether to trigger updated

                        bandwidth values to be flooded in the IGP TE extensions.

                        MIRRORED\-UP\-DOWN indicates that a single value (or set of

                        values) should be used for both increasing and decreasing

                        values, where SEPARATE\-UP\-DOWN specifies that the increasing

                        and decreasing values will be separately specified

                        .. data:: MIRRORED_UP_DOWN = 0

                        	MIRRORED_UP_DOWN indicates that a single set of

                        	threshold values should be used for both increasing

                        	and decreasing bandwidth when determining whether

                        	to trigger updated bandwidth values to be flooded

                        	in the IGP TE extensions.

                        .. data:: SEPARATE_UP_DOWN = 1

                        	SEPARATE_UP_DOWN indicates that a separate

                        	threshold values should be used for the increasing

                        	and decreasing bandwidth when determining whether

                        	to trigger updated bandwidth values to be flooded

                        	in the IGP TE extensions.

                        """

                        MIRRORED_UP_DOWN = Enum.YLeaf(0, "MIRRORED_UP_DOWN")

                        SEPARATE_UP_DOWN = Enum.YLeaf(1, "SEPARATE_UP_DOWN")


                    class ThresholdType(Enum):
                        """
                        ThresholdType (Enum Class)

                        The type of threshold that should be used to specify the

                        values at which bandwidth is flooded. DELTA indicates that

                        the local system should flood IGP updates when a change in

                        reserved bandwidth >= the specified delta occurs on the

                        interface. Where THRESHOLD\_CROSSED is specified, the local

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

                        THRESHOLD_CROSSED = Enum.YLeaf(1, "THRESHOLD_CROSSED")




                class State(_Entity_):
                    """
                    State parameters for TED update threshold 
                    
                    .. attribute:: threshold_type
                    
                    	The type of threshold that should be used to specify the values at which bandwidth is flooded. DELTA indicates that the local system should flood IGP updates when a change in reserved bandwidth >= the specified delta occurs on the interface. Where THRESHOLD\_CROSSED is specified, the local system should trigger an update (and hence flood) the reserved bandwidth when the reserved bandwidth changes such that it crosses, or becomes equal to one of the threshold values
                    	**type**\:  :py:class:`ThresholdType <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdType>`
                    
                    	**config**\: False
                    
                    .. attribute:: delta_percentage
                    
                    	The percentage of the maximum\-reservable\-bandwidth considered as the delta that results in an IGP update being flooded
                    	**type**\: int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: threshold_specification
                    
                    	This value specifies whether a single set of threshold values should be used for both increasing and decreasing bandwidth when determining whether to trigger updated bandwidth values to be flooded in the IGP TE extensions. MIRRORED\-UP\-DOWN indicates that a single value (or set of values) should be used for both increasing and decreasing values, where SEPARATE\-UP\-DOWN specifies that the increasing and decreasing values will be separately specified
                    	**type**\:  :py:class:`ThresholdSpecification <ydk.models.openconfig.openconfig_mpls.Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdSpecification>`
                    
                    	**config**\: False
                    
                    .. attribute:: up_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is increasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth) at which bandwidth updates are to be triggered when the bandwidth is decreasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    .. attribute:: up_down_thresholds
                    
                    	The thresholds (expressed as a percentage of the maximum reservable bandwidth of the interface) at which bandwidth updates are flooded \- used both when the bandwidth is increasing and decreasing
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "igp-flooding-bandwidth"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('threshold_type', (YLeaf(YType.enumeration, 'threshold-type'), [('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdType')])),
                            ('delta_percentage', (YLeaf(YType.uint8, 'delta-percentage'), ['int'])),
                            ('threshold_specification', (YLeaf(YType.enumeration, 'threshold-specification'), [('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdSpecification')])),
                            ('up_thresholds', (YLeafList(YType.uint8, 'up-thresholds'), ['int'])),
                            ('down_thresholds', (YLeafList(YType.uint8, 'down-thresholds'), ['int'])),
                            ('up_down_thresholds', (YLeafList(YType.uint8, 'up-down-thresholds'), ['int'])),
                        ])
                        self.threshold_type = None
                        self.delta_percentage = None
                        self.threshold_specification = None
                        self.up_thresholds = []
                        self.down_thresholds = []
                        self.up_down_thresholds = []
                        self._segment_path = lambda: "state"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State, ['threshold_type', 'delta_percentage', 'threshold_specification', 'up_thresholds', 'down_thresholds', 'up_down_thresholds'], name, value)

                    class ThresholdSpecification(Enum):
                        """
                        ThresholdSpecification (Enum Class)

                        This value specifies whether a single set of threshold

                        values should be used for both increasing and decreasing

                        bandwidth when determining whether to trigger updated

                        bandwidth values to be flooded in the IGP TE extensions.

                        MIRRORED\-UP\-DOWN indicates that a single value (or set of

                        values) should be used for both increasing and decreasing

                        values, where SEPARATE\-UP\-DOWN specifies that the increasing

                        and decreasing values will be separately specified

                        .. data:: MIRRORED_UP_DOWN = 0

                        	MIRRORED_UP_DOWN indicates that a single set of

                        	threshold values should be used for both increasing

                        	and decreasing bandwidth when determining whether

                        	to trigger updated bandwidth values to be flooded

                        	in the IGP TE extensions.

                        .. data:: SEPARATE_UP_DOWN = 1

                        	SEPARATE_UP_DOWN indicates that a separate

                        	threshold values should be used for the increasing

                        	and decreasing bandwidth when determining whether

                        	to trigger updated bandwidth values to be flooded

                        	in the IGP TE extensions.

                        """

                        MIRRORED_UP_DOWN = Enum.YLeaf(0, "MIRRORED_UP_DOWN")

                        SEPARATE_UP_DOWN = Enum.YLeaf(1, "SEPARATE_UP_DOWN")


                    class ThresholdType(Enum):
                        """
                        ThresholdType (Enum Class)

                        The type of threshold that should be used to specify the

                        values at which bandwidth is flooded. DELTA indicates that

                        the local system should flood IGP updates when a change in

                        reserved bandwidth >= the specified delta occurs on the

                        interface. Where THRESHOLD\_CROSSED is specified, the local

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

                        THRESHOLD_CROSSED = Enum.YLeaf(1, "THRESHOLD_CROSSED")







    class SignalingProtocols(_Entity_):
        """
        top\-level signaling protocol configuration
        
        .. attribute:: rsvp_te
        
        	RSVP\-TE global signaling protocol configuration
        	**type**\:  :py:class:`RsvpTe <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe>`
        
        .. attribute:: ldp
        
        	LDP global signaling configuration
        	**type**\:  :py:class:`Ldp <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.Ldp>`
        
        .. attribute:: segment_routing
        
        	MPLS\-specific Segment Routing configuration and operational state parameters
        	**type**\:  :py:class:`SegmentRouting <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting>`
        
        

        """

        _prefix = 'oc-mpls'
        _revision = '2017-03-22'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mpls.SignalingProtocols, self).__init__()

            self.yang_name = "signaling-protocols"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsvp-te", ("rsvp_te", Mpls.SignalingProtocols.RsvpTe)), ("ldp", ("ldp", Mpls.SignalingProtocols.Ldp)), ("segment-routing", ("segment_routing", Mpls.SignalingProtocols.SegmentRouting))])
            self._leafs = OrderedDict()

            self.rsvp_te = Mpls.SignalingProtocols.RsvpTe()
            self.rsvp_te.parent = self
            self._children_name_map["rsvp_te"] = "rsvp-te"

            self.ldp = Mpls.SignalingProtocols.Ldp()
            self.ldp.parent = self
            self._children_name_map["ldp"] = "ldp"

            self.segment_routing = Mpls.SignalingProtocols.SegmentRouting()
            self.segment_routing.parent = self
            self._children_name_map["segment_routing"] = "segment-routing"
            self._segment_path = lambda: "signaling-protocols"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mpls.SignalingProtocols, [], name, value)


        class RsvpTe(_Entity_):
            """
            RSVP\-TE global signaling protocol configuration
            
            .. attribute:: sessions
            
            	Enclosing container for sessions
            	**type**\:  :py:class:`Sessions <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions>`
            
            .. attribute:: neighbors
            
            	Configuration and state for RSVP neighbors connecting to the device
            	**type**\:  :py:class:`Neighbors <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors>`
            
            .. attribute:: global_
            
            	Platform wide RSVP configuration and state
            	**type**\:  :py:class:`Global <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global>`
            
            .. attribute:: interface_attributes
            
            	Attributes relating to RSVP\-TE enabled interfaces
            	**type**\:  :py:class:`InterfaceAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.SignalingProtocols.RsvpTe, self).__init__()

                self.yang_name = "rsvp-te"
                self.yang_parent_name = "signaling-protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sessions", ("sessions", Mpls.SignalingProtocols.RsvpTe.Sessions)), ("neighbors", ("neighbors", Mpls.SignalingProtocols.RsvpTe.Neighbors)), ("global", ("global_", Mpls.SignalingProtocols.RsvpTe.Global)), ("interface-attributes", ("interface_attributes", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes))])
                self._leafs = OrderedDict()

                self.sessions = Mpls.SignalingProtocols.RsvpTe.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"

                self.neighbors = Mpls.SignalingProtocols.RsvpTe.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"

                self.global_ = Mpls.SignalingProtocols.RsvpTe.Global()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"

                self.interface_attributes = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes()
                self.interface_attributes.parent = self
                self._children_name_map["interface_attributes"] = "interface-attributes"
                self._segment_path = lambda: "rsvp-te"
                self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe, [], name, value)


            class Sessions(_Entity_):
                """
                Enclosing container for sessions
                
                .. attribute:: session
                
                	List of RSVP sessions
                	**type**\: list of  		 :py:class:`Session <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.SignalingProtocols.RsvpTe.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "rsvp-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", Mpls.SignalingProtocols.RsvpTe.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                    List of RSVP sessions
                    
                    .. attribute:: local_index  (key)
                    
                    	Reference to the local index for the RSVP session
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**refers to**\:  :py:class:`local_index <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: record_route_objects
                    
                    	Enclosing container for MPLS RRO objects associated with the traffic engineered tunnel
                    	**type**\:  :py:class:`RecordRouteObjects <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects>`
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Operational state parameters relating to the RSVP session
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.RsvpTe.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['local_index']
                        self._child_classes = OrderedDict([("record-route-objects", ("record_route_objects", Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State))])
                        self._leafs = OrderedDict([
                            ('local_index', (YLeaf(YType.str, 'local-index'), ['int'])),
                        ])
                        self.local_index = None

                        self.record_route_objects = Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects()
                        self.record_route_objects.parent = self
                        self._children_name_map["record_route_objects"] = "record-route-objects"

                        self.state = Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "session" + "[local-index='" + str(self.local_index) + "']"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions.Session, ['local_index'], name, value)


                    class RecordRouteObjects(_Entity_):
                        """
                        Enclosing container for MPLS RRO objects associated with the
                        traffic engineered tunnel.
                        
                        .. attribute:: record_route_object
                        
                        	Read\-only list of record route objects associated with the traffic engineered tunnel. Each entry in the list may contain a hop IP address, MPLS label allocated at the hop, and the flags associated with the entry
                        	**type**\: list of  		 :py:class:`RecordRouteObject <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects, self).__init__()

                            self.yang_name = "record-route-objects"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("record-route-object", ("record_route_object", Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject))])
                            self._leafs = OrderedDict()

                            self.record_route_object = YList(self)
                            self._segment_path = lambda: "record-route-objects"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects, [], name, value)


                        class RecordRouteObject(_Entity_):
                            """
                            Read\-only list of record route objects associated with the
                            traffic engineered tunnel. Each entry in the list
                            may contain a hop IP address, MPLS label allocated
                            at the hop, and the flags associated with the entry.
                            
                            .. attribute:: index  (key)
                            
                            	Reference to the index of the record route object. The index is used to indicate the ordering of hops in the path
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject.State>`
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	Information related to RRO objects. The hop, label, and optional flags are present for each entry in the list
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject.State>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject, self).__init__()

                                self.yang_name = "record-route-object"
                                self.yang_parent_name = "record-route-objects"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['index']
                                self._child_classes = OrderedDict([("state", ("state", Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject.State))])
                                self._leafs = OrderedDict([
                                    ('index', (YLeaf(YType.str, 'index'), ['int'])),
                                ])
                                self.index = None

                                self.state = Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "record-route-object" + "[index='" + str(self.index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject, ['index'], name, value)


                            class State(_Entity_):
                                """
                                Information related to RRO objects. The hop, label, and
                                optional flags are present for each entry in the list.
                                
                                .. attribute:: index
                                
                                	Index of object in the list. Used for ordering
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: address
                                
                                	IP router hop for RRO entry
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                
                                	**config**\: False
                                
                                .. attribute:: reported_label
                                
                                	Label reported for RRO hop
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 16..1048575
                                
                                		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                                
                                	**config**\: False
                                
                                .. attribute:: reported_flags
                                
                                	Subobject flags for MPLS label
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "record-route-object"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('index', (YLeaf(YType.uint8, 'index'), ['int'])),
                                        ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                        ('reported_label', (YLeaf(YType.str, 'reported-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                        ('reported_flags', (YLeaf(YType.uint8, 'reported-flags'), ['int'])),
                                    ])
                                    self.index = None
                                    self.address = None
                                    self.reported_label = None
                                    self.reported_flags = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.RecordRouteObjects.RecordRouteObject.State, ['index', 'address', 'reported_label', 'reported_flags'], name, value)





                    class State(_Entity_):
                        """
                        Operational state parameters relating to the
                        RSVP session
                        
                        .. attribute:: local_index
                        
                        	The index used to identify the RSVP session on the local network element. This index is generated by the device and is unique only to the local network element
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: source_address
                        
                        	Origin address of RSVP session
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: destination_address
                        
                        	Destination address of RSVP session
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: tunnel_id
                        
                        	The tunnel ID is an identifier used in the RSVP session, which remains constant over the life of the tunnel
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: lsp_id
                        
                        	The LSP ID distinguishes between two LSPs originated from the same headend, and is commonly used to distinguish RSVP sessions during make before break operations
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: session_name
                        
                        	The signaled name of this RSVP session
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: status
                        
                        	Enumeration of RSVP session states
                        	**type**\:  :py:class:`Status <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State.Status>`
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	The type/role of the RSVP session, signifing the session's role on the current device, such as a transit session vs. an ingress session
                        	**type**\:  :py:class:`LSPROLE <ydk.models.openconfig.openconfig_mpls_types.LSPROLE>`
                        
                        	**config**\: False
                        
                        .. attribute:: protection_requested
                        
                        	The type of protection requested for the RSVP session
                        	**type**\:  :py:class:`PROTECTIONTYPE <ydk.models.openconfig.openconfig_mpls_types.PROTECTIONTYPE>`
                        
                        	**config**\: False
                        
                        .. attribute:: label_in
                        
                        	Incoming MPLS label associated with this RSVP session
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        .. attribute:: label_out
                        
                        	Outgoing MPLS label associated with this RSVP session
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        .. attribute:: sender_tspec
                        
                        	Operational state statistics relating to the SENDER\_TSPEC received for the RSVP session
                        	**type**\:  :py:class:`SenderTspec <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State.SenderTspec>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sender-tspec", ("sender_tspec", Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State.SenderTspec))])
                            self._leafs = OrderedDict([
                                ('local_index', (YLeaf(YType.uint64, 'local-index'), ['int'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                                ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str','str'])),
                                ('tunnel_id', (YLeaf(YType.uint16, 'tunnel-id'), ['int'])),
                                ('lsp_id', (YLeaf(YType.uint16, 'lsp-id'), ['int'])),
                                ('session_name', (YLeaf(YType.str, 'session-name'), ['str'])),
                                ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'SignalingProtocols.RsvpTe.Sessions.Session.State.Status')])),
                                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_mpls_types', 'LSPROLE')])),
                                ('protection_requested', (YLeaf(YType.identityref, 'protection-requested'), [('ydk.models.openconfig.openconfig_mpls_types', 'PROTECTIONTYPE')])),
                                ('label_in', (YLeaf(YType.str, 'label-in'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                ('label_out', (YLeaf(YType.str, 'label-out'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ])
                            self.local_index = None
                            self.source_address = None
                            self.destination_address = None
                            self.tunnel_id = None
                            self.lsp_id = None
                            self.session_name = None
                            self.status = None
                            self.type = None
                            self.protection_requested = None
                            self.label_in = None
                            self.label_out = None

                            self.sender_tspec = Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State.SenderTspec()
                            self.sender_tspec.parent = self
                            self._children_name_map["sender_tspec"] = "sender-tspec"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State, ['local_index', 'source_address', 'destination_address', 'tunnel_id', 'lsp_id', 'session_name', 'status', 'type', 'protection_requested', 'label_in', 'label_out'], name, value)

                        class Status(Enum):
                            """
                            Status (Enum Class)

                            Enumeration of RSVP session states

                            .. data:: UP = 0

                            	RSVP session is up

                            .. data:: DOWN = 1

                            	RSVP session is down

                            """

                            UP = Enum.YLeaf(0, "UP")

                            DOWN = Enum.YLeaf(1, "DOWN")



                        class SenderTspec(_Entity_):
                            """
                            Operational state statistics relating to the SENDER\_TSPEC
                            received for the RSVP session
                            
                            .. attribute:: rate
                            
                            	The rate at which the head\-end device generates traffic, expressed in bytes per second
                            	**type**\: str
                            
                            	**length:** 4..4
                            
                            	**config**\: False
                            
                            	**units**\: Bps
                            
                            .. attribute:: size
                            
                            	The size of the token bucket that is used to determine the rate at which the head\-end device generates traffic, expressed in bytes per second
                            	**type**\: str
                            
                            	**length:** 4..4
                            
                            	**config**\: False
                            
                            	**units**\: bytes per second
                            
                            .. attribute:: peak_data_rate
                            
                            	The maximum traffic generation rate that the head\-end device sends traffic at
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**length:** 4..4
                            
                            		**type**\:  :py:class:`PeakDataRate <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State.SenderTspec.PeakDataRate>`
                            
                            	**config**\: False
                            
                            	**units**\: bytes per second
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State.SenderTspec, self).__init__()

                                self.yang_name = "sender-tspec"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rate', (YLeaf(YType.str, 'rate'), ['str'])),
                                    ('size', (YLeaf(YType.str, 'size'), ['str'])),
                                    ('peak_data_rate', (YLeaf(YType.str, 'peak-data-rate'), ['str',('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'SignalingProtocols.RsvpTe.Sessions.Session.State.SenderTspec.PeakDataRate')])),
                                ])
                                self.rate = None
                                self.size = None
                                self.peak_data_rate = None
                                self._segment_path = lambda: "sender-tspec"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Sessions.Session.State.SenderTspec, ['rate', 'size', 'peak_data_rate'], name, value)

                            class PeakDataRate(Enum):
                                """
                                PeakDataRate (Enum Class)

                                The maximum traffic generation rate that the head\-end

                                device sends traffic at.

                                .. data:: INFINITY = 0

                                	The head-end device has no maximum data rate.

                                """

                                INFINITY = Enum.YLeaf(0, "INFINITY")







            class Neighbors(_Entity_):
                """
                Configuration and state for RSVP neighbors connecting
                to the device
                
                .. attribute:: neighbor
                
                	List of RSVP neighbors of the local system
                	**type**\: list of  		 :py:class:`Neighbor <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.SignalingProtocols.RsvpTe.Neighbors, self).__init__()

                    self.yang_name = "neighbors"
                    self.yang_parent_name = "rsvp-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("neighbor", ("neighbor", Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor))])
                    self._leafs = OrderedDict()

                    self.neighbor = YList(self)
                    self._segment_path = lambda: "neighbors"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Neighbors, [], name, value)


                class Neighbor(_Entity_):
                    """
                    List of RSVP neighbors of the local system
                    
                    .. attribute:: address  (key)
                    
                    	Reference to the address of the RSVP neighbor
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                    
                    		**type**\: str
                    
                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                    
                    	**refers to**\:  :py:class:`address <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	Operational state parameters relating to the RSVP neighbor
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor, self).__init__()

                        self.yang_name = "neighbor"
                        self.yang_parent_name = "neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['address']
                        self._child_classes = OrderedDict([("state", ("state", Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor.State))])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ])
                        self.address = None

                        self.state = Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "neighbor" + "[address='" + str(self.address) + "']"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/neighbors/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor, ['address'], name, value)


                    class State(_Entity_):
                        """
                        Operational state parameters relating to the
                        RSVP neighbor
                        
                        .. attribute:: address
                        
                        	Address of RSVP neighbor
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: detected_interface
                        
                        	Interface where RSVP neighbor was detected
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: neighbor_status
                        
                        	Enumuration of possible RSVP neighbor states
                        	**type**\:  :py:class:`NeighborStatus <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor.State.NeighborStatus>`
                        
                        	**config**\: False
                        
                        .. attribute:: refresh_reduction
                        
                        	Suppport of neighbor for RSVP refresh reduction
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('detected_interface', (YLeaf(YType.str, 'detected-interface'), ['str'])),
                                ('neighbor_status', (YLeaf(YType.enumeration, 'neighbor-status'), [('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'SignalingProtocols.RsvpTe.Neighbors.Neighbor.State.NeighborStatus')])),
                                ('refresh_reduction', (YLeaf(YType.boolean, 'refresh-reduction'), ['bool'])),
                            ])
                            self.address = None
                            self.detected_interface = None
                            self.neighbor_status = None
                            self.refresh_reduction = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Neighbors.Neighbor.State, ['address', 'detected_interface', 'neighbor_status', 'refresh_reduction'], name, value)

                        class NeighborStatus(Enum):
                            """
                            NeighborStatus (Enum Class)

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






            class Global(_Entity_):
                """
                Platform wide RSVP configuration and state
                
                .. attribute:: graceful_restart
                
                	Operational state and configuration parameters relating to graceful\-restart for RSVP
                	**type**\:  :py:class:`GracefulRestart <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart>`
                
                .. attribute:: soft_preemption
                
                	Protocol options relating to RSVP soft preemption
                	**type**\:  :py:class:`SoftPreemption <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption>`
                
                .. attribute:: hellos
                
                	Top level container for RSVP hello parameters
                	**type**\:  :py:class:`Hellos <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.Hellos>`
                
                .. attribute:: state
                
                	Platform wide RSVP state, including counters
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.State>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.SignalingProtocols.RsvpTe.Global, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "rsvp-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("graceful-restart", ("graceful_restart", Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart)), ("soft-preemption", ("soft_preemption", Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption)), ("hellos", ("hellos", Mpls.SignalingProtocols.RsvpTe.Global.Hellos)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.Global.State))])
                    self._leafs = OrderedDict()

                    self.graceful_restart = Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart()
                    self.graceful_restart.parent = self
                    self._children_name_map["graceful_restart"] = "graceful-restart"

                    self.soft_preemption = Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption()
                    self.soft_preemption.parent = self
                    self._children_name_map["soft_preemption"] = "soft-preemption"

                    self.hellos = Mpls.SignalingProtocols.RsvpTe.Global.Hellos()
                    self.hellos.parent = self
                    self._children_name_map["hellos"] = "hellos"

                    self.state = Mpls.SignalingProtocols.RsvpTe.Global.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"
                    self._segment_path = lambda: "global"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global, [], name, value)


                class GracefulRestart(_Entity_):
                    """
                    Operational state and configuration parameters relating to
                    graceful\-restart for RSVP
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to graceful\-restart
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with RSVP graceful\-restart
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart, self).__init__()

                        self.yang_name = "graceful-restart"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.State))])
                        self._leafs = OrderedDict()

                        self.config = Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "graceful-restart"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration parameters relating to
                        graceful\-restart
                        
                        .. attribute:: enable
                        
                        	Enables graceful restart on the node
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: restart_time
                        
                        	Graceful restart time (seconds)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: recovery_time
                        
                        	RSVP state recovery time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "graceful-restart"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ('restart_time', (YLeaf(YType.uint32, 'restart-time'), ['int'])),
                                ('recovery_time', (YLeaf(YType.uint32, 'recovery-time'), ['int'])),
                            ])
                            self.enable = None
                            self.restart_time = None
                            self.recovery_time = None
                            self._segment_path = lambda: "config"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/graceful-restart/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.Config, ['enable', 'restart_time', 'recovery_time'], name, value)



                    class State(_Entity_):
                        """
                        State information associated with
                        RSVP graceful\-restart
                        
                        .. attribute:: enable
                        
                        	Enables graceful restart on the node
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: false
                        
                        .. attribute:: restart_time
                        
                        	Graceful restart time (seconds)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: recovery_time
                        
                        	RSVP state recovery time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "graceful-restart"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ('restart_time', (YLeaf(YType.uint32, 'restart-time'), ['int'])),
                                ('recovery_time', (YLeaf(YType.uint32, 'recovery-time'), ['int'])),
                            ])
                            self.enable = None
                            self.restart_time = None
                            self.recovery_time = None
                            self._segment_path = lambda: "state"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/graceful-restart/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.GracefulRestart.State, ['enable', 'restart_time', 'recovery_time'], name, value)




                class SoftPreemption(_Entity_):
                    """
                    Protocol options relating to RSVP
                    soft preemption
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to RSVP soft preemption support
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters relating to RSVP soft preemption support
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption, self).__init__()

                        self.yang_name = "soft-preemption"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.State))])
                        self._leafs = OrderedDict()

                        self.config = Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "soft-preemption"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration parameters relating to RSVP
                        soft preemption support
                        
                        .. attribute:: enable
                        
                        	Enables soft preemption on a node
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: soft_preemption_timeout
                        
                        	Timeout value for soft preemption to revert to hard preemption. The default timeout for soft\-preemption is 30 seconds \- after which the local system reverts to hard pre\-emption
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**default value**\: 30
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "soft-preemption"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ('soft_preemption_timeout', (YLeaf(YType.uint16, 'soft-preemption-timeout'), ['int'])),
                            ])
                            self.enable = None
                            self.soft_preemption_timeout = None
                            self._segment_path = lambda: "config"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/soft-preemption/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.Config, ['enable', 'soft_preemption_timeout'], name, value)



                    class State(_Entity_):
                        """
                        State parameters relating to RSVP
                        soft preemption support
                        
                        .. attribute:: enable
                        
                        	Enables soft preemption on a node
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: false
                        
                        .. attribute:: soft_preemption_timeout
                        
                        	Timeout value for soft preemption to revert to hard preemption. The default timeout for soft\-preemption is 30 seconds \- after which the local system reverts to hard pre\-emption
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**default value**\: 30
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "soft-preemption"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ('soft_preemption_timeout', (YLeaf(YType.uint16, 'soft-preemption-timeout'), ['int'])),
                            ])
                            self.enable = None
                            self.soft_preemption_timeout = None
                            self._segment_path = lambda: "state"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/soft-preemption/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.SoftPreemption.State, ['enable', 'soft_preemption_timeout'], name, value)




                class Hellos(_Entity_):
                    """
                    Top level container for RSVP hello parameters
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to RSVP hellos
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.Hellos.Config>`
                    
                    .. attribute:: state
                    
                    	State information associated with RSVP hellos
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.Hellos.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.RsvpTe.Global.Hellos, self).__init__()

                        self.yang_name = "hellos"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.Global.Hellos.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.Global.Hellos.State))])
                        self._leafs = OrderedDict()

                        self.config = Mpls.SignalingProtocols.RsvpTe.Global.Hellos.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.SignalingProtocols.RsvpTe.Global.Hellos.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "hellos"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.Hellos, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration parameters relating to RSVP
                        hellos
                        
                        .. attribute:: hello_interval
                        
                        	set the interval in ms between RSVP hello messages
                        	**type**\: int
                        
                        	**range:** 1000..60000
                        
                        	**units**\: milliseconds
                        
                        	**default value**\: 9000
                        
                        .. attribute:: refresh_reduction
                        
                        	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Global.Hellos.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "hellos"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                                ('refresh_reduction', (YLeaf(YType.boolean, 'refresh-reduction'), ['bool'])),
                            ])
                            self.hello_interval = None
                            self.refresh_reduction = None
                            self._segment_path = lambda: "config"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/hellos/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.Hellos.Config, ['hello_interval', 'refresh_reduction'], name, value)



                    class State(_Entity_):
                        """
                        State information associated with RSVP hellos
                        
                        .. attribute:: hello_interval
                        
                        	set the interval in ms between RSVP hello messages
                        	**type**\: int
                        
                        	**range:** 1000..60000
                        
                        	**config**\: False
                        
                        	**units**\: milliseconds
                        
                        	**default value**\: 9000
                        
                        .. attribute:: refresh_reduction
                        
                        	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: true
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Global.Hellos.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "hellos"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                                ('refresh_reduction', (YLeaf(YType.boolean, 'refresh-reduction'), ['bool'])),
                            ])
                            self.hello_interval = None
                            self.refresh_reduction = None
                            self._segment_path = lambda: "state"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/hellos/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.Hellos.State, ['hello_interval', 'refresh_reduction'], name, value)




                class State(_Entity_):
                    """
                    Platform wide RSVP state, including counters
                    
                    .. attribute:: counters
                    
                    	Platform wide RSVP statistics and counters
                    	**type**\:  :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Global.State.Counters>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.RsvpTe.Global.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "global"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("counters", ("counters", Mpls.SignalingProtocols.RsvpTe.Global.State.Counters))])
                        self._leafs = OrderedDict()

                        self.counters = Mpls.SignalingProtocols.RsvpTe.Global.State.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._segment_path = lambda: "state"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.State, [], name, value)


                    class Counters(_Entity_):
                        """
                        Platform wide RSVP statistics and counters
                        
                        .. attribute:: path_timeouts
                        
                        	TODO
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: reservation_timeouts
                        
                        	TODO
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: rate_limited_messages
                        
                        	RSVP messages dropped due to rate limiting
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_path_messages
                        
                        	Number of received RSVP Path messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_path_error_messages
                        
                        	Number of received RSVP Path Error messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_path_tear_messages
                        
                        	Number of received RSVP Path Tear messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_reservation_messages
                        
                        	Number of received RSVP Resv messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_reservation_error_messages
                        
                        	Number of received RSVP Resv Error messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_reservation_tear_messages
                        
                        	Number of received RSVP Resv Tear messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_hello_messages
                        
                        	Number of received RSVP hello messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_srefresh_messages
                        
                        	Number of received RSVP summary refresh messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_ack_messages
                        
                        	Number of received RSVP refresh reduction ack messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_path_messages
                        
                        	Number of sent RSVP PATH messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_path_error_messages
                        
                        	Number of sent RSVP Path Error messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_path_tear_messages
                        
                        	Number of sent RSVP Path Tear messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_reservation_messages
                        
                        	Number of sent RSVP Resv messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_reservation_error_messages
                        
                        	Number of sent RSVP Resv Error messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_reservation_tear_messages
                        
                        	Number of sent RSVP Resv Tear messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_hello_messages
                        
                        	Number of sent RSVP hello messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_srefresh_messages
                        
                        	Number of sent RSVP summary refresh messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_ack_messages
                        
                        	Number of sent RSVP refresh reduction ack messages
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.Global.State.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "state"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('path_timeouts', (YLeaf(YType.uint64, 'path-timeouts'), ['int'])),
                                ('reservation_timeouts', (YLeaf(YType.uint64, 'reservation-timeouts'), ['int'])),
                                ('rate_limited_messages', (YLeaf(YType.uint64, 'rate-limited-messages'), ['int'])),
                                ('in_path_messages', (YLeaf(YType.uint64, 'in-path-messages'), ['int'])),
                                ('in_path_error_messages', (YLeaf(YType.uint64, 'in-path-error-messages'), ['int'])),
                                ('in_path_tear_messages', (YLeaf(YType.uint64, 'in-path-tear-messages'), ['int'])),
                                ('in_reservation_messages', (YLeaf(YType.uint64, 'in-reservation-messages'), ['int'])),
                                ('in_reservation_error_messages', (YLeaf(YType.uint64, 'in-reservation-error-messages'), ['int'])),
                                ('in_reservation_tear_messages', (YLeaf(YType.uint64, 'in-reservation-tear-messages'), ['int'])),
                                ('in_hello_messages', (YLeaf(YType.uint64, 'in-hello-messages'), ['int'])),
                                ('in_srefresh_messages', (YLeaf(YType.uint64, 'in-srefresh-messages'), ['int'])),
                                ('in_ack_messages', (YLeaf(YType.uint64, 'in-ack-messages'), ['int'])),
                                ('out_path_messages', (YLeaf(YType.uint64, 'out-path-messages'), ['int'])),
                                ('out_path_error_messages', (YLeaf(YType.uint64, 'out-path-error-messages'), ['int'])),
                                ('out_path_tear_messages', (YLeaf(YType.uint64, 'out-path-tear-messages'), ['int'])),
                                ('out_reservation_messages', (YLeaf(YType.uint64, 'out-reservation-messages'), ['int'])),
                                ('out_reservation_error_messages', (YLeaf(YType.uint64, 'out-reservation-error-messages'), ['int'])),
                                ('out_reservation_tear_messages', (YLeaf(YType.uint64, 'out-reservation-tear-messages'), ['int'])),
                                ('out_hello_messages', (YLeaf(YType.uint64, 'out-hello-messages'), ['int'])),
                                ('out_srefresh_messages', (YLeaf(YType.uint64, 'out-srefresh-messages'), ['int'])),
                                ('out_ack_messages', (YLeaf(YType.uint64, 'out-ack-messages'), ['int'])),
                            ])
                            self.path_timeouts = None
                            self.reservation_timeouts = None
                            self.rate_limited_messages = None
                            self.in_path_messages = None
                            self.in_path_error_messages = None
                            self.in_path_tear_messages = None
                            self.in_reservation_messages = None
                            self.in_reservation_error_messages = None
                            self.in_reservation_tear_messages = None
                            self.in_hello_messages = None
                            self.in_srefresh_messages = None
                            self.in_ack_messages = None
                            self.out_path_messages = None
                            self.out_path_error_messages = None
                            self.out_path_tear_messages = None
                            self.out_reservation_messages = None
                            self.out_reservation_error_messages = None
                            self.out_reservation_tear_messages = None
                            self.out_hello_messages = None
                            self.out_srefresh_messages = None
                            self.out_ack_messages = None
                            self._segment_path = lambda: "counters"
                            self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/global/state/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.Global.State.Counters, ['path_timeouts', 'reservation_timeouts', 'rate_limited_messages', 'in_path_messages', 'in_path_error_messages', 'in_path_tear_messages', 'in_reservation_messages', 'in_reservation_error_messages', 'in_reservation_tear_messages', 'in_hello_messages', 'in_srefresh_messages', 'in_ack_messages', 'out_path_messages', 'out_path_error_messages', 'out_path_tear_messages', 'out_reservation_messages', 'out_reservation_error_messages', 'out_reservation_tear_messages', 'out_hello_messages', 'out_srefresh_messages', 'out_ack_messages'], name, value)





            class InterfaceAttributes(_Entity_):
                """
                Attributes relating to RSVP\-TE enabled interfaces
                
                .. attribute:: interface
                
                	list of per\-interface RSVP configurations
                	**type**\: list of  		 :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface>`
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes, self).__init__()

                    self.yang_name = "interface-attributes"
                    self.yang_parent_name = "rsvp-te"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interface-attributes"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes, [], name, value)


                class Interface(_Entity_):
                    """
                    list of per\-interface RSVP configurations
                    
                    .. attribute:: interface_id  (key)
                    
                    	reference to the interface\-id data
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`interface_id <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration of per\-interface RSVP parameters
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config>`
                    
                    .. attribute:: state
                    
                    	Per\-interface RSVP protocol and state information
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: interface_ref
                    
                    	Reference to an interface or subinterface
                    	**type**\:  :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef>`
                    
                    .. attribute:: bandwidth_reservations
                    
                    	Enclosing container for bandwidth reservation
                    	**type**\:  :py:class:`BandwidthReservations <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations>`
                    
                    .. attribute:: hellos
                    
                    	Top level container for RSVP hello parameters
                    	**type**\:  :py:class:`Hellos <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos>`
                    
                    .. attribute:: authentication
                    
                    	Configuration and state parameters relating to RSVP authentication as per RFC2747
                    	**type**\:  :py:class:`Authentication <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication>`
                    
                    .. attribute:: subscription
                    
                    	Bandwidth percentage reservable by RSVP on an interface
                    	**type**\:  :py:class:`Subscription <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription>`
                    
                    .. attribute:: protection
                    
                    	link\-protection (NHOP) related configuration
                    	**type**\:  :py:class:`Protection <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection>`
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interface-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_id']
                        self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State)), ("interface-ref", ("interface_ref", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef)), ("bandwidth-reservations", ("bandwidth_reservations", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations)), ("hellos", ("hellos", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos)), ("authentication", ("authentication", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication)), ("subscription", ("subscription", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription)), ("protection", ("protection", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection))])
                        self._leafs = OrderedDict([
                            ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                        ])
                        self.interface_id = None

                        self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"

                        self.interface_ref = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef()
                        self.interface_ref.parent = self
                        self._children_name_map["interface_ref"] = "interface-ref"

                        self.bandwidth_reservations = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations()
                        self.bandwidth_reservations.parent = self
                        self._children_name_map["bandwidth_reservations"] = "bandwidth-reservations"

                        self.hellos = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos()
                        self.hellos.parent = self
                        self._children_name_map["hellos"] = "hellos"

                        self.authentication = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"

                        self.subscription = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription()
                        self.subscription.parent = self
                        self._children_name_map["subscription"] = "subscription"

                        self.protection = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection()
                        self.protection.parent = self
                        self._children_name_map["protection"] = "protection"
                        self._segment_path = lambda: "interface" + "[interface-id='" + str(self.interface_id) + "']"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/rsvp-te/interface-attributes/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface, ['interface_id'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration of per\-interface RSVP parameters
                        
                        .. attribute:: interface_id
                        
                        	Identifier for the interface
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                            ])
                            self.interface_id = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config, ['interface_id'], name, value)



                    class State(_Entity_):
                        """
                        Per\-interface RSVP protocol and state information
                        
                        .. attribute:: interface_id
                        
                        	Identifier for the interface
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: counters
                        
                        	Interface specific RSVP statistics and counters
                        	**type**\:  :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("counters", ("counters", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters))])
                            self._leafs = OrderedDict([
                                ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                            ])
                            self.interface_id = None

                            self.counters = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters()
                            self.counters.parent = self
                            self._children_name_map["counters"] = "counters"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State, ['interface_id'], name, value)


                        class Counters(_Entity_):
                            """
                            Interface specific RSVP statistics and counters
                            
                            .. attribute:: in_path_messages
                            
                            	Number of received RSVP Path messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_path_error_messages
                            
                            	Number of received RSVP Path Error messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_path_tear_messages
                            
                            	Number of received RSVP Path Tear messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_reservation_messages
                            
                            	Number of received RSVP Resv messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_reservation_error_messages
                            
                            	Number of received RSVP Resv Error messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_reservation_tear_messages
                            
                            	Number of received RSVP Resv Tear messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_hello_messages
                            
                            	Number of received RSVP hello messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_srefresh_messages
                            
                            	Number of received RSVP summary refresh messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: in_ack_messages
                            
                            	Number of received RSVP refresh reduction ack messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_path_messages
                            
                            	Number of sent RSVP PATH messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_path_error_messages
                            
                            	Number of sent RSVP Path Error messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_path_tear_messages
                            
                            	Number of sent RSVP Path Tear messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_reservation_messages
                            
                            	Number of sent RSVP Resv messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_reservation_error_messages
                            
                            	Number of sent RSVP Resv Error messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_reservation_tear_messages
                            
                            	Number of sent RSVP Resv Tear messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_hello_messages
                            
                            	Number of sent RSVP hello messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_srefresh_messages
                            
                            	Number of sent RSVP summary refresh messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: out_ack_messages
                            
                            	Number of sent RSVP refresh reduction ack messages
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters, self).__init__()

                                self.yang_name = "counters"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_path_messages', (YLeaf(YType.uint64, 'in-path-messages'), ['int'])),
                                    ('in_path_error_messages', (YLeaf(YType.uint64, 'in-path-error-messages'), ['int'])),
                                    ('in_path_tear_messages', (YLeaf(YType.uint64, 'in-path-tear-messages'), ['int'])),
                                    ('in_reservation_messages', (YLeaf(YType.uint64, 'in-reservation-messages'), ['int'])),
                                    ('in_reservation_error_messages', (YLeaf(YType.uint64, 'in-reservation-error-messages'), ['int'])),
                                    ('in_reservation_tear_messages', (YLeaf(YType.uint64, 'in-reservation-tear-messages'), ['int'])),
                                    ('in_hello_messages', (YLeaf(YType.uint64, 'in-hello-messages'), ['int'])),
                                    ('in_srefresh_messages', (YLeaf(YType.uint64, 'in-srefresh-messages'), ['int'])),
                                    ('in_ack_messages', (YLeaf(YType.uint64, 'in-ack-messages'), ['int'])),
                                    ('out_path_messages', (YLeaf(YType.uint64, 'out-path-messages'), ['int'])),
                                    ('out_path_error_messages', (YLeaf(YType.uint64, 'out-path-error-messages'), ['int'])),
                                    ('out_path_tear_messages', (YLeaf(YType.uint64, 'out-path-tear-messages'), ['int'])),
                                    ('out_reservation_messages', (YLeaf(YType.uint64, 'out-reservation-messages'), ['int'])),
                                    ('out_reservation_error_messages', (YLeaf(YType.uint64, 'out-reservation-error-messages'), ['int'])),
                                    ('out_reservation_tear_messages', (YLeaf(YType.uint64, 'out-reservation-tear-messages'), ['int'])),
                                    ('out_hello_messages', (YLeaf(YType.uint64, 'out-hello-messages'), ['int'])),
                                    ('out_srefresh_messages', (YLeaf(YType.uint64, 'out-srefresh-messages'), ['int'])),
                                    ('out_ack_messages', (YLeaf(YType.uint64, 'out-ack-messages'), ['int'])),
                                ])
                                self.in_path_messages = None
                                self.in_path_error_messages = None
                                self.in_path_tear_messages = None
                                self.in_reservation_messages = None
                                self.in_reservation_error_messages = None
                                self.in_reservation_tear_messages = None
                                self.in_hello_messages = None
                                self.in_srefresh_messages = None
                                self.in_ack_messages = None
                                self.out_path_messages = None
                                self.out_path_error_messages = None
                                self.out_path_tear_messages = None
                                self.out_reservation_messages = None
                                self.out_reservation_error_messages = None
                                self.out_reservation_tear_messages = None
                                self.out_hello_messages = None
                                self.out_srefresh_messages = None
                                self.out_ack_messages = None
                                self._segment_path = lambda: "counters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters, ['in_path_messages', 'in_path_error_messages', 'in_path_tear_messages', 'in_reservation_messages', 'in_reservation_error_messages', 'in_reservation_tear_messages', 'in_hello_messages', 'in_srefresh_messages', 'in_ack_messages', 'out_path_messages', 'out_path_error_messages', 'out_path_tear_messages', 'out_reservation_messages', 'out_reservation_error_messages', 'out_reservation_tear_messages', 'out_hello_messages', 'out_srefresh_messages', 'out_ack_messages'], name, value)




                    class InterfaceRef(_Entity_):
                        """
                        Reference to an interface or subinterface
                        
                        .. attribute:: config
                        
                        	Configured reference to interface / subinterface
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for interface\-ref
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef, self).__init__()

                            self.yang_name = "interface-ref"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.State))])
                            self._leafs = OrderedDict()

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "interface-ref"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef, [], name, value)


                        class Config(_Entity_):
                            """
                            Configured reference to interface / subinterface
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                                ])
                                self.interface = None
                                self.subinterface = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.Config, ['interface', 'subinterface'], name, value)



                        class State(_Entity_):
                            """
                            Operational state for interface\-ref
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            	**config**\: False
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                                ])
                                self.interface = None
                                self.subinterface = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.InterfaceRef.State, ['interface', 'subinterface'], name, value)




                    class BandwidthReservations(_Entity_):
                        """
                        Enclosing container for bandwidth reservation
                        
                        .. attribute:: bandwidth_reservation
                        
                        	Available and reserved bandwidth by priority on the interface
                        	**type**\: list of  		 :py:class:`BandwidthReservation <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations, self).__init__()

                            self.yang_name = "bandwidth-reservations"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("bandwidth-reservation", ("bandwidth_reservation", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation))])
                            self._leafs = OrderedDict()

                            self.bandwidth_reservation = YList(self)
                            self._segment_path = lambda: "bandwidth-reservations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations, [], name, value)


                        class BandwidthReservation(_Entity_):
                            """
                            Available and reserved bandwidth by priority on
                            the interface.
                            
                            .. attribute:: priority  (key)
                            
                            	Reference to the RSVP priority level
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..7
                            
                            		**type**\:  :py:class:`Priority <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State.Priority>`
                            
                            	**refers to**\:  :py:class:`priority <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State>`
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	Operational state parameters relating to a bandwidth reservation at a certain priority
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation, self).__init__()

                                self.yang_name = "bandwidth-reservation"
                                self.yang_parent_name = "bandwidth-reservations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['priority']
                                self._child_classes = OrderedDict([("state", ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State))])
                                self._leafs = OrderedDict([
                                    ('priority', (YLeaf(YType.str, 'priority'), ['str'])),
                                ])
                                self.priority = None

                                self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "bandwidth-reservation" + "[priority='" + str(self.priority) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation, ['priority'], name, value)


                            class State(_Entity_):
                                """
                                Operational state parameters relating to a
                                bandwidth reservation at a certain priority
                                
                                .. attribute:: priority
                                
                                	RSVP priority level for LSPs traversing the interface
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 0..7
                                
                                		**type**\:  :py:class:`Priority <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State.Priority>`
                                
                                	**config**\: False
                                
                                .. attribute:: available_bandwidth
                                
                                	Bandwidth currently available with the priority level, or for the entire interface when the priority is set to ALL
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: reserved_bandwidth
                                
                                	Bandwidth currently reserved within the priority level, or the sum of all priority levels when the keyword is set to ALL
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: active_reservations_count
                                
                                	Number of active RSVP reservations in the associated priority, or the sum of all reservations when the priority level is set to ALL
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: highwater_mark
                                
                                	Maximum bandwidth reserved on the interface within the priority, or across all priorities in the case that the priority level is set to ALL
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "bandwidth-reservation"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('priority', (YLeaf(YType.str, 'priority'), ['int',('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State.Priority')])),
                                        ('available_bandwidth', (YLeaf(YType.uint64, 'available-bandwidth'), ['int'])),
                                        ('reserved_bandwidth', (YLeaf(YType.uint64, 'reserved-bandwidth'), ['int'])),
                                        ('active_reservations_count', (YLeaf(YType.uint64, 'active-reservations-count'), ['int'])),
                                        ('highwater_mark', (YLeaf(YType.uint64, 'highwater-mark'), ['int'])),
                                    ])
                                    self.priority = None
                                    self.available_bandwidth = None
                                    self.reserved_bandwidth = None
                                    self.active_reservations_count = None
                                    self.highwater_mark = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.BandwidthReservations.BandwidthReservation.State, ['priority', 'available_bandwidth', 'reserved_bandwidth', 'active_reservations_count', 'highwater_mark'], name, value)

                                class Priority(Enum):
                                    """
                                    Priority (Enum Class)

                                    RSVP priority level for LSPs traversing the interface

                                    .. data:: ALL = 0

                                    	The ALL keyword represents the overall

                                    	state of the interface - i.e., the union

                                    	of all of the priority levels

                                    """

                                    ALL = Enum.YLeaf(0, "ALL")






                    class Hellos(_Entity_):
                        """
                        Top level container for RSVP hello parameters
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to RSVP hellos
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config>`
                        
                        .. attribute:: state
                        
                        	State information associated with RSVP hellos
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos, self).__init__()

                            self.yang_name = "hellos"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State))])
                            self._leafs = OrderedDict()

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "hellos"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration parameters relating to RSVP
                            hellos
                            
                            .. attribute:: hello_interval
                            
                            	set the interval in ms between RSVP hello messages
                            	**type**\: int
                            
                            	**range:** 1000..60000
                            
                            	**units**\: milliseconds
                            
                            	**default value**\: 9000
                            
                            .. attribute:: refresh_reduction
                            
                            	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                            	**type**\: bool
                            
                            	**default value**\: true
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "hellos"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                                    ('refresh_reduction', (YLeaf(YType.boolean, 'refresh-reduction'), ['bool'])),
                                ])
                                self.hello_interval = None
                                self.refresh_reduction = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config, ['hello_interval', 'refresh_reduction'], name, value)



                        class State(_Entity_):
                            """
                            State information associated with RSVP hellos
                            
                            .. attribute:: hello_interval
                            
                            	set the interval in ms between RSVP hello messages
                            	**type**\: int
                            
                            	**range:** 1000..60000
                            
                            	**config**\: False
                            
                            	**units**\: milliseconds
                            
                            	**default value**\: 9000
                            
                            .. attribute:: refresh_reduction
                            
                            	enables all RSVP refresh reduction message bundling, RSVP message ID, reliable message delivery and summary refresh
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            	**default value**\: true
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "hellos"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                                    ('refresh_reduction', (YLeaf(YType.boolean, 'refresh-reduction'), ['bool'])),
                                ])
                                self.hello_interval = None
                                self.refresh_reduction = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State, ['hello_interval', 'refresh_reduction'], name, value)




                    class Authentication(_Entity_):
                        """
                        Configuration and state parameters relating to RSVP
                        authentication as per RFC2747
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to authentication
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config>`
                        
                        .. attribute:: state
                        
                        	State information associated with authentication
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State))])
                            self._leafs = OrderedDict()

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "authentication"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration parameters relating
                            to authentication
                            
                            .. attribute:: enable
                            
                            	Enables RSVP authentication on the node
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: authentication_key
                            
                            	authenticate RSVP signaling messages
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "authentication"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                    ('authentication_key', (YLeaf(YType.str, 'authentication-key'), ['str'])),
                                ])
                                self.enable = None
                                self.authentication_key = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config, ['enable', 'authentication_key'], name, value)



                        class State(_Entity_):
                            """
                            State information associated
                            with authentication
                            
                            .. attribute:: enable
                            
                            	Enables RSVP authentication on the node
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            	**default value**\: false
                            
                            .. attribute:: authentication_key
                            
                            	authenticate RSVP signaling messages
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "authentication"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                    ('authentication_key', (YLeaf(YType.str, 'authentication-key'), ['str'])),
                                ])
                                self.enable = None
                                self.authentication_key = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State, ['enable', 'authentication_key'], name, value)




                    class Subscription(_Entity_):
                        """
                        Bandwidth percentage reservable by RSVP
                        on an interface
                        
                        .. attribute:: config
                        
                        	Configuration parameters relating to RSVP subscription options
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters relating to RSVP subscription options
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription, self).__init__()

                            self.yang_name = "subscription"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State))])
                            self._leafs = OrderedDict()

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "subscription"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration parameters relating to RSVP
                            subscription options
                            
                            .. attribute:: subscription
                            
                            	percentage of the interface bandwidth that RSVP can reserve
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "subscription"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('subscription', (YLeaf(YType.uint8, 'subscription'), ['int'])),
                                ])
                                self.subscription = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config, ['subscription'], name, value)



                        class State(_Entity_):
                            """
                            State parameters relating to RSVP
                            subscription options
                            
                            .. attribute:: subscription
                            
                            	percentage of the interface bandwidth that RSVP can reserve
                            	**type**\: int
                            
                            	**range:** 0..100
                            
                            	**config**\: False
                            
                            .. attribute:: calculated_absolute_subscription_bw
                            
                            	The calculated absolute value of the bandwidth which is reservable to RSVP\-TE on the interface prior to any adjustments that may be made from external sources
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: kbps
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "subscription"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('subscription', (YLeaf(YType.uint8, 'subscription'), ['int'])),
                                    ('calculated_absolute_subscription_bw', (YLeaf(YType.uint64, 'calculated-absolute-subscription-bw'), ['int'])),
                                ])
                                self.subscription = None
                                self.calculated_absolute_subscription_bw = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State, ['subscription', 'calculated_absolute_subscription_bw'], name, value)




                    class Protection(_Entity_):
                        """
                        link\-protection (NHOP) related configuration
                        
                        .. attribute:: config
                        
                        	Configuration for link\-protection
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config>`
                        
                        .. attribute:: state
                        
                        	State for link\-protection
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection, self).__init__()

                            self.yang_name = "protection"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config)), ("state", ("state", Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State))])
                            self._leafs = OrderedDict()

                            self.config = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "protection"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration for link\-protection
                            
                            .. attribute:: link_protection_style_requested
                            
                            	Style of mpls frr protection desired\: link, link\-node, or unprotected
                            	**type**\:  :py:class:`PROTECTIONTYPE <ydk.models.openconfig.openconfig_mpls_types.PROTECTIONTYPE>`
                            
                            	**default value**\: oc-mplst:LINK_NODE_PROTECTION_REQUESTED
                            
                            .. attribute:: bypass_optimize_interval
                            
                            	interval between periodic optimization of the bypass LSPs
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "protection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('link_protection_style_requested', (YLeaf(YType.identityref, 'link-protection-style-requested'), [('ydk.models.openconfig.openconfig_mpls_types', 'PROTECTIONTYPE')])),
                                    ('bypass_optimize_interval', (YLeaf(YType.uint16, 'bypass-optimize-interval'), ['int'])),
                                ])
                                self.link_protection_style_requested = None
                                self.bypass_optimize_interval = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config, ['link_protection_style_requested', 'bypass_optimize_interval'], name, value)



                        class State(_Entity_):
                            """
                            State for link\-protection
                            
                            .. attribute:: link_protection_style_requested
                            
                            	Style of mpls frr protection desired\: link, link\-node, or unprotected
                            	**type**\:  :py:class:`PROTECTIONTYPE <ydk.models.openconfig.openconfig_mpls_types.PROTECTIONTYPE>`
                            
                            	**config**\: False
                            
                            	**default value**\: oc-mplst:LINK_NODE_PROTECTION_REQUESTED
                            
                            .. attribute:: bypass_optimize_interval
                            
                            	interval between periodic optimization of the bypass LSPs
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            	**units**\: seconds
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "protection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('link_protection_style_requested', (YLeaf(YType.identityref, 'link-protection-style-requested'), [('ydk.models.openconfig.openconfig_mpls_types', 'PROTECTIONTYPE')])),
                                    ('bypass_optimize_interval', (YLeaf(YType.uint16, 'bypass-optimize-interval'), ['int'])),
                                ])
                                self.link_protection_style_requested = None
                                self.bypass_optimize_interval = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State, ['link_protection_style_requested', 'bypass_optimize_interval'], name, value)







        class Ldp(_Entity_):
            """
            LDP global signaling configuration
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.SignalingProtocols.Ldp, self).__init__()

                self.yang_name = "ldp"
                self.yang_parent_name = "signaling-protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict()
                self._segment_path = lambda: "ldp"
                self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/%s" % self._segment_path()
                self._is_frozen = True



        class SegmentRouting(_Entity_):
            """
            MPLS\-specific Segment Routing configuration and operational state
            parameters
            
            .. attribute:: aggregate_sid_counters
            
            	Per\-SID counters aggregated across all interfaces on the local system
            	**type**\:  :py:class:`AggregateSidCounters <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters>`
            
            .. attribute:: interfaces
            
            	Interface related Segment Routing parameters
            	**type**\:  :py:class:`Interfaces <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.SignalingProtocols.SegmentRouting, self).__init__()

                self.yang_name = "segment-routing"
                self.yang_parent_name = "signaling-protocols"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("aggregate-sid-counters", ("aggregate_sid_counters", Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters)), ("interfaces", ("interfaces", Mpls.SignalingProtocols.SegmentRouting.Interfaces))])
                self._leafs = OrderedDict()

                self.aggregate_sid_counters = Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters()
                self.aggregate_sid_counters.parent = self
                self._children_name_map["aggregate_sid_counters"] = "aggregate-sid-counters"

                self.interfaces = Mpls.SignalingProtocols.SegmentRouting.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "segment-routing"
                self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting, [], name, value)


            class AggregateSidCounters(_Entity_):
                """
                Per\-SID counters aggregated across all interfaces on the local system
                
                .. attribute:: aggregate_sid_counter
                
                	Counters aggregated across all of the interfaces of the local system corresponding to traffic received or forwarded with a particular SID
                	**type**\: list of  		 :py:class:`AggregateSidCounter <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter>`
                
                	**config**\: False
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters, self).__init__()

                    self.yang_name = "aggregate-sid-counters"
                    self.yang_parent_name = "segment-routing"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("aggregate-sid-counter", ("aggregate_sid_counter", Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter))])
                    self._leafs = OrderedDict()

                    self.aggregate_sid_counter = YList(self)
                    self._segment_path = lambda: "aggregate-sid-counters"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/segment-routing/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters, [], name, value)


                class AggregateSidCounter(_Entity_):
                    """
                    Counters aggregated across all of the interfaces of the local
                    system corresponding to traffic received or forwarded with a
                    particular SID
                    
                    .. attribute:: mpls_label  (key)
                    
                    	The MPLS label representing the segment identifier
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 16..1048575
                    
                    		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                    
                    	**refers to**\:  :py:class:`mpls_label <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	State parameters for per\-SID statistics
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter, self).__init__()

                        self.yang_name = "aggregate-sid-counter"
                        self.yang_parent_name = "aggregate-sid-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['mpls_label']
                        self._child_classes = OrderedDict([("state", ("state", Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter.State))])
                        self._leafs = OrderedDict([
                            ('mpls_label', (YLeaf(YType.str, 'mpls-label'), ['str'])),
                        ])
                        self.mpls_label = None

                        self.state = Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "aggregate-sid-counter" + "[mpls-label='" + str(self.mpls_label) + "']"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/segment-routing/aggregate-sid-counters/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter, ['mpls_label'], name, value)


                    class State(_Entity_):
                        """
                        State parameters for per\-SID statistics
                        
                        .. attribute:: mpls_label
                        
                        	The MPLS label used for the segment identifier
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        .. attribute:: in_pkts
                        
                        	A cumulative counter of the packets received within the context which have matched a label corresponding to an SR Segment Identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_octets
                        
                        	The cumulative counter of the total bytes received within the context which have matched a label corresponding to an SR Segment Identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_pkts
                        
                        	A cumulative counter of the total number of packets transmitted by the local system within the context which have a label imposed that corresponds to an Segment Identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_octets
                        
                        	A cumulative counter of the total bytes transmitted by the local system within the context which have a label imported that corresponds to an SR Segment Identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "aggregate-sid-counter"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mpls_label', (YLeaf(YType.str, 'mpls-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                ('in_pkts', (YLeaf(YType.uint64, 'in-pkts'), ['int'])),
                                ('in_octets', (YLeaf(YType.uint64, 'in-octets'), ['int'])),
                                ('out_pkts', (YLeaf(YType.uint64, 'out-pkts'), ['int'])),
                                ('out_octets', (YLeaf(YType.uint64, 'out-octets'), ['int'])),
                            ])
                            self.mpls_label = None
                            self.in_pkts = None
                            self.in_octets = None
                            self.out_pkts = None
                            self.out_octets = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.AggregateSidCounters.AggregateSidCounter.State, ['mpls_label', 'in_pkts', 'in_octets', 'out_pkts', 'out_octets'], name, value)





            class Interfaces(_Entity_):
                """
                Interface related Segment Routing parameters.
                
                .. attribute:: interface
                
                	Parameters and MPLS\-specific configuration relating to Segment Routing on an interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface>`
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.SignalingProtocols.SegmentRouting.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "segment-routing"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/segment-routing/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces, [], name, value)


                class Interface(_Entity_):
                    """
                    Parameters and MPLS\-specific configuration relating to Segment
                    Routing on an interface.
                    
                    .. attribute:: interface_id  (key)
                    
                    	A reference to the ID for the interface for which SR is configured
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`interface_id <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.Config>`
                    
                    .. attribute:: config
                    
                    	MPLS\-specific Segment Routing configuration parameters related to an interface
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.Config>`
                    
                    .. attribute:: state
                    
                    	MPLS\-specific Segment Routing operational state parameters related to an interface
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: sid_counters
                    
                    	Per\-SID statistics for MPLS
                    	**type**\:  :py:class:`SidCounters <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters>`
                    
                    .. attribute:: interface_ref
                    
                    	Reference to an interface or subinterface
                    	**type**\:  :py:class:`InterfaceRef <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef>`
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_id']
                        self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.Config)), ("state", ("state", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.State)), ("sid-counters", ("sid_counters", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters)), ("interface-ref", ("interface_ref", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef))])
                        self._leafs = OrderedDict([
                            ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                        ])
                        self.interface_id = None

                        self.config = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"

                        self.sid_counters = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters()
                        self.sid_counters.parent = self
                        self._children_name_map["sid_counters"] = "sid-counters"

                        self.interface_ref = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef()
                        self.interface_ref.parent = self
                        self._children_name_map["interface_ref"] = "interface-ref"
                        self._segment_path = lambda: "interface" + "[interface-id='" + str(self.interface_id) + "']"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/signaling-protocols/segment-routing/interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface, ['interface_id'], name, value)


                    class Config(_Entity_):
                        """
                        MPLS\-specific Segment Routing configuration parameters
                        related to an interface.
                        
                        .. attribute:: interface_id
                        
                        	A unique identifier for the interface
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                            ])
                            self.interface_id = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.Config, ['interface_id'], name, value)



                    class State(_Entity_):
                        """
                        MPLS\-specific Segment Routing operational state parameters
                        related to an interface.
                        
                        .. attribute:: interface_id
                        
                        	A unique identifier for the interface
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: in_pkts
                        
                        	A cumulative counter of the packets received within the context which have matched a label corresponding to an SR Segment Identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: in_octets
                        
                        	The cumulative counter of the total bytes received within the context which have matched a label corresponding to an SR Segment Identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_pkts
                        
                        	A cumulative counter of the total number of packets transmitted by the local system within the context which have a label imposed that corresponds to an Segment Identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: out_octets
                        
                        	A cumulative counter of the total bytes transmitted by the local system within the context which have a label imported that corresponds to an SR Segment Identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_id', (YLeaf(YType.str, 'interface-id'), ['str'])),
                                ('in_pkts', (YLeaf(YType.uint64, 'in-pkts'), ['int'])),
                                ('in_octets', (YLeaf(YType.uint64, 'in-octets'), ['int'])),
                                ('out_pkts', (YLeaf(YType.uint64, 'out-pkts'), ['int'])),
                                ('out_octets', (YLeaf(YType.uint64, 'out-octets'), ['int'])),
                            ])
                            self.interface_id = None
                            self.in_pkts = None
                            self.in_octets = None
                            self.out_pkts = None
                            self.out_octets = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.State, ['interface_id', 'in_pkts', 'in_octets', 'out_pkts', 'out_octets'], name, value)



                    class SidCounters(_Entity_):
                        """
                        Per\-SID statistics for MPLS
                        
                        .. attribute:: sid_counter
                        
                        	Per segment identifier counters for the MPLS dataplane
                        	**type**\: list of  		 :py:class:`SidCounter <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters, self).__init__()

                            self.yang_name = "sid-counters"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sid-counter", ("sid_counter", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter))])
                            self._leafs = OrderedDict()

                            self.sid_counter = YList(self)
                            self._segment_path = lambda: "sid-counters"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters, [], name, value)


                        class SidCounter(_Entity_):
                            """
                            Per segment identifier counters for the MPLS dataplane.
                            
                            .. attribute:: mpls_label  (key)
                            
                            	The MPLS label representing the segment identifier
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 16..1048575
                            
                            		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                            
                            	**refers to**\:  :py:class:`mpls_label <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.State>`
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	State parameters for per\-SID statistics
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.State>`
                            
                            	**config**\: False
                            
                            .. attribute:: forwarding_classes
                            
                            	Per\-SID per\-forwarding class counters for Segment Routing
                            	**type**\:  :py:class:`ForwardingClasses <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter, self).__init__()

                                self.yang_name = "sid-counter"
                                self.yang_parent_name = "sid-counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mpls_label']
                                self._child_classes = OrderedDict([("state", ("state", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.State)), ("forwarding-classes", ("forwarding_classes", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses))])
                                self._leafs = OrderedDict([
                                    ('mpls_label', (YLeaf(YType.str, 'mpls-label'), ['str'])),
                                ])
                                self.mpls_label = None

                                self.state = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"

                                self.forwarding_classes = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses()
                                self.forwarding_classes.parent = self
                                self._children_name_map["forwarding_classes"] = "forwarding-classes"
                                self._segment_path = lambda: "sid-counter" + "[mpls-label='" + str(self.mpls_label) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter, ['mpls_label'], name, value)


                            class State(_Entity_):
                                """
                                State parameters for per\-SID statistics
                                
                                .. attribute:: mpls_label
                                
                                	The MPLS label used for the segment identifier
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 16..1048575
                                
                                		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                                
                                	**config**\: False
                                
                                .. attribute:: in_pkts
                                
                                	A cumulative counter of the packets received within the context which have matched a label corresponding to an SR Segment Identifier
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: in_octets
                                
                                	The cumulative counter of the total bytes received within the context which have matched a label corresponding to an SR Segment Identifier
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: out_pkts
                                
                                	A cumulative counter of the total number of packets transmitted by the local system within the context which have a label imposed that corresponds to an Segment Identifier
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: out_octets
                                
                                	A cumulative counter of the total bytes transmitted by the local system within the context which have a label imported that corresponds to an SR Segment Identifier
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "sid-counter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mpls_label', (YLeaf(YType.str, 'mpls-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                        ('in_pkts', (YLeaf(YType.uint64, 'in-pkts'), ['int'])),
                                        ('in_octets', (YLeaf(YType.uint64, 'in-octets'), ['int'])),
                                        ('out_pkts', (YLeaf(YType.uint64, 'out-pkts'), ['int'])),
                                        ('out_octets', (YLeaf(YType.uint64, 'out-octets'), ['int'])),
                                    ])
                                    self.mpls_label = None
                                    self.in_pkts = None
                                    self.in_octets = None
                                    self.out_pkts = None
                                    self.out_octets = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.State, ['mpls_label', 'in_pkts', 'in_octets', 'out_pkts', 'out_octets'], name, value)



                            class ForwardingClasses(_Entity_):
                                """
                                Per\-SID per\-forwarding class counters for Segment Routing.
                                
                                .. attribute:: forwarding_class
                                
                                	SID entries for the forwarding class associated with the referenced MPLS EXP
                                	**type**\: list of  		 :py:class:`ForwardingClass <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses, self).__init__()

                                    self.yang_name = "forwarding-classes"
                                    self.yang_parent_name = "sid-counter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("forwarding-class", ("forwarding_class", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass))])
                                    self._leafs = OrderedDict()

                                    self.forwarding_class = YList(self)
                                    self._segment_path = lambda: "forwarding-classes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses, [], name, value)


                                class ForwardingClass(_Entity_):
                                    """
                                    SID entries for the forwarding class associated with the
                                    referenced MPLS EXP.
                                    
                                    .. attribute:: exp  (key)
                                    
                                    	Reference to the value of the EXP bits of the segment identifier
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**refers to**\:  :py:class:`exp <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass.State>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: state
                                    
                                    	Per\-SID, per forwarding class counters for Segment Routing with the MPLS dataplane
                                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass.State>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass, self).__init__()

                                        self.yang_name = "forwarding-class"
                                        self.yang_parent_name = "forwarding-classes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['exp']
                                        self._child_classes = OrderedDict([("state", ("state", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass.State))])
                                        self._leafs = OrderedDict([
                                            ('exp', (YLeaf(YType.str, 'exp'), ['int'])),
                                        ])
                                        self.exp = None

                                        self.state = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._segment_path = lambda: "forwarding-class" + "[exp='" + str(self.exp) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass, ['exp'], name, value)


                                    class State(_Entity_):
                                        """
                                        Per\-SID, per forwarding class counters for Segment Routing
                                        with the MPLS dataplane
                                        
                                        .. attribute:: exp
                                        
                                        	The value of the MPLS EXP (experimental) or Traffic Class bits that the SID statistics relate to. Packets received with a MPLS label value equal to the SID's MPLS label and EXP bits equal to the this value should be counted towards the associated ingress statistics. Packets that are forwarded to the destination MPLS label corresponding to the SID should be counted towards this value. In the egress direction, where forwarding follows a SID value that requires PHP at the local node, packets should still be counted towards the egress counters
                                        	**type**\: int
                                        
                                        	**range:** 0..7
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: in_pkts
                                        
                                        	A cumulative counter of the packets received within the context which have matched a label corresponding to an SR Segment Identifier
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: in_octets
                                        
                                        	The cumulative counter of the total bytes received within the context which have matched a label corresponding to an SR Segment Identifier
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: out_pkts
                                        
                                        	A cumulative counter of the total number of packets transmitted by the local system within the context which have a label imposed that corresponds to an Segment Identifier
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: out_octets
                                        
                                        	A cumulative counter of the total bytes transmitted by the local system within the context which have a label imported that corresponds to an SR Segment Identifier
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'oc-mpls'
                                        _revision = '2017-03-22'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "forwarding-class"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('exp', (YLeaf(YType.uint8, 'exp'), ['int'])),
                                                ('in_pkts', (YLeaf(YType.uint64, 'in-pkts'), ['int'])),
                                                ('in_octets', (YLeaf(YType.uint64, 'in-octets'), ['int'])),
                                                ('out_pkts', (YLeaf(YType.uint64, 'out-pkts'), ['int'])),
                                                ('out_octets', (YLeaf(YType.uint64, 'out-octets'), ['int'])),
                                            ])
                                            self.exp = None
                                            self.in_pkts = None
                                            self.in_octets = None
                                            self.out_pkts = None
                                            self.out_octets = None
                                            self._segment_path = lambda: "state"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.SidCounters.SidCounter.ForwardingClasses.ForwardingClass.State, ['exp', 'in_pkts', 'in_octets', 'out_pkts', 'out_octets'], name, value)







                    class InterfaceRef(_Entity_):
                        """
                        Reference to an interface or subinterface
                        
                        .. attribute:: config
                        
                        	Configured reference to interface / subinterface
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.Config>`
                        
                        .. attribute:: state
                        
                        	Operational state for interface\-ref
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.State>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef, self).__init__()

                            self.yang_name = "interface-ref"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.Config)), ("state", ("state", Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.State))])
                            self._leafs = OrderedDict()

                            self.config = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"
                            self._segment_path = lambda: "interface-ref"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef, [], name, value)


                        class Config(_Entity_):
                            """
                            Configured reference to interface / subinterface
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                                ])
                                self.interface = None
                                self.subinterface = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.Config, ['interface', 'subinterface'], name, value)



                        class State(_Entity_):
                            """
                            Operational state for interface\-ref
                            
                            .. attribute:: interface
                            
                            	Reference to a base interface.  If a reference to a subinterface is required, this leaf must be specified to indicate the base interface
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface>`
                            
                            	**config**\: False
                            
                            .. attribute:: subinterface
                            
                            	Reference to a subinterface \-\- this requires the base interface to be specified using the interface leaf in this container.  If only a reference to a base interface is requuired, this leaf should not be set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_interfaces.Interfaces.Interface.Subinterfaces.Subinterface>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "interface-ref"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('subinterface', (YLeaf(YType.str, 'subinterface'), ['int'])),
                                ])
                                self.interface = None
                                self.subinterface = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.SignalingProtocols.SegmentRouting.Interfaces.Interface.InterfaceRef.State, ['interface', 'subinterface'], name, value)








    class Lsps(_Entity_):
        """
        LSP definitions and configuration
        
        .. attribute:: constrained_path
        
        	traffic\-engineered LSPs supporting different path computation and signaling methods
        	**type**\:  :py:class:`ConstrainedPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath>`
        
        .. attribute:: unconstrained_path
        
        	LSPs that use the IGP\-determined path, i.e., non traffic\-engineered, or non constrained\-path
        	**type**\:  :py:class:`UnconstrainedPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath>`
        
        .. attribute:: static_lsps
        
        	statically configured LSPs, without dynamic signaling
        	**type**\:  :py:class:`StaticLsps <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps>`
        
        

        """

        _prefix = 'oc-mpls'
        _revision = '2017-03-22'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Mpls.Lsps, self).__init__()

            self.yang_name = "lsps"
            self.yang_parent_name = "mpls"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("constrained-path", ("constrained_path", Mpls.Lsps.ConstrainedPath)), ("unconstrained-path", ("unconstrained_path", Mpls.Lsps.UnconstrainedPath)), ("static-lsps", ("static_lsps", Mpls.Lsps.StaticLsps))])
            self._leafs = OrderedDict()

            self.constrained_path = Mpls.Lsps.ConstrainedPath()
            self.constrained_path.parent = self
            self._children_name_map["constrained_path"] = "constrained-path"

            self.unconstrained_path = Mpls.Lsps.UnconstrainedPath()
            self.unconstrained_path.parent = self
            self._children_name_map["unconstrained_path"] = "unconstrained-path"

            self.static_lsps = Mpls.Lsps.StaticLsps()
            self.static_lsps.parent = self
            self._children_name_map["static_lsps"] = "static-lsps"
            self._segment_path = lambda: "lsps"
            self._absolute_path = lambda: "openconfig-mpls:mpls/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Mpls.Lsps, [], name, value)


        class ConstrainedPath(_Entity_):
            """
            traffic\-engineered LSPs supporting different
            path computation and signaling methods
            
            .. attribute:: named_explicit_paths
            
            	Enclosing container for the named explicit paths
            	**type**\:  :py:class:`NamedExplicitPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths>`
            
            .. attribute:: tunnels
            
            	Enclosing container for tunnels
            	**type**\:  :py:class:`Tunnels <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.Lsps.ConstrainedPath, self).__init__()

                self.yang_name = "constrained-path"
                self.yang_parent_name = "lsps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("named-explicit-paths", ("named_explicit_paths", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths)), ("tunnels", ("tunnels", Mpls.Lsps.ConstrainedPath.Tunnels))])
                self._leafs = OrderedDict()

                self.named_explicit_paths = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths()
                self.named_explicit_paths.parent = self
                self._children_name_map["named_explicit_paths"] = "named-explicit-paths"

                self.tunnels = Mpls.Lsps.ConstrainedPath.Tunnels()
                self.tunnels.parent = self
                self._children_name_map["tunnels"] = "tunnels"
                self._segment_path = lambda: "constrained-path"
                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Lsps.ConstrainedPath, [], name, value)


            class NamedExplicitPaths(_Entity_):
                """
                Enclosing container for the named explicit paths
                
                .. attribute:: named_explicit_path
                
                	A list of explicit paths
                	**type**\: list of  		 :py:class:`NamedExplicitPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath>`
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths, self).__init__()

                    self.yang_name = "named-explicit-paths"
                    self.yang_parent_name = "constrained-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("named-explicit-path", ("named_explicit_path", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath))])
                    self._leafs = OrderedDict()

                    self.named_explicit_path = YList(self)
                    self._segment_path = lambda: "named-explicit-paths"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/constrained-path/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths, [], name, value)


                class NamedExplicitPath(_Entity_):
                    """
                    A list of explicit paths
                    
                    .. attribute:: name  (key)
                    
                    	A string name that uniquely identifies an explicit path
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters relating to named explicit paths
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state parameters relating to the named explicit paths
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: explicit_route_objects
                    
                    	Enclosing container for EROs
                    	**type**\:  :py:class:`ExplicitRouteObjects <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects>`
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath, self).__init__()

                        self.yang_name = "named-explicit-path"
                        self.yang_parent_name = "named-explicit-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.State)), ("explicit-route-objects", ("explicit_route_objects", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.config = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"

                        self.explicit_route_objects = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects()
                        self.explicit_route_objects.parent = self
                        self._children_name_map["explicit_route_objects"] = "explicit-route-objects"
                        self._segment_path = lambda: "named-explicit-path" + "[name='" + str(self.name) + "']"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/constrained-path/named-explicit-paths/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath, ['name'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration parameters relating to named explicit
                        paths
                        
                        .. attribute:: name
                        
                        	A string name that uniquely identifies an explicit path
                        	**type**\: str
                        
                        .. attribute:: sid_selection_mode
                        
                        	The restrictions placed on the SIDs to be selected by the calculation method for the explicit path when it is instantiated for a SR\-TE LSP
                        	**type**\:  :py:class:`SidSelectionMode <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config.SidSelectionMode>`
                        
                        	**default value**\: MIXED_MODE
                        
                        .. attribute:: sid_protection_required
                        
                        	When this value is set to true, only SIDs that are protected are to be selected by the calculating method when the explicit path is instantiated by a SR\-TE LSP
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "named-explicit-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('sid_selection_mode', (YLeaf(YType.enumeration, 'sid-selection-mode'), [('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config.SidSelectionMode')])),
                                ('sid_protection_required', (YLeaf(YType.boolean, 'sid-protection-required'), ['bool'])),
                            ])
                            self.name = None
                            self.sid_selection_mode = None
                            self.sid_protection_required = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config, ['name', 'sid_selection_mode', 'sid_protection_required'], name, value)

                        class SidSelectionMode(Enum):
                            """
                            SidSelectionMode (Enum Class)

                            The restrictions placed on the SIDs to be selected by the

                            calculation method for the explicit path when it is

                            instantiated for a SR\-TE LSP

                            .. data:: ADJ_SID_ONLY = 0

                            	The SR-TE tunnel should only use adjacency SIDs

                            	to build the SID stack to be pushed for the LSP

                            .. data:: MIXED_MODE = 1

                            	The SR-TE tunnel can use a mix of adjacency

                            	and prefix SIDs to build the SID stack to be pushed

                            	to the LSP

                            """

                            ADJ_SID_ONLY = Enum.YLeaf(0, "ADJ_SID_ONLY")

                            MIXED_MODE = Enum.YLeaf(1, "MIXED_MODE")




                    class State(_Entity_):
                        """
                        Operational state parameters relating to the named
                        explicit paths
                        
                        .. attribute:: name
                        
                        	A string name that uniquely identifies an explicit path
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sid_selection_mode
                        
                        	The restrictions placed on the SIDs to be selected by the calculation method for the explicit path when it is instantiated for a SR\-TE LSP
                        	**type**\:  :py:class:`SidSelectionMode <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.State.SidSelectionMode>`
                        
                        	**config**\: False
                        
                        	**default value**\: MIXED_MODE
                        
                        .. attribute:: sid_protection_required
                        
                        	When this value is set to true, only SIDs that are protected are to be selected by the calculating method when the explicit path is instantiated by a SR\-TE LSP
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "named-explicit-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('sid_selection_mode', (YLeaf(YType.enumeration, 'sid-selection-mode'), [('ydk.models.openconfig.openconfig_mpls', 'Mpls', 'Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.State.SidSelectionMode')])),
                                ('sid_protection_required', (YLeaf(YType.boolean, 'sid-protection-required'), ['bool'])),
                            ])
                            self.name = None
                            self.sid_selection_mode = None
                            self.sid_protection_required = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.State, ['name', 'sid_selection_mode', 'sid_protection_required'], name, value)

                        class SidSelectionMode(Enum):
                            """
                            SidSelectionMode (Enum Class)

                            The restrictions placed on the SIDs to be selected by the

                            calculation method for the explicit path when it is

                            instantiated for a SR\-TE LSP

                            .. data:: ADJ_SID_ONLY = 0

                            	The SR-TE tunnel should only use adjacency SIDs

                            	to build the SID stack to be pushed for the LSP

                            .. data:: MIXED_MODE = 1

                            	The SR-TE tunnel can use a mix of adjacency

                            	and prefix SIDs to build the SID stack to be pushed

                            	to the LSP

                            """

                            ADJ_SID_ONLY = Enum.YLeaf(0, "ADJ_SID_ONLY")

                            MIXED_MODE = Enum.YLeaf(1, "MIXED_MODE")




                    class ExplicitRouteObjects(_Entity_):
                        """
                        Enclosing container for EROs
                        
                        .. attribute:: explicit_route_object
                        
                        	List of explicit route objects
                        	**type**\: list of  		 :py:class:`ExplicitRouteObject <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject>`
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects, self).__init__()

                            self.yang_name = "explicit-route-objects"
                            self.yang_parent_name = "named-explicit-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("explicit-route-object", ("explicit_route_object", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject))])
                            self._leafs = OrderedDict()

                            self.explicit_route_object = YList(self)
                            self._segment_path = lambda: "explicit-route-objects"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects, [], name, value)


                        class ExplicitRouteObject(_Entity_):
                            """
                            List of explicit route objects
                            
                            .. attribute:: index  (key)
                            
                            	Index of this explicit route object, to express the order of hops in path
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**refers to**\:  :py:class:`index <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.Config>`
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to an explicit route
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.Config>`
                            
                            .. attribute:: state
                            
                            	State parameters relating to an explicit route
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.State>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject, self).__init__()

                                self.yang_name = "explicit-route-object"
                                self.yang_parent_name = "explicit-route-objects"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['index']
                                self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.State))])
                                self._leafs = OrderedDict([
                                    ('index', (YLeaf(YType.str, 'index'), ['int'])),
                                ])
                                self.index = None

                                self.config = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"

                                self.state = Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"
                                self._segment_path = lambda: "explicit-route-object" + "[index='" + str(self.index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject, ['index'], name, value)


                            class Config(_Entity_):
                                """
                                Configuration parameters relating to an explicit
                                route
                                
                                .. attribute:: address
                                
                                	router hop for the LSP path
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                
                                .. attribute:: hop_type
                                
                                	strict or loose hop
                                	**type**\:  :py:class:`MplsHopType <ydk.models.openconfig.openconfig_mpls.MplsHopType>`
                                
                                .. attribute:: index
                                
                                	Index of this explicit route object to express the order of hops in the path
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "explicit-route-object"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                        ('hop_type', (YLeaf(YType.enumeration, 'hop-type'), [('ydk.models.openconfig.openconfig_mpls', 'MplsHopType', '')])),
                                        ('index', (YLeaf(YType.uint8, 'index'), ['int'])),
                                    ])
                                    self.address = None
                                    self.hop_type = None
                                    self.index = None
                                    self._segment_path = lambda: "config"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.Config, ['address', 'hop_type', 'index'], name, value)



                            class State(_Entity_):
                                """
                                State parameters relating to an explicit route
                                
                                .. attribute:: address
                                
                                	router hop for the LSP path
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                
                                		**type**\: str
                                
                                			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                
                                	**config**\: False
                                
                                .. attribute:: hop_type
                                
                                	strict or loose hop
                                	**type**\:  :py:class:`MplsHopType <ydk.models.openconfig.openconfig_mpls.MplsHopType>`
                                
                                	**config**\: False
                                
                                .. attribute:: index
                                
                                	Index of this explicit route object to express the order of hops in the path
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "explicit-route-object"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                        ('hop_type', (YLeaf(YType.enumeration, 'hop-type'), [('ydk.models.openconfig.openconfig_mpls', 'MplsHopType', '')])),
                                        ('index', (YLeaf(YType.uint8, 'index'), ['int'])),
                                    ])
                                    self.address = None
                                    self.hop_type = None
                                    self.index = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.ExplicitRouteObjects.ExplicitRouteObject.State, ['address', 'hop_type', 'index'], name, value)







            class Tunnels(_Entity_):
                """
                Enclosing container for tunnels
                
                .. attribute:: tunnel
                
                	List of TE tunnels. This list contains only the LSPs that the current device originates (i.e., for which it is the head\-end). Where the signaling protocol utilised for an LSP allows a mid\-point or tail device to be aware of the LSP (e.g., RSVP\-TE), then the associated sessions are maintained per protocol
                	**type**\: list of  		 :py:class:`Tunnel <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel>`
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.Lsps.ConstrainedPath.Tunnels, self).__init__()

                    self.yang_name = "tunnels"
                    self.yang_parent_name = "constrained-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tunnel", ("tunnel", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel))])
                    self._leafs = OrderedDict()

                    self.tunnel = YList(self)
                    self._segment_path = lambda: "tunnels"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/constrained-path/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels, [], name, value)


                class Tunnel(_Entity_):
                    """
                    List of TE tunnels. This list contains only the LSPs that the
                    current device originates (i.e., for which it is the head\-end).
                    Where the signaling protocol utilised for an LSP allows a mid\-point
                    or tail device to be aware of the LSP (e.g., RSVP\-TE), then the
                    associated sessions are maintained per protocol
                    
                    .. attribute:: name  (key)
                    
                    	The tunnel name
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Config>`
                    
                    .. attribute:: config
                    
                    	Configuration parameters related to TE tunnels\:
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Config>`
                    
                    .. attribute:: state
                    
                    	State parameters related to TE tunnels
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State>`
                    
                    	**config**\: False
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth configuration for TE LSPs
                    	**type**\:  :py:class:`Bandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth>`
                    
                    .. attribute:: p2p_tunnel_attributes
                    
                    	Parameters related to LSPs of type P2P
                    	**type**\:  :py:class:`P2pTunnelAttributes <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes>`
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel, self).__init__()

                        self.yang_name = "tunnel"
                        self.yang_parent_name = "tunnels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State)), ("bandwidth", ("bandwidth", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth)), ("p2p-tunnel-attributes", ("p2p_tunnel_attributes", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"

                        self.bandwidth = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth()
                        self.bandwidth.parent = self
                        self._children_name_map["bandwidth"] = "bandwidth"

                        self.p2p_tunnel_attributes = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes()
                        self.p2p_tunnel_attributes.parent = self
                        self._children_name_map["p2p_tunnel_attributes"] = "p2p-tunnel-attributes"
                        self._segment_path = lambda: "tunnel" + "[name='" + str(self.name) + "']"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/constrained-path/tunnels/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel, ['name'], name, value)


                    class Config(_Entity_):
                        """
                        Configuration parameters related to TE tunnels\:
                        
                        .. attribute:: name
                        
                        	The tunnel name
                        	**type**\: str
                        
                        .. attribute:: type
                        
                        	Tunnel type, p2p or p2mp
                        	**type**\:  :py:class:`TUNNELTYPE <ydk.models.openconfig.openconfig_mpls_types.TUNNELTYPE>`
                        
                        .. attribute:: signaling_protocol
                        
                        	Signaling protocol used to set up this tunnel
                        	**type**\:  :py:class:`PATHSETUPPROTOCOL <ydk.models.openconfig.openconfig_mpls_types.PATHSETUPPROTOCOL>`
                        
                        .. attribute:: description
                        
                        	optional text description for the tunnel
                        	**type**\: str
                        
                        .. attribute:: admin_status
                        
                        	TE tunnel administrative state
                        	**type**\:  :py:class:`TUNNELADMINSTATUS <ydk.models.openconfig.openconfig_mpls_types.TUNNELADMINSTATUS>`
                        
                        	**default value**\: oc-mplst:ADMIN_UP
                        
                        .. attribute:: preference
                        
                        	Specifies a preference for this tunnel. A lower number signifies a better preference
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: metric_type
                        
                        	The type of metric specification that should be used to set the LSP(s) metric
                        	**type**\:  :py:class:`LSPMETRICTYPE <ydk.models.openconfig.openconfig_mpls_types.LSPMETRICTYPE>`
                        
                        	**default value**\: oc-mplst:LSP_METRIC_INHERITED
                        
                        .. attribute:: metric
                        
                        	The value of the metric that should be specified. The value supplied in this leaf is used in conjunction with the metric type to determine the value of the metric used by the system. Where the metric\-type is set to LSP\_METRIC\_ABSOLUTE \- the value of this leaf is used directly; where it is set to LSP\_METRIC\_RELATIVE, the relevant (positive or negative) offset is used to formulate the metric; where metric\-type is LSP\_METRIC\_INHERITED, the value of this leaf is not utilised
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: shortcut_eligible
                        
                        	Whether this LSP is considered to be eligible for us as a shortcut in the IGP. In the case that this leaf is set to true, the IGP SPF calculation uses the metric specified to determine whether traffic should be carried over this LSP
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: protection_style_requested
                        
                        	style of mpls frr protection desired\: can be link, link\-node or unprotected
                        	**type**\:  :py:class:`PROTECTIONTYPE <ydk.models.openconfig.openconfig_mpls_types.PROTECTIONTYPE>`
                        
                        	**default value**\: oc-mplst:UNPROTECTED
                        
                        .. attribute:: reoptimize_timer
                        
                        	frequency of reoptimization of a traffic engineered LSP
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**units**\: seconds
                        
                        .. attribute:: source
                        
                        	RSVP\-TE tunnel source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        .. attribute:: soft_preemption
                        
                        	Enables RSVP soft\-preemption on this LSP
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: setup_priority
                        
                        	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        	**default value**\: 7
                        
                        .. attribute:: hold_priority
                        
                        	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_mpls_types', 'TUNNELTYPE')])),
                                ('signaling_protocol', (YLeaf(YType.identityref, 'signaling-protocol'), [('ydk.models.openconfig.openconfig_mpls_types', 'PATHSETUPPROTOCOL')])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('admin_status', (YLeaf(YType.identityref, 'admin-status'), [('ydk.models.openconfig.openconfig_mpls_types', 'TUNNELADMINSTATUS')])),
                                ('preference', (YLeaf(YType.uint8, 'preference'), ['int'])),
                                ('metric_type', (YLeaf(YType.identityref, 'metric-type'), [('ydk.models.openconfig.openconfig_mpls_types', 'LSPMETRICTYPE')])),
                                ('metric', (YLeaf(YType.int32, 'metric'), ['int'])),
                                ('shortcut_eligible', (YLeaf(YType.boolean, 'shortcut-eligible'), ['bool'])),
                                ('protection_style_requested', (YLeaf(YType.identityref, 'protection-style-requested'), [('ydk.models.openconfig.openconfig_mpls_types', 'PROTECTIONTYPE')])),
                                ('reoptimize_timer', (YLeaf(YType.uint16, 'reoptimize-timer'), ['int'])),
                                ('source', (YLeaf(YType.str, 'source'), ['str','str'])),
                                ('soft_preemption', (YLeaf(YType.boolean, 'soft-preemption'), ['bool'])),
                                ('setup_priority', (YLeaf(YType.uint8, 'setup-priority'), ['int'])),
                                ('hold_priority', (YLeaf(YType.uint8, 'hold-priority'), ['int'])),
                            ])
                            self.name = None
                            self.type = None
                            self.signaling_protocol = None
                            self.description = None
                            self.admin_status = None
                            self.preference = None
                            self.metric_type = None
                            self.metric = None
                            self.shortcut_eligible = None
                            self.protection_style_requested = None
                            self.reoptimize_timer = None
                            self.source = None
                            self.soft_preemption = None
                            self.setup_priority = None
                            self.hold_priority = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Config, ['name', 'type', 'signaling_protocol', 'description', 'admin_status', 'preference', 'metric_type', 'metric', 'shortcut_eligible', 'protection_style_requested', 'reoptimize_timer', 'source', 'soft_preemption', 'setup_priority', 'hold_priority'], name, value)



                    class State(_Entity_):
                        """
                        State parameters related to TE tunnels
                        
                        .. attribute:: name
                        
                        	The tunnel name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: type
                        
                        	Tunnel type, p2p or p2mp
                        	**type**\:  :py:class:`TUNNELTYPE <ydk.models.openconfig.openconfig_mpls_types.TUNNELTYPE>`
                        
                        	**config**\: False
                        
                        .. attribute:: signaling_protocol
                        
                        	Signaling protocol used to set up this tunnel
                        	**type**\:  :py:class:`PATHSETUPPROTOCOL <ydk.models.openconfig.openconfig_mpls_types.PATHSETUPPROTOCOL>`
                        
                        	**config**\: False
                        
                        .. attribute:: description
                        
                        	optional text description for the tunnel
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: admin_status
                        
                        	TE tunnel administrative state
                        	**type**\:  :py:class:`TUNNELADMINSTATUS <ydk.models.openconfig.openconfig_mpls_types.TUNNELADMINSTATUS>`
                        
                        	**config**\: False
                        
                        	**default value**\: oc-mplst:ADMIN_UP
                        
                        .. attribute:: preference
                        
                        	Specifies a preference for this tunnel. A lower number signifies a better preference
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**config**\: False
                        
                        .. attribute:: metric_type
                        
                        	The type of metric specification that should be used to set the LSP(s) metric
                        	**type**\:  :py:class:`LSPMETRICTYPE <ydk.models.openconfig.openconfig_mpls_types.LSPMETRICTYPE>`
                        
                        	**config**\: False
                        
                        	**default value**\: oc-mplst:LSP_METRIC_INHERITED
                        
                        .. attribute:: metric
                        
                        	The value of the metric that should be specified. The value supplied in this leaf is used in conjunction with the metric type to determine the value of the metric used by the system. Where the metric\-type is set to LSP\_METRIC\_ABSOLUTE \- the value of this leaf is used directly; where it is set to LSP\_METRIC\_RELATIVE, the relevant (positive or negative) offset is used to formulate the metric; where metric\-type is LSP\_METRIC\_INHERITED, the value of this leaf is not utilised
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**config**\: False
                        
                        .. attribute:: shortcut_eligible
                        
                        	Whether this LSP is considered to be eligible for us as a shortcut in the IGP. In the case that this leaf is set to true, the IGP SPF calculation uses the metric specified to determine whether traffic should be carried over this LSP
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: true
                        
                        .. attribute:: protection_style_requested
                        
                        	style of mpls frr protection desired\: can be link, link\-node or unprotected
                        	**type**\:  :py:class:`PROTECTIONTYPE <ydk.models.openconfig.openconfig_mpls_types.PROTECTIONTYPE>`
                        
                        	**config**\: False
                        
                        	**default value**\: oc-mplst:UNPROTECTED
                        
                        .. attribute:: reoptimize_timer
                        
                        	frequency of reoptimization of a traffic engineered LSP
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**units**\: seconds
                        
                        .. attribute:: source
                        
                        	RSVP\-TE tunnel source address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: soft_preemption
                        
                        	Enables RSVP soft\-preemption on this LSP
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        	**default value**\: false
                        
                        .. attribute:: setup_priority
                        
                        	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        	**config**\: False
                        
                        	**default value**\: 7
                        
                        .. attribute:: hold_priority
                        
                        	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: oper_status
                        
                        	The operational status of the TE tunnel
                        	**type**\:  :py:class:`LSPOPERSTATUS <ydk.models.openconfig.openconfig_mpls_types.LSPOPERSTATUS>`
                        
                        	**config**\: False
                        
                        .. attribute:: role
                        
                        	The lsp role at the current node, whether it is headend, transit or tailend
                        	**type**\:  :py:class:`LSPROLE <ydk.models.openconfig.openconfig_mpls_types.LSPROLE>`
                        
                        	**config**\: False
                        
                        .. attribute:: counters
                        
                        	State data for MPLS label switched paths. This state data is specific to a single label switched path
                        	**type**\:  :py:class:`Counters <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State.Counters>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("counters", ("counters", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State.Counters))])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.openconfig.openconfig_mpls_types', 'TUNNELTYPE')])),
                                ('signaling_protocol', (YLeaf(YType.identityref, 'signaling-protocol'), [('ydk.models.openconfig.openconfig_mpls_types', 'PATHSETUPPROTOCOL')])),
                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ('admin_status', (YLeaf(YType.identityref, 'admin-status'), [('ydk.models.openconfig.openconfig_mpls_types', 'TUNNELADMINSTATUS')])),
                                ('preference', (YLeaf(YType.uint8, 'preference'), ['int'])),
                                ('metric_type', (YLeaf(YType.identityref, 'metric-type'), [('ydk.models.openconfig.openconfig_mpls_types', 'LSPMETRICTYPE')])),
                                ('metric', (YLeaf(YType.int32, 'metric'), ['int'])),
                                ('shortcut_eligible', (YLeaf(YType.boolean, 'shortcut-eligible'), ['bool'])),
                                ('protection_style_requested', (YLeaf(YType.identityref, 'protection-style-requested'), [('ydk.models.openconfig.openconfig_mpls_types', 'PROTECTIONTYPE')])),
                                ('reoptimize_timer', (YLeaf(YType.uint16, 'reoptimize-timer'), ['int'])),
                                ('source', (YLeaf(YType.str, 'source'), ['str','str'])),
                                ('soft_preemption', (YLeaf(YType.boolean, 'soft-preemption'), ['bool'])),
                                ('setup_priority', (YLeaf(YType.uint8, 'setup-priority'), ['int'])),
                                ('hold_priority', (YLeaf(YType.uint8, 'hold-priority'), ['int'])),
                                ('oper_status', (YLeaf(YType.identityref, 'oper-status'), [('ydk.models.openconfig.openconfig_mpls_types', 'LSPOPERSTATUS')])),
                                ('role', (YLeaf(YType.identityref, 'role'), [('ydk.models.openconfig.openconfig_mpls_types', 'LSPROLE')])),
                            ])
                            self.name = None
                            self.type = None
                            self.signaling_protocol = None
                            self.description = None
                            self.admin_status = None
                            self.preference = None
                            self.metric_type = None
                            self.metric = None
                            self.shortcut_eligible = None
                            self.protection_style_requested = None
                            self.reoptimize_timer = None
                            self.source = None
                            self.soft_preemption = None
                            self.setup_priority = None
                            self.hold_priority = None
                            self.oper_status = None
                            self.role = None

                            self.counters = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State.Counters()
                            self.counters.parent = self
                            self._children_name_map["counters"] = "counters"
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State, ['name', 'type', 'signaling_protocol', 'description', 'admin_status', 'preference', 'metric_type', 'metric', 'shortcut_eligible', 'protection_style_requested', 'reoptimize_timer', 'source', 'soft_preemption', 'setup_priority', 'hold_priority', 'oper_status', 'role'], name, value)


                        class Counters(_Entity_):
                            """
                            State data for MPLS label switched paths. This state
                            data is specific to a single label switched path.
                            
                            .. attribute:: bytes
                            
                            	Number of bytes that have been forwarded over the label switched path
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: packets
                            
                            	Number of pacets that have been forwarded over the label switched path
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: path_changes
                            
                            	Number of path changes for the label switched path
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: state_changes
                            
                            	Number of state changes for the label switched path
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: online_time
                            
                            	Indication of the time the label switched path transitioned to an Oper Up or in\-service state
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9]{4}\\\-[0\-9]{2}\\\-[0\-9]{2}T[0\-9]{2}\:[0\-9]{2}\:[0\-9]{2}(\\.[0\-9]+)?Z[+\-][0\-9]{2}\:[0\-9]{2}$
                            
                            	**config**\: False
                            
                            .. attribute:: current_path_time
                            
                            	Indicates the time the LSP switched onto its current path. This is reset upon a LSP path change
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9]{4}\\\-[0\-9]{2}\\\-[0\-9]{2}T[0\-9]{2}\:[0\-9]{2}\:[0\-9]{2}(\\.[0\-9]+)?Z[+\-][0\-9]{2}\:[0\-9]{2}$
                            
                            	**config**\: False
                            
                            .. attribute:: next_reoptimization_time
                            
                            	Indicates the next scheduled time the LSP will be reoptimized
                            	**type**\: str
                            
                            	**pattern:** ^[0\-9]{4}\\\-[0\-9]{2}\\\-[0\-9]{2}T[0\-9]{2}\:[0\-9]{2}\:[0\-9]{2}(\\.[0\-9]+)?Z[+\-][0\-9]{2}\:[0\-9]{2}$
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State.Counters, self).__init__()

                                self.yang_name = "counters"
                                self.yang_parent_name = "state"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('path_changes', (YLeaf(YType.uint64, 'path-changes'), ['int'])),
                                    ('state_changes', (YLeaf(YType.uint64, 'state-changes'), ['int'])),
                                    ('online_time', (YLeaf(YType.str, 'online-time'), ['str'])),
                                    ('current_path_time', (YLeaf(YType.str, 'current-path-time'), ['str'])),
                                    ('next_reoptimization_time', (YLeaf(YType.str, 'next-reoptimization-time'), ['str'])),
                                ])
                                self.bytes = None
                                self.packets = None
                                self.path_changes = None
                                self.state_changes = None
                                self.online_time = None
                                self.current_path_time = None
                                self.next_reoptimization_time = None
                                self._segment_path = lambda: "counters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.State.Counters, ['bytes', 'packets', 'path_changes', 'state_changes', 'online_time', 'current_path_time', 'next_reoptimization_time'], name, value)




                    class Bandwidth(_Entity_):
                        """
                        Bandwidth configuration for TE LSPs
                        
                        .. attribute:: config
                        
                        	Configuration parameters related to bandwidth on TE tunnels\:
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters related to bandwidth configuration of TE tunnels
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.State>`
                        
                        	**config**\: False
                        
                        .. attribute:: auto_bandwidth
                        
                        	Parameters related to auto\-bandwidth
                        	**type**\:  :py:class:`AutoBandwidth <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth>`
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth, self).__init__()

                            self.yang_name = "bandwidth"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.State)), ("auto-bandwidth", ("auto_bandwidth", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth))])
                            self._leafs = OrderedDict()

                            self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"

                            self.auto_bandwidth = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth()
                            self.auto_bandwidth.parent = self
                            self._children_name_map["auto_bandwidth"] = "auto-bandwidth"
                            self._segment_path = lambda: "bandwidth"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration parameters related to bandwidth on TE
                            tunnels\:
                            
                            .. attribute:: specification_type
                            
                            	The method used for settign the bandwidth, either explicitly specified or configured
                            	**type**\:  :py:class:`TeBandwidthType <ydk.models.openconfig.openconfig_mpls.TeBandwidthType>`
                            
                            	**default value**\: SPECIFIED
                            
                            .. attribute:: set_bandwidth
                            
                            	set bandwidth explicitly, e.g., using offline calculation
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('specification_type', (YLeaf(YType.enumeration, 'specification-type'), [('ydk.models.openconfig.openconfig_mpls', 'TeBandwidthType', '')])),
                                    ('set_bandwidth', (YLeaf(YType.uint64, 'set-bandwidth'), ['int'])),
                                ])
                                self.specification_type = None
                                self.set_bandwidth = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.Config, ['specification_type', 'set_bandwidth'], name, value)



                        class State(_Entity_):
                            """
                            State parameters related to bandwidth
                            configuration of TE tunnels
                            
                            .. attribute:: specification_type
                            
                            	The method used for settign the bandwidth, either explicitly specified or configured
                            	**type**\:  :py:class:`TeBandwidthType <ydk.models.openconfig.openconfig_mpls.TeBandwidthType>`
                            
                            	**config**\: False
                            
                            	**default value**\: SPECIFIED
                            
                            .. attribute:: set_bandwidth
                            
                            	set bandwidth explicitly, e.g., using offline calculation
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: signaled_bandwidth
                            
                            	The currently signaled bandwidth of the LSP. In the case where the bandwidth is specified explicitly, then this will match the value of the set\-bandwidth leaf; in cases where the bandwidth is dynamically computed by the system, the current value of the bandwidth should be reflected
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('specification_type', (YLeaf(YType.enumeration, 'specification-type'), [('ydk.models.openconfig.openconfig_mpls', 'TeBandwidthType', '')])),
                                    ('set_bandwidth', (YLeaf(YType.uint64, 'set-bandwidth'), ['int'])),
                                    ('signaled_bandwidth', (YLeaf(YType.uint64, 'signaled-bandwidth'), ['int'])),
                                ])
                                self.specification_type = None
                                self.set_bandwidth = None
                                self.signaled_bandwidth = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.State, ['specification_type', 'set_bandwidth', 'signaled_bandwidth'], name, value)



                        class AutoBandwidth(_Entity_):
                            """
                            Parameters related to auto\-bandwidth
                            
                            .. attribute:: config
                            
                            	Configuration parameters relating to MPLS auto\-bandwidth on the tunnel
                            	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Config>`
                            
                            .. attribute:: state
                            
                            	State parameters relating to MPLS auto\-bandwidth on the tunnel
                            	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.State>`
                            
                            	**config**\: False
                            
                            .. attribute:: overflow
                            
                            	configuration of MPLS overflow bandwidth adjustement for the LSP
                            	**type**\:  :py:class:`Overflow <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow>`
                            
                            .. attribute:: underflow
                            
                            	configuration of MPLS underflow bandwidth adjustement for the LSP
                            	**type**\:  :py:class:`Underflow <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow>`
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth, self).__init__()

                                self.yang_name = "auto-bandwidth"
                                self.yang_parent_name = "bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.State)), ("overflow", ("overflow", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow)), ("underflow", ("underflow", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow))])
                                self._leafs = OrderedDict()

                                self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Config()
                                self.config.parent = self
                                self._children_name_map["config"] = "config"

                                self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.State()
                                self.state.parent = self
                                self._children_name_map["state"] = "state"

                                self.overflow = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow()
                                self.overflow.parent = self
                                self._children_name_map["overflow"] = "overflow"

                                self.underflow = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow()
                                self.underflow.parent = self
                                self._children_name_map["underflow"] = "underflow"
                                self._segment_path = lambda: "auto-bandwidth"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth, [], name, value)


                            class Config(_Entity_):
                                """
                                Configuration parameters relating to MPLS
                                auto\-bandwidth on the tunnel.
                                
                                .. attribute:: enabled
                                
                                	enables mpls auto\-bandwidth on the lsp
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: min_bw
                                
                                	set the minimum bandwidth in Kbps for an auto\-bandwidth LSP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: max_bw
                                
                                	set the maximum bandwidth in Kbps for an auto\-bandwidth LSP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: adjust_interval
                                
                                	time in seconds between adjustments to LSP bandwidth
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: adjust_threshold
                                
                                	percentage difference between the LSP's specified bandwidth and its current bandwidth allocation \-\- if the difference is greater than the specified percentage, auto\-bandwidth adjustment is triggered
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Config, self).__init__()

                                    self.yang_name = "config"
                                    self.yang_parent_name = "auto-bandwidth"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                        ('min_bw', (YLeaf(YType.uint64, 'min-bw'), ['int'])),
                                        ('max_bw', (YLeaf(YType.uint64, 'max-bw'), ['int'])),
                                        ('adjust_interval', (YLeaf(YType.uint32, 'adjust-interval'), ['int'])),
                                        ('adjust_threshold', (YLeaf(YType.uint8, 'adjust-threshold'), ['int'])),
                                    ])
                                    self.enabled = None
                                    self.min_bw = None
                                    self.max_bw = None
                                    self.adjust_interval = None
                                    self.adjust_threshold = None
                                    self._segment_path = lambda: "config"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Config, ['enabled', 'min_bw', 'max_bw', 'adjust_interval', 'adjust_threshold'], name, value)



                            class State(_Entity_):
                                """
                                State parameters relating to MPLS
                                auto\-bandwidth on the tunnel.
                                
                                .. attribute:: enabled
                                
                                	enables mpls auto\-bandwidth on the lsp
                                	**type**\: bool
                                
                                	**config**\: False
                                
                                	**default value**\: false
                                
                                .. attribute:: min_bw
                                
                                	set the minimum bandwidth in Kbps for an auto\-bandwidth LSP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: max_bw
                                
                                	set the maximum bandwidth in Kbps for an auto\-bandwidth LSP
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: adjust_interval
                                
                                	time in seconds between adjustments to LSP bandwidth
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                .. attribute:: adjust_threshold
                                
                                	percentage difference between the LSP's specified bandwidth and its current bandwidth allocation \-\- if the difference is greater than the specified percentage, auto\-bandwidth adjustment is triggered
                                	**type**\: int
                                
                                	**range:** 0..100
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.State, self).__init__()

                                    self.yang_name = "state"
                                    self.yang_parent_name = "auto-bandwidth"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                        ('min_bw', (YLeaf(YType.uint64, 'min-bw'), ['int'])),
                                        ('max_bw', (YLeaf(YType.uint64, 'max-bw'), ['int'])),
                                        ('adjust_interval', (YLeaf(YType.uint32, 'adjust-interval'), ['int'])),
                                        ('adjust_threshold', (YLeaf(YType.uint8, 'adjust-threshold'), ['int'])),
                                    ])
                                    self.enabled = None
                                    self.min_bw = None
                                    self.max_bw = None
                                    self.adjust_interval = None
                                    self.adjust_threshold = None
                                    self._segment_path = lambda: "state"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.State, ['enabled', 'min_bw', 'max_bw', 'adjust_interval', 'adjust_threshold'], name, value)



                            class Overflow(_Entity_):
                                """
                                configuration of MPLS overflow bandwidth
                                adjustement for the LSP
                                
                                .. attribute:: config
                                
                                	Config information for MPLS overflow bandwidth adjustment
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config>`
                                
                                .. attribute:: state
                                
                                	Config information for MPLS overflow bandwidth adjustment
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.State>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow, self).__init__()

                                    self.yang_name = "overflow"
                                    self.yang_parent_name = "auto-bandwidth"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.State))])
                                    self._leafs = OrderedDict()

                                    self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"

                                    self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._segment_path = lambda: "overflow"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow, [], name, value)


                                class Config(_Entity_):
                                    """
                                    Config information for MPLS overflow bandwidth
                                    adjustment
                                    
                                    .. attribute:: enabled
                                    
                                    	enables mpls lsp bandwidth overflow adjustment on the lsp
                                    	**type**\: bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: overflow_threshold
                                    
                                    	bandwidth percentage change to trigger an overflow event
                                    	**type**\: int
                                    
                                    	**range:** 0..100
                                    
                                    .. attribute:: trigger_event_count
                                    
                                    	number of consecutive overflow sample events needed to trigger an overflow adjustment
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "overflow"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                            ('overflow_threshold', (YLeaf(YType.uint8, 'overflow-threshold'), ['int'])),
                                            ('trigger_event_count', (YLeaf(YType.uint16, 'trigger-event-count'), ['int'])),
                                        ])
                                        self.enabled = None
                                        self.overflow_threshold = None
                                        self.trigger_event_count = None
                                        self._segment_path = lambda: "config"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config, ['enabled', 'overflow_threshold', 'trigger_event_count'], name, value)



                                class State(_Entity_):
                                    """
                                    Config information for MPLS overflow bandwidth
                                    adjustment
                                    
                                    .. attribute:: enabled
                                    
                                    	enables mpls lsp bandwidth overflow adjustment on the lsp
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: overflow_threshold
                                    
                                    	bandwidth percentage change to trigger an overflow event
                                    	**type**\: int
                                    
                                    	**range:** 0..100
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: trigger_event_count
                                    
                                    	number of consecutive overflow sample events needed to trigger an overflow adjustment
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "overflow"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                            ('overflow_threshold', (YLeaf(YType.uint8, 'overflow-threshold'), ['int'])),
                                            ('trigger_event_count', (YLeaf(YType.uint16, 'trigger-event-count'), ['int'])),
                                        ])
                                        self.enabled = None
                                        self.overflow_threshold = None
                                        self.trigger_event_count = None
                                        self._segment_path = lambda: "state"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Overflow.State, ['enabled', 'overflow_threshold', 'trigger_event_count'], name, value)




                            class Underflow(_Entity_):
                                """
                                configuration of MPLS underflow bandwidth
                                adjustement for the LSP
                                
                                .. attribute:: config
                                
                                	Config information for MPLS underflow bandwidth adjustment
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config>`
                                
                                .. attribute:: state
                                
                                	State information for MPLS underflow bandwidth adjustment
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.State>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow, self).__init__()

                                    self.yang_name = "underflow"
                                    self.yang_parent_name = "auto-bandwidth"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.State))])
                                    self._leafs = OrderedDict()

                                    self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"

                                    self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"
                                    self._segment_path = lambda: "underflow"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow, [], name, value)


                                class Config(_Entity_):
                                    """
                                    Config information for MPLS underflow bandwidth
                                    adjustment
                                    
                                    .. attribute:: enabled
                                    
                                    	enables bandwidth underflow adjustment on the lsp
                                    	**type**\: bool
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: underflow_threshold
                                    
                                    	bandwidth percentage change to trigger and underflow event
                                    	**type**\: int
                                    
                                    	**range:** 0..100
                                    
                                    .. attribute:: trigger_event_count
                                    
                                    	number of consecutive underflow sample events needed to trigger an underflow adjustment
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "underflow"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                            ('underflow_threshold', (YLeaf(YType.uint8, 'underflow-threshold'), ['int'])),
                                            ('trigger_event_count', (YLeaf(YType.uint16, 'trigger-event-count'), ['int'])),
                                        ])
                                        self.enabled = None
                                        self.underflow_threshold = None
                                        self.trigger_event_count = None
                                        self._segment_path = lambda: "config"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config, ['enabled', 'underflow_threshold', 'trigger_event_count'], name, value)



                                class State(_Entity_):
                                    """
                                    State information for MPLS underflow bandwidth
                                    adjustment
                                    
                                    .. attribute:: enabled
                                    
                                    	enables bandwidth underflow adjustment on the lsp
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    	**default value**\: false
                                    
                                    .. attribute:: underflow_threshold
                                    
                                    	bandwidth percentage change to trigger and underflow event
                                    	**type**\: int
                                    
                                    	**range:** 0..100
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: trigger_event_count
                                    
                                    	number of consecutive underflow sample events needed to trigger an underflow adjustment
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "underflow"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                            ('underflow_threshold', (YLeaf(YType.uint8, 'underflow-threshold'), ['int'])),
                                            ('trigger_event_count', (YLeaf(YType.uint16, 'trigger-event-count'), ['int'])),
                                        ])
                                        self.enabled = None
                                        self.underflow_threshold = None
                                        self.trigger_event_count = None
                                        self._segment_path = lambda: "state"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.Bandwidth.AutoBandwidth.Underflow.State, ['enabled', 'underflow_threshold', 'trigger_event_count'], name, value)






                    class P2pTunnelAttributes(_Entity_):
                        """
                        Parameters related to LSPs of type P2P
                        
                        .. attribute:: config
                        
                        	Configuration parameters for P2P LSPs
                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.Config>`
                        
                        .. attribute:: state
                        
                        	State parameters for P2P LSPs
                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.State>`
                        
                        	**config**\: False
                        
                        .. attribute:: p2p_primary_path
                        
                        	Primary paths associated with the LSP
                        	**type**\:  :py:class:`P2pPrimaryPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath>`
                        
                        .. attribute:: p2p_secondary_paths
                        
                        	Secondary paths for the LSP
                        	**type**\:  :py:class:`P2pSecondaryPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths>`
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes, self).__init__()

                            self.yang_name = "p2p-tunnel-attributes"
                            self.yang_parent_name = "tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.State)), ("p2p-primary-path", ("p2p_primary_path", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath)), ("p2p-secondary-paths", ("p2p_secondary_paths", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths))])
                            self._leafs = OrderedDict()

                            self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"

                            self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.State()
                            self.state.parent = self
                            self._children_name_map["state"] = "state"

                            self.p2p_primary_path = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath()
                            self.p2p_primary_path.parent = self
                            self._children_name_map["p2p_primary_path"] = "p2p-primary-path"

                            self.p2p_secondary_paths = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths()
                            self.p2p_secondary_paths.parent = self
                            self._children_name_map["p2p_secondary_paths"] = "p2p-secondary-paths"
                            self._segment_path = lambda: "p2p-tunnel-attributes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes, [], name, value)


                        class Config(_Entity_):
                            """
                            Configuration parameters for P2P LSPs
                            
                            .. attribute:: destination
                            
                            	P2P tunnel destination address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "p2p-tunnel-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('destination', (YLeaf(YType.str, 'destination'), ['str','str'])),
                                ])
                                self.destination = None
                                self._segment_path = lambda: "config"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.Config, ['destination'], name, value)



                        class State(_Entity_):
                            """
                            State parameters for P2P LSPs
                            
                            .. attribute:: destination
                            
                            	P2P tunnel destination address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                            
                            		**type**\: str
                            
                            			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.State, self).__init__()

                                self.yang_name = "state"
                                self.yang_parent_name = "p2p-tunnel-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('destination', (YLeaf(YType.str, 'destination'), ['str','str'])),
                                ])
                                self.destination = None
                                self._segment_path = lambda: "state"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.State, ['destination'], name, value)



                        class P2pPrimaryPath(_Entity_):
                            """
                            Primary paths associated with the LSP
                            
                            .. attribute:: p2p_primary_path
                            
                            	List of p2p primary paths for a tunnel
                            	**type**\: list of  		 :py:class:`P2pPrimaryPath_ <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_>`
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath, self).__init__()

                                self.yang_name = "p2p-primary-path"
                                self.yang_parent_name = "p2p-tunnel-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("p2p-primary-path", ("p2p_primary_path", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_))])
                                self._leafs = OrderedDict()

                                self.p2p_primary_path = YList(self)
                                self._segment_path = lambda: "p2p-primary-path"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath, [], name, value)


                            class P2pPrimaryPath_(_Entity_):
                                """
                                List of p2p primary paths for a tunnel
                                
                                .. attribute:: name  (key)
                                
                                	Path name
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.Config>`
                                
                                .. attribute:: config
                                
                                	Configuration parameters related to paths
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.Config>`
                                
                                .. attribute:: state
                                
                                	State parameters related to paths
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.State>`
                                
                                	**config**\: False
                                
                                .. attribute:: candidate_secondary_paths
                                
                                	The set of candidate secondary paths which may be used for this primary path. When secondary paths are specified in the list the path of the secondary LSP in use must be restricted to those path options referenced. The priority of the secondary paths is specified within the list. Higher priority values are less preferred \- that is to say that a path with priority 0 is the most preferred path. In the case that the list is empty, any secondary path option may be utilised when the current primary path is in use
                                	**type**\:  :py:class:`CandidateSecondaryPaths <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths>`
                                
                                .. attribute:: admin_groups
                                
                                	Top\-level container for include/exclude constraints for link affinities
                                	**type**\:  :py:class:`AdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups>`
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_, self).__init__()

                                    self.yang_name = "p2p-primary-path"
                                    self.yang_parent_name = "p2p-primary-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.State)), ("candidate-secondary-paths", ("candidate_secondary_paths", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths)), ("admin-groups", ("admin_groups", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups))])
                                    self._leafs = OrderedDict([
                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ])
                                    self.name = None

                                    self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"

                                    self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"

                                    self.candidate_secondary_paths = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths()
                                    self.candidate_secondary_paths.parent = self
                                    self._children_name_map["candidate_secondary_paths"] = "candidate-secondary-paths"

                                    self.admin_groups = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups()
                                    self.admin_groups.parent = self
                                    self._children_name_map["admin_groups"] = "admin-groups"
                                    self._segment_path = lambda: "p2p-primary-path" + "[name='" + str(self.name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_, ['name'], name, value)


                                class Config(_Entity_):
                                    """
                                    Configuration parameters related to paths
                                    
                                    .. attribute:: name
                                    
                                    	Path name
                                    	**type**\: str
                                    
                                    .. attribute:: path_computation_method
                                    
                                    	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                                    	**type**\:  :py:class:`PATHCOMPUTATIONMETHOD <ydk.models.openconfig.openconfig_mpls_types.PATHCOMPUTATIONMETHOD>`
                                    
                                    	**default value**\: oc-mplst:LOCALLY_COMPUTED
                                    
                                    .. attribute:: use_cspf
                                    
                                    	Flag to enable CSPF for locally computed LSPs
                                    	**type**\: bool
                                    
                                    .. attribute:: cspf_tiebreaker
                                    
                                    	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                                    	**type**\:  :py:class:`CspfTieBreaking <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking>`
                                    
                                    .. attribute:: path_computation_server
                                    
                                    	Address of the external path computation server
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                    
                                    .. attribute:: explicit_path_name
                                    
                                    	reference to a defined path
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config>`
                                    
                                    .. attribute:: preference
                                    
                                    	Specifies a preference for this path. The lower the number higher the preference
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    .. attribute:: setup_priority
                                    
                                    	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**default value**\: 7
                                    
                                    .. attribute:: hold_priority
                                    
                                    	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: retry_timer
                                    
                                    	sets the time between attempts to establish the LSP
                                    	**type**\: int
                                    
                                    	**range:** 1..600
                                    
                                    	**units**\: seconds
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "p2p-primary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('path_computation_method', (YLeaf(YType.identityref, 'path-computation-method'), [('ydk.models.openconfig.openconfig_mpls_types', 'PATHCOMPUTATIONMETHOD')])),
                                            ('use_cspf', (YLeaf(YType.boolean, 'use-cspf'), ['bool'])),
                                            ('cspf_tiebreaker', (YLeaf(YType.enumeration, 'cspf-tiebreaker'), [('ydk.models.openconfig.openconfig_mpls', 'CspfTieBreaking', '')])),
                                            ('path_computation_server', (YLeaf(YType.str, 'path-computation-server'), ['str','str'])),
                                            ('explicit_path_name', (YLeaf(YType.str, 'explicit-path-name'), ['str'])),
                                            ('preference', (YLeaf(YType.uint8, 'preference'), ['int'])),
                                            ('setup_priority', (YLeaf(YType.uint8, 'setup-priority'), ['int'])),
                                            ('hold_priority', (YLeaf(YType.uint8, 'hold-priority'), ['int'])),
                                            ('retry_timer', (YLeaf(YType.uint16, 'retry-timer'), ['int'])),
                                        ])
                                        self.name = None
                                        self.path_computation_method = None
                                        self.use_cspf = None
                                        self.cspf_tiebreaker = None
                                        self.path_computation_server = None
                                        self.explicit_path_name = None
                                        self.preference = None
                                        self.setup_priority = None
                                        self.hold_priority = None
                                        self.retry_timer = None
                                        self._segment_path = lambda: "config"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.Config, ['name', 'path_computation_method', 'use_cspf', 'cspf_tiebreaker', 'path_computation_server', 'explicit_path_name', 'preference', 'setup_priority', 'hold_priority', 'retry_timer'], name, value)



                                class State(_Entity_):
                                    """
                                    State parameters related to paths
                                    
                                    .. attribute:: name
                                    
                                    	Path name
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_computation_method
                                    
                                    	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                                    	**type**\:  :py:class:`PATHCOMPUTATIONMETHOD <ydk.models.openconfig.openconfig_mpls_types.PATHCOMPUTATIONMETHOD>`
                                    
                                    	**config**\: False
                                    
                                    	**default value**\: oc-mplst:LOCALLY_COMPUTED
                                    
                                    .. attribute:: use_cspf
                                    
                                    	Flag to enable CSPF for locally computed LSPs
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cspf_tiebreaker
                                    
                                    	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                                    	**type**\:  :py:class:`CspfTieBreaking <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_computation_server
                                    
                                    	Address of the external path computation server
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: explicit_path_name
                                    
                                    	reference to a defined path
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: preference
                                    
                                    	Specifies a preference for this path. The lower the number higher the preference
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: setup_priority
                                    
                                    	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**config**\: False
                                    
                                    	**default value**\: 7
                                    
                                    .. attribute:: hold_priority
                                    
                                    	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**config**\: False
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: retry_timer
                                    
                                    	sets the time between attempts to establish the LSP
                                    	**type**\: int
                                    
                                    	**range:** 1..600
                                    
                                    	**config**\: False
                                    
                                    	**units**\: seconds
                                    
                                    .. attribute:: associated_rsvp_session
                                    
                                    	If the signalling protocol specified for this path is RSVP\-TE, this leaf provides a reference to the associated session within the RSVP\-TE protocol sessions list, such that details of the signaling can be retrieved
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**refers to**\:  :py:class:`local_index <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "p2p-primary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('path_computation_method', (YLeaf(YType.identityref, 'path-computation-method'), [('ydk.models.openconfig.openconfig_mpls_types', 'PATHCOMPUTATIONMETHOD')])),
                                            ('use_cspf', (YLeaf(YType.boolean, 'use-cspf'), ['bool'])),
                                            ('cspf_tiebreaker', (YLeaf(YType.enumeration, 'cspf-tiebreaker'), [('ydk.models.openconfig.openconfig_mpls', 'CspfTieBreaking', '')])),
                                            ('path_computation_server', (YLeaf(YType.str, 'path-computation-server'), ['str','str'])),
                                            ('explicit_path_name', (YLeaf(YType.str, 'explicit-path-name'), ['str'])),
                                            ('preference', (YLeaf(YType.uint8, 'preference'), ['int'])),
                                            ('setup_priority', (YLeaf(YType.uint8, 'setup-priority'), ['int'])),
                                            ('hold_priority', (YLeaf(YType.uint8, 'hold-priority'), ['int'])),
                                            ('retry_timer', (YLeaf(YType.uint16, 'retry-timer'), ['int'])),
                                            ('associated_rsvp_session', (YLeaf(YType.str, 'associated-rsvp-session'), ['int'])),
                                        ])
                                        self.name = None
                                        self.path_computation_method = None
                                        self.use_cspf = None
                                        self.cspf_tiebreaker = None
                                        self.path_computation_server = None
                                        self.explicit_path_name = None
                                        self.preference = None
                                        self.setup_priority = None
                                        self.hold_priority = None
                                        self.retry_timer = None
                                        self.associated_rsvp_session = None
                                        self._segment_path = lambda: "state"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.State, ['name', 'path_computation_method', 'use_cspf', 'cspf_tiebreaker', 'path_computation_server', 'explicit_path_name', 'preference', 'setup_priority', 'hold_priority', 'retry_timer', 'associated_rsvp_session'], name, value)



                                class CandidateSecondaryPaths(_Entity_):
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
                                    	**type**\: list of  		 :py:class:`CandidateSecondaryPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath>`
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths, self).__init__()

                                        self.yang_name = "candidate-secondary-paths"
                                        self.yang_parent_name = "p2p-primary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("candidate-secondary-path", ("candidate_secondary_path", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath))])
                                        self._leafs = OrderedDict()

                                        self.candidate_secondary_path = YList(self)
                                        self._segment_path = lambda: "candidate-secondary-paths"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths, [], name, value)


                                    class CandidateSecondaryPath(_Entity_):
                                        """
                                        List of secondary paths which may be utilised when the
                                        current primary path is in use
                                        
                                        .. attribute:: secondary_path  (key)
                                        
                                        	A reference to the secondary path option reference which acts as the key of the candidate\-secondary\-path list
                                        	**type**\: str
                                        
                                        	**refers to**\:  :py:class:`secondary_path <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.Config>`
                                        
                                        .. attribute:: config
                                        
                                        	Configuration parameters relating to the candidate secondary path
                                        	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.Config>`
                                        
                                        .. attribute:: state
                                        
                                        	Operational state parameters relating to the candidate secondary path
                                        	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.State>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'oc-mpls'
                                        _revision = '2017-03-22'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath, self).__init__()

                                            self.yang_name = "candidate-secondary-path"
                                            self.yang_parent_name = "candidate-secondary-paths"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['secondary_path']
                                            self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.State))])
                                            self._leafs = OrderedDict([
                                                ('secondary_path', (YLeaf(YType.str, 'secondary-path'), ['str'])),
                                            ])
                                            self.secondary_path = None

                                            self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.Config()
                                            self.config.parent = self
                                            self._children_name_map["config"] = "config"

                                            self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.State()
                                            self.state.parent = self
                                            self._children_name_map["state"] = "state"
                                            self._segment_path = lambda: "candidate-secondary-path" + "[secondary-path='" + str(self.secondary_path) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath, ['secondary_path'], name, value)


                                        class Config(_Entity_):
                                            """
                                            Configuration parameters relating to the candidate
                                            secondary path
                                            
                                            .. attribute:: secondary_path
                                            
                                            	A reference to the secondary path that should be utilised when the containing primary path option is in use
                                            	**type**\: str
                                            
                                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.Config>`
                                            
                                            .. attribute:: priority
                                            
                                            	The priority of the specified secondary path option. Higher priority options are less preferable \- such that a secondary path reference with a priority of 0 is the most preferred
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            

                                            """

                                            _prefix = 'oc-mpls'
                                            _revision = '2017-03-22'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.Config, self).__init__()

                                                self.yang_name = "config"
                                                self.yang_parent_name = "candidate-secondary-path"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('secondary_path', (YLeaf(YType.str, 'secondary-path'), ['str'])),
                                                    ('priority', (YLeaf(YType.uint16, 'priority'), ['int'])),
                                                ])
                                                self.secondary_path = None
                                                self.priority = None
                                                self._segment_path = lambda: "config"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.Config, ['secondary_path', 'priority'], name, value)



                                        class State(_Entity_):
                                            """
                                            Operational state parameters relating to the candidate
                                            secondary path
                                            
                                            .. attribute:: secondary_path
                                            
                                            	A reference to the secondary path that should be utilised when the containing primary path option is in use
                                            	**type**\: str
                                            
                                            	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.Config>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: priority
                                            
                                            	The priority of the specified secondary path option. Higher priority options are less preferable \- such that a secondary path reference with a priority of 0 is the most preferred
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: active
                                            
                                            	Indicates the current active path option that has been selected of the candidate secondary paths
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'oc-mpls'
                                            _revision = '2017-03-22'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.State, self).__init__()

                                                self.yang_name = "state"
                                                self.yang_parent_name = "candidate-secondary-path"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('secondary_path', (YLeaf(YType.str, 'secondary-path'), ['str'])),
                                                    ('priority', (YLeaf(YType.uint16, 'priority'), ['int'])),
                                                    ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                                                ])
                                                self.secondary_path = None
                                                self.priority = None
                                                self.active = None
                                                self._segment_path = lambda: "state"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.CandidateSecondaryPaths.CandidateSecondaryPath.State, ['secondary_path', 'priority', 'active'], name, value)





                                class AdminGroups(_Entity_):
                                    """
                                    Top\-level container for include/exclude constraints for
                                    link affinities
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data 
                                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data 
                                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.State>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups, self).__init__()

                                        self.yang_name = "admin-groups"
                                        self.yang_parent_name = "p2p-primary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.State))])
                                        self._leafs = OrderedDict()

                                        self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"

                                        self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._segment_path = lambda: "admin-groups"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups, [], name, value)


                                    class Config(_Entity_):
                                        """
                                        Configuration data 
                                        
                                        .. attribute:: exclude_group
                                        
                                        	list of references to named admin\-groups to exclude in path calculation
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        .. attribute:: include_all_group
                                        
                                        	list of references to named admin\-groups of which all must be included
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        .. attribute:: include_any_group
                                        
                                        	list of references to named admin\-groups of which one must be included
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        

                                        """

                                        _prefix = 'oc-mpls'
                                        _revision = '2017-03-22'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "admin-groups"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('exclude_group', (YLeafList(YType.str, 'exclude-group'), ['str'])),
                                                ('include_all_group', (YLeafList(YType.str, 'include-all-group'), ['str'])),
                                                ('include_any_group', (YLeafList(YType.str, 'include-any-group'), ['str'])),
                                            ])
                                            self.exclude_group = []
                                            self.include_all_group = []
                                            self.include_any_group = []
                                            self._segment_path = lambda: "config"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.Config, ['exclude_group', 'include_all_group', 'include_any_group'], name, value)



                                    class State(_Entity_):
                                        """
                                        Operational state data 
                                        
                                        .. attribute:: exclude_group
                                        
                                        	list of references to named admin\-groups to exclude in path calculation
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: include_all_group
                                        
                                        	list of references to named admin\-groups of which all must be included
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: include_any_group
                                        
                                        	list of references to named admin\-groups of which one must be included
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'oc-mpls'
                                        _revision = '2017-03-22'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "admin-groups"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('exclude_group', (YLeafList(YType.str, 'exclude-group'), ['str'])),
                                                ('include_all_group', (YLeafList(YType.str, 'include-all-group'), ['str'])),
                                                ('include_any_group', (YLeafList(YType.str, 'include-any-group'), ['str'])),
                                            ])
                                            self.exclude_group = []
                                            self.include_all_group = []
                                            self.include_any_group = []
                                            self._segment_path = lambda: "state"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pPrimaryPath.P2pPrimaryPath_.AdminGroups.State, ['exclude_group', 'include_all_group', 'include_any_group'], name, value)






                        class P2pSecondaryPaths(_Entity_):
                            """
                            Secondary paths for the LSP
                            
                            .. attribute:: p2p_secondary_path
                            
                            	List of p2p primary paths for a tunnel
                            	**type**\: list of  		 :py:class:`P2pSecondaryPath <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath>`
                            
                            

                            """

                            _prefix = 'oc-mpls'
                            _revision = '2017-03-22'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths, self).__init__()

                                self.yang_name = "p2p-secondary-paths"
                                self.yang_parent_name = "p2p-tunnel-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("p2p-secondary-path", ("p2p_secondary_path", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath))])
                                self._leafs = OrderedDict()

                                self.p2p_secondary_path = YList(self)
                                self._segment_path = lambda: "p2p-secondary-paths"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths, [], name, value)


                            class P2pSecondaryPath(_Entity_):
                                """
                                List of p2p primary paths for a tunnel
                                
                                .. attribute:: name  (key)
                                
                                	Path name
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.Config>`
                                
                                .. attribute:: config
                                
                                	Configuration parameters related to paths
                                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.Config>`
                                
                                .. attribute:: state
                                
                                	State parameters related to paths
                                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.State>`
                                
                                	**config**\: False
                                
                                .. attribute:: admin_groups
                                
                                	Top\-level container for include/exclude constraints for link affinities
                                	**type**\:  :py:class:`AdminGroups <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups>`
                                
                                

                                """

                                _prefix = 'oc-mpls'
                                _revision = '2017-03-22'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath, self).__init__()

                                    self.yang_name = "p2p-secondary-path"
                                    self.yang_parent_name = "p2p-secondary-paths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.State)), ("admin-groups", ("admin_groups", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups))])
                                    self._leafs = OrderedDict([
                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ])
                                    self.name = None

                                    self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.Config()
                                    self.config.parent = self
                                    self._children_name_map["config"] = "config"

                                    self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.State()
                                    self.state.parent = self
                                    self._children_name_map["state"] = "state"

                                    self.admin_groups = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups()
                                    self.admin_groups.parent = self
                                    self._children_name_map["admin_groups"] = "admin-groups"
                                    self._segment_path = lambda: "p2p-secondary-path" + "[name='" + str(self.name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath, ['name'], name, value)


                                class Config(_Entity_):
                                    """
                                    Configuration parameters related to paths
                                    
                                    .. attribute:: name
                                    
                                    	Path name
                                    	**type**\: str
                                    
                                    .. attribute:: path_computation_method
                                    
                                    	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                                    	**type**\:  :py:class:`PATHCOMPUTATIONMETHOD <ydk.models.openconfig.openconfig_mpls_types.PATHCOMPUTATIONMETHOD>`
                                    
                                    	**default value**\: oc-mplst:LOCALLY_COMPUTED
                                    
                                    .. attribute:: use_cspf
                                    
                                    	Flag to enable CSPF for locally computed LSPs
                                    	**type**\: bool
                                    
                                    .. attribute:: cspf_tiebreaker
                                    
                                    	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                                    	**type**\:  :py:class:`CspfTieBreaking <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking>`
                                    
                                    .. attribute:: path_computation_server
                                    
                                    	Address of the external path computation server
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                    
                                    .. attribute:: explicit_path_name
                                    
                                    	reference to a defined path
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config>`
                                    
                                    .. attribute:: preference
                                    
                                    	Specifies a preference for this path. The lower the number higher the preference
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    .. attribute:: setup_priority
                                    
                                    	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**default value**\: 7
                                    
                                    .. attribute:: hold_priority
                                    
                                    	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: retry_timer
                                    
                                    	sets the time between attempts to establish the LSP
                                    	**type**\: int
                                    
                                    	**range:** 1..600
                                    
                                    	**units**\: seconds
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.Config, self).__init__()

                                        self.yang_name = "config"
                                        self.yang_parent_name = "p2p-secondary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('path_computation_method', (YLeaf(YType.identityref, 'path-computation-method'), [('ydk.models.openconfig.openconfig_mpls_types', 'PATHCOMPUTATIONMETHOD')])),
                                            ('use_cspf', (YLeaf(YType.boolean, 'use-cspf'), ['bool'])),
                                            ('cspf_tiebreaker', (YLeaf(YType.enumeration, 'cspf-tiebreaker'), [('ydk.models.openconfig.openconfig_mpls', 'CspfTieBreaking', '')])),
                                            ('path_computation_server', (YLeaf(YType.str, 'path-computation-server'), ['str','str'])),
                                            ('explicit_path_name', (YLeaf(YType.str, 'explicit-path-name'), ['str'])),
                                            ('preference', (YLeaf(YType.uint8, 'preference'), ['int'])),
                                            ('setup_priority', (YLeaf(YType.uint8, 'setup-priority'), ['int'])),
                                            ('hold_priority', (YLeaf(YType.uint8, 'hold-priority'), ['int'])),
                                            ('retry_timer', (YLeaf(YType.uint16, 'retry-timer'), ['int'])),
                                        ])
                                        self.name = None
                                        self.path_computation_method = None
                                        self.use_cspf = None
                                        self.cspf_tiebreaker = None
                                        self.path_computation_server = None
                                        self.explicit_path_name = None
                                        self.preference = None
                                        self.setup_priority = None
                                        self.hold_priority = None
                                        self.retry_timer = None
                                        self._segment_path = lambda: "config"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.Config, ['name', 'path_computation_method', 'use_cspf', 'cspf_tiebreaker', 'path_computation_server', 'explicit_path_name', 'preference', 'setup_priority', 'hold_priority', 'retry_timer'], name, value)



                                class State(_Entity_):
                                    """
                                    State parameters related to paths
                                    
                                    .. attribute:: name
                                    
                                    	Path name
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_computation_method
                                    
                                    	The method used for computing the path, either locally computed, queried from a server or not computed at all (explicitly configured)
                                    	**type**\:  :py:class:`PATHCOMPUTATIONMETHOD <ydk.models.openconfig.openconfig_mpls_types.PATHCOMPUTATIONMETHOD>`
                                    
                                    	**config**\: False
                                    
                                    	**default value**\: oc-mplst:LOCALLY_COMPUTED
                                    
                                    .. attribute:: use_cspf
                                    
                                    	Flag to enable CSPF for locally computed LSPs
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: cspf_tiebreaker
                                    
                                    	Determine the tie\-breaking method to choose between equally desirable paths during CSFP computation
                                    	**type**\:  :py:class:`CspfTieBreaking <ydk.models.openconfig.openconfig_mpls.CspfTieBreaking>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: path_computation_server
                                    
                                    	Address of the external path computation server
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: explicit_path_name
                                    
                                    	reference to a defined path
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.NamedExplicitPath.Config>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: preference
                                    
                                    	Specifies a preference for this path. The lower the number higher the preference
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: setup_priority
                                    
                                    	RSVP\-TE preemption priority during LSP setup, lower is higher priority; default 7 indicates that LSP will not preempt established LSPs during setup
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**config**\: False
                                    
                                    	**default value**\: 7
                                    
                                    .. attribute:: hold_priority
                                    
                                    	preemption priority once the LSP is established, lower is higher priority; default 0 indicates other LSPs will not preempt the LSPs once established
                                    	**type**\: int
                                    
                                    	**range:** 0..7
                                    
                                    	**config**\: False
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: retry_timer
                                    
                                    	sets the time between attempts to establish the LSP
                                    	**type**\: int
                                    
                                    	**range:** 1..600
                                    
                                    	**config**\: False
                                    
                                    	**units**\: seconds
                                    
                                    .. attribute:: associated_rsvp_session
                                    
                                    	If the signalling protocol specified for this path is RSVP\-TE, this leaf provides a reference to the associated session within the RSVP\-TE protocol sessions list, such that details of the signaling can be retrieved
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**refers to**\:  :py:class:`local_index <ydk.models.openconfig.openconfig_mpls.Mpls.SignalingProtocols.RsvpTe.Sessions.Session>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "p2p-secondary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('path_computation_method', (YLeaf(YType.identityref, 'path-computation-method'), [('ydk.models.openconfig.openconfig_mpls_types', 'PATHCOMPUTATIONMETHOD')])),
                                            ('use_cspf', (YLeaf(YType.boolean, 'use-cspf'), ['bool'])),
                                            ('cspf_tiebreaker', (YLeaf(YType.enumeration, 'cspf-tiebreaker'), [('ydk.models.openconfig.openconfig_mpls', 'CspfTieBreaking', '')])),
                                            ('path_computation_server', (YLeaf(YType.str, 'path-computation-server'), ['str','str'])),
                                            ('explicit_path_name', (YLeaf(YType.str, 'explicit-path-name'), ['str'])),
                                            ('preference', (YLeaf(YType.uint8, 'preference'), ['int'])),
                                            ('setup_priority', (YLeaf(YType.uint8, 'setup-priority'), ['int'])),
                                            ('hold_priority', (YLeaf(YType.uint8, 'hold-priority'), ['int'])),
                                            ('retry_timer', (YLeaf(YType.uint16, 'retry-timer'), ['int'])),
                                            ('associated_rsvp_session', (YLeaf(YType.str, 'associated-rsvp-session'), ['int'])),
                                        ])
                                        self.name = None
                                        self.path_computation_method = None
                                        self.use_cspf = None
                                        self.cspf_tiebreaker = None
                                        self.path_computation_server = None
                                        self.explicit_path_name = None
                                        self.preference = None
                                        self.setup_priority = None
                                        self.hold_priority = None
                                        self.retry_timer = None
                                        self.associated_rsvp_session = None
                                        self._segment_path = lambda: "state"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.State, ['name', 'path_computation_method', 'use_cspf', 'cspf_tiebreaker', 'path_computation_server', 'explicit_path_name', 'preference', 'setup_priority', 'hold_priority', 'retry_timer', 'associated_rsvp_session'], name, value)



                                class AdminGroups(_Entity_):
                                    """
                                    Top\-level container for include/exclude constraints for
                                    link affinities
                                    
                                    .. attribute:: config
                                    
                                    	Configuration data 
                                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.Config>`
                                    
                                    .. attribute:: state
                                    
                                    	Operational state data 
                                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.State>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'oc-mpls'
                                    _revision = '2017-03-22'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups, self).__init__()

                                        self.yang_name = "admin-groups"
                                        self.yang_parent_name = "p2p-secondary-path"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.Config)), ("state", ("state", Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.State))])
                                        self._leafs = OrderedDict()

                                        self.config = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.Config()
                                        self.config.parent = self
                                        self._children_name_map["config"] = "config"

                                        self.state = Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.State()
                                        self.state.parent = self
                                        self._children_name_map["state"] = "state"
                                        self._segment_path = lambda: "admin-groups"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups, [], name, value)


                                    class Config(_Entity_):
                                        """
                                        Configuration data 
                                        
                                        .. attribute:: exclude_group
                                        
                                        	list of references to named admin\-groups to exclude in path calculation
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        .. attribute:: include_all_group
                                        
                                        	list of references to named admin\-groups of which all must be included
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        .. attribute:: include_any_group
                                        
                                        	list of references to named admin\-groups of which one must be included
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        

                                        """

                                        _prefix = 'oc-mpls'
                                        _revision = '2017-03-22'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.Config, self).__init__()

                                            self.yang_name = "config"
                                            self.yang_parent_name = "admin-groups"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('exclude_group', (YLeafList(YType.str, 'exclude-group'), ['str'])),
                                                ('include_all_group', (YLeafList(YType.str, 'include-all-group'), ['str'])),
                                                ('include_any_group', (YLeafList(YType.str, 'include-any-group'), ['str'])),
                                            ])
                                            self.exclude_group = []
                                            self.include_all_group = []
                                            self.include_any_group = []
                                            self._segment_path = lambda: "config"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.Config, ['exclude_group', 'include_all_group', 'include_any_group'], name, value)



                                    class State(_Entity_):
                                        """
                                        Operational state data 
                                        
                                        .. attribute:: exclude_group
                                        
                                        	list of references to named admin\-groups to exclude in path calculation
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: include_all_group
                                        
                                        	list of references to named admin\-groups of which all must be included
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: include_any_group
                                        
                                        	list of references to named admin\-groups of which one must be included
                                        	**type**\: list of str
                                        
                                        	**refers to**\:  :py:class:`admin_group_name <ydk.models.openconfig.openconfig_mpls.Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'oc-mpls'
                                        _revision = '2017-03-22'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.State, self).__init__()

                                            self.yang_name = "state"
                                            self.yang_parent_name = "admin-groups"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('exclude_group', (YLeafList(YType.str, 'exclude-group'), ['str'])),
                                                ('include_all_group', (YLeafList(YType.str, 'include-all-group'), ['str'])),
                                                ('include_any_group', (YLeafList(YType.str, 'include-any-group'), ['str'])),
                                            ])
                                            self.exclude_group = []
                                            self.include_all_group = []
                                            self.include_any_group = []
                                            self._segment_path = lambda: "state"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Mpls.Lsps.ConstrainedPath.Tunnels.Tunnel.P2pTunnelAttributes.P2pSecondaryPaths.P2pSecondaryPath.AdminGroups.State, ['exclude_group', 'include_all_group', 'include_any_group'], name, value)










        class UnconstrainedPath(_Entity_):
            """
            LSPs that use the IGP\-determined path, i.e., non
            traffic\-engineered, or non constrained\-path
            
            .. attribute:: path_setup_protocol
            
            	select and configure the signaling method for  the LSP
            	**type**\:  :py:class:`PathSetupProtocol <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.Lsps.UnconstrainedPath, self).__init__()

                self.yang_name = "unconstrained-path"
                self.yang_parent_name = "lsps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("path-setup-protocol", ("path_setup_protocol", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol))])
                self._leafs = OrderedDict()

                self.path_setup_protocol = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol()
                self.path_setup_protocol.parent = self
                self._children_name_map["path_setup_protocol"] = "path-setup-protocol"
                self._segment_path = lambda: "unconstrained-path"
                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Lsps.UnconstrainedPath, [], name, value)


            class PathSetupProtocol(_Entity_):
                """
                select and configure the signaling method for
                 the LSP
                
                .. attribute:: ldp
                
                	LDP signaling setup for IGP\-congruent LSPs
                	**type**\:  :py:class:`Ldp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp>`
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol, self).__init__()

                    self.yang_name = "path-setup-protocol"
                    self.yang_parent_name = "unconstrained-path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ldp", ("ldp", Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp))])
                    self._leafs = OrderedDict()

                    self.ldp = Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp()
                    self.ldp.parent = self
                    self._children_name_map["ldp"] = "ldp"
                    self._segment_path = lambda: "path-setup-protocol"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol, [], name, value)


                class Ldp(_Entity_):
                    """
                    LDP signaling setup for IGP\-congruent LSPs
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp, self).__init__()

                        self.yang_name = "ldp"
                        self.yang_parent_name = "path-setup-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict()
                        self._segment_path = lambda: "ldp"
                        self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/unconstrained-path/path-setup-protocol/%s" % self._segment_path()
                        self._is_frozen = True





        class StaticLsps(_Entity_):
            """
            statically configured LSPs, without dynamic
            signaling
            
            .. attribute:: static_lsp
            
            	list of defined static LSPs
            	**type**\: list of  		 :py:class:`StaticLsp <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp>`
            
            

            """

            _prefix = 'oc-mpls'
            _revision = '2017-03-22'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Mpls.Lsps.StaticLsps, self).__init__()

                self.yang_name = "static-lsps"
                self.yang_parent_name = "lsps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("static-lsp", ("static_lsp", Mpls.Lsps.StaticLsps.StaticLsp))])
                self._leafs = OrderedDict()

                self.static_lsp = YList(self)
                self._segment_path = lambda: "static-lsps"
                self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Mpls.Lsps.StaticLsps, [], name, value)


            class StaticLsp(_Entity_):
                """
                list of defined static LSPs
                
                .. attribute:: name  (key)
                
                	Reference the name list key
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Config>`
                
                .. attribute:: config
                
                	Configuration data for the static lsp
                	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Config>`
                
                .. attribute:: state
                
                	Operational state data for the static lsp
                	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.State>`
                
                	**config**\: False
                
                .. attribute:: ingress
                
                	Static LSPs for which the router is an  ingress node
                	**type**\:  :py:class:`Ingress <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Ingress>`
                
                .. attribute:: transit
                
                	Static LSPs for which the router is an  transit node
                	**type**\:  :py:class:`Transit <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Transit>`
                
                .. attribute:: egress
                
                	Static LSPs for which the router is an  egress node
                	**type**\:  :py:class:`Egress <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Egress>`
                
                

                """

                _prefix = 'oc-mpls'
                _revision = '2017-03-22'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Mpls.Lsps.StaticLsps.StaticLsp, self).__init__()

                    self.yang_name = "static-lsp"
                    self.yang_parent_name = "static-lsps"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.StaticLsps.StaticLsp.Config)), ("state", ("state", Mpls.Lsps.StaticLsps.StaticLsp.State)), ("ingress", ("ingress", Mpls.Lsps.StaticLsps.StaticLsp.Ingress)), ("transit", ("transit", Mpls.Lsps.StaticLsps.StaticLsp.Transit)), ("egress", ("egress", Mpls.Lsps.StaticLsps.StaticLsp.Egress))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.config = Mpls.Lsps.StaticLsps.StaticLsp.Config()
                    self.config.parent = self
                    self._children_name_map["config"] = "config"

                    self.state = Mpls.Lsps.StaticLsps.StaticLsp.State()
                    self.state.parent = self
                    self._children_name_map["state"] = "state"

                    self.ingress = Mpls.Lsps.StaticLsps.StaticLsp.Ingress()
                    self.ingress.parent = self
                    self._children_name_map["ingress"] = "ingress"

                    self.transit = Mpls.Lsps.StaticLsps.StaticLsp.Transit()
                    self.transit.parent = self
                    self._children_name_map["transit"] = "transit"

                    self.egress = Mpls.Lsps.StaticLsps.StaticLsp.Egress()
                    self.egress.parent = self
                    self._children_name_map["egress"] = "egress"
                    self._segment_path = lambda: "static-lsp" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "openconfig-mpls:mpls/lsps/static-lsps/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp, ['name'], name, value)


                class Config(_Entity_):
                    """
                    Configuration data for the static lsp
                    
                    .. attribute:: name
                    
                    	name to identify the LSP
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Lsps.StaticLsps.StaticLsp.Config, self).__init__()

                        self.yang_name = "config"
                        self.yang_parent_name = "static-lsp"
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
                        self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Config, ['name'], name, value)



                class State(_Entity_):
                    """
                    Operational state data for the static lsp
                    
                    .. attribute:: name
                    
                    	name to identify the LSP
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Lsps.StaticLsps.StaticLsp.State, self).__init__()

                        self.yang_name = "state"
                        self.yang_parent_name = "static-lsp"
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
                        self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.State, ['name'], name, value)



                class Ingress(_Entity_):
                    """
                    Static LSPs for which the router is an
                     ingress node
                    
                    .. attribute:: config
                    
                    	Configuration data for ingress LSPs
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Ingress.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for ingress LSPs
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Ingress.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Lsps.StaticLsps.StaticLsp.Ingress, self).__init__()

                        self.yang_name = "ingress"
                        self.yang_parent_name = "static-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.StaticLsps.StaticLsp.Ingress.Config)), ("state", ("state", Mpls.Lsps.StaticLsps.StaticLsp.Ingress.State))])
                        self._leafs = OrderedDict()

                        self.config = Mpls.Lsps.StaticLsps.StaticLsp.Ingress.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.Lsps.StaticLsps.StaticLsp.Ingress.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "ingress"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Ingress, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for ingress LSPs
                        
                        .. attribute:: next_hop
                        
                        	next hop IP address for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        .. attribute:: incoming_label
                        
                        	label value on the incoming packet
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        .. attribute:: push_label
                        
                        	label value to push at the current hop for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.StaticLsps.StaticLsp.Ingress.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "ingress"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str','str'])),
                                ('incoming_label', (YLeaf(YType.str, 'incoming-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                ('push_label', (YLeaf(YType.str, 'push-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ])
                            self.next_hop = None
                            self.incoming_label = None
                            self.push_label = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Ingress.Config, ['next_hop', 'incoming_label', 'push_label'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data for ingress LSPs
                        
                        .. attribute:: next_hop
                        
                        	next hop IP address for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: incoming_label
                        
                        	label value on the incoming packet
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        .. attribute:: push_label
                        
                        	label value to push at the current hop for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.StaticLsps.StaticLsp.Ingress.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "ingress"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str','str'])),
                                ('incoming_label', (YLeaf(YType.str, 'incoming-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                ('push_label', (YLeaf(YType.str, 'push-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ])
                            self.next_hop = None
                            self.incoming_label = None
                            self.push_label = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Ingress.State, ['next_hop', 'incoming_label', 'push_label'], name, value)




                class Transit(_Entity_):
                    """
                    Static LSPs for which the router is an
                     transit node
                    
                    .. attribute:: config
                    
                    	Configuration data for transit LSPs
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Transit.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for transit LSPs
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Transit.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Lsps.StaticLsps.StaticLsp.Transit, self).__init__()

                        self.yang_name = "transit"
                        self.yang_parent_name = "static-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.StaticLsps.StaticLsp.Transit.Config)), ("state", ("state", Mpls.Lsps.StaticLsps.StaticLsp.Transit.State))])
                        self._leafs = OrderedDict()

                        self.config = Mpls.Lsps.StaticLsps.StaticLsp.Transit.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.Lsps.StaticLsps.StaticLsp.Transit.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "transit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Transit, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for transit LSPs
                        
                        .. attribute:: next_hop
                        
                        	next hop IP address for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        .. attribute:: incoming_label
                        
                        	label value on the incoming packet
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        .. attribute:: push_label
                        
                        	label value to push at the current hop for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.StaticLsps.StaticLsp.Transit.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "transit"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str','str'])),
                                ('incoming_label', (YLeaf(YType.str, 'incoming-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                ('push_label', (YLeaf(YType.str, 'push-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ])
                            self.next_hop = None
                            self.incoming_label = None
                            self.push_label = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Transit.Config, ['next_hop', 'incoming_label', 'push_label'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data for transit LSPs
                        
                        .. attribute:: next_hop
                        
                        	next hop IP address for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: incoming_label
                        
                        	label value on the incoming packet
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        .. attribute:: push_label
                        
                        	label value to push at the current hop for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.StaticLsps.StaticLsp.Transit.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "transit"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str','str'])),
                                ('incoming_label', (YLeaf(YType.str, 'incoming-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                ('push_label', (YLeaf(YType.str, 'push-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ])
                            self.next_hop = None
                            self.incoming_label = None
                            self.push_label = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Transit.State, ['next_hop', 'incoming_label', 'push_label'], name, value)




                class Egress(_Entity_):
                    """
                    Static LSPs for which the router is an
                     egress node
                    
                    .. attribute:: config
                    
                    	Configuration data for egress LSPs
                    	**type**\:  :py:class:`Config <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Egress.Config>`
                    
                    .. attribute:: state
                    
                    	Operational state data for egress LSPs
                    	**type**\:  :py:class:`State <ydk.models.openconfig.openconfig_mpls.Mpls.Lsps.StaticLsps.StaticLsp.Egress.State>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'oc-mpls'
                    _revision = '2017-03-22'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Mpls.Lsps.StaticLsps.StaticLsp.Egress, self).__init__()

                        self.yang_name = "egress"
                        self.yang_parent_name = "static-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("config", ("config", Mpls.Lsps.StaticLsps.StaticLsp.Egress.Config)), ("state", ("state", Mpls.Lsps.StaticLsps.StaticLsp.Egress.State))])
                        self._leafs = OrderedDict()

                        self.config = Mpls.Lsps.StaticLsps.StaticLsp.Egress.Config()
                        self.config.parent = self
                        self._children_name_map["config"] = "config"

                        self.state = Mpls.Lsps.StaticLsps.StaticLsp.Egress.State()
                        self.state.parent = self
                        self._children_name_map["state"] = "state"
                        self._segment_path = lambda: "egress"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Egress, [], name, value)


                    class Config(_Entity_):
                        """
                        Configuration data for egress LSPs
                        
                        .. attribute:: next_hop
                        
                        	next hop IP address for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        .. attribute:: incoming_label
                        
                        	label value on the incoming packet
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        .. attribute:: push_label
                        
                        	label value to push at the current hop for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.StaticLsps.StaticLsp.Egress.Config, self).__init__()

                            self.yang_name = "config"
                            self.yang_parent_name = "egress"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str','str'])),
                                ('incoming_label', (YLeaf(YType.str, 'incoming-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                ('push_label', (YLeaf(YType.str, 'push-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ])
                            self.next_hop = None
                            self.incoming_label = None
                            self.push_label = None
                            self._segment_path = lambda: "config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Egress.Config, ['next_hop', 'incoming_label', 'push_label'], name, value)



                    class State(_Entity_):
                        """
                        Operational state data for egress LSPs
                        
                        .. attribute:: next_hop
                        
                        	next hop IP address for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])$
                        
                        		**type**\: str
                        
                        			**pattern:** ^(([0\-9a\-fA\-F]{1,4}\:){7}[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,7}\:\|([0\-9a\-fA\-F]{1,4}\:){1,6}\:[0\-9a\-fA\-F]{1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,5}(\:[0\-9a\-fA\-F]{1,4}){1,2}\|([0\-9a\-fA\-F]{1,4}\:){1,4}(\:[0\-9a\-fA\-F]{1,4}){1,3}\|([0\-9a\-fA\-F]{1,4}\:){1,3}(\:[0\-9a\-fA\-F]{1,4}){1,4}\|([0\-9a\-fA\-F]{1,4}\:){1,2}(\:[0\-9a\-fA\-F]{1,4}){1,5}\|[0\-9a\-fA\-F]{1,4}\:((\:[0\-9a\-fA\-F]{1,4}){1,6})\|\:((\:[0\-9a\-fA\-F]{1,4}){1,7}\|\:))$
                        
                        	**config**\: False
                        
                        .. attribute:: incoming_label
                        
                        	label value on the incoming packet
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        .. attribute:: push_label
                        
                        	label value to push at the current hop for the LSP
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 16..1048575
                        
                        		**type**\:  :py:class:`MplsLabel <ydk.models.openconfig.openconfig_segment_routing.MplsLabel>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'oc-mpls'
                        _revision = '2017-03-22'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Mpls.Lsps.StaticLsps.StaticLsp.Egress.State, self).__init__()

                            self.yang_name = "state"
                            self.yang_parent_name = "egress"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str','str'])),
                                ('incoming_label', (YLeaf(YType.str, 'incoming-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                                ('push_label', (YLeaf(YType.str, 'push-label'), ['int',('ydk.models.openconfig.openconfig_segment_routing', 'MplsLabel', '')])),
                            ])
                            self.next_hop = None
                            self.incoming_label = None
                            self.push_label = None
                            self._segment_path = lambda: "state"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpls.Lsps.StaticLsps.StaticLsp.Egress.State, ['next_hop', 'incoming_label', 'push_label'], name, value)






    def clone_ptr(self):
        self._top_entity = Mpls()
        return self._top_entity



