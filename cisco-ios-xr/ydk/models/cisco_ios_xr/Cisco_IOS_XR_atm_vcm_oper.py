""" Cisco_IOS_XR_atm_vcm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR atm\-vcm package operational data.

This module contains definitions
for the following management objects\:
  atm\-vcm\: ATM VCM operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ClassLinkOamInheritLevel(Enum):
    """
    ClassLinkOamInheritLevel (Enum Class)

    ATM VC\-class inheritence level for class\-link

    .. data:: vc_configured_onvc = 0

    	Configured on VC

    .. data:: vc_class_onvc = 1

    	Class on VC

    .. data:: vc_class_on_sub_interface = 2

    	Class on sub-if

    .. data:: vc_class_on_main_interface = 3

    	Class on main-if

    .. data:: vc_global_default = 4

    	Global default values

    .. data:: vc_inherit_level_unknown = 5

    	Unknown (invalid)

    """

    vc_configured_onvc = Enum.YLeaf(0, "vc-configured-onvc")

    vc_class_onvc = Enum.YLeaf(1, "vc-class-onvc")

    vc_class_on_sub_interface = Enum.YLeaf(2, "vc-class-on-sub-interface")

    vc_class_on_main_interface = Enum.YLeaf(3, "vc-class-on-main-interface")

    vc_global_default = Enum.YLeaf(4, "vc-global-default")

    vc_inherit_level_unknown = Enum.YLeaf(5, "vc-inherit-level-unknown")


class Vc(Enum):
    """
    Vc (Enum Class)

     ATM VC type

    .. data:: layer3_vc = 0

    	 ATM Layer 3 VC type

    .. data:: layer2_vc = 1

    	 ATM Layer 2 VC type

    .. data:: layer2_vp = 2

    	 ATM Layer 2 VP type

    .. data:: vc_type_unknown = 3

    	 ATM type unknown

    """

    layer3_vc = Enum.YLeaf(0, "layer3-vc")

    layer2_vc = Enum.YLeaf(1, "layer2-vc")

    layer2_vp = Enum.YLeaf(2, "layer2-vp")

    vc_type_unknown = Enum.YLeaf(3, "vc-type-unknown")


class VcCellPackingMode(Enum):
    """
    VcCellPackingMode (Enum Class)

    ATM VC cell packing mode

    .. data:: vp = 1

    	VP mode

    .. data:: vc = 2

    	VC mode

    .. data:: port_mode = 3

    	Port mode

    """

    vp = Enum.YLeaf(1, "vp")

    vc = Enum.YLeaf(2, "vc")

    port_mode = Enum.YLeaf(3, "port-mode")


class VcEncap(Enum):
    """
    VcEncap (Enum Class)

    VC Encapsulation Type

    .. data:: ilmi = 1

    	ILMI Encapsulation

    .. data:: qsaal = 2

    	QSAAL Encapsulation

    .. data:: snap = 3

    	SNAP Encapsulation

    .. data:: mux = 4

    	MUX Encapsulation

    .. data:: nlpid = 5

    	NLPID Encapsulation

    .. data:: f4oam = 6

    	F4OAM Encapsulation

    .. data:: aal0 = 7

    	AAL0 Encapsulation

    .. data:: aal5 = 8

    	AAL5 Encapsulation

    .. data:: encap_unknown = 9

    	Uknown (invalid) Encapsulation

    """

    ilmi = Enum.YLeaf(1, "ilmi")

    qsaal = Enum.YLeaf(2, "qsaal")

    snap = Enum.YLeaf(3, "snap")

    mux = Enum.YLeaf(4, "mux")

    nlpid = Enum.YLeaf(5, "nlpid")

    f4oam = Enum.YLeaf(6, "f4oam")

    aal0 = Enum.YLeaf(7, "aal0")

    aal5 = Enum.YLeaf(8, "aal5")

    encap_unknown = Enum.YLeaf(9, "encap-unknown")


class VcInheritLevel(Enum):
    """
    VcInheritLevel (Enum Class)

    ATM vc\-class inheritence level

    .. data:: directly_configured_onvc = 0

    	ATM vc-class inherit level: Config of VC

    .. data:: vc_class_configured_onvc = 1

    	ATM vc-class inherit level: Class of VC

    .. data:: vc_class_configured_on_sub_interface = 2

    	ATM vc-class inherit level: Class of Sub-if

    .. data:: vc_class_configured_on_main_interface = 3

    	ATM vc-class inherit level: Class of Main-if

    .. data:: global_default = 4

    	ATM vc-class inherit level: Global Default

    .. data:: unknown = 5

    	ATM vc-class inherit level: Unknown (invalid)

    .. data:: not_supported = 6

    	ATM vc-class inherit level: Not supported on

    	this VC class

    """

    directly_configured_onvc = Enum.YLeaf(0, "directly-configured-onvc")

    vc_class_configured_onvc = Enum.YLeaf(1, "vc-class-configured-onvc")

    vc_class_configured_on_sub_interface = Enum.YLeaf(2, "vc-class-configured-on-sub-interface")

    vc_class_configured_on_main_interface = Enum.YLeaf(3, "vc-class-configured-on-main-interface")

    global_default = Enum.YLeaf(4, "global-default")

    unknown = Enum.YLeaf(5, "unknown")

    not_supported = Enum.YLeaf(6, "not-supported")


class VcManageLevel(Enum):
    """
    VcManageLevel (Enum Class)

    ATM Class link manage level

    .. data:: manage = 1

    	Managed

    .. data:: not_managed = 2

    	Not managed

    """

    manage = Enum.YLeaf(1, "manage")

    not_managed = Enum.YLeaf(2, "not-managed")


class VcState(Enum):
    """
    VcState (Enum Class)

    VC State

    .. data:: initialized = 0

    	ATM VC State: only VC data structure

    	initialized   

    .. data:: modifying = 1

    	ATM VC State: configuration currently being

    	changed

    .. data:: modified = 2

    	ATM VC State: configuration changed            

    .. data:: activating = 3

    	ATM VC State: command sent to hardware to

    	activate 

    .. data:: activated = 4

    	ATM VC State: activated in h/w or protocol     

    .. data:: not_verified = 5

    	ATM VC State: OAM/ILMI - yet to verify         

    .. data:: ready = 6

    	ATM VC State: Ready state                      

    .. data:: deactivating = 7

    	ATM VC State: command sent to h/w to deactivate

    .. data:: inactive = 8

    	ATM VC State: inactive/not present in hardware 

    .. data:: deleting = 9

    	ATM VC State: VC is being deleted              

    .. data:: deleted = 10

    	ATM VC State: VC is already delete in hardware 

    .. data:: state_unknown = 11

    	ATM VC State: Unknown(invalid)

    """

    initialized = Enum.YLeaf(0, "initialized")

    modifying = Enum.YLeaf(1, "modifying")

    modified = Enum.YLeaf(2, "modified")

    activating = Enum.YLeaf(3, "activating")

    activated = Enum.YLeaf(4, "activated")

    not_verified = Enum.YLeaf(5, "not-verified")

    ready = Enum.YLeaf(6, "ready")

    deactivating = Enum.YLeaf(7, "deactivating")

    inactive = Enum.YLeaf(8, "inactive")

    deleting = Enum.YLeaf(9, "deleting")

    deleted = Enum.YLeaf(10, "deleted")

    state_unknown = Enum.YLeaf(11, "state-unknown")


class VcTestMode(Enum):
    """
    VcTestMode (Enum Class)

    VC Test Mode Type

    .. data:: test_mode_none = 1

    	VC not in test mode

    .. data:: loop = 2

    	VC in test mode Loop

    .. data:: reserved = 3

    	VC in test mode Reserved

    """

    test_mode_none = Enum.YLeaf(1, "test-mode-none")

    loop = Enum.YLeaf(2, "loop")

    reserved = Enum.YLeaf(3, "reserved")


class VcTrafShaping(Enum):
    """
    VcTrafShaping (Enum Class)

    VC traffic shaping type

    .. data:: cbr = 1

    	VC traffic shaping type CBR

    .. data:: vbr_nrt = 2

    	VC traffic shaping type VBR-NR

    .. data:: vbr_rt = 3

    	VC traffic shaping type VBR-RT

    .. data:: abr = 4

    	VC traffic shaping type ABR

    .. data:: ubr_plus = 5

    	VC traffic shaping type UBR+

    .. data:: ubr = 6

    	VC traffic shaping type UBR

    .. data:: traf_shaping_unknown = 7

    	VC traffic shaping type Unknown (invalid)

    """

    cbr = Enum.YLeaf(1, "cbr")

    vbr_nrt = Enum.YLeaf(2, "vbr-nrt")

    vbr_rt = Enum.YLeaf(3, "vbr-rt")

    abr = Enum.YLeaf(4, "abr")

    ubr_plus = Enum.YLeaf(5, "ubr-plus")

    ubr = Enum.YLeaf(6, "ubr")

    traf_shaping_unknown = Enum.YLeaf(7, "traf-shaping-unknown")


class VcmPort(Enum):
    """
    VcmPort (Enum Class)

    ATM port type

    .. data:: port_type_layer_2 = 0

    	 Layer 2 ATM port type 

    .. data:: port_type_layer_3 = 1

    	 Layer 3 ATM port type 

    .. data:: port_type_unknown = 3

    	 ATM port type unknown 

    """

    port_type_layer_2 = Enum.YLeaf(0, "port-type-layer-2")

    port_type_layer_3 = Enum.YLeaf(1, "port-type-layer-3")

    port_type_unknown = Enum.YLeaf(3, "port-type-unknown")


class VpState(Enum):
    """
    VpState (Enum Class)

    VP\-Tunnel State

    .. data:: vp_initialized = 0

    	VP-Tunnel State: Initialized

    .. data:: vp_modifying = 1

    	VP-Tunnel State: Modifying

    .. data:: vp_ready = 2

    	VP-Tunnel State: Ready

    .. data:: vp_mgd_down = 3

    	VP-Tunnel State: Managed Down

    .. data:: vp_deleting = 4

    	VP-Tunnel State: Deleting

    .. data:: vp_deleted = 5

    	VP-Tunnel State: Deleted

    .. data:: vp_state_unknown = 6

    	VP-Tunnel State: Unknown

    """

    vp_initialized = Enum.YLeaf(0, "vp-initialized")

    vp_modifying = Enum.YLeaf(1, "vp-modifying")

    vp_ready = Enum.YLeaf(2, "vp-ready")

    vp_mgd_down = Enum.YLeaf(3, "vp-mgd-down")

    vp_deleting = Enum.YLeaf(4, "vp-deleting")

    vp_deleted = Enum.YLeaf(5, "vp-deleted")

    vp_state_unknown = Enum.YLeaf(6, "vp-state-unknown")


class VpTrafShaping(Enum):
    """
    VpTrafShaping (Enum Class)

    VP\-Tunnel traffic shaping type

    .. data:: vp_cbr = 1

    	VP-Tunnel traffic shaping type CBR

    .. data:: vp_vbr_nrt = 2

    	VP-Tunnel traffic shaping type VBR-NR

    .. data:: vp_vbr_rt = 3

    	VP-Tunnel traffic shaping type VBR-RT

    .. data:: vp_abr = 4

    	VP-Tunnel traffic shaping type ABR

    .. data:: vp_ubr_plus = 5

    	VP-Tunnel traffic shaping type UBR+

    .. data:: vp_ubr = 6

    	VP-Tunnel traffic shaping type UBR

    .. data:: vp_traf_shaping_unknown = 7

    	VP-Tunnel traffic shaping type Unknown

    	(invalid)

    """

    vp_cbr = Enum.YLeaf(1, "vp-cbr")

    vp_vbr_nrt = Enum.YLeaf(2, "vp-vbr-nrt")

    vp_vbr_rt = Enum.YLeaf(3, "vp-vbr-rt")

    vp_abr = Enum.YLeaf(4, "vp-abr")

    vp_ubr_plus = Enum.YLeaf(5, "vp-ubr-plus")

    vp_ubr = Enum.YLeaf(6, "vp-ubr")

    vp_traf_shaping_unknown = Enum.YLeaf(7, "vp-traf-shaping-unknown")



class AtmVcm(Entity):
    """
    ATM VCM operational data
    
    .. attribute:: nodes
    
    	Contains all the nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'atm-vcm-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(AtmVcm, self).__init__()
        self._top_entity = None

        self.yang_name = "atm-vcm"
        self.yang_parent_name = "Cisco-IOS-XR-atm-vcm-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", AtmVcm.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = AtmVcm.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-atm-vcm-oper:atm-vcm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(AtmVcm, [], name, value)


    class Nodes(Entity):
        """
        Contains all the nodes
        
        .. attribute:: node
        
        	The node on which ATM Interfaces/VCs/VPs are located
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'atm-vcm-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(AtmVcm.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "atm-vcm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", AtmVcm.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-atm-vcm-oper:atm-vcm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AtmVcm.Nodes, [], name, value)


        class Node(Entity):
            """
            The node on which ATM Interfaces/VCs/VPs are
            located
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: vcs
            
            	Contains all VC information for node
            	**type**\:  :py:class:`Vcs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Vcs>`
            
            	**config**\: False
            
            .. attribute:: cell_packs
            
            	Contains all cell packing information for node
            	**type**\:  :py:class:`CellPacks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.CellPacks>`
            
            	**config**\: False
            
            .. attribute:: pvps
            
            	Contains all L2 PVP information for node
            	**type**\:  :py:class:`Pvps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Pvps>`
            
            	**config**\: False
            
            .. attribute:: class_links
            
            	Contains all class link information for node
            	**type**\:  :py:class:`ClassLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks>`
            
            	**config**\: False
            
            .. attribute:: interfaces
            
            	Contains all Interface information for node
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Interfaces>`
            
            	**config**\: False
            
            .. attribute:: vp_tunnels
            
            	Contains all VP\-tunnel information for node
            	**type**\:  :py:class:`VpTunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.VpTunnels>`
            
            	**config**\: False
            
            

            """

            _prefix = 'atm-vcm-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(AtmVcm.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("vcs", ("vcs", AtmVcm.Nodes.Node.Vcs)), ("cell-packs", ("cell_packs", AtmVcm.Nodes.Node.CellPacks)), ("pvps", ("pvps", AtmVcm.Nodes.Node.Pvps)), ("class-links", ("class_links", AtmVcm.Nodes.Node.ClassLinks)), ("interfaces", ("interfaces", AtmVcm.Nodes.Node.Interfaces)), ("vp-tunnels", ("vp_tunnels", AtmVcm.Nodes.Node.VpTunnels))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.vcs = AtmVcm.Nodes.Node.Vcs()
                self.vcs.parent = self
                self._children_name_map["vcs"] = "vcs"

                self.cell_packs = AtmVcm.Nodes.Node.CellPacks()
                self.cell_packs.parent = self
                self._children_name_map["cell_packs"] = "cell-packs"

                self.pvps = AtmVcm.Nodes.Node.Pvps()
                self.pvps.parent = self
                self._children_name_map["pvps"] = "pvps"

                self.class_links = AtmVcm.Nodes.Node.ClassLinks()
                self.class_links.parent = self
                self._children_name_map["class_links"] = "class-links"

                self.interfaces = AtmVcm.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.vp_tunnels = AtmVcm.Nodes.Node.VpTunnels()
                self.vp_tunnels.parent = self
                self._children_name_map["vp_tunnels"] = "vp-tunnels"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-atm-vcm-oper:atm-vcm/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AtmVcm.Nodes.Node, ['node_name'], name, value)


            class Vcs(Entity):
                """
                Contains all VC information for node
                
                .. attribute:: vc
                
                	All VC information on a node
                	**type**\: list of  		 :py:class:`Vc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Vcs.Vc>`
                
                	**config**\: False
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.Vcs, self).__init__()

                    self.yang_name = "vcs"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vc", ("vc", AtmVcm.Nodes.Node.Vcs.Vc))])
                    self._leafs = OrderedDict()

                    self.vc = YList(self)
                    self._segment_path = lambda: "vcs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AtmVcm.Nodes.Node.Vcs, [], name, value)


                class Vc(Entity):
                    """
                    All VC information on a node
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vpi
                    
                    	VPI
                    	**type**\: int
                    
                    	**range:** 0..4095
                    
                    	**config**\: False
                    
                    .. attribute:: vci
                    
                    	VCI
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**config**\: False
                    
                    .. attribute:: cell_packing_data
                    
                    	Cell packing specific data
                    	**type**\:  :py:class:`CellPackingData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData>`
                    
                    	**config**\: False
                    
                    .. attribute:: main_interface
                    
                    	Main Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: sub_interface
                    
                    	Subinterface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vc_interface
                    
                    	VC Interfcace handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vpi_xr
                    
                    	VC VPI value
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: vci_xr
                    
                    	VC VCI value
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	VC Type
                    	**type**\:  :py:class:`Vc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.Vc>`
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation type
                    	**type**\:  :py:class:`VcEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: shape
                    
                    	ATM VC traffic shaping type
                    	**type**\:  :py:class:`VcTrafShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShaping>`
                    
                    	**config**\: False
                    
                    .. attribute:: peak_cell_rate
                    
                    	Peak cell rate in Kbps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: sustained_cell_rate
                    
                    	Sustained cell rate in Kbps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: burst_rate
                    
                    	Burst size in cells
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: encaps_inherit_level
                    
                    	Encapsulation inherit level \- identifies if encapsulation is set to default, configured on the VC, or inherited from the vcclass
                    	**type**\:  :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                    
                    	**config**\: False
                    
                    .. attribute:: qos_inherit_level
                    
                    	Quality of Service inherit level \- identifies if QoS is set to default, configured on the VC, or inherited from the vcclass
                    	**type**\:  :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                    
                    	**config**\: False
                    
                    .. attribute:: transmit_mtu
                    
                    	Transmit MTU
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: receive_mtu
                    
                    	Receive MTU
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vc_onvp_tunnel
                    
                    	VC on VP\-tunnel flag
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: vc_on_p2p_sub_interface
                    
                    	VC on Point\-to\-point Sub\-interface
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: oper_status
                    
                    	TRUE value indicates that the VC is operationally UP
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: amin_status
                    
                    	TRUE value indicates that the VC is administratively UP
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: internal_state
                    
                    	VC Internal state
                    	**type**\:  :py:class:`VcState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcState>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_state_change_time
                    
                    	Time when VC was last changed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: test_mode
                    
                    	VC test mode
                    	**type**\:  :py:class:`VcTestMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTestMode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.Vcs.Vc, self).__init__()

                        self.yang_name = "vc"
                        self.yang_parent_name = "vcs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("cell-packing-data", ("cell_packing_data", AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('vpi', (YLeaf(YType.uint32, 'vpi'), ['int'])),
                            ('vci', (YLeaf(YType.uint32, 'vci'), ['int'])),
                            ('main_interface', (YLeaf(YType.str, 'main-interface'), ['str'])),
                            ('sub_interface', (YLeaf(YType.str, 'sub-interface'), ['str'])),
                            ('vc_interface', (YLeaf(YType.str, 'vc-interface'), ['str'])),
                            ('vpi_xr', (YLeaf(YType.uint16, 'vpi-xr'), ['int'])),
                            ('vci_xr', (YLeaf(YType.uint16, 'vci-xr'), ['int'])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'Vc', '')])),
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEncap', '')])),
                            ('shape', (YLeaf(YType.enumeration, 'shape'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTrafShaping', '')])),
                            ('peak_cell_rate', (YLeaf(YType.uint32, 'peak-cell-rate'), ['int'])),
                            ('sustained_cell_rate', (YLeaf(YType.uint32, 'sustained-cell-rate'), ['int'])),
                            ('burst_rate', (YLeaf(YType.uint32, 'burst-rate'), ['int'])),
                            ('encaps_inherit_level', (YLeaf(YType.enumeration, 'encaps-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevel', '')])),
                            ('qos_inherit_level', (YLeaf(YType.enumeration, 'qos-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevel', '')])),
                            ('transmit_mtu', (YLeaf(YType.uint32, 'transmit-mtu'), ['int'])),
                            ('receive_mtu', (YLeaf(YType.uint32, 'receive-mtu'), ['int'])),
                            ('vc_onvp_tunnel', (YLeaf(YType.boolean, 'vc-onvp-tunnel'), ['bool'])),
                            ('vc_on_p2p_sub_interface', (YLeaf(YType.boolean, 'vc-on-p2p-sub-interface'), ['bool'])),
                            ('oper_status', (YLeaf(YType.boolean, 'oper-status'), ['bool'])),
                            ('amin_status', (YLeaf(YType.boolean, 'amin-status'), ['bool'])),
                            ('internal_state', (YLeaf(YType.enumeration, 'internal-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcState', '')])),
                            ('last_state_change_time', (YLeaf(YType.uint32, 'last-state-change-time'), ['int'])),
                            ('test_mode', (YLeaf(YType.enumeration, 'test-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTestMode', '')])),
                        ])
                        self.interface_name = None
                        self.vpi = None
                        self.vci = None
                        self.main_interface = None
                        self.sub_interface = None
                        self.vc_interface = None
                        self.vpi_xr = None
                        self.vci_xr = None
                        self.type = None
                        self.encapsulation = None
                        self.shape = None
                        self.peak_cell_rate = None
                        self.sustained_cell_rate = None
                        self.burst_rate = None
                        self.encaps_inherit_level = None
                        self.qos_inherit_level = None
                        self.transmit_mtu = None
                        self.receive_mtu = None
                        self.vc_onvp_tunnel = None
                        self.vc_on_p2p_sub_interface = None
                        self.oper_status = None
                        self.amin_status = None
                        self.internal_state = None
                        self.last_state_change_time = None
                        self.test_mode = None

                        self.cell_packing_data = AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData()
                        self.cell_packing_data.parent = self
                        self._children_name_map["cell_packing_data"] = "cell-packing-data"
                        self._segment_path = lambda: "vc" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AtmVcm.Nodes.Node.Vcs.Vc, ['interface_name', 'vpi', 'vci', 'main_interface', 'sub_interface', 'vc_interface', 'vpi_xr', 'vci_xr', 'type', 'encapsulation', 'shape', 'peak_cell_rate', 'sustained_cell_rate', 'burst_rate', 'encaps_inherit_level', 'qos_inherit_level', 'transmit_mtu', 'receive_mtu', 'vc_onvp_tunnel', 'vc_on_p2p_sub_interface', 'oper_status', 'amin_status', 'internal_state', 'last_state_change_time', 'test_mode'], name, value)


                    class CellPackingData(Entity):
                        """
                        Cell packing specific data
                        
                        .. attribute:: local_max_cells_packed_per_packet
                        
                        	Local configuration of maximum number of cells to be packed per packet
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: negotiated_max_cells_packed_per_packet
                        
                        	Negotiated value of maximum number of cells to be packed per packed
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: max_cell_packed_timeout
                        
                        	Maximum cell packing timeout inmicro seconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**units**\: microsecond
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData, self).__init__()

                            self.yang_name = "cell-packing-data"
                            self.yang_parent_name = "vc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('local_max_cells_packed_per_packet', (YLeaf(YType.uint16, 'local-max-cells-packed-per-packet'), ['int'])),
                                ('negotiated_max_cells_packed_per_packet', (YLeaf(YType.uint16, 'negotiated-max-cells-packed-per-packet'), ['int'])),
                                ('max_cell_packed_timeout', (YLeaf(YType.uint16, 'max-cell-packed-timeout'), ['int'])),
                            ])
                            self.local_max_cells_packed_per_packet = None
                            self.negotiated_max_cells_packed_per_packet = None
                            self.max_cell_packed_timeout = None
                            self._segment_path = lambda: "cell-packing-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData, ['local_max_cells_packed_per_packet', 'negotiated_max_cells_packed_per_packet', 'max_cell_packed_timeout'], name, value)





            class CellPacks(Entity):
                """
                Contains all cell packing information for node
                
                .. attribute:: cell_pack
                
                	All cell packing information on a node
                	**type**\: list of  		 :py:class:`CellPack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.CellPacks.CellPack>`
                
                	**config**\: False
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.CellPacks, self).__init__()

                    self.yang_name = "cell-packs"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("cell-pack", ("cell_pack", AtmVcm.Nodes.Node.CellPacks.CellPack))])
                    self._leafs = OrderedDict()

                    self.cell_pack = YList(self)
                    self._segment_path = lambda: "cell-packs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AtmVcm.Nodes.Node.CellPacks, [], name, value)


                class CellPack(Entity):
                    """
                    All cell packing information on a node
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: pci
                    
                    	PCI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: cell_packing
                    
                    	Cell packing specific data
                    	**type**\:  :py:class:`CellPacking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking>`
                    
                    	**config**\: False
                    
                    .. attribute:: sub_interface_name
                    
                    	Sub\-interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: cell_packing_mode
                    
                    	ATM cell packing mode
                    	**type**\:  :py:class:`VcCellPackingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcCellPackingMode>`
                    
                    	**config**\: False
                    
                    .. attribute:: vpi
                    
                    	VPI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vci
                    
                    	VCI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: received_average_cells_packets
                    
                    	Average cells/packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: sent_cells_packets
                    
                    	Average cells/packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.CellPacks.CellPack, self).__init__()

                        self.yang_name = "cell-pack"
                        self.yang_parent_name = "cell-packs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("cell-packing", ("cell_packing", AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('pci', (YLeaf(YType.uint32, 'pci'), ['int'])),
                            ('sub_interface_name', (YLeaf(YType.str, 'sub-interface-name'), ['str'])),
                            ('cell_packing_mode', (YLeaf(YType.enumeration, 'cell-packing-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcCellPackingMode', '')])),
                            ('vpi', (YLeaf(YType.uint32, 'vpi'), ['int'])),
                            ('vci', (YLeaf(YType.uint32, 'vci'), ['int'])),
                            ('received_average_cells_packets', (YLeaf(YType.uint64, 'received-average-cells-packets'), ['int'])),
                            ('sent_cells_packets', (YLeaf(YType.uint64, 'sent-cells-packets'), ['int'])),
                        ])
                        self.interface_name = None
                        self.pci = None
                        self.sub_interface_name = None
                        self.cell_packing_mode = None
                        self.vpi = None
                        self.vci = None
                        self.received_average_cells_packets = None
                        self.sent_cells_packets = None

                        self.cell_packing = AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking()
                        self.cell_packing.parent = self
                        self._children_name_map["cell_packing"] = "cell-packing"
                        self._segment_path = lambda: "cell-pack"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AtmVcm.Nodes.Node.CellPacks.CellPack, ['interface_name', 'pci', 'sub_interface_name', 'cell_packing_mode', 'vpi', 'vci', 'received_average_cells_packets', 'sent_cells_packets'], name, value)


                    class CellPacking(Entity):
                        """
                        Cell packing specific data
                        
                        .. attribute:: local_max_cells_packed_per_packet
                        
                        	Local configuration of maximum number of cells to be packed per packet
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: negotiated_max_cells_packed_per_packet
                        
                        	Negotiated value of maximum number of cells to be packed per packed
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: max_cell_packed_timeout
                        
                        	Maximum cell packing timeout inmicro seconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**units**\: microsecond
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking, self).__init__()

                            self.yang_name = "cell-packing"
                            self.yang_parent_name = "cell-pack"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('local_max_cells_packed_per_packet', (YLeaf(YType.uint16, 'local-max-cells-packed-per-packet'), ['int'])),
                                ('negotiated_max_cells_packed_per_packet', (YLeaf(YType.uint16, 'negotiated-max-cells-packed-per-packet'), ['int'])),
                                ('max_cell_packed_timeout', (YLeaf(YType.uint16, 'max-cell-packed-timeout'), ['int'])),
                            ])
                            self.local_max_cells_packed_per_packet = None
                            self.negotiated_max_cells_packed_per_packet = None
                            self.max_cell_packed_timeout = None
                            self._segment_path = lambda: "cell-packing"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking, ['local_max_cells_packed_per_packet', 'negotiated_max_cells_packed_per_packet', 'max_cell_packed_timeout'], name, value)





            class Pvps(Entity):
                """
                Contains all L2 PVP information for node
                
                .. attribute:: pvp
                
                	All L2 PVP information on a node
                	**type**\: list of  		 :py:class:`Pvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Pvps.Pvp>`
                
                	**config**\: False
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.Pvps, self).__init__()

                    self.yang_name = "pvps"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pvp", ("pvp", AtmVcm.Nodes.Node.Pvps.Pvp))])
                    self._leafs = OrderedDict()

                    self.pvp = YList(self)
                    self._segment_path = lambda: "pvps"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AtmVcm.Nodes.Node.Pvps, [], name, value)


                class Pvp(Entity):
                    """
                    All L2 PVP information on a node
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vpi
                    
                    	VPI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: cell_packing_data
                    
                    	Cell packing specific data
                    	**type**\:  :py:class:`CellPackingData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData>`
                    
                    	**config**\: False
                    
                    .. attribute:: main_interface
                    
                    	Main Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: sub_interface
                    
                    	Subinterface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vc_interface
                    
                    	VC Interfcace handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vpi_xr
                    
                    	VC VPI value
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: vci_xr
                    
                    	VC VCI value
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	VC Type
                    	**type**\:  :py:class:`Vc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.Vc>`
                    
                    	**config**\: False
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation type
                    	**type**\:  :py:class:`VcEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncap>`
                    
                    	**config**\: False
                    
                    .. attribute:: shape
                    
                    	ATM VC traffic shaping type
                    	**type**\:  :py:class:`VcTrafShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShaping>`
                    
                    	**config**\: False
                    
                    .. attribute:: peak_cell_rate
                    
                    	Peak cell rate in Kbps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: sustained_cell_rate
                    
                    	Sustained cell rate in Kbps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: burst_rate
                    
                    	Burst size in cells
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: encaps_inherit_level
                    
                    	Encapsulation inherit level \- identifies if encapsulation is set to default, configured on the VC, or inherited from the vcclass
                    	**type**\:  :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                    
                    	**config**\: False
                    
                    .. attribute:: qos_inherit_level
                    
                    	Quality of Service inherit level \- identifies if QoS is set to default, configured on the VC, or inherited from the vcclass
                    	**type**\:  :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                    
                    	**config**\: False
                    
                    .. attribute:: transmit_mtu
                    
                    	Transmit MTU
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: receive_mtu
                    
                    	Receive MTU
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vc_onvp_tunnel
                    
                    	VC on VP\-tunnel flag
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: vc_on_p2p_sub_interface
                    
                    	VC on Point\-to\-point Sub\-interface
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: oper_status
                    
                    	TRUE value indicates that the VC is operationally UP
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: amin_status
                    
                    	TRUE value indicates that the VC is administratively UP
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: internal_state
                    
                    	VC Internal state
                    	**type**\:  :py:class:`VcState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcState>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_state_change_time
                    
                    	Time when VC was last changed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: test_mode
                    
                    	VC test mode
                    	**type**\:  :py:class:`VcTestMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTestMode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.Pvps.Pvp, self).__init__()

                        self.yang_name = "pvp"
                        self.yang_parent_name = "pvps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("cell-packing-data", ("cell_packing_data", AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('vpi', (YLeaf(YType.uint32, 'vpi'), ['int'])),
                            ('main_interface', (YLeaf(YType.str, 'main-interface'), ['str'])),
                            ('sub_interface', (YLeaf(YType.str, 'sub-interface'), ['str'])),
                            ('vc_interface', (YLeaf(YType.str, 'vc-interface'), ['str'])),
                            ('vpi_xr', (YLeaf(YType.uint16, 'vpi-xr'), ['int'])),
                            ('vci_xr', (YLeaf(YType.uint16, 'vci-xr'), ['int'])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'Vc', '')])),
                            ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEncap', '')])),
                            ('shape', (YLeaf(YType.enumeration, 'shape'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTrafShaping', '')])),
                            ('peak_cell_rate', (YLeaf(YType.uint32, 'peak-cell-rate'), ['int'])),
                            ('sustained_cell_rate', (YLeaf(YType.uint32, 'sustained-cell-rate'), ['int'])),
                            ('burst_rate', (YLeaf(YType.uint32, 'burst-rate'), ['int'])),
                            ('encaps_inherit_level', (YLeaf(YType.enumeration, 'encaps-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevel', '')])),
                            ('qos_inherit_level', (YLeaf(YType.enumeration, 'qos-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevel', '')])),
                            ('transmit_mtu', (YLeaf(YType.uint32, 'transmit-mtu'), ['int'])),
                            ('receive_mtu', (YLeaf(YType.uint32, 'receive-mtu'), ['int'])),
                            ('vc_onvp_tunnel', (YLeaf(YType.boolean, 'vc-onvp-tunnel'), ['bool'])),
                            ('vc_on_p2p_sub_interface', (YLeaf(YType.boolean, 'vc-on-p2p-sub-interface'), ['bool'])),
                            ('oper_status', (YLeaf(YType.boolean, 'oper-status'), ['bool'])),
                            ('amin_status', (YLeaf(YType.boolean, 'amin-status'), ['bool'])),
                            ('internal_state', (YLeaf(YType.enumeration, 'internal-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcState', '')])),
                            ('last_state_change_time', (YLeaf(YType.uint32, 'last-state-change-time'), ['int'])),
                            ('test_mode', (YLeaf(YType.enumeration, 'test-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTestMode', '')])),
                        ])
                        self.interface_name = None
                        self.vpi = None
                        self.main_interface = None
                        self.sub_interface = None
                        self.vc_interface = None
                        self.vpi_xr = None
                        self.vci_xr = None
                        self.type = None
                        self.encapsulation = None
                        self.shape = None
                        self.peak_cell_rate = None
                        self.sustained_cell_rate = None
                        self.burst_rate = None
                        self.encaps_inherit_level = None
                        self.qos_inherit_level = None
                        self.transmit_mtu = None
                        self.receive_mtu = None
                        self.vc_onvp_tunnel = None
                        self.vc_on_p2p_sub_interface = None
                        self.oper_status = None
                        self.amin_status = None
                        self.internal_state = None
                        self.last_state_change_time = None
                        self.test_mode = None

                        self.cell_packing_data = AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData()
                        self.cell_packing_data.parent = self
                        self._children_name_map["cell_packing_data"] = "cell-packing-data"
                        self._segment_path = lambda: "pvp" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AtmVcm.Nodes.Node.Pvps.Pvp, ['interface_name', 'vpi', 'main_interface', 'sub_interface', 'vc_interface', 'vpi_xr', 'vci_xr', 'type', 'encapsulation', 'shape', 'peak_cell_rate', 'sustained_cell_rate', 'burst_rate', 'encaps_inherit_level', 'qos_inherit_level', 'transmit_mtu', 'receive_mtu', 'vc_onvp_tunnel', 'vc_on_p2p_sub_interface', 'oper_status', 'amin_status', 'internal_state', 'last_state_change_time', 'test_mode'], name, value)


                    class CellPackingData(Entity):
                        """
                        Cell packing specific data
                        
                        .. attribute:: local_max_cells_packed_per_packet
                        
                        	Local configuration of maximum number of cells to be packed per packet
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: negotiated_max_cells_packed_per_packet
                        
                        	Negotiated value of maximum number of cells to be packed per packed
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: max_cell_packed_timeout
                        
                        	Maximum cell packing timeout inmicro seconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**units**\: microsecond
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData, self).__init__()

                            self.yang_name = "cell-packing-data"
                            self.yang_parent_name = "pvp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('local_max_cells_packed_per_packet', (YLeaf(YType.uint16, 'local-max-cells-packed-per-packet'), ['int'])),
                                ('negotiated_max_cells_packed_per_packet', (YLeaf(YType.uint16, 'negotiated-max-cells-packed-per-packet'), ['int'])),
                                ('max_cell_packed_timeout', (YLeaf(YType.uint16, 'max-cell-packed-timeout'), ['int'])),
                            ])
                            self.local_max_cells_packed_per_packet = None
                            self.negotiated_max_cells_packed_per_packet = None
                            self.max_cell_packed_timeout = None
                            self._segment_path = lambda: "cell-packing-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData, ['local_max_cells_packed_per_packet', 'negotiated_max_cells_packed_per_packet', 'max_cell_packed_timeout'], name, value)





            class ClassLinks(Entity):
                """
                Contains all class link information for node
                
                .. attribute:: class_link
                
                	All ATM VC information on a node
                	**type**\: list of  		 :py:class:`ClassLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink>`
                
                	**config**\: False
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.ClassLinks, self).__init__()

                    self.yang_name = "class-links"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("class-link", ("class_link", AtmVcm.Nodes.Node.ClassLinks.ClassLink))])
                    self._leafs = OrderedDict()

                    self.class_link = YList(self)
                    self._segment_path = lambda: "class-links"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks, [], name, value)


                class ClassLink(Entity):
                    """
                    All ATM VC information on a node
                    
                    .. attribute:: vpi  (key)
                    
                    	VPI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vci
                    
                    	VCI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: vc_class_not_supported
                    
                    	Not supported VC class
                    	**type**\:  :py:class:`VcClassNotSupported <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported>`
                    
                    	**config**\: False
                    
                    .. attribute:: oam_config
                    
                    	Oam values for class link
                    	**type**\:  :py:class:`OamConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig>`
                    
                    	**config**\: False
                    
                    .. attribute:: sub_interface_name
                    
                    	Sub\-interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.ClassLinks.ClassLink, self).__init__()

                        self.yang_name = "class-link"
                        self.yang_parent_name = "class-links"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['vpi']
                        self._child_classes = OrderedDict([("vc-class-not-supported", ("vc_class_not_supported", AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported)), ("oam-config", ("oam_config", AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig))])
                        self._leafs = OrderedDict([
                            ('vpi', (YLeaf(YType.uint32, 'vpi'), ['int'])),
                            ('vci', (YLeaf(YType.uint32, 'vci'), ['int'])),
                            ('sub_interface_name', (YLeaf(YType.str, 'sub-interface-name'), ['str'])),
                        ])
                        self.vpi = None
                        self.vci = None
                        self.sub_interface_name = None

                        self.vc_class_not_supported = AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported()
                        self.vc_class_not_supported.parent = self
                        self._children_name_map["vc_class_not_supported"] = "vc-class-not-supported"

                        self.oam_config = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig()
                        self.oam_config.parent = self
                        self._children_name_map["oam_config"] = "oam-config"
                        self._segment_path = lambda: "class-link" + "[vpi='" + str(self.vpi) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks.ClassLink, ['vpi', 'vci', u'sub_interface_name'], name, value)


                    class VcClassNotSupported(Entity):
                        """
                        Not supported VC class
                        
                        .. attribute:: encapsulation_not_supported
                        
                        	Encapsulation type not supported
                        	**type**\:  :py:class:`VcEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncap>`
                        
                        	**config**\: False
                        
                        .. attribute:: not_supported_inherit_level
                        
                        	NotSupportedInheritLevel
                        	**type**\:  :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported, self).__init__()

                            self.yang_name = "vc-class-not-supported"
                            self.yang_parent_name = "class-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('encapsulation_not_supported', (YLeaf(YType.enumeration, 'encapsulation-not-supported'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEncap', '')])),
                                ('not_supported_inherit_level', (YLeaf(YType.enumeration, 'not-supported-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevel', '')])),
                            ])
                            self.encapsulation_not_supported = None
                            self.not_supported_inherit_level = None
                            self._segment_path = lambda: "vc-class-not-supported"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported, [u'encapsulation_not_supported', u'not_supported_inherit_level'], name, value)



                    class OamConfig(Entity):
                        """
                        Oam values for class link
                        
                        .. attribute:: class_link_shaping
                        
                        	Traffic Shaping detail of VC class
                        	**type**\:  :py:class:`ClassLinkShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping>`
                        
                        	**config**\: False
                        
                        .. attribute:: class_link_encapsulation
                        
                        	Encapsulation details of VC class
                        	**type**\:  :py:class:`ClassLinkEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation>`
                        
                        	**config**\: False
                        
                        .. attribute:: oam_pvc
                        
                        	OAM PVC details of VC class
                        	**type**\:  :py:class:`OamPvc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc>`
                        
                        	**config**\: False
                        
                        .. attribute:: oam_retry
                        
                        	OAM Retry details of VC class
                        	**type**\:  :py:class:`OamRetry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry>`
                        
                        	**config**\: False
                        
                        .. attribute:: ais_rdi
                        
                        	AIS RDI details of a VC class
                        	**type**\:  :py:class:`AisRdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig, self).__init__()

                            self.yang_name = "oam-config"
                            self.yang_parent_name = "class-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("class-link-shaping", ("class_link_shaping", AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping)), ("class-link-encapsulation", ("class_link_encapsulation", AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation)), ("oam-pvc", ("oam_pvc", AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc)), ("oam-retry", ("oam_retry", AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry)), ("ais-rdi", ("ais_rdi", AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi))])
                            self._leafs = OrderedDict()

                            self.class_link_shaping = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping()
                            self.class_link_shaping.parent = self
                            self._children_name_map["class_link_shaping"] = "class-link-shaping"

                            self.class_link_encapsulation = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation()
                            self.class_link_encapsulation.parent = self
                            self._children_name_map["class_link_encapsulation"] = "class-link-encapsulation"

                            self.oam_pvc = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc()
                            self.oam_pvc.parent = self
                            self._children_name_map["oam_pvc"] = "oam-pvc"

                            self.oam_retry = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry()
                            self.oam_retry.parent = self
                            self._children_name_map["oam_retry"] = "oam-retry"

                            self.ais_rdi = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi()
                            self.ais_rdi.parent = self
                            self._children_name_map["ais_rdi"] = "ais-rdi"
                            self._segment_path = lambda: "oam-config"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig, [], name, value)


                        class ClassLinkShaping(Entity):
                            """
                            Traffic Shaping detail of VC class
                            
                            .. attribute:: shaping_type
                            
                            	ATM VC traffic shaping type
                            	**type**\:  :py:class:`VcTrafShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShaping>`
                            
                            	**config**\: False
                            
                            .. attribute:: peak_output_rate
                            
                            	Peak output rate in Kbps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: average_output_rate
                            
                            	Average output rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: burst_output_rate
                            
                            	Burst output rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: shaping_inherit_level
                            
                            	Shaping inherit level
                            	**type**\:  :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping, self).__init__()

                                self.yang_name = "class-link-shaping"
                                self.yang_parent_name = "oam-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('shaping_type', (YLeaf(YType.enumeration, 'shaping-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcTrafShaping', '')])),
                                    ('peak_output_rate', (YLeaf(YType.uint32, 'peak-output-rate'), ['int'])),
                                    ('average_output_rate', (YLeaf(YType.uint32, 'average-output-rate'), ['int'])),
                                    ('burst_output_rate', (YLeaf(YType.uint32, 'burst-output-rate'), ['int'])),
                                    ('shaping_inherit_level', (YLeaf(YType.enumeration, 'shaping-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevel', '')])),
                                ])
                                self.shaping_type = None
                                self.peak_output_rate = None
                                self.average_output_rate = None
                                self.burst_output_rate = None
                                self.shaping_inherit_level = None
                                self._segment_path = lambda: "class-link-shaping"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping, [u'shaping_type', u'peak_output_rate', u'average_output_rate', u'burst_output_rate', u'shaping_inherit_level'], name, value)



                        class ClassLinkEncapsulation(Entity):
                            """
                            Encapsulation details of VC class
                            
                            .. attribute:: encapsulation_type
                            
                            	Encapsulation type
                            	**type**\:  :py:class:`VcEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncap>`
                            
                            	**config**\: False
                            
                            .. attribute:: encapsulation_inherit_level
                            
                            	Encapsulation inherit level
                            	**type**\:  :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation, self).__init__()

                                self.yang_name = "class-link-encapsulation"
                                self.yang_parent_name = "oam-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('encapsulation_type', (YLeaf(YType.enumeration, 'encapsulation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcEncap', '')])),
                                    ('encapsulation_inherit_level', (YLeaf(YType.enumeration, 'encapsulation-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcInheritLevel', '')])),
                                ])
                                self.encapsulation_type = None
                                self.encapsulation_inherit_level = None
                                self._segment_path = lambda: "class-link-encapsulation"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation, [u'encapsulation_type', u'encapsulation_inherit_level'], name, value)



                        class OamPvc(Entity):
                            """
                            OAM PVC details of VC class
                            
                            .. attribute:: manage_level
                            
                            	Manage Level
                            	**type**\:  :py:class:`VcManageLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcManageLevel>`
                            
                            	**config**\: False
                            
                            .. attribute:: pvc_frequency
                            
                            	PVC Frequency
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: keep_vc_up
                            
                            	Keep vc up
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: ais_rdi_failure
                            
                            	AIS RDI failure
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: manage_inherit_level
                            
                            	Manage inherit level
                            	**type**\:  :py:class:`ClassLinkOamInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevel>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc, self).__init__()

                                self.yang_name = "oam-pvc"
                                self.yang_parent_name = "oam-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('manage_level', (YLeaf(YType.enumeration, 'manage-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcManageLevel', '')])),
                                    ('pvc_frequency', (YLeaf(YType.uint32, 'pvc-frequency'), ['int'])),
                                    ('keep_vc_up', (YLeaf(YType.boolean, 'keep-vc-up'), ['bool'])),
                                    ('ais_rdi_failure', (YLeaf(YType.boolean, 'ais-rdi-failure'), ['bool'])),
                                    ('manage_inherit_level', (YLeaf(YType.enumeration, 'manage-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'ClassLinkOamInheritLevel', '')])),
                                ])
                                self.manage_level = None
                                self.pvc_frequency = None
                                self.keep_vc_up = None
                                self.ais_rdi_failure = None
                                self.manage_inherit_level = None
                                self._segment_path = lambda: "oam-pvc"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc, [u'manage_level', u'pvc_frequency', u'keep_vc_up', u'ais_rdi_failure', u'manage_inherit_level'], name, value)



                        class OamRetry(Entity):
                            """
                            OAM Retry details of VC class
                            
                            .. attribute:: retry_up_count
                            
                            	Retry Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: down_count
                            
                            	Down Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: retry_frequency
                            
                            	Retry frequency
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: retry_inherit_level
                            
                            	Retry inherit level
                            	**type**\:  :py:class:`ClassLinkOamInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevel>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry, self).__init__()

                                self.yang_name = "oam-retry"
                                self.yang_parent_name = "oam-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('retry_up_count', (YLeaf(YType.uint32, 'retry-up-count'), ['int'])),
                                    ('down_count', (YLeaf(YType.uint32, 'down-count'), ['int'])),
                                    ('retry_frequency', (YLeaf(YType.uint32, 'retry-frequency'), ['int'])),
                                    ('retry_inherit_level', (YLeaf(YType.enumeration, 'retry-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'ClassLinkOamInheritLevel', '')])),
                                ])
                                self.retry_up_count = None
                                self.down_count = None
                                self.retry_frequency = None
                                self.retry_inherit_level = None
                                self._segment_path = lambda: "oam-retry"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry, [u'retry_up_count', u'down_count', u'retry_frequency', u'retry_inherit_level'], name, value)



                        class AisRdi(Entity):
                            """
                            AIS RDI details of a VC class
                            
                            .. attribute:: ais_rdi_up_count
                            
                            	AIS RDI up count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: ais_rdi_up_time
                            
                            	Time (in seconds) with no AIS/RDI cells before declaring a VC as up
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            	**units**\: second
                            
                            .. attribute:: ais_rdi_inherit_level
                            
                            	AIS RDI inherit level
                            	**type**\:  :py:class:`ClassLinkOamInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevel>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi, self).__init__()

                                self.yang_name = "ais-rdi"
                                self.yang_parent_name = "oam-config"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ais_rdi_up_count', (YLeaf(YType.uint32, 'ais-rdi-up-count'), ['int'])),
                                    ('ais_rdi_up_time', (YLeaf(YType.uint32, 'ais-rdi-up-time'), ['int'])),
                                    ('ais_rdi_inherit_level', (YLeaf(YType.enumeration, 'ais-rdi-inherit-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'ClassLinkOamInheritLevel', '')])),
                                ])
                                self.ais_rdi_up_count = None
                                self.ais_rdi_up_time = None
                                self.ais_rdi_inherit_level = None
                                self._segment_path = lambda: "ais-rdi"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi, [u'ais_rdi_up_count', u'ais_rdi_up_time', u'ais_rdi_inherit_level'], name, value)






            class Interfaces(Entity):
                """
                Contains all Interface information for node
                
                .. attribute:: interface
                
                	ATM Interface data
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Interfaces.Interface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", AtmVcm.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AtmVcm.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    ATM Interface data
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: cell_packing_data
                    
                    	Cell packing specific information
                    	**type**\:  :py:class:`CellPackingData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData>`
                    
                    	**config**\: False
                    
                    .. attribute:: ilmi_vpi
                    
                    	ILMI VPI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ilmi_vci
                    
                    	ILMI VCI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pvc_failures
                    
                    	Number of PVC Failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: currently_failing_layer2pv_ps
                    
                    	Number of currently failing Layer 2 PVPs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: currently_failing_layer2pv_cs
                    
                    	Number of currently failing Layer 2 PVCs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: currently_failing_layer3vp_tunnels
                    
                    	Number of currently failing Layer 3 VP tunnels
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: currently_failing_layer3pv_cs
                    
                    	Number of currently failing Layer 3 PVCs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pvc_failures_trap_enable
                    
                    	If true, PVC failures trap is enabled
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: pvc_notification_interval
                    
                    	PVC trap notification interval
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: configured_layer2pv_ps
                    
                    	Number of Layer 2 PVPs configured
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: configured_layer2pv_cs
                    
                    	Number of Layer 2 PVCs configured
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: configured_layer3vp_tunnels
                    
                    	Number of Layer 3 VP tunnels configured
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: configured_layer3pv_cs
                    
                    	Number of Layer 3 PVCs configured
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: port_type
                    
                    	ATM interface port type
                    	**type**\:  :py:class:`VcmPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcmPort>`
                    
                    	**config**\: False
                    
                    .. attribute:: main_interface
                    
                    	Main Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: l2_cell_packing_count
                    
                    	Number of L2 attachment circuits with the cell packing feature enabled on this main interface
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("cell-packing-data", ("cell_packing_data", AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('ilmi_vpi', (YLeaf(YType.uint32, 'ilmi-vpi'), ['int'])),
                            ('ilmi_vci', (YLeaf(YType.uint32, 'ilmi-vci'), ['int'])),
                            ('pvc_failures', (YLeaf(YType.uint32, 'pvc-failures'), ['int'])),
                            ('currently_failing_layer2pv_ps', (YLeaf(YType.uint32, 'currently-failing-layer2pv-ps'), ['int'])),
                            ('currently_failing_layer2pv_cs', (YLeaf(YType.uint32, 'currently-failing-layer2pv-cs'), ['int'])),
                            ('currently_failing_layer3vp_tunnels', (YLeaf(YType.uint32, 'currently-failing-layer3vp-tunnels'), ['int'])),
                            ('currently_failing_layer3pv_cs', (YLeaf(YType.uint32, 'currently-failing-layer3pv-cs'), ['int'])),
                            ('pvc_failures_trap_enable', (YLeaf(YType.boolean, 'pvc-failures-trap-enable'), ['bool'])),
                            ('pvc_notification_interval', (YLeaf(YType.uint32, 'pvc-notification-interval'), ['int'])),
                            ('configured_layer2pv_ps', (YLeaf(YType.uint32, 'configured-layer2pv-ps'), ['int'])),
                            ('configured_layer2pv_cs', (YLeaf(YType.uint32, 'configured-layer2pv-cs'), ['int'])),
                            ('configured_layer3vp_tunnels', (YLeaf(YType.uint32, 'configured-layer3vp-tunnels'), ['int'])),
                            ('configured_layer3pv_cs', (YLeaf(YType.uint32, 'configured-layer3pv-cs'), ['int'])),
                            ('port_type', (YLeaf(YType.enumeration, 'port-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VcmPort', '')])),
                            ('main_interface', (YLeaf(YType.str, 'main-interface'), ['str'])),
                            ('l2_cell_packing_count', (YLeaf(YType.uint16, 'l2-cell-packing-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.ilmi_vpi = None
                        self.ilmi_vci = None
                        self.pvc_failures = None
                        self.currently_failing_layer2pv_ps = None
                        self.currently_failing_layer2pv_cs = None
                        self.currently_failing_layer3vp_tunnels = None
                        self.currently_failing_layer3pv_cs = None
                        self.pvc_failures_trap_enable = None
                        self.pvc_notification_interval = None
                        self.configured_layer2pv_ps = None
                        self.configured_layer2pv_cs = None
                        self.configured_layer3vp_tunnels = None
                        self.configured_layer3pv_cs = None
                        self.port_type = None
                        self.main_interface = None
                        self.l2_cell_packing_count = None

                        self.cell_packing_data = AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData()
                        self.cell_packing_data.parent = self
                        self._children_name_map["cell_packing_data"] = "cell-packing-data"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AtmVcm.Nodes.Node.Interfaces.Interface, ['interface_name', u'ilmi_vpi', u'ilmi_vci', u'pvc_failures', u'currently_failing_layer2pv_ps', u'currently_failing_layer2pv_cs', u'currently_failing_layer3vp_tunnels', u'currently_failing_layer3pv_cs', u'pvc_failures_trap_enable', u'pvc_notification_interval', u'configured_layer2pv_ps', u'configured_layer2pv_cs', u'configured_layer3vp_tunnels', u'configured_layer3pv_cs', u'port_type', u'main_interface', u'l2_cell_packing_count'], name, value)


                    class CellPackingData(Entity):
                        """
                        Cell packing specific information
                        
                        .. attribute:: local_max_cells_packed_per_packet
                        
                        	Local configuration of maximum number of cells to be packed per packet
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: negotiated_max_cells_packed_per_packet
                        
                        	Negotiated value of maximum number of cells to be packed per packed
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: max_cell_packed_timeout
                        
                        	Maximum cell packing timeout inmicro seconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**units**\: microsecond
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData, self).__init__()

                            self.yang_name = "cell-packing-data"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('local_max_cells_packed_per_packet', (YLeaf(YType.uint16, 'local-max-cells-packed-per-packet'), ['int'])),
                                ('negotiated_max_cells_packed_per_packet', (YLeaf(YType.uint16, 'negotiated-max-cells-packed-per-packet'), ['int'])),
                                ('max_cell_packed_timeout', (YLeaf(YType.uint16, 'max-cell-packed-timeout'), ['int'])),
                            ])
                            self.local_max_cells_packed_per_packet = None
                            self.negotiated_max_cells_packed_per_packet = None
                            self.max_cell_packed_timeout = None
                            self._segment_path = lambda: "cell-packing-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData, ['local_max_cells_packed_per_packet', 'negotiated_max_cells_packed_per_packet', 'max_cell_packed_timeout'], name, value)





            class VpTunnels(Entity):
                """
                Contains all VP\-tunnel information for node
                
                .. attribute:: vp_tunnel
                
                	All VP\-tunnel information on a node
                	**type**\: list of  		 :py:class:`VpTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.VpTunnels.VpTunnel>`
                
                	**config**\: False
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.VpTunnels, self).__init__()

                    self.yang_name = "vp-tunnels"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vp-tunnel", ("vp_tunnel", AtmVcm.Nodes.Node.VpTunnels.VpTunnel))])
                    self._leafs = OrderedDict()

                    self.vp_tunnel = YList(self)
                    self._segment_path = lambda: "vp-tunnels"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AtmVcm.Nodes.Node.VpTunnels, [], name, value)


                class VpTunnel(Entity):
                    """
                    All VP\-tunnel information on a node
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vpi
                    
                    	VPI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: main_interface
                    
                    	Main Interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vp_interface
                    
                    	VP Interfcace handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: vpi_xr
                    
                    	VP\-Tunnel VPI value
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: shape
                    
                    	ATM VP traffic shaping type
                    	**type**\:  :py:class:`VpTrafShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VpTrafShaping>`
                    
                    	**config**\: False
                    
                    .. attribute:: peak_cell_rate
                    
                    	Peak cell rate in Kbps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: sustained_cell_rate
                    
                    	Sustained cell rate in Kbps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: burst_rate
                    
                    	Burst size in cells
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: f4oam_enabled
                    
                    	F4OAM Enabled flag
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: data_vc_count
                    
                    	Number of Data PVCs under this VP\-tunnel
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: oper_status
                    
                    	TRUE value indicates that the VP is operationally UP
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: amin_status
                    
                    	TRUE value indicates that the VP is administratively UP
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: internal_state
                    
                    	Internal state
                    	**type**\:  :py:class:`VpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VpState>`
                    
                    	**config**\: False
                    
                    .. attribute:: last_vp_state_change_time
                    
                    	Time when VP\-Tunnel state was last changed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.VpTunnels.VpTunnel, self).__init__()

                        self.yang_name = "vp-tunnel"
                        self.yang_parent_name = "vp-tunnels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('vpi', (YLeaf(YType.uint32, 'vpi'), ['int'])),
                            ('main_interface', (YLeaf(YType.str, 'main-interface'), ['str'])),
                            ('vp_interface', (YLeaf(YType.str, 'vp-interface'), ['str'])),
                            ('vpi_xr', (YLeaf(YType.uint16, 'vpi-xr'), ['int'])),
                            ('shape', (YLeaf(YType.enumeration, 'shape'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VpTrafShaping', '')])),
                            ('peak_cell_rate', (YLeaf(YType.uint32, 'peak-cell-rate'), ['int'])),
                            ('sustained_cell_rate', (YLeaf(YType.uint32, 'sustained-cell-rate'), ['int'])),
                            ('burst_rate', (YLeaf(YType.uint32, 'burst-rate'), ['int'])),
                            ('f4oam_enabled', (YLeaf(YType.boolean, 'f4oam-enabled'), ['bool'])),
                            ('data_vc_count', (YLeaf(YType.uint32, 'data-vc-count'), ['int'])),
                            ('oper_status', (YLeaf(YType.boolean, 'oper-status'), ['bool'])),
                            ('amin_status', (YLeaf(YType.boolean, 'amin-status'), ['bool'])),
                            ('internal_state', (YLeaf(YType.enumeration, 'internal-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper', 'VpState', '')])),
                            ('last_vp_state_change_time', (YLeaf(YType.uint32, 'last-vp-state-change-time'), ['int'])),
                        ])
                        self.interface_name = None
                        self.vpi = None
                        self.main_interface = None
                        self.vp_interface = None
                        self.vpi_xr = None
                        self.shape = None
                        self.peak_cell_rate = None
                        self.sustained_cell_rate = None
                        self.burst_rate = None
                        self.f4oam_enabled = None
                        self.data_vc_count = None
                        self.oper_status = None
                        self.amin_status = None
                        self.internal_state = None
                        self.last_vp_state_change_time = None
                        self._segment_path = lambda: "vp-tunnel" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AtmVcm.Nodes.Node.VpTunnels.VpTunnel, ['interface_name', 'vpi', 'main_interface', 'vp_interface', 'vpi_xr', 'shape', 'peak_cell_rate', 'sustained_cell_rate', 'burst_rate', 'f4oam_enabled', 'data_vc_count', 'oper_status', 'amin_status', 'internal_state', 'last_vp_state_change_time'], name, value)





    def clone_ptr(self):
        self._top_entity = AtmVcm()
        return self._top_entity



