""" Cisco_IOS_XR_atm_vcm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR atm\-vcm package operational data.

This module contains definitions
for the following management objects\:
  atm\-vcm\: ATM VCM operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ClassLinkOamInheritLevel(Enum):
    """
    ClassLinkOamInheritLevel

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
    Vc

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
    VcCellPackingMode

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
    VcEncap

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
    VcInheritLevel

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
    VcManageLevel

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
    VcState

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
    VcTestMode

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
    VcTrafShaping

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
    VcmPort

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
    VpState

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
    VpTrafShaping

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
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes>`
    
    

    """

    _prefix = 'atm-vcm-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(AtmVcm, self).__init__()
        self._top_entity = None

        self.yang_name = "atm-vcm"
        self.yang_parent_name = "Cisco-IOS-XR-atm-vcm-oper"

        self.nodes = AtmVcm.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Contains all the nodes
        
        .. attribute:: node
        
        	The node on which ATM Interfaces/VCs/VPs are located
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node>`
        
        

        """

        _prefix = 'atm-vcm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AtmVcm.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "atm-vcm"

            self.node = YList(self)

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
                        super(AtmVcm.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AtmVcm.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            The node on which ATM Interfaces/VCs/VPs are
            located
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: cell_packs
            
            	Contains all cell packing information for node
            	**type**\:   :py:class:`CellPacks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.CellPacks>`
            
            .. attribute:: class_links
            
            	Contains all class link information for node
            	**type**\:   :py:class:`ClassLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks>`
            
            .. attribute:: interfaces
            
            	Contains all Interface information for node
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Interfaces>`
            
            .. attribute:: pvps
            
            	Contains all L2 PVP information for node
            	**type**\:   :py:class:`Pvps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Pvps>`
            
            .. attribute:: vcs
            
            	Contains all VC information for node
            	**type**\:   :py:class:`Vcs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Vcs>`
            
            .. attribute:: vp_tunnels
            
            	Contains all VP\-tunnel information for node
            	**type**\:   :py:class:`VpTunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.VpTunnels>`
            
            

            """

            _prefix = 'atm-vcm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AtmVcm.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.cell_packs = AtmVcm.Nodes.Node.CellPacks()
                self.cell_packs.parent = self
                self._children_name_map["cell_packs"] = "cell-packs"
                self._children_yang_names.add("cell-packs")

                self.class_links = AtmVcm.Nodes.Node.ClassLinks()
                self.class_links.parent = self
                self._children_name_map["class_links"] = "class-links"
                self._children_yang_names.add("class-links")

                self.interfaces = AtmVcm.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.pvps = AtmVcm.Nodes.Node.Pvps()
                self.pvps.parent = self
                self._children_name_map["pvps"] = "pvps"
                self._children_yang_names.add("pvps")

                self.vcs = AtmVcm.Nodes.Node.Vcs()
                self.vcs.parent = self
                self._children_name_map["vcs"] = "vcs"
                self._children_yang_names.add("vcs")

                self.vp_tunnels = AtmVcm.Nodes.Node.VpTunnels()
                self.vp_tunnels.parent = self
                self._children_name_map["vp_tunnels"] = "vp-tunnels"
                self._children_yang_names.add("vp-tunnels")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AtmVcm.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AtmVcm.Nodes.Node, self).__setattr__(name, value)


            class Vcs(Entity):
                """
                Contains all VC information for node
                
                .. attribute:: vc
                
                	All VC information on a node
                	**type**\: list of    :py:class:`Vc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Vcs.Vc>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.Vcs, self).__init__()

                    self.yang_name = "vcs"
                    self.yang_parent_name = "node"

                    self.vc = YList(self)

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
                                super(AtmVcm.Nodes.Node.Vcs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AtmVcm.Nodes.Node.Vcs, self).__setattr__(name, value)


                class Vc(Entity):
                    """
                    All VC information on a node
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: amin_status
                    
                    	TRUE value indicates that the VC is administratively UP
                    	**type**\:  bool
                    
                    .. attribute:: burst_rate
                    
                    	Burst size in cells
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cell_packing_data
                    
                    	Cell packing specific data
                    	**type**\:   :py:class:`CellPackingData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData>`
                    
                    .. attribute:: encaps_inherit_level
                    
                    	Encapsulation inherit level \- identifies if encapsulation is set to default, configured on the VC, or inherited from the vcclass
                    	**type**\:   :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation type
                    	**type**\:   :py:class:`VcEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncap>`
                    
                    .. attribute:: internal_state
                    
                    	VC Internal state
                    	**type**\:   :py:class:`VcState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcState>`
                    
                    .. attribute:: last_state_change_time
                    
                    	Time when VC was last changed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: main_interface
                    
                    	Main Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: oper_status
                    
                    	TRUE value indicates that the VC is operationally UP
                    	**type**\:  bool
                    
                    .. attribute:: peak_cell_rate
                    
                    	Peak cell rate in Kbps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: qos_inherit_level
                    
                    	Quality of Service inherit level \- identifies if QoS is set to default, configured on the VC, or inherited from the vcclass
                    	**type**\:   :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                    
                    .. attribute:: receive_mtu
                    
                    	Receive MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: shape
                    
                    	ATM VC traffic shaping type
                    	**type**\:   :py:class:`VcTrafShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShaping>`
                    
                    .. attribute:: sub_interface
                    
                    	Subinterface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: sustained_cell_rate
                    
                    	Sustained cell rate in Kbps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: test_mode
                    
                    	VC test mode
                    	**type**\:   :py:class:`VcTestMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTestMode>`
                    
                    .. attribute:: transmit_mtu
                    
                    	Transmit MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	VC Type
                    	**type**\:   :py:class:`Vc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.Vc>`
                    
                    .. attribute:: vc_interface
                    
                    	VC Interfcace handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: vc_on_p2p_sub_interface
                    
                    	VC on Point\-to\-point Sub\-interface
                    	**type**\:  bool
                    
                    .. attribute:: vc_onvp_tunnel
                    
                    	VC on VP\-tunnel flag
                    	**type**\:  bool
                    
                    .. attribute:: vci
                    
                    	VCI
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: vci_xr
                    
                    	VC VCI value
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: vpi
                    
                    	VPI
                    	**type**\:  int
                    
                    	**range:** 0..4095
                    
                    .. attribute:: vpi_xr
                    
                    	VC VPI value
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.Vcs.Vc, self).__init__()

                        self.yang_name = "vc"
                        self.yang_parent_name = "vcs"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.amin_status = YLeaf(YType.boolean, "amin-status")

                        self.burst_rate = YLeaf(YType.uint32, "burst-rate")

                        self.encaps_inherit_level = YLeaf(YType.enumeration, "encaps-inherit-level")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.internal_state = YLeaf(YType.enumeration, "internal-state")

                        self.last_state_change_time = YLeaf(YType.uint32, "last-state-change-time")

                        self.main_interface = YLeaf(YType.str, "main-interface")

                        self.oper_status = YLeaf(YType.boolean, "oper-status")

                        self.peak_cell_rate = YLeaf(YType.uint32, "peak-cell-rate")

                        self.qos_inherit_level = YLeaf(YType.enumeration, "qos-inherit-level")

                        self.receive_mtu = YLeaf(YType.uint32, "receive-mtu")

                        self.shape = YLeaf(YType.enumeration, "shape")

                        self.sub_interface = YLeaf(YType.str, "sub-interface")

                        self.sustained_cell_rate = YLeaf(YType.uint32, "sustained-cell-rate")

                        self.test_mode = YLeaf(YType.enumeration, "test-mode")

                        self.transmit_mtu = YLeaf(YType.uint32, "transmit-mtu")

                        self.type = YLeaf(YType.enumeration, "type")

                        self.vc_interface = YLeaf(YType.str, "vc-interface")

                        self.vc_on_p2p_sub_interface = YLeaf(YType.boolean, "vc-on-p2p-sub-interface")

                        self.vc_onvp_tunnel = YLeaf(YType.boolean, "vc-onvp-tunnel")

                        self.vci = YLeaf(YType.uint32, "vci")

                        self.vci_xr = YLeaf(YType.uint16, "vci-xr")

                        self.vpi = YLeaf(YType.uint32, "vpi")

                        self.vpi_xr = YLeaf(YType.uint16, "vpi-xr")

                        self.cell_packing_data = AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData()
                        self.cell_packing_data.parent = self
                        self._children_name_map["cell_packing_data"] = "cell-packing-data"
                        self._children_yang_names.add("cell-packing-data")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "amin_status",
                                        "burst_rate",
                                        "encaps_inherit_level",
                                        "encapsulation",
                                        "internal_state",
                                        "last_state_change_time",
                                        "main_interface",
                                        "oper_status",
                                        "peak_cell_rate",
                                        "qos_inherit_level",
                                        "receive_mtu",
                                        "shape",
                                        "sub_interface",
                                        "sustained_cell_rate",
                                        "test_mode",
                                        "transmit_mtu",
                                        "type",
                                        "vc_interface",
                                        "vc_on_p2p_sub_interface",
                                        "vc_onvp_tunnel",
                                        "vci",
                                        "vci_xr",
                                        "vpi",
                                        "vpi_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AtmVcm.Nodes.Node.Vcs.Vc, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AtmVcm.Nodes.Node.Vcs.Vc, self).__setattr__(name, value)


                    class CellPackingData(Entity):
                        """
                        Cell packing specific data
                        
                        .. attribute:: local_max_cells_packed_per_packet
                        
                        	Local configuration of maximum number of cells to be packed per packet
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: max_cell_packed_timeout
                        
                        	Maximum cell packing timeout inmicro seconds
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**units**\: microsecond
                        
                        .. attribute:: negotiated_max_cells_packed_per_packet
                        
                        	Negotiated value of maximum number of cells to be packed per packed
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData, self).__init__()

                            self.yang_name = "cell-packing-data"
                            self.yang_parent_name = "vc"

                            self.local_max_cells_packed_per_packet = YLeaf(YType.uint16, "local-max-cells-packed-per-packet")

                            self.max_cell_packed_timeout = YLeaf(YType.uint16, "max-cell-packed-timeout")

                            self.negotiated_max_cells_packed_per_packet = YLeaf(YType.uint16, "negotiated-max-cells-packed-per-packet")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("local_max_cells_packed_per_packet",
                                            "max_cell_packed_timeout",
                                            "negotiated_max_cells_packed_per_packet") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.local_max_cells_packed_per_packet.is_set or
                                self.max_cell_packed_timeout.is_set or
                                self.negotiated_max_cells_packed_per_packet.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.local_max_cells_packed_per_packet.yfilter != YFilter.not_set or
                                self.max_cell_packed_timeout.yfilter != YFilter.not_set or
                                self.negotiated_max_cells_packed_per_packet.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "cell-packing-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.local_max_cells_packed_per_packet.is_set or self.local_max_cells_packed_per_packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_max_cells_packed_per_packet.get_name_leafdata())
                            if (self.max_cell_packed_timeout.is_set or self.max_cell_packed_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_cell_packed_timeout.get_name_leafdata())
                            if (self.negotiated_max_cells_packed_per_packet.is_set or self.negotiated_max_cells_packed_per_packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.negotiated_max_cells_packed_per_packet.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "local-max-cells-packed-per-packet" or name == "max-cell-packed-timeout" or name == "negotiated-max-cells-packed-per-packet"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "local-max-cells-packed-per-packet"):
                                self.local_max_cells_packed_per_packet = value
                                self.local_max_cells_packed_per_packet.value_namespace = name_space
                                self.local_max_cells_packed_per_packet.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-cell-packed-timeout"):
                                self.max_cell_packed_timeout = value
                                self.max_cell_packed_timeout.value_namespace = name_space
                                self.max_cell_packed_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "negotiated-max-cells-packed-per-packet"):
                                self.negotiated_max_cells_packed_per_packet = value
                                self.negotiated_max_cells_packed_per_packet.value_namespace = name_space
                                self.negotiated_max_cells_packed_per_packet.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.amin_status.is_set or
                            self.burst_rate.is_set or
                            self.encaps_inherit_level.is_set or
                            self.encapsulation.is_set or
                            self.internal_state.is_set or
                            self.last_state_change_time.is_set or
                            self.main_interface.is_set or
                            self.oper_status.is_set or
                            self.peak_cell_rate.is_set or
                            self.qos_inherit_level.is_set or
                            self.receive_mtu.is_set or
                            self.shape.is_set or
                            self.sub_interface.is_set or
                            self.sustained_cell_rate.is_set or
                            self.test_mode.is_set or
                            self.transmit_mtu.is_set or
                            self.type.is_set or
                            self.vc_interface.is_set or
                            self.vc_on_p2p_sub_interface.is_set or
                            self.vc_onvp_tunnel.is_set or
                            self.vci.is_set or
                            self.vci_xr.is_set or
                            self.vpi.is_set or
                            self.vpi_xr.is_set or
                            (self.cell_packing_data is not None and self.cell_packing_data.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.amin_status.yfilter != YFilter.not_set or
                            self.burst_rate.yfilter != YFilter.not_set or
                            self.encaps_inherit_level.yfilter != YFilter.not_set or
                            self.encapsulation.yfilter != YFilter.not_set or
                            self.internal_state.yfilter != YFilter.not_set or
                            self.last_state_change_time.yfilter != YFilter.not_set or
                            self.main_interface.yfilter != YFilter.not_set or
                            self.oper_status.yfilter != YFilter.not_set or
                            self.peak_cell_rate.yfilter != YFilter.not_set or
                            self.qos_inherit_level.yfilter != YFilter.not_set or
                            self.receive_mtu.yfilter != YFilter.not_set or
                            self.shape.yfilter != YFilter.not_set or
                            self.sub_interface.yfilter != YFilter.not_set or
                            self.sustained_cell_rate.yfilter != YFilter.not_set or
                            self.test_mode.yfilter != YFilter.not_set or
                            self.transmit_mtu.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.vc_interface.yfilter != YFilter.not_set or
                            self.vc_on_p2p_sub_interface.yfilter != YFilter.not_set or
                            self.vc_onvp_tunnel.yfilter != YFilter.not_set or
                            self.vci.yfilter != YFilter.not_set or
                            self.vci_xr.yfilter != YFilter.not_set or
                            self.vpi.yfilter != YFilter.not_set or
                            self.vpi_xr.yfilter != YFilter.not_set or
                            (self.cell_packing_data is not None and self.cell_packing_data.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vc" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.amin_status.is_set or self.amin_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.amin_status.get_name_leafdata())
                        if (self.burst_rate.is_set or self.burst_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.burst_rate.get_name_leafdata())
                        if (self.encaps_inherit_level.is_set or self.encaps_inherit_level.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encaps_inherit_level.get_name_leafdata())
                        if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encapsulation.get_name_leafdata())
                        if (self.internal_state.is_set or self.internal_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.internal_state.get_name_leafdata())
                        if (self.last_state_change_time.is_set or self.last_state_change_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_state_change_time.get_name_leafdata())
                        if (self.main_interface.is_set or self.main_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.main_interface.get_name_leafdata())
                        if (self.oper_status.is_set or self.oper_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oper_status.get_name_leafdata())
                        if (self.peak_cell_rate.is_set or self.peak_cell_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_cell_rate.get_name_leafdata())
                        if (self.qos_inherit_level.is_set or self.qos_inherit_level.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qos_inherit_level.get_name_leafdata())
                        if (self.receive_mtu.is_set or self.receive_mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_mtu.get_name_leafdata())
                        if (self.shape.is_set or self.shape.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.shape.get_name_leafdata())
                        if (self.sub_interface.is_set or self.sub_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sub_interface.get_name_leafdata())
                        if (self.sustained_cell_rate.is_set or self.sustained_cell_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sustained_cell_rate.get_name_leafdata())
                        if (self.test_mode.is_set or self.test_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.test_mode.get_name_leafdata())
                        if (self.transmit_mtu.is_set or self.transmit_mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_mtu.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())
                        if (self.vc_interface.is_set or self.vc_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vc_interface.get_name_leafdata())
                        if (self.vc_on_p2p_sub_interface.is_set or self.vc_on_p2p_sub_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vc_on_p2p_sub_interface.get_name_leafdata())
                        if (self.vc_onvp_tunnel.is_set or self.vc_onvp_tunnel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vc_onvp_tunnel.get_name_leafdata())
                        if (self.vci.is_set or self.vci.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vci.get_name_leafdata())
                        if (self.vci_xr.is_set or self.vci_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vci_xr.get_name_leafdata())
                        if (self.vpi.is_set or self.vpi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vpi.get_name_leafdata())
                        if (self.vpi_xr.is_set or self.vpi_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vpi_xr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "cell-packing-data"):
                            if (self.cell_packing_data is None):
                                self.cell_packing_data = AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData()
                                self.cell_packing_data.parent = self
                                self._children_name_map["cell_packing_data"] = "cell-packing-data"
                            return self.cell_packing_data

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cell-packing-data" or name == "interface-name" or name == "amin-status" or name == "burst-rate" or name == "encaps-inherit-level" or name == "encapsulation" or name == "internal-state" or name == "last-state-change-time" or name == "main-interface" or name == "oper-status" or name == "peak-cell-rate" or name == "qos-inherit-level" or name == "receive-mtu" or name == "shape" or name == "sub-interface" or name == "sustained-cell-rate" or name == "test-mode" or name == "transmit-mtu" or name == "type" or name == "vc-interface" or name == "vc-on-p2p-sub-interface" or name == "vc-onvp-tunnel" or name == "vci" or name == "vci-xr" or name == "vpi" or name == "vpi-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "amin-status"):
                            self.amin_status = value
                            self.amin_status.value_namespace = name_space
                            self.amin_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "burst-rate"):
                            self.burst_rate = value
                            self.burst_rate.value_namespace = name_space
                            self.burst_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "encaps-inherit-level"):
                            self.encaps_inherit_level = value
                            self.encaps_inherit_level.value_namespace = name_space
                            self.encaps_inherit_level.value_namespace_prefix = name_space_prefix
                        if(value_path == "encapsulation"):
                            self.encapsulation = value
                            self.encapsulation.value_namespace = name_space
                            self.encapsulation.value_namespace_prefix = name_space_prefix
                        if(value_path == "internal-state"):
                            self.internal_state = value
                            self.internal_state.value_namespace = name_space
                            self.internal_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-state-change-time"):
                            self.last_state_change_time = value
                            self.last_state_change_time.value_namespace = name_space
                            self.last_state_change_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "main-interface"):
                            self.main_interface = value
                            self.main_interface.value_namespace = name_space
                            self.main_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "oper-status"):
                            self.oper_status = value
                            self.oper_status.value_namespace = name_space
                            self.oper_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-cell-rate"):
                            self.peak_cell_rate = value
                            self.peak_cell_rate.value_namespace = name_space
                            self.peak_cell_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "qos-inherit-level"):
                            self.qos_inherit_level = value
                            self.qos_inherit_level.value_namespace = name_space
                            self.qos_inherit_level.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-mtu"):
                            self.receive_mtu = value
                            self.receive_mtu.value_namespace = name_space
                            self.receive_mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "shape"):
                            self.shape = value
                            self.shape.value_namespace = name_space
                            self.shape.value_namespace_prefix = name_space_prefix
                        if(value_path == "sub-interface"):
                            self.sub_interface = value
                            self.sub_interface.value_namespace = name_space
                            self.sub_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "sustained-cell-rate"):
                            self.sustained_cell_rate = value
                            self.sustained_cell_rate.value_namespace = name_space
                            self.sustained_cell_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "test-mode"):
                            self.test_mode = value
                            self.test_mode.value_namespace = name_space
                            self.test_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-mtu"):
                            self.transmit_mtu = value
                            self.transmit_mtu.value_namespace = name_space
                            self.transmit_mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "vc-interface"):
                            self.vc_interface = value
                            self.vc_interface.value_namespace = name_space
                            self.vc_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "vc-on-p2p-sub-interface"):
                            self.vc_on_p2p_sub_interface = value
                            self.vc_on_p2p_sub_interface.value_namespace = name_space
                            self.vc_on_p2p_sub_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "vc-onvp-tunnel"):
                            self.vc_onvp_tunnel = value
                            self.vc_onvp_tunnel.value_namespace = name_space
                            self.vc_onvp_tunnel.value_namespace_prefix = name_space_prefix
                        if(value_path == "vci"):
                            self.vci = value
                            self.vci.value_namespace = name_space
                            self.vci.value_namespace_prefix = name_space_prefix
                        if(value_path == "vci-xr"):
                            self.vci_xr = value
                            self.vci_xr.value_namespace = name_space
                            self.vci_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "vpi"):
                            self.vpi = value
                            self.vpi.value_namespace = name_space
                            self.vpi.value_namespace_prefix = name_space_prefix
                        if(value_path == "vpi-xr"):
                            self.vpi_xr = value
                            self.vpi_xr.value_namespace = name_space
                            self.vpi_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vc:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vc:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vcs" + path_buffer

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

                    if (child_yang_name == "vc"):
                        for c in self.vc:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AtmVcm.Nodes.Node.Vcs.Vc()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vc.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vc"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class CellPacks(Entity):
                """
                Contains all cell packing information for node
                
                .. attribute:: cell_pack
                
                	All cell packing information on a node
                	**type**\: list of    :py:class:`CellPack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.CellPacks.CellPack>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.CellPacks, self).__init__()

                    self.yang_name = "cell-packs"
                    self.yang_parent_name = "node"

                    self.cell_pack = YList(self)

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
                                super(AtmVcm.Nodes.Node.CellPacks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AtmVcm.Nodes.Node.CellPacks, self).__setattr__(name, value)


                class CellPack(Entity):
                    """
                    All cell packing information on a node
                    
                    .. attribute:: cell_packing
                    
                    	Cell packing specific data
                    	**type**\:   :py:class:`CellPacking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking>`
                    
                    .. attribute:: cell_packing_mode
                    
                    	ATM cell packing mode
                    	**type**\:   :py:class:`VcCellPackingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcCellPackingMode>`
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: pci
                    
                    	PCI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: received_average_cells_packets
                    
                    	Average cells/packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sent_cells_packets
                    
                    	Average cells/packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sub_interface_name
                    
                    	Sub\-interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: vci
                    
                    	VCI
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vpi
                    
                    	VPI
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.CellPacks.CellPack, self).__init__()

                        self.yang_name = "cell-pack"
                        self.yang_parent_name = "cell-packs"

                        self.cell_packing_mode = YLeaf(YType.enumeration, "cell-packing-mode")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.pci = YLeaf(YType.int32, "pci")

                        self.received_average_cells_packets = YLeaf(YType.uint64, "received-average-cells-packets")

                        self.sent_cells_packets = YLeaf(YType.uint64, "sent-cells-packets")

                        self.sub_interface_name = YLeaf(YType.str, "sub-interface-name")

                        self.vci = YLeaf(YType.uint32, "vci")

                        self.vpi = YLeaf(YType.uint32, "vpi")

                        self.cell_packing = AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking()
                        self.cell_packing.parent = self
                        self._children_name_map["cell_packing"] = "cell-packing"
                        self._children_yang_names.add("cell-packing")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cell_packing_mode",
                                        "interface_name",
                                        "pci",
                                        "received_average_cells_packets",
                                        "sent_cells_packets",
                                        "sub_interface_name",
                                        "vci",
                                        "vpi") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AtmVcm.Nodes.Node.CellPacks.CellPack, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AtmVcm.Nodes.Node.CellPacks.CellPack, self).__setattr__(name, value)


                    class CellPacking(Entity):
                        """
                        Cell packing specific data
                        
                        .. attribute:: local_max_cells_packed_per_packet
                        
                        	Local configuration of maximum number of cells to be packed per packet
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: max_cell_packed_timeout
                        
                        	Maximum cell packing timeout inmicro seconds
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**units**\: microsecond
                        
                        .. attribute:: negotiated_max_cells_packed_per_packet
                        
                        	Negotiated value of maximum number of cells to be packed per packed
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking, self).__init__()

                            self.yang_name = "cell-packing"
                            self.yang_parent_name = "cell-pack"

                            self.local_max_cells_packed_per_packet = YLeaf(YType.uint16, "local-max-cells-packed-per-packet")

                            self.max_cell_packed_timeout = YLeaf(YType.uint16, "max-cell-packed-timeout")

                            self.negotiated_max_cells_packed_per_packet = YLeaf(YType.uint16, "negotiated-max-cells-packed-per-packet")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("local_max_cells_packed_per_packet",
                                            "max_cell_packed_timeout",
                                            "negotiated_max_cells_packed_per_packet") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.local_max_cells_packed_per_packet.is_set or
                                self.max_cell_packed_timeout.is_set or
                                self.negotiated_max_cells_packed_per_packet.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.local_max_cells_packed_per_packet.yfilter != YFilter.not_set or
                                self.max_cell_packed_timeout.yfilter != YFilter.not_set or
                                self.negotiated_max_cells_packed_per_packet.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "cell-packing" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.local_max_cells_packed_per_packet.is_set or self.local_max_cells_packed_per_packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_max_cells_packed_per_packet.get_name_leafdata())
                            if (self.max_cell_packed_timeout.is_set or self.max_cell_packed_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_cell_packed_timeout.get_name_leafdata())
                            if (self.negotiated_max_cells_packed_per_packet.is_set or self.negotiated_max_cells_packed_per_packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.negotiated_max_cells_packed_per_packet.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "local-max-cells-packed-per-packet" or name == "max-cell-packed-timeout" or name == "negotiated-max-cells-packed-per-packet"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "local-max-cells-packed-per-packet"):
                                self.local_max_cells_packed_per_packet = value
                                self.local_max_cells_packed_per_packet.value_namespace = name_space
                                self.local_max_cells_packed_per_packet.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-cell-packed-timeout"):
                                self.max_cell_packed_timeout = value
                                self.max_cell_packed_timeout.value_namespace = name_space
                                self.max_cell_packed_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "negotiated-max-cells-packed-per-packet"):
                                self.negotiated_max_cells_packed_per_packet = value
                                self.negotiated_max_cells_packed_per_packet.value_namespace = name_space
                                self.negotiated_max_cells_packed_per_packet.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.cell_packing_mode.is_set or
                            self.interface_name.is_set or
                            self.pci.is_set or
                            self.received_average_cells_packets.is_set or
                            self.sent_cells_packets.is_set or
                            self.sub_interface_name.is_set or
                            self.vci.is_set or
                            self.vpi.is_set or
                            (self.cell_packing is not None and self.cell_packing.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cell_packing_mode.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.pci.yfilter != YFilter.not_set or
                            self.received_average_cells_packets.yfilter != YFilter.not_set or
                            self.sent_cells_packets.yfilter != YFilter.not_set or
                            self.sub_interface_name.yfilter != YFilter.not_set or
                            self.vci.yfilter != YFilter.not_set or
                            self.vpi.yfilter != YFilter.not_set or
                            (self.cell_packing is not None and self.cell_packing.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "cell-pack" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cell_packing_mode.is_set or self.cell_packing_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cell_packing_mode.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.pci.is_set or self.pci.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pci.get_name_leafdata())
                        if (self.received_average_cells_packets.is_set or self.received_average_cells_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_average_cells_packets.get_name_leafdata())
                        if (self.sent_cells_packets.is_set or self.sent_cells_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent_cells_packets.get_name_leafdata())
                        if (self.sub_interface_name.is_set or self.sub_interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sub_interface_name.get_name_leafdata())
                        if (self.vci.is_set or self.vci.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vci.get_name_leafdata())
                        if (self.vpi.is_set or self.vpi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vpi.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "cell-packing"):
                            if (self.cell_packing is None):
                                self.cell_packing = AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking()
                                self.cell_packing.parent = self
                                self._children_name_map["cell_packing"] = "cell-packing"
                            return self.cell_packing

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cell-packing" or name == "cell-packing-mode" or name == "interface-name" or name == "pci" or name == "received-average-cells-packets" or name == "sent-cells-packets" or name == "sub-interface-name" or name == "vci" or name == "vpi"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cell-packing-mode"):
                            self.cell_packing_mode = value
                            self.cell_packing_mode.value_namespace = name_space
                            self.cell_packing_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "pci"):
                            self.pci = value
                            self.pci.value_namespace = name_space
                            self.pci.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-average-cells-packets"):
                            self.received_average_cells_packets = value
                            self.received_average_cells_packets.value_namespace = name_space
                            self.received_average_cells_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent-cells-packets"):
                            self.sent_cells_packets = value
                            self.sent_cells_packets.value_namespace = name_space
                            self.sent_cells_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "sub-interface-name"):
                            self.sub_interface_name = value
                            self.sub_interface_name.value_namespace = name_space
                            self.sub_interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "vci"):
                            self.vci = value
                            self.vci.value_namespace = name_space
                            self.vci.value_namespace_prefix = name_space_prefix
                        if(value_path == "vpi"):
                            self.vpi = value
                            self.vpi.value_namespace = name_space
                            self.vpi.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.cell_pack:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.cell_pack:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cell-packs" + path_buffer

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

                    if (child_yang_name == "cell-pack"):
                        for c in self.cell_pack:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AtmVcm.Nodes.Node.CellPacks.CellPack()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.cell_pack.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cell-pack"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Pvps(Entity):
                """
                Contains all L2 PVP information for node
                
                .. attribute:: pvp
                
                	All L2 PVP information on a node
                	**type**\: list of    :py:class:`Pvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Pvps.Pvp>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.Pvps, self).__init__()

                    self.yang_name = "pvps"
                    self.yang_parent_name = "node"

                    self.pvp = YList(self)

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
                                super(AtmVcm.Nodes.Node.Pvps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AtmVcm.Nodes.Node.Pvps, self).__setattr__(name, value)


                class Pvp(Entity):
                    """
                    All L2 PVP information on a node
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: amin_status
                    
                    	TRUE value indicates that the VC is administratively UP
                    	**type**\:  bool
                    
                    .. attribute:: burst_rate
                    
                    	Burst size in cells
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cell_packing_data
                    
                    	Cell packing specific data
                    	**type**\:   :py:class:`CellPackingData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData>`
                    
                    .. attribute:: encaps_inherit_level
                    
                    	Encapsulation inherit level \- identifies if encapsulation is set to default, configured on the VC, or inherited from the vcclass
                    	**type**\:   :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation type
                    	**type**\:   :py:class:`VcEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncap>`
                    
                    .. attribute:: internal_state
                    
                    	VC Internal state
                    	**type**\:   :py:class:`VcState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcState>`
                    
                    .. attribute:: last_state_change_time
                    
                    	Time when VC was last changed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: main_interface
                    
                    	Main Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: oper_status
                    
                    	TRUE value indicates that the VC is operationally UP
                    	**type**\:  bool
                    
                    .. attribute:: peak_cell_rate
                    
                    	Peak cell rate in Kbps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: qos_inherit_level
                    
                    	Quality of Service inherit level \- identifies if QoS is set to default, configured on the VC, or inherited from the vcclass
                    	**type**\:   :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                    
                    .. attribute:: receive_mtu
                    
                    	Receive MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: shape
                    
                    	ATM VC traffic shaping type
                    	**type**\:   :py:class:`VcTrafShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShaping>`
                    
                    .. attribute:: sub_interface
                    
                    	Subinterface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: sustained_cell_rate
                    
                    	Sustained cell rate in Kbps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: test_mode
                    
                    	VC test mode
                    	**type**\:   :py:class:`VcTestMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTestMode>`
                    
                    .. attribute:: transmit_mtu
                    
                    	Transmit MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	VC Type
                    	**type**\:   :py:class:`Vc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.Vc>`
                    
                    .. attribute:: vc_interface
                    
                    	VC Interfcace handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: vc_on_p2p_sub_interface
                    
                    	VC on Point\-to\-point Sub\-interface
                    	**type**\:  bool
                    
                    .. attribute:: vc_onvp_tunnel
                    
                    	VC on VP\-tunnel flag
                    	**type**\:  bool
                    
                    .. attribute:: vci_xr
                    
                    	VC VCI value
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: vpi
                    
                    	VPI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: vpi_xr
                    
                    	VC VPI value
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.Pvps.Pvp, self).__init__()

                        self.yang_name = "pvp"
                        self.yang_parent_name = "pvps"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.amin_status = YLeaf(YType.boolean, "amin-status")

                        self.burst_rate = YLeaf(YType.uint32, "burst-rate")

                        self.encaps_inherit_level = YLeaf(YType.enumeration, "encaps-inherit-level")

                        self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                        self.internal_state = YLeaf(YType.enumeration, "internal-state")

                        self.last_state_change_time = YLeaf(YType.uint32, "last-state-change-time")

                        self.main_interface = YLeaf(YType.str, "main-interface")

                        self.oper_status = YLeaf(YType.boolean, "oper-status")

                        self.peak_cell_rate = YLeaf(YType.uint32, "peak-cell-rate")

                        self.qos_inherit_level = YLeaf(YType.enumeration, "qos-inherit-level")

                        self.receive_mtu = YLeaf(YType.uint32, "receive-mtu")

                        self.shape = YLeaf(YType.enumeration, "shape")

                        self.sub_interface = YLeaf(YType.str, "sub-interface")

                        self.sustained_cell_rate = YLeaf(YType.uint32, "sustained-cell-rate")

                        self.test_mode = YLeaf(YType.enumeration, "test-mode")

                        self.transmit_mtu = YLeaf(YType.uint32, "transmit-mtu")

                        self.type = YLeaf(YType.enumeration, "type")

                        self.vc_interface = YLeaf(YType.str, "vc-interface")

                        self.vc_on_p2p_sub_interface = YLeaf(YType.boolean, "vc-on-p2p-sub-interface")

                        self.vc_onvp_tunnel = YLeaf(YType.boolean, "vc-onvp-tunnel")

                        self.vci_xr = YLeaf(YType.uint16, "vci-xr")

                        self.vpi = YLeaf(YType.int32, "vpi")

                        self.vpi_xr = YLeaf(YType.uint16, "vpi-xr")

                        self.cell_packing_data = AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData()
                        self.cell_packing_data.parent = self
                        self._children_name_map["cell_packing_data"] = "cell-packing-data"
                        self._children_yang_names.add("cell-packing-data")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "amin_status",
                                        "burst_rate",
                                        "encaps_inherit_level",
                                        "encapsulation",
                                        "internal_state",
                                        "last_state_change_time",
                                        "main_interface",
                                        "oper_status",
                                        "peak_cell_rate",
                                        "qos_inherit_level",
                                        "receive_mtu",
                                        "shape",
                                        "sub_interface",
                                        "sustained_cell_rate",
                                        "test_mode",
                                        "transmit_mtu",
                                        "type",
                                        "vc_interface",
                                        "vc_on_p2p_sub_interface",
                                        "vc_onvp_tunnel",
                                        "vci_xr",
                                        "vpi",
                                        "vpi_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AtmVcm.Nodes.Node.Pvps.Pvp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AtmVcm.Nodes.Node.Pvps.Pvp, self).__setattr__(name, value)


                    class CellPackingData(Entity):
                        """
                        Cell packing specific data
                        
                        .. attribute:: local_max_cells_packed_per_packet
                        
                        	Local configuration of maximum number of cells to be packed per packet
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: max_cell_packed_timeout
                        
                        	Maximum cell packing timeout inmicro seconds
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**units**\: microsecond
                        
                        .. attribute:: negotiated_max_cells_packed_per_packet
                        
                        	Negotiated value of maximum number of cells to be packed per packed
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData, self).__init__()

                            self.yang_name = "cell-packing-data"
                            self.yang_parent_name = "pvp"

                            self.local_max_cells_packed_per_packet = YLeaf(YType.uint16, "local-max-cells-packed-per-packet")

                            self.max_cell_packed_timeout = YLeaf(YType.uint16, "max-cell-packed-timeout")

                            self.negotiated_max_cells_packed_per_packet = YLeaf(YType.uint16, "negotiated-max-cells-packed-per-packet")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("local_max_cells_packed_per_packet",
                                            "max_cell_packed_timeout",
                                            "negotiated_max_cells_packed_per_packet") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.local_max_cells_packed_per_packet.is_set or
                                self.max_cell_packed_timeout.is_set or
                                self.negotiated_max_cells_packed_per_packet.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.local_max_cells_packed_per_packet.yfilter != YFilter.not_set or
                                self.max_cell_packed_timeout.yfilter != YFilter.not_set or
                                self.negotiated_max_cells_packed_per_packet.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "cell-packing-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.local_max_cells_packed_per_packet.is_set or self.local_max_cells_packed_per_packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_max_cells_packed_per_packet.get_name_leafdata())
                            if (self.max_cell_packed_timeout.is_set or self.max_cell_packed_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_cell_packed_timeout.get_name_leafdata())
                            if (self.negotiated_max_cells_packed_per_packet.is_set or self.negotiated_max_cells_packed_per_packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.negotiated_max_cells_packed_per_packet.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "local-max-cells-packed-per-packet" or name == "max-cell-packed-timeout" or name == "negotiated-max-cells-packed-per-packet"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "local-max-cells-packed-per-packet"):
                                self.local_max_cells_packed_per_packet = value
                                self.local_max_cells_packed_per_packet.value_namespace = name_space
                                self.local_max_cells_packed_per_packet.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-cell-packed-timeout"):
                                self.max_cell_packed_timeout = value
                                self.max_cell_packed_timeout.value_namespace = name_space
                                self.max_cell_packed_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "negotiated-max-cells-packed-per-packet"):
                                self.negotiated_max_cells_packed_per_packet = value
                                self.negotiated_max_cells_packed_per_packet.value_namespace = name_space
                                self.negotiated_max_cells_packed_per_packet.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.amin_status.is_set or
                            self.burst_rate.is_set or
                            self.encaps_inherit_level.is_set or
                            self.encapsulation.is_set or
                            self.internal_state.is_set or
                            self.last_state_change_time.is_set or
                            self.main_interface.is_set or
                            self.oper_status.is_set or
                            self.peak_cell_rate.is_set or
                            self.qos_inherit_level.is_set or
                            self.receive_mtu.is_set or
                            self.shape.is_set or
                            self.sub_interface.is_set or
                            self.sustained_cell_rate.is_set or
                            self.test_mode.is_set or
                            self.transmit_mtu.is_set or
                            self.type.is_set or
                            self.vc_interface.is_set or
                            self.vc_on_p2p_sub_interface.is_set or
                            self.vc_onvp_tunnel.is_set or
                            self.vci_xr.is_set or
                            self.vpi.is_set or
                            self.vpi_xr.is_set or
                            (self.cell_packing_data is not None and self.cell_packing_data.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.amin_status.yfilter != YFilter.not_set or
                            self.burst_rate.yfilter != YFilter.not_set or
                            self.encaps_inherit_level.yfilter != YFilter.not_set or
                            self.encapsulation.yfilter != YFilter.not_set or
                            self.internal_state.yfilter != YFilter.not_set or
                            self.last_state_change_time.yfilter != YFilter.not_set or
                            self.main_interface.yfilter != YFilter.not_set or
                            self.oper_status.yfilter != YFilter.not_set or
                            self.peak_cell_rate.yfilter != YFilter.not_set or
                            self.qos_inherit_level.yfilter != YFilter.not_set or
                            self.receive_mtu.yfilter != YFilter.not_set or
                            self.shape.yfilter != YFilter.not_set or
                            self.sub_interface.yfilter != YFilter.not_set or
                            self.sustained_cell_rate.yfilter != YFilter.not_set or
                            self.test_mode.yfilter != YFilter.not_set or
                            self.transmit_mtu.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set or
                            self.vc_interface.yfilter != YFilter.not_set or
                            self.vc_on_p2p_sub_interface.yfilter != YFilter.not_set or
                            self.vc_onvp_tunnel.yfilter != YFilter.not_set or
                            self.vci_xr.yfilter != YFilter.not_set or
                            self.vpi.yfilter != YFilter.not_set or
                            self.vpi_xr.yfilter != YFilter.not_set or
                            (self.cell_packing_data is not None and self.cell_packing_data.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pvp" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.amin_status.is_set or self.amin_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.amin_status.get_name_leafdata())
                        if (self.burst_rate.is_set or self.burst_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.burst_rate.get_name_leafdata())
                        if (self.encaps_inherit_level.is_set or self.encaps_inherit_level.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encaps_inherit_level.get_name_leafdata())
                        if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encapsulation.get_name_leafdata())
                        if (self.internal_state.is_set or self.internal_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.internal_state.get_name_leafdata())
                        if (self.last_state_change_time.is_set or self.last_state_change_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_state_change_time.get_name_leafdata())
                        if (self.main_interface.is_set or self.main_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.main_interface.get_name_leafdata())
                        if (self.oper_status.is_set or self.oper_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oper_status.get_name_leafdata())
                        if (self.peak_cell_rate.is_set or self.peak_cell_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_cell_rate.get_name_leafdata())
                        if (self.qos_inherit_level.is_set or self.qos_inherit_level.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qos_inherit_level.get_name_leafdata())
                        if (self.receive_mtu.is_set or self.receive_mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_mtu.get_name_leafdata())
                        if (self.shape.is_set or self.shape.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.shape.get_name_leafdata())
                        if (self.sub_interface.is_set or self.sub_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sub_interface.get_name_leafdata())
                        if (self.sustained_cell_rate.is_set or self.sustained_cell_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sustained_cell_rate.get_name_leafdata())
                        if (self.test_mode.is_set or self.test_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.test_mode.get_name_leafdata())
                        if (self.transmit_mtu.is_set or self.transmit_mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transmit_mtu.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())
                        if (self.vc_interface.is_set or self.vc_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vc_interface.get_name_leafdata())
                        if (self.vc_on_p2p_sub_interface.is_set or self.vc_on_p2p_sub_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vc_on_p2p_sub_interface.get_name_leafdata())
                        if (self.vc_onvp_tunnel.is_set or self.vc_onvp_tunnel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vc_onvp_tunnel.get_name_leafdata())
                        if (self.vci_xr.is_set or self.vci_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vci_xr.get_name_leafdata())
                        if (self.vpi.is_set or self.vpi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vpi.get_name_leafdata())
                        if (self.vpi_xr.is_set or self.vpi_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vpi_xr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "cell-packing-data"):
                            if (self.cell_packing_data is None):
                                self.cell_packing_data = AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData()
                                self.cell_packing_data.parent = self
                                self._children_name_map["cell_packing_data"] = "cell-packing-data"
                            return self.cell_packing_data

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cell-packing-data" or name == "interface-name" or name == "amin-status" or name == "burst-rate" or name == "encaps-inherit-level" or name == "encapsulation" or name == "internal-state" or name == "last-state-change-time" or name == "main-interface" or name == "oper-status" or name == "peak-cell-rate" or name == "qos-inherit-level" or name == "receive-mtu" or name == "shape" or name == "sub-interface" or name == "sustained-cell-rate" or name == "test-mode" or name == "transmit-mtu" or name == "type" or name == "vc-interface" or name == "vc-on-p2p-sub-interface" or name == "vc-onvp-tunnel" or name == "vci-xr" or name == "vpi" or name == "vpi-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "amin-status"):
                            self.amin_status = value
                            self.amin_status.value_namespace = name_space
                            self.amin_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "burst-rate"):
                            self.burst_rate = value
                            self.burst_rate.value_namespace = name_space
                            self.burst_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "encaps-inherit-level"):
                            self.encaps_inherit_level = value
                            self.encaps_inherit_level.value_namespace = name_space
                            self.encaps_inherit_level.value_namespace_prefix = name_space_prefix
                        if(value_path == "encapsulation"):
                            self.encapsulation = value
                            self.encapsulation.value_namespace = name_space
                            self.encapsulation.value_namespace_prefix = name_space_prefix
                        if(value_path == "internal-state"):
                            self.internal_state = value
                            self.internal_state.value_namespace = name_space
                            self.internal_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-state-change-time"):
                            self.last_state_change_time = value
                            self.last_state_change_time.value_namespace = name_space
                            self.last_state_change_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "main-interface"):
                            self.main_interface = value
                            self.main_interface.value_namespace = name_space
                            self.main_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "oper-status"):
                            self.oper_status = value
                            self.oper_status.value_namespace = name_space
                            self.oper_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-cell-rate"):
                            self.peak_cell_rate = value
                            self.peak_cell_rate.value_namespace = name_space
                            self.peak_cell_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "qos-inherit-level"):
                            self.qos_inherit_level = value
                            self.qos_inherit_level.value_namespace = name_space
                            self.qos_inherit_level.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-mtu"):
                            self.receive_mtu = value
                            self.receive_mtu.value_namespace = name_space
                            self.receive_mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "shape"):
                            self.shape = value
                            self.shape.value_namespace = name_space
                            self.shape.value_namespace_prefix = name_space_prefix
                        if(value_path == "sub-interface"):
                            self.sub_interface = value
                            self.sub_interface.value_namespace = name_space
                            self.sub_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "sustained-cell-rate"):
                            self.sustained_cell_rate = value
                            self.sustained_cell_rate.value_namespace = name_space
                            self.sustained_cell_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "test-mode"):
                            self.test_mode = value
                            self.test_mode.value_namespace = name_space
                            self.test_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "transmit-mtu"):
                            self.transmit_mtu = value
                            self.transmit_mtu.value_namespace = name_space
                            self.transmit_mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix
                        if(value_path == "vc-interface"):
                            self.vc_interface = value
                            self.vc_interface.value_namespace = name_space
                            self.vc_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "vc-on-p2p-sub-interface"):
                            self.vc_on_p2p_sub_interface = value
                            self.vc_on_p2p_sub_interface.value_namespace = name_space
                            self.vc_on_p2p_sub_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "vc-onvp-tunnel"):
                            self.vc_onvp_tunnel = value
                            self.vc_onvp_tunnel.value_namespace = name_space
                            self.vc_onvp_tunnel.value_namespace_prefix = name_space_prefix
                        if(value_path == "vci-xr"):
                            self.vci_xr = value
                            self.vci_xr.value_namespace = name_space
                            self.vci_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "vpi"):
                            self.vpi = value
                            self.vpi.value_namespace = name_space
                            self.vpi.value_namespace_prefix = name_space_prefix
                        if(value_path == "vpi-xr"):
                            self.vpi_xr = value
                            self.vpi_xr.value_namespace = name_space
                            self.vpi_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.pvp:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.pvp:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "pvps" + path_buffer

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

                    if (child_yang_name == "pvp"):
                        for c in self.pvp:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AtmVcm.Nodes.Node.Pvps.Pvp()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.pvp.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pvp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ClassLinks(Entity):
                """
                Contains all class link information for node
                
                .. attribute:: class_link
                
                	All ATM VC information on a node
                	**type**\: list of    :py:class:`ClassLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.ClassLinks, self).__init__()

                    self.yang_name = "class-links"
                    self.yang_parent_name = "node"

                    self.class_link = YList(self)

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
                                super(AtmVcm.Nodes.Node.ClassLinks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AtmVcm.Nodes.Node.ClassLinks, self).__setattr__(name, value)


                class ClassLink(Entity):
                    """
                    All ATM VC information on a node
                    
                    .. attribute:: vpi  <key>
                    
                    	VPI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: oam_config
                    
                    	Oam values for class link
                    	**type**\:   :py:class:`OamConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig>`
                    
                    .. attribute:: sub_interface_name
                    
                    	Sub\-interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: vc_class_not_supported
                    
                    	Not supported VC class
                    	**type**\:   :py:class:`VcClassNotSupported <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported>`
                    
                    .. attribute:: vci
                    
                    	VCI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.ClassLinks.ClassLink, self).__init__()

                        self.yang_name = "class-link"
                        self.yang_parent_name = "class-links"

                        self.vpi = YLeaf(YType.int32, "vpi")

                        self.sub_interface_name = YLeaf(YType.str, "sub-interface-name")

                        self.vci = YLeaf(YType.int32, "vci")

                        self.oam_config = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig()
                        self.oam_config.parent = self
                        self._children_name_map["oam_config"] = "oam-config"
                        self._children_yang_names.add("oam-config")

                        self.vc_class_not_supported = AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported()
                        self.vc_class_not_supported.parent = self
                        self._children_name_map["vc_class_not_supported"] = "vc-class-not-supported"
                        self._children_yang_names.add("vc-class-not-supported")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vpi",
                                        "sub_interface_name",
                                        "vci") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AtmVcm.Nodes.Node.ClassLinks.ClassLink, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink, self).__setattr__(name, value)


                    class VcClassNotSupported(Entity):
                        """
                        Not supported VC class
                        
                        .. attribute:: encapsulation_not_supported
                        
                        	Encapsulation type not supported
                        	**type**\:   :py:class:`VcEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncap>`
                        
                        .. attribute:: not_supported_inherit_level
                        
                        	NotSupportedInheritLevel
                        	**type**\:   :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported, self).__init__()

                            self.yang_name = "vc-class-not-supported"
                            self.yang_parent_name = "class-link"

                            self.encapsulation_not_supported = YLeaf(YType.enumeration, "encapsulation-not-supported")

                            self.not_supported_inherit_level = YLeaf(YType.enumeration, "not-supported-inherit-level")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("encapsulation_not_supported",
                                            "not_supported_inherit_level") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.encapsulation_not_supported.is_set or
                                self.not_supported_inherit_level.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.encapsulation_not_supported.yfilter != YFilter.not_set or
                                self.not_supported_inherit_level.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "vc-class-not-supported" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.encapsulation_not_supported.is_set or self.encapsulation_not_supported.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.encapsulation_not_supported.get_name_leafdata())
                            if (self.not_supported_inherit_level.is_set or self.not_supported_inherit_level.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.not_supported_inherit_level.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "encapsulation-not-supported" or name == "not-supported-inherit-level"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "encapsulation-not-supported"):
                                self.encapsulation_not_supported = value
                                self.encapsulation_not_supported.value_namespace = name_space
                                self.encapsulation_not_supported.value_namespace_prefix = name_space_prefix
                            if(value_path == "not-supported-inherit-level"):
                                self.not_supported_inherit_level = value
                                self.not_supported_inherit_level.value_namespace = name_space
                                self.not_supported_inherit_level.value_namespace_prefix = name_space_prefix


                    class OamConfig(Entity):
                        """
                        Oam values for class link
                        
                        .. attribute:: ais_rdi
                        
                        	AIS RDI details of a VC class
                        	**type**\:   :py:class:`AisRdi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi>`
                        
                        .. attribute:: class_link_encapsulation
                        
                        	Encapsulation details of VC class
                        	**type**\:   :py:class:`ClassLinkEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation>`
                        
                        .. attribute:: class_link_shaping
                        
                        	Traffic Shaping detail of VC class
                        	**type**\:   :py:class:`ClassLinkShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping>`
                        
                        .. attribute:: oam_pvc
                        
                        	OAM PVC details of VC class
                        	**type**\:   :py:class:`OamPvc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc>`
                        
                        .. attribute:: oam_retry
                        
                        	OAM Retry details of VC class
                        	**type**\:   :py:class:`OamRetry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry>`
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig, self).__init__()

                            self.yang_name = "oam-config"
                            self.yang_parent_name = "class-link"

                            self.ais_rdi = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi()
                            self.ais_rdi.parent = self
                            self._children_name_map["ais_rdi"] = "ais-rdi"
                            self._children_yang_names.add("ais-rdi")

                            self.class_link_encapsulation = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation()
                            self.class_link_encapsulation.parent = self
                            self._children_name_map["class_link_encapsulation"] = "class-link-encapsulation"
                            self._children_yang_names.add("class-link-encapsulation")

                            self.class_link_shaping = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping()
                            self.class_link_shaping.parent = self
                            self._children_name_map["class_link_shaping"] = "class-link-shaping"
                            self._children_yang_names.add("class-link-shaping")

                            self.oam_pvc = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc()
                            self.oam_pvc.parent = self
                            self._children_name_map["oam_pvc"] = "oam-pvc"
                            self._children_yang_names.add("oam-pvc")

                            self.oam_retry = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry()
                            self.oam_retry.parent = self
                            self._children_name_map["oam_retry"] = "oam-retry"
                            self._children_yang_names.add("oam-retry")


                        class ClassLinkShaping(Entity):
                            """
                            Traffic Shaping detail of VC class
                            
                            .. attribute:: average_output_rate
                            
                            	Average output rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: burst_output_rate
                            
                            	Burst output rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peak_output_rate
                            
                            	Peak output rate in Kbps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: shaping_inherit_level
                            
                            	Shaping inherit level
                            	**type**\:   :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                            
                            .. attribute:: shaping_type
                            
                            	ATM VC traffic shaping type
                            	**type**\:   :py:class:`VcTrafShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShaping>`
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping, self).__init__()

                                self.yang_name = "class-link-shaping"
                                self.yang_parent_name = "oam-config"

                                self.average_output_rate = YLeaf(YType.uint32, "average-output-rate")

                                self.burst_output_rate = YLeaf(YType.uint32, "burst-output-rate")

                                self.peak_output_rate = YLeaf(YType.uint32, "peak-output-rate")

                                self.shaping_inherit_level = YLeaf(YType.enumeration, "shaping-inherit-level")

                                self.shaping_type = YLeaf(YType.enumeration, "shaping-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("average_output_rate",
                                                "burst_output_rate",
                                                "peak_output_rate",
                                                "shaping_inherit_level",
                                                "shaping_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.average_output_rate.is_set or
                                    self.burst_output_rate.is_set or
                                    self.peak_output_rate.is_set or
                                    self.shaping_inherit_level.is_set or
                                    self.shaping_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.average_output_rate.yfilter != YFilter.not_set or
                                    self.burst_output_rate.yfilter != YFilter.not_set or
                                    self.peak_output_rate.yfilter != YFilter.not_set or
                                    self.shaping_inherit_level.yfilter != YFilter.not_set or
                                    self.shaping_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "class-link-shaping" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.average_output_rate.is_set or self.average_output_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.average_output_rate.get_name_leafdata())
                                if (self.burst_output_rate.is_set or self.burst_output_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.burst_output_rate.get_name_leafdata())
                                if (self.peak_output_rate.is_set or self.peak_output_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.peak_output_rate.get_name_leafdata())
                                if (self.shaping_inherit_level.is_set or self.shaping_inherit_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.shaping_inherit_level.get_name_leafdata())
                                if (self.shaping_type.is_set or self.shaping_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.shaping_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "average-output-rate" or name == "burst-output-rate" or name == "peak-output-rate" or name == "shaping-inherit-level" or name == "shaping-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "average-output-rate"):
                                    self.average_output_rate = value
                                    self.average_output_rate.value_namespace = name_space
                                    self.average_output_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "burst-output-rate"):
                                    self.burst_output_rate = value
                                    self.burst_output_rate.value_namespace = name_space
                                    self.burst_output_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "peak-output-rate"):
                                    self.peak_output_rate = value
                                    self.peak_output_rate.value_namespace = name_space
                                    self.peak_output_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "shaping-inherit-level"):
                                    self.shaping_inherit_level = value
                                    self.shaping_inherit_level.value_namespace = name_space
                                    self.shaping_inherit_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "shaping-type"):
                                    self.shaping_type = value
                                    self.shaping_type.value_namespace = name_space
                                    self.shaping_type.value_namespace_prefix = name_space_prefix


                        class ClassLinkEncapsulation(Entity):
                            """
                            Encapsulation details of VC class
                            
                            .. attribute:: encapsulation_inherit_level
                            
                            	Encapsulation inherit level
                            	**type**\:   :py:class:`VcInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevel>`
                            
                            .. attribute:: encapsulation_type
                            
                            	Encapsulation type
                            	**type**\:   :py:class:`VcEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncap>`
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation, self).__init__()

                                self.yang_name = "class-link-encapsulation"
                                self.yang_parent_name = "oam-config"

                                self.encapsulation_inherit_level = YLeaf(YType.enumeration, "encapsulation-inherit-level")

                                self.encapsulation_type = YLeaf(YType.enumeration, "encapsulation-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("encapsulation_inherit_level",
                                                "encapsulation_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.encapsulation_inherit_level.is_set or
                                    self.encapsulation_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.encapsulation_inherit_level.yfilter != YFilter.not_set or
                                    self.encapsulation_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "class-link-encapsulation" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.encapsulation_inherit_level.is_set or self.encapsulation_inherit_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encapsulation_inherit_level.get_name_leafdata())
                                if (self.encapsulation_type.is_set or self.encapsulation_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.encapsulation_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "encapsulation-inherit-level" or name == "encapsulation-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "encapsulation-inherit-level"):
                                    self.encapsulation_inherit_level = value
                                    self.encapsulation_inherit_level.value_namespace = name_space
                                    self.encapsulation_inherit_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "encapsulation-type"):
                                    self.encapsulation_type = value
                                    self.encapsulation_type.value_namespace = name_space
                                    self.encapsulation_type.value_namespace_prefix = name_space_prefix


                        class OamPvc(Entity):
                            """
                            OAM PVC details of VC class
                            
                            .. attribute:: ais_rdi_failure
                            
                            	AIS RDI failure
                            	**type**\:  bool
                            
                            .. attribute:: keep_vc_up
                            
                            	Keep vc up
                            	**type**\:  bool
                            
                            .. attribute:: manage_inherit_level
                            
                            	Manage inherit level
                            	**type**\:   :py:class:`ClassLinkOamInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevel>`
                            
                            .. attribute:: manage_level
                            
                            	Manage Level
                            	**type**\:   :py:class:`VcManageLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcManageLevel>`
                            
                            .. attribute:: pvc_frequency
                            
                            	PVC Frequency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc, self).__init__()

                                self.yang_name = "oam-pvc"
                                self.yang_parent_name = "oam-config"

                                self.ais_rdi_failure = YLeaf(YType.boolean, "ais-rdi-failure")

                                self.keep_vc_up = YLeaf(YType.boolean, "keep-vc-up")

                                self.manage_inherit_level = YLeaf(YType.enumeration, "manage-inherit-level")

                                self.manage_level = YLeaf(YType.enumeration, "manage-level")

                                self.pvc_frequency = YLeaf(YType.uint32, "pvc-frequency")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ais_rdi_failure",
                                                "keep_vc_up",
                                                "manage_inherit_level",
                                                "manage_level",
                                                "pvc_frequency") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ais_rdi_failure.is_set or
                                    self.keep_vc_up.is_set or
                                    self.manage_inherit_level.is_set or
                                    self.manage_level.is_set or
                                    self.pvc_frequency.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ais_rdi_failure.yfilter != YFilter.not_set or
                                    self.keep_vc_up.yfilter != YFilter.not_set or
                                    self.manage_inherit_level.yfilter != YFilter.not_set or
                                    self.manage_level.yfilter != YFilter.not_set or
                                    self.pvc_frequency.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "oam-pvc" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ais_rdi_failure.is_set or self.ais_rdi_failure.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ais_rdi_failure.get_name_leafdata())
                                if (self.keep_vc_up.is_set or self.keep_vc_up.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.keep_vc_up.get_name_leafdata())
                                if (self.manage_inherit_level.is_set or self.manage_inherit_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.manage_inherit_level.get_name_leafdata())
                                if (self.manage_level.is_set or self.manage_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.manage_level.get_name_leafdata())
                                if (self.pvc_frequency.is_set or self.pvc_frequency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pvc_frequency.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ais-rdi-failure" or name == "keep-vc-up" or name == "manage-inherit-level" or name == "manage-level" or name == "pvc-frequency"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ais-rdi-failure"):
                                    self.ais_rdi_failure = value
                                    self.ais_rdi_failure.value_namespace = name_space
                                    self.ais_rdi_failure.value_namespace_prefix = name_space_prefix
                                if(value_path == "keep-vc-up"):
                                    self.keep_vc_up = value
                                    self.keep_vc_up.value_namespace = name_space
                                    self.keep_vc_up.value_namespace_prefix = name_space_prefix
                                if(value_path == "manage-inherit-level"):
                                    self.manage_inherit_level = value
                                    self.manage_inherit_level.value_namespace = name_space
                                    self.manage_inherit_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "manage-level"):
                                    self.manage_level = value
                                    self.manage_level.value_namespace = name_space
                                    self.manage_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "pvc-frequency"):
                                    self.pvc_frequency = value
                                    self.pvc_frequency.value_namespace = name_space
                                    self.pvc_frequency.value_namespace_prefix = name_space_prefix


                        class OamRetry(Entity):
                            """
                            OAM Retry details of VC class
                            
                            .. attribute:: down_count
                            
                            	Down Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: retry_frequency
                            
                            	Retry frequency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: retry_inherit_level
                            
                            	Retry inherit level
                            	**type**\:   :py:class:`ClassLinkOamInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevel>`
                            
                            .. attribute:: retry_up_count
                            
                            	Retry Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry, self).__init__()

                                self.yang_name = "oam-retry"
                                self.yang_parent_name = "oam-config"

                                self.down_count = YLeaf(YType.uint32, "down-count")

                                self.retry_frequency = YLeaf(YType.uint32, "retry-frequency")

                                self.retry_inherit_level = YLeaf(YType.enumeration, "retry-inherit-level")

                                self.retry_up_count = YLeaf(YType.uint32, "retry-up-count")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("down_count",
                                                "retry_frequency",
                                                "retry_inherit_level",
                                                "retry_up_count") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.down_count.is_set or
                                    self.retry_frequency.is_set or
                                    self.retry_inherit_level.is_set or
                                    self.retry_up_count.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.down_count.yfilter != YFilter.not_set or
                                    self.retry_frequency.yfilter != YFilter.not_set or
                                    self.retry_inherit_level.yfilter != YFilter.not_set or
                                    self.retry_up_count.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "oam-retry" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.down_count.is_set or self.down_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.down_count.get_name_leafdata())
                                if (self.retry_frequency.is_set or self.retry_frequency.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.retry_frequency.get_name_leafdata())
                                if (self.retry_inherit_level.is_set or self.retry_inherit_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.retry_inherit_level.get_name_leafdata())
                                if (self.retry_up_count.is_set or self.retry_up_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.retry_up_count.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "down-count" or name == "retry-frequency" or name == "retry-inherit-level" or name == "retry-up-count"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "down-count"):
                                    self.down_count = value
                                    self.down_count.value_namespace = name_space
                                    self.down_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "retry-frequency"):
                                    self.retry_frequency = value
                                    self.retry_frequency.value_namespace = name_space
                                    self.retry_frequency.value_namespace_prefix = name_space_prefix
                                if(value_path == "retry-inherit-level"):
                                    self.retry_inherit_level = value
                                    self.retry_inherit_level.value_namespace = name_space
                                    self.retry_inherit_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "retry-up-count"):
                                    self.retry_up_count = value
                                    self.retry_up_count.value_namespace = name_space
                                    self.retry_up_count.value_namespace_prefix = name_space_prefix


                        class AisRdi(Entity):
                            """
                            AIS RDI details of a VC class
                            
                            .. attribute:: ais_rdi_inherit_level
                            
                            	AIS RDI inherit level
                            	**type**\:   :py:class:`ClassLinkOamInheritLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevel>`
                            
                            .. attribute:: ais_rdi_up_count
                            
                            	AIS RDI up count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ais_rdi_up_time
                            
                            	Time (in seconds) with no AIS/RDI cells before declaring a VC as up
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi, self).__init__()

                                self.yang_name = "ais-rdi"
                                self.yang_parent_name = "oam-config"

                                self.ais_rdi_inherit_level = YLeaf(YType.enumeration, "ais-rdi-inherit-level")

                                self.ais_rdi_up_count = YLeaf(YType.uint32, "ais-rdi-up-count")

                                self.ais_rdi_up_time = YLeaf(YType.uint32, "ais-rdi-up-time")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ais_rdi_inherit_level",
                                                "ais_rdi_up_count",
                                                "ais_rdi_up_time") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ais_rdi_inherit_level.is_set or
                                    self.ais_rdi_up_count.is_set or
                                    self.ais_rdi_up_time.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ais_rdi_inherit_level.yfilter != YFilter.not_set or
                                    self.ais_rdi_up_count.yfilter != YFilter.not_set or
                                    self.ais_rdi_up_time.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ais-rdi" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ais_rdi_inherit_level.is_set or self.ais_rdi_inherit_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ais_rdi_inherit_level.get_name_leafdata())
                                if (self.ais_rdi_up_count.is_set or self.ais_rdi_up_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ais_rdi_up_count.get_name_leafdata())
                                if (self.ais_rdi_up_time.is_set or self.ais_rdi_up_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ais_rdi_up_time.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ais-rdi-inherit-level" or name == "ais-rdi-up-count" or name == "ais-rdi-up-time"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ais-rdi-inherit-level"):
                                    self.ais_rdi_inherit_level = value
                                    self.ais_rdi_inherit_level.value_namespace = name_space
                                    self.ais_rdi_inherit_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "ais-rdi-up-count"):
                                    self.ais_rdi_up_count = value
                                    self.ais_rdi_up_count.value_namespace = name_space
                                    self.ais_rdi_up_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "ais-rdi-up-time"):
                                    self.ais_rdi_up_time = value
                                    self.ais_rdi_up_time.value_namespace = name_space
                                    self.ais_rdi_up_time.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.ais_rdi is not None and self.ais_rdi.has_data()) or
                                (self.class_link_encapsulation is not None and self.class_link_encapsulation.has_data()) or
                                (self.class_link_shaping is not None and self.class_link_shaping.has_data()) or
                                (self.oam_pvc is not None and self.oam_pvc.has_data()) or
                                (self.oam_retry is not None and self.oam_retry.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.ais_rdi is not None and self.ais_rdi.has_operation()) or
                                (self.class_link_encapsulation is not None and self.class_link_encapsulation.has_operation()) or
                                (self.class_link_shaping is not None and self.class_link_shaping.has_operation()) or
                                (self.oam_pvc is not None and self.oam_pvc.has_operation()) or
                                (self.oam_retry is not None and self.oam_retry.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "oam-config" + path_buffer

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

                            if (child_yang_name == "ais-rdi"):
                                if (self.ais_rdi is None):
                                    self.ais_rdi = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi()
                                    self.ais_rdi.parent = self
                                    self._children_name_map["ais_rdi"] = "ais-rdi"
                                return self.ais_rdi

                            if (child_yang_name == "class-link-encapsulation"):
                                if (self.class_link_encapsulation is None):
                                    self.class_link_encapsulation = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation()
                                    self.class_link_encapsulation.parent = self
                                    self._children_name_map["class_link_encapsulation"] = "class-link-encapsulation"
                                return self.class_link_encapsulation

                            if (child_yang_name == "class-link-shaping"):
                                if (self.class_link_shaping is None):
                                    self.class_link_shaping = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping()
                                    self.class_link_shaping.parent = self
                                    self._children_name_map["class_link_shaping"] = "class-link-shaping"
                                return self.class_link_shaping

                            if (child_yang_name == "oam-pvc"):
                                if (self.oam_pvc is None):
                                    self.oam_pvc = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc()
                                    self.oam_pvc.parent = self
                                    self._children_name_map["oam_pvc"] = "oam-pvc"
                                return self.oam_pvc

                            if (child_yang_name == "oam-retry"):
                                if (self.oam_retry is None):
                                    self.oam_retry = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry()
                                    self.oam_retry.parent = self
                                    self._children_name_map["oam_retry"] = "oam-retry"
                                return self.oam_retry

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ais-rdi" or name == "class-link-encapsulation" or name == "class-link-shaping" or name == "oam-pvc" or name == "oam-retry"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.vpi.is_set or
                            self.sub_interface_name.is_set or
                            self.vci.is_set or
                            (self.oam_config is not None and self.oam_config.has_data()) or
                            (self.vc_class_not_supported is not None and self.vc_class_not_supported.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vpi.yfilter != YFilter.not_set or
                            self.sub_interface_name.yfilter != YFilter.not_set or
                            self.vci.yfilter != YFilter.not_set or
                            (self.oam_config is not None and self.oam_config.has_operation()) or
                            (self.vc_class_not_supported is not None and self.vc_class_not_supported.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "class-link" + "[vpi='" + self.vpi.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vpi.is_set or self.vpi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vpi.get_name_leafdata())
                        if (self.sub_interface_name.is_set or self.sub_interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sub_interface_name.get_name_leafdata())
                        if (self.vci.is_set or self.vci.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vci.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "oam-config"):
                            if (self.oam_config is None):
                                self.oam_config = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig()
                                self.oam_config.parent = self
                                self._children_name_map["oam_config"] = "oam-config"
                            return self.oam_config

                        if (child_yang_name == "vc-class-not-supported"):
                            if (self.vc_class_not_supported is None):
                                self.vc_class_not_supported = AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported()
                                self.vc_class_not_supported.parent = self
                                self._children_name_map["vc_class_not_supported"] = "vc-class-not-supported"
                            return self.vc_class_not_supported

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "oam-config" or name == "vc-class-not-supported" or name == "vpi" or name == "sub-interface-name" or name == "vci"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vpi"):
                            self.vpi = value
                            self.vpi.value_namespace = name_space
                            self.vpi.value_namespace_prefix = name_space_prefix
                        if(value_path == "sub-interface-name"):
                            self.sub_interface_name = value
                            self.sub_interface_name.value_namespace = name_space
                            self.sub_interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "vci"):
                            self.vci = value
                            self.vci.value_namespace = name_space
                            self.vci.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.class_link:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.class_link:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "class-links" + path_buffer

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

                    if (child_yang_name == "class-link"):
                        for c in self.class_link:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AtmVcm.Nodes.Node.ClassLinks.ClassLink()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.class_link.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "class-link"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                Contains all Interface information for node
                
                .. attribute:: interface
                
                	ATM Interface data
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"

                    self.interface = YList(self)

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
                                super(AtmVcm.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AtmVcm.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    ATM Interface data
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: cell_packing_data
                    
                    	Cell packing specific information
                    	**type**\:   :py:class:`CellPackingData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData>`
                    
                    .. attribute:: configured_layer2pv_cs
                    
                    	Number of Layer 2 PVCs configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_layer2pv_ps
                    
                    	Number of Layer 2 PVPs configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_layer3pv_cs
                    
                    	Number of Layer 3 PVCs configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_layer3vp_tunnels
                    
                    	Number of Layer 3 VP tunnels configured
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: currently_failing_layer2pv_cs
                    
                    	Number of currently failing Layer 2 PVCs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: currently_failing_layer2pv_ps
                    
                    	Number of currently failing Layer 2 PVPs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: currently_failing_layer3pv_cs
                    
                    	Number of currently failing Layer 3 PVCs
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: currently_failing_layer3vp_tunnels
                    
                    	Number of currently failing Layer 3 VP tunnels
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ilmi_vci
                    
                    	ILMI VCI
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ilmi_vpi
                    
                    	ILMI VPI
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: l2_cell_packing_count
                    
                    	Number of L2 attachment circuits with the cell packing feature enabled on this main interface
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: main_interface
                    
                    	Main Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: port_type
                    
                    	ATM interface port type
                    	**type**\:   :py:class:`VcmPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcmPort>`
                    
                    .. attribute:: pvc_failures
                    
                    	Number of PVC Failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pvc_failures_trap_enable
                    
                    	If true, PVC failures trap is enabled
                    	**type**\:  bool
                    
                    .. attribute:: pvc_notification_interval
                    
                    	PVC trap notification interval
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.configured_layer2pv_cs = YLeaf(YType.uint32, "configured-layer2pv-cs")

                        self.configured_layer2pv_ps = YLeaf(YType.uint32, "configured-layer2pv-ps")

                        self.configured_layer3pv_cs = YLeaf(YType.uint32, "configured-layer3pv-cs")

                        self.configured_layer3vp_tunnels = YLeaf(YType.uint32, "configured-layer3vp-tunnels")

                        self.currently_failing_layer2pv_cs = YLeaf(YType.uint32, "currently-failing-layer2pv-cs")

                        self.currently_failing_layer2pv_ps = YLeaf(YType.uint32, "currently-failing-layer2pv-ps")

                        self.currently_failing_layer3pv_cs = YLeaf(YType.uint32, "currently-failing-layer3pv-cs")

                        self.currently_failing_layer3vp_tunnels = YLeaf(YType.uint32, "currently-failing-layer3vp-tunnels")

                        self.ilmi_vci = YLeaf(YType.uint32, "ilmi-vci")

                        self.ilmi_vpi = YLeaf(YType.uint32, "ilmi-vpi")

                        self.l2_cell_packing_count = YLeaf(YType.uint16, "l2-cell-packing-count")

                        self.main_interface = YLeaf(YType.str, "main-interface")

                        self.port_type = YLeaf(YType.enumeration, "port-type")

                        self.pvc_failures = YLeaf(YType.uint32, "pvc-failures")

                        self.pvc_failures_trap_enable = YLeaf(YType.boolean, "pvc-failures-trap-enable")

                        self.pvc_notification_interval = YLeaf(YType.uint32, "pvc-notification-interval")

                        self.cell_packing_data = AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData()
                        self.cell_packing_data.parent = self
                        self._children_name_map["cell_packing_data"] = "cell-packing-data"
                        self._children_yang_names.add("cell-packing-data")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "configured_layer2pv_cs",
                                        "configured_layer2pv_ps",
                                        "configured_layer3pv_cs",
                                        "configured_layer3vp_tunnels",
                                        "currently_failing_layer2pv_cs",
                                        "currently_failing_layer2pv_ps",
                                        "currently_failing_layer3pv_cs",
                                        "currently_failing_layer3vp_tunnels",
                                        "ilmi_vci",
                                        "ilmi_vpi",
                                        "l2_cell_packing_count",
                                        "main_interface",
                                        "port_type",
                                        "pvc_failures",
                                        "pvc_failures_trap_enable",
                                        "pvc_notification_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AtmVcm.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AtmVcm.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


                    class CellPackingData(Entity):
                        """
                        Cell packing specific information
                        
                        .. attribute:: local_max_cells_packed_per_packet
                        
                        	Local configuration of maximum number of cells to be packed per packet
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: max_cell_packed_timeout
                        
                        	Maximum cell packing timeout inmicro seconds
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**units**\: microsecond
                        
                        .. attribute:: negotiated_max_cells_packed_per_packet
                        
                        	Negotiated value of maximum number of cells to be packed per packed
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData, self).__init__()

                            self.yang_name = "cell-packing-data"
                            self.yang_parent_name = "interface"

                            self.local_max_cells_packed_per_packet = YLeaf(YType.uint16, "local-max-cells-packed-per-packet")

                            self.max_cell_packed_timeout = YLeaf(YType.uint16, "max-cell-packed-timeout")

                            self.negotiated_max_cells_packed_per_packet = YLeaf(YType.uint16, "negotiated-max-cells-packed-per-packet")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("local_max_cells_packed_per_packet",
                                            "max_cell_packed_timeout",
                                            "negotiated_max_cells_packed_per_packet") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.local_max_cells_packed_per_packet.is_set or
                                self.max_cell_packed_timeout.is_set or
                                self.negotiated_max_cells_packed_per_packet.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.local_max_cells_packed_per_packet.yfilter != YFilter.not_set or
                                self.max_cell_packed_timeout.yfilter != YFilter.not_set or
                                self.negotiated_max_cells_packed_per_packet.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "cell-packing-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.local_max_cells_packed_per_packet.is_set or self.local_max_cells_packed_per_packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.local_max_cells_packed_per_packet.get_name_leafdata())
                            if (self.max_cell_packed_timeout.is_set or self.max_cell_packed_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_cell_packed_timeout.get_name_leafdata())
                            if (self.negotiated_max_cells_packed_per_packet.is_set or self.negotiated_max_cells_packed_per_packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.negotiated_max_cells_packed_per_packet.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "local-max-cells-packed-per-packet" or name == "max-cell-packed-timeout" or name == "negotiated-max-cells-packed-per-packet"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "local-max-cells-packed-per-packet"):
                                self.local_max_cells_packed_per_packet = value
                                self.local_max_cells_packed_per_packet.value_namespace = name_space
                                self.local_max_cells_packed_per_packet.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-cell-packed-timeout"):
                                self.max_cell_packed_timeout = value
                                self.max_cell_packed_timeout.value_namespace = name_space
                                self.max_cell_packed_timeout.value_namespace_prefix = name_space_prefix
                            if(value_path == "negotiated-max-cells-packed-per-packet"):
                                self.negotiated_max_cells_packed_per_packet = value
                                self.negotiated_max_cells_packed_per_packet.value_namespace = name_space
                                self.negotiated_max_cells_packed_per_packet.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.configured_layer2pv_cs.is_set or
                            self.configured_layer2pv_ps.is_set or
                            self.configured_layer3pv_cs.is_set or
                            self.configured_layer3vp_tunnels.is_set or
                            self.currently_failing_layer2pv_cs.is_set or
                            self.currently_failing_layer2pv_ps.is_set or
                            self.currently_failing_layer3pv_cs.is_set or
                            self.currently_failing_layer3vp_tunnels.is_set or
                            self.ilmi_vci.is_set or
                            self.ilmi_vpi.is_set or
                            self.l2_cell_packing_count.is_set or
                            self.main_interface.is_set or
                            self.port_type.is_set or
                            self.pvc_failures.is_set or
                            self.pvc_failures_trap_enable.is_set or
                            self.pvc_notification_interval.is_set or
                            (self.cell_packing_data is not None and self.cell_packing_data.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.configured_layer2pv_cs.yfilter != YFilter.not_set or
                            self.configured_layer2pv_ps.yfilter != YFilter.not_set or
                            self.configured_layer3pv_cs.yfilter != YFilter.not_set or
                            self.configured_layer3vp_tunnels.yfilter != YFilter.not_set or
                            self.currently_failing_layer2pv_cs.yfilter != YFilter.not_set or
                            self.currently_failing_layer2pv_ps.yfilter != YFilter.not_set or
                            self.currently_failing_layer3pv_cs.yfilter != YFilter.not_set or
                            self.currently_failing_layer3vp_tunnels.yfilter != YFilter.not_set or
                            self.ilmi_vci.yfilter != YFilter.not_set or
                            self.ilmi_vpi.yfilter != YFilter.not_set or
                            self.l2_cell_packing_count.yfilter != YFilter.not_set or
                            self.main_interface.yfilter != YFilter.not_set or
                            self.port_type.yfilter != YFilter.not_set or
                            self.pvc_failures.yfilter != YFilter.not_set or
                            self.pvc_failures_trap_enable.yfilter != YFilter.not_set or
                            self.pvc_notification_interval.yfilter != YFilter.not_set or
                            (self.cell_packing_data is not None and self.cell_packing_data.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.configured_layer2pv_cs.is_set or self.configured_layer2pv_cs.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_layer2pv_cs.get_name_leafdata())
                        if (self.configured_layer2pv_ps.is_set or self.configured_layer2pv_ps.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_layer2pv_ps.get_name_leafdata())
                        if (self.configured_layer3pv_cs.is_set or self.configured_layer3pv_cs.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_layer3pv_cs.get_name_leafdata())
                        if (self.configured_layer3vp_tunnels.is_set or self.configured_layer3vp_tunnels.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured_layer3vp_tunnels.get_name_leafdata())
                        if (self.currently_failing_layer2pv_cs.is_set or self.currently_failing_layer2pv_cs.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.currently_failing_layer2pv_cs.get_name_leafdata())
                        if (self.currently_failing_layer2pv_ps.is_set or self.currently_failing_layer2pv_ps.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.currently_failing_layer2pv_ps.get_name_leafdata())
                        if (self.currently_failing_layer3pv_cs.is_set or self.currently_failing_layer3pv_cs.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.currently_failing_layer3pv_cs.get_name_leafdata())
                        if (self.currently_failing_layer3vp_tunnels.is_set or self.currently_failing_layer3vp_tunnels.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.currently_failing_layer3vp_tunnels.get_name_leafdata())
                        if (self.ilmi_vci.is_set or self.ilmi_vci.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ilmi_vci.get_name_leafdata())
                        if (self.ilmi_vpi.is_set or self.ilmi_vpi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ilmi_vpi.get_name_leafdata())
                        if (self.l2_cell_packing_count.is_set or self.l2_cell_packing_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.l2_cell_packing_count.get_name_leafdata())
                        if (self.main_interface.is_set or self.main_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.main_interface.get_name_leafdata())
                        if (self.port_type.is_set or self.port_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port_type.get_name_leafdata())
                        if (self.pvc_failures.is_set or self.pvc_failures.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pvc_failures.get_name_leafdata())
                        if (self.pvc_failures_trap_enable.is_set or self.pvc_failures_trap_enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pvc_failures_trap_enable.get_name_leafdata())
                        if (self.pvc_notification_interval.is_set or self.pvc_notification_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pvc_notification_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "cell-packing-data"):
                            if (self.cell_packing_data is None):
                                self.cell_packing_data = AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData()
                                self.cell_packing_data.parent = self
                                self._children_name_map["cell_packing_data"] = "cell-packing-data"
                            return self.cell_packing_data

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cell-packing-data" or name == "interface-name" or name == "configured-layer2pv-cs" or name == "configured-layer2pv-ps" or name == "configured-layer3pv-cs" or name == "configured-layer3vp-tunnels" or name == "currently-failing-layer2pv-cs" or name == "currently-failing-layer2pv-ps" or name == "currently-failing-layer3pv-cs" or name == "currently-failing-layer3vp-tunnels" or name == "ilmi-vci" or name == "ilmi-vpi" or name == "l2-cell-packing-count" or name == "main-interface" or name == "port-type" or name == "pvc-failures" or name == "pvc-failures-trap-enable" or name == "pvc-notification-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-layer2pv-cs"):
                            self.configured_layer2pv_cs = value
                            self.configured_layer2pv_cs.value_namespace = name_space
                            self.configured_layer2pv_cs.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-layer2pv-ps"):
                            self.configured_layer2pv_ps = value
                            self.configured_layer2pv_ps.value_namespace = name_space
                            self.configured_layer2pv_ps.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-layer3pv-cs"):
                            self.configured_layer3pv_cs = value
                            self.configured_layer3pv_cs.value_namespace = name_space
                            self.configured_layer3pv_cs.value_namespace_prefix = name_space_prefix
                        if(value_path == "configured-layer3vp-tunnels"):
                            self.configured_layer3vp_tunnels = value
                            self.configured_layer3vp_tunnels.value_namespace = name_space
                            self.configured_layer3vp_tunnels.value_namespace_prefix = name_space_prefix
                        if(value_path == "currently-failing-layer2pv-cs"):
                            self.currently_failing_layer2pv_cs = value
                            self.currently_failing_layer2pv_cs.value_namespace = name_space
                            self.currently_failing_layer2pv_cs.value_namespace_prefix = name_space_prefix
                        if(value_path == "currently-failing-layer2pv-ps"):
                            self.currently_failing_layer2pv_ps = value
                            self.currently_failing_layer2pv_ps.value_namespace = name_space
                            self.currently_failing_layer2pv_ps.value_namespace_prefix = name_space_prefix
                        if(value_path == "currently-failing-layer3pv-cs"):
                            self.currently_failing_layer3pv_cs = value
                            self.currently_failing_layer3pv_cs.value_namespace = name_space
                            self.currently_failing_layer3pv_cs.value_namespace_prefix = name_space_prefix
                        if(value_path == "currently-failing-layer3vp-tunnels"):
                            self.currently_failing_layer3vp_tunnels = value
                            self.currently_failing_layer3vp_tunnels.value_namespace = name_space
                            self.currently_failing_layer3vp_tunnels.value_namespace_prefix = name_space_prefix
                        if(value_path == "ilmi-vci"):
                            self.ilmi_vci = value
                            self.ilmi_vci.value_namespace = name_space
                            self.ilmi_vci.value_namespace_prefix = name_space_prefix
                        if(value_path == "ilmi-vpi"):
                            self.ilmi_vpi = value
                            self.ilmi_vpi.value_namespace = name_space
                            self.ilmi_vpi.value_namespace_prefix = name_space_prefix
                        if(value_path == "l2-cell-packing-count"):
                            self.l2_cell_packing_count = value
                            self.l2_cell_packing_count.value_namespace = name_space
                            self.l2_cell_packing_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "main-interface"):
                            self.main_interface = value
                            self.main_interface.value_namespace = name_space
                            self.main_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "port-type"):
                            self.port_type = value
                            self.port_type.value_namespace = name_space
                            self.port_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "pvc-failures"):
                            self.pvc_failures = value
                            self.pvc_failures.value_namespace = name_space
                            self.pvc_failures.value_namespace_prefix = name_space_prefix
                        if(value_path == "pvc-failures-trap-enable"):
                            self.pvc_failures_trap_enable = value
                            self.pvc_failures_trap_enable.value_namespace = name_space
                            self.pvc_failures_trap_enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "pvc-notification-interval"):
                            self.pvc_notification_interval = value
                            self.pvc_notification_interval.value_namespace = name_space
                            self.pvc_notification_interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

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

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AtmVcm.Nodes.Node.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class VpTunnels(Entity):
                """
                Contains all VP\-tunnel information for node
                
                .. attribute:: vp_tunnel
                
                	All VP\-tunnel information on a node
                	**type**\: list of    :py:class:`VpTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.VpTunnels.VpTunnel>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AtmVcm.Nodes.Node.VpTunnels, self).__init__()

                    self.yang_name = "vp-tunnels"
                    self.yang_parent_name = "node"

                    self.vp_tunnel = YList(self)

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
                                super(AtmVcm.Nodes.Node.VpTunnels, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AtmVcm.Nodes.Node.VpTunnels, self).__setattr__(name, value)


                class VpTunnel(Entity):
                    """
                    All VP\-tunnel information on a node
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: amin_status
                    
                    	TRUE value indicates that the VP is administratively UP
                    	**type**\:  bool
                    
                    .. attribute:: burst_rate
                    
                    	Burst size in cells
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data_vc_count
                    
                    	Number of Data PVCs under this VP\-tunnel
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: f4oam_enabled
                    
                    	F4OAM Enabled flag
                    	**type**\:  bool
                    
                    .. attribute:: internal_state
                    
                    	Internal state
                    	**type**\:   :py:class:`VpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VpState>`
                    
                    .. attribute:: last_vp_state_change_time
                    
                    	Time when VP\-Tunnel state was last changed
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: main_interface
                    
                    	Main Interface handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: oper_status
                    
                    	TRUE value indicates that the VP is operationally UP
                    	**type**\:  bool
                    
                    .. attribute:: peak_cell_rate
                    
                    	Peak cell rate in Kbps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: shape
                    
                    	ATM VP traffic shaping type
                    	**type**\:   :py:class:`VpTrafShaping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VpTrafShaping>`
                    
                    .. attribute:: sustained_cell_rate
                    
                    	Sustained cell rate in Kbps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: vp_interface
                    
                    	VP Interfcace handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: vpi
                    
                    	VPI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: vpi_xr
                    
                    	VP\-Tunnel VPI value
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'atm-vcm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AtmVcm.Nodes.Node.VpTunnels.VpTunnel, self).__init__()

                        self.yang_name = "vp-tunnel"
                        self.yang_parent_name = "vp-tunnels"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.amin_status = YLeaf(YType.boolean, "amin-status")

                        self.burst_rate = YLeaf(YType.uint32, "burst-rate")

                        self.data_vc_count = YLeaf(YType.uint32, "data-vc-count")

                        self.f4oam_enabled = YLeaf(YType.boolean, "f4oam-enabled")

                        self.internal_state = YLeaf(YType.enumeration, "internal-state")

                        self.last_vp_state_change_time = YLeaf(YType.uint32, "last-vp-state-change-time")

                        self.main_interface = YLeaf(YType.str, "main-interface")

                        self.oper_status = YLeaf(YType.boolean, "oper-status")

                        self.peak_cell_rate = YLeaf(YType.uint32, "peak-cell-rate")

                        self.shape = YLeaf(YType.enumeration, "shape")

                        self.sustained_cell_rate = YLeaf(YType.uint32, "sustained-cell-rate")

                        self.vp_interface = YLeaf(YType.str, "vp-interface")

                        self.vpi = YLeaf(YType.int32, "vpi")

                        self.vpi_xr = YLeaf(YType.uint16, "vpi-xr")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "amin_status",
                                        "burst_rate",
                                        "data_vc_count",
                                        "f4oam_enabled",
                                        "internal_state",
                                        "last_vp_state_change_time",
                                        "main_interface",
                                        "oper_status",
                                        "peak_cell_rate",
                                        "shape",
                                        "sustained_cell_rate",
                                        "vp_interface",
                                        "vpi",
                                        "vpi_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AtmVcm.Nodes.Node.VpTunnels.VpTunnel, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AtmVcm.Nodes.Node.VpTunnels.VpTunnel, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.amin_status.is_set or
                            self.burst_rate.is_set or
                            self.data_vc_count.is_set or
                            self.f4oam_enabled.is_set or
                            self.internal_state.is_set or
                            self.last_vp_state_change_time.is_set or
                            self.main_interface.is_set or
                            self.oper_status.is_set or
                            self.peak_cell_rate.is_set or
                            self.shape.is_set or
                            self.sustained_cell_rate.is_set or
                            self.vp_interface.is_set or
                            self.vpi.is_set or
                            self.vpi_xr.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.amin_status.yfilter != YFilter.not_set or
                            self.burst_rate.yfilter != YFilter.not_set or
                            self.data_vc_count.yfilter != YFilter.not_set or
                            self.f4oam_enabled.yfilter != YFilter.not_set or
                            self.internal_state.yfilter != YFilter.not_set or
                            self.last_vp_state_change_time.yfilter != YFilter.not_set or
                            self.main_interface.yfilter != YFilter.not_set or
                            self.oper_status.yfilter != YFilter.not_set or
                            self.peak_cell_rate.yfilter != YFilter.not_set or
                            self.shape.yfilter != YFilter.not_set or
                            self.sustained_cell_rate.yfilter != YFilter.not_set or
                            self.vp_interface.yfilter != YFilter.not_set or
                            self.vpi.yfilter != YFilter.not_set or
                            self.vpi_xr.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vp-tunnel" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.amin_status.is_set or self.amin_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.amin_status.get_name_leafdata())
                        if (self.burst_rate.is_set or self.burst_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.burst_rate.get_name_leafdata())
                        if (self.data_vc_count.is_set or self.data_vc_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.data_vc_count.get_name_leafdata())
                        if (self.f4oam_enabled.is_set or self.f4oam_enabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.f4oam_enabled.get_name_leafdata())
                        if (self.internal_state.is_set or self.internal_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.internal_state.get_name_leafdata())
                        if (self.last_vp_state_change_time.is_set or self.last_vp_state_change_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_vp_state_change_time.get_name_leafdata())
                        if (self.main_interface.is_set or self.main_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.main_interface.get_name_leafdata())
                        if (self.oper_status.is_set or self.oper_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oper_status.get_name_leafdata())
                        if (self.peak_cell_rate.is_set or self.peak_cell_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_cell_rate.get_name_leafdata())
                        if (self.shape.is_set or self.shape.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.shape.get_name_leafdata())
                        if (self.sustained_cell_rate.is_set or self.sustained_cell_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sustained_cell_rate.get_name_leafdata())
                        if (self.vp_interface.is_set or self.vp_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vp_interface.get_name_leafdata())
                        if (self.vpi.is_set or self.vpi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vpi.get_name_leafdata())
                        if (self.vpi_xr.is_set or self.vpi_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vpi_xr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "amin-status" or name == "burst-rate" or name == "data-vc-count" or name == "f4oam-enabled" or name == "internal-state" or name == "last-vp-state-change-time" or name == "main-interface" or name == "oper-status" or name == "peak-cell-rate" or name == "shape" or name == "sustained-cell-rate" or name == "vp-interface" or name == "vpi" or name == "vpi-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "amin-status"):
                            self.amin_status = value
                            self.amin_status.value_namespace = name_space
                            self.amin_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "burst-rate"):
                            self.burst_rate = value
                            self.burst_rate.value_namespace = name_space
                            self.burst_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "data-vc-count"):
                            self.data_vc_count = value
                            self.data_vc_count.value_namespace = name_space
                            self.data_vc_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "f4oam-enabled"):
                            self.f4oam_enabled = value
                            self.f4oam_enabled.value_namespace = name_space
                            self.f4oam_enabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "internal-state"):
                            self.internal_state = value
                            self.internal_state.value_namespace = name_space
                            self.internal_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-vp-state-change-time"):
                            self.last_vp_state_change_time = value
                            self.last_vp_state_change_time.value_namespace = name_space
                            self.last_vp_state_change_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "main-interface"):
                            self.main_interface = value
                            self.main_interface.value_namespace = name_space
                            self.main_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "oper-status"):
                            self.oper_status = value
                            self.oper_status.value_namespace = name_space
                            self.oper_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-cell-rate"):
                            self.peak_cell_rate = value
                            self.peak_cell_rate.value_namespace = name_space
                            self.peak_cell_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "shape"):
                            self.shape = value
                            self.shape.value_namespace = name_space
                            self.shape.value_namespace_prefix = name_space_prefix
                        if(value_path == "sustained-cell-rate"):
                            self.sustained_cell_rate = value
                            self.sustained_cell_rate.value_namespace = name_space
                            self.sustained_cell_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "vp-interface"):
                            self.vp_interface = value
                            self.vp_interface.value_namespace = name_space
                            self.vp_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "vpi"):
                            self.vpi = value
                            self.vpi.value_namespace = name_space
                            self.vpi.value_namespace_prefix = name_space_prefix
                        if(value_path == "vpi-xr"):
                            self.vpi_xr = value
                            self.vpi_xr.value_namespace = name_space
                            self.vpi_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vp_tunnel:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vp_tunnel:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vp-tunnels" + path_buffer

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

                    if (child_yang_name == "vp-tunnel"):
                        for c in self.vp_tunnel:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AtmVcm.Nodes.Node.VpTunnels.VpTunnel()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vp_tunnel.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vp-tunnel"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.cell_packs is not None and self.cell_packs.has_data()) or
                    (self.class_links is not None and self.class_links.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()) or
                    (self.pvps is not None and self.pvps.has_data()) or
                    (self.vcs is not None and self.vcs.has_data()) or
                    (self.vp_tunnels is not None and self.vp_tunnels.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.cell_packs is not None and self.cell_packs.has_operation()) or
                    (self.class_links is not None and self.class_links.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()) or
                    (self.pvps is not None and self.pvps.has_operation()) or
                    (self.vcs is not None and self.vcs.has_operation()) or
                    (self.vp_tunnels is not None and self.vp_tunnels.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-atm-vcm-oper:atm-vcm/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "cell-packs"):
                    if (self.cell_packs is None):
                        self.cell_packs = AtmVcm.Nodes.Node.CellPacks()
                        self.cell_packs.parent = self
                        self._children_name_map["cell_packs"] = "cell-packs"
                    return self.cell_packs

                if (child_yang_name == "class-links"):
                    if (self.class_links is None):
                        self.class_links = AtmVcm.Nodes.Node.ClassLinks()
                        self.class_links.parent = self
                        self._children_name_map["class_links"] = "class-links"
                    return self.class_links

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = AtmVcm.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                if (child_yang_name == "pvps"):
                    if (self.pvps is None):
                        self.pvps = AtmVcm.Nodes.Node.Pvps()
                        self.pvps.parent = self
                        self._children_name_map["pvps"] = "pvps"
                    return self.pvps

                if (child_yang_name == "vcs"):
                    if (self.vcs is None):
                        self.vcs = AtmVcm.Nodes.Node.Vcs()
                        self.vcs.parent = self
                        self._children_name_map["vcs"] = "vcs"
                    return self.vcs

                if (child_yang_name == "vp-tunnels"):
                    if (self.vp_tunnels is None):
                        self.vp_tunnels = AtmVcm.Nodes.Node.VpTunnels()
                        self.vp_tunnels.parent = self
                        self._children_name_map["vp_tunnels"] = "vp-tunnels"
                    return self.vp_tunnels

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cell-packs" or name == "class-links" or name == "interfaces" or name == "pvps" or name == "vcs" or name == "vp-tunnels" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-atm-vcm-oper:atm-vcm/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AtmVcm.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-atm-vcm-oper:atm-vcm" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = AtmVcm.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AtmVcm()
        return self._top_entity

