""" Cisco_IOS_XR_atm_vcm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR atm\-vcm package operational data.

This module contains definitions
for the following management objects\:
  atm\-vcm\: ATM VCM operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ClassLinkOamInheritLevelEnum(Enum):
    """
    ClassLinkOamInheritLevelEnum

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

    vc_configured_onvc = 0

    vc_class_onvc = 1

    vc_class_on_sub_interface = 2

    vc_class_on_main_interface = 3

    vc_global_default = 4

    vc_inherit_level_unknown = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['ClassLinkOamInheritLevelEnum']


class VcCellPackingModeEnum(Enum):
    """
    VcCellPackingModeEnum

    ATM VC cell packing mode

    .. data:: vp = 1

    	VP mode

    .. data:: vc = 2

    	VC mode

    .. data:: port_mode = 3

    	Port mode

    """

    vp = 1

    vc = 2

    port_mode = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcCellPackingModeEnum']


class VcEncapEnum(Enum):
    """
    VcEncapEnum

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

    ilmi = 1

    qsaal = 2

    snap = 3

    mux = 4

    nlpid = 5

    f4oam = 6

    aal0 = 7

    aal5 = 8

    encap_unknown = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcEncapEnum']


class VcEnum(Enum):
    """
    VcEnum

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

    layer3_vc = 0

    layer2_vc = 1

    layer2_vp = 2

    vc_type_unknown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcEnum']


class VcInheritLevelEnum(Enum):
    """
    VcInheritLevelEnum

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

    directly_configured_onvc = 0

    vc_class_configured_onvc = 1

    vc_class_configured_on_sub_interface = 2

    vc_class_configured_on_main_interface = 3

    global_default = 4

    unknown = 5

    not_supported = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcInheritLevelEnum']


class VcManageLevelEnum(Enum):
    """
    VcManageLevelEnum

    ATM Class link manage level

    .. data:: manage = 1

    	Managed

    .. data:: not_managed = 2

    	Not managed

    """

    manage = 1

    not_managed = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcManageLevelEnum']


class VcStateEnum(Enum):
    """
    VcStateEnum

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

    initialized = 0

    modifying = 1

    modified = 2

    activating = 3

    activated = 4

    not_verified = 5

    ready = 6

    deactivating = 7

    inactive = 8

    deleting = 9

    deleted = 10

    state_unknown = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcStateEnum']


class VcTestModeEnum(Enum):
    """
    VcTestModeEnum

    VC Test Mode Type

    .. data:: test_mode_none = 1

    	VC not in test mode

    .. data:: loop = 2

    	VC in test mode Loop

    .. data:: reserved = 3

    	VC in test mode Reserved

    """

    test_mode_none = 1

    loop = 2

    reserved = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcTestModeEnum']


class VcTrafShapingEnum(Enum):
    """
    VcTrafShapingEnum

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

    cbr = 1

    vbr_nrt = 2

    vbr_rt = 3

    abr = 4

    ubr_plus = 5

    ubr = 6

    traf_shaping_unknown = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcTrafShapingEnum']


class VcmPortEnum(Enum):
    """
    VcmPortEnum

    ATM port type

    .. data:: port_type_layer_2 = 0

    	 Layer 2 ATM port type 

    .. data:: port_type_layer_3 = 1

    	 Layer 3 ATM port type 

    .. data:: port_type_unknown = 3

    	 ATM port type unknown 

    """

    port_type_layer_2 = 0

    port_type_layer_3 = 1

    port_type_unknown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VcmPortEnum']


class VpStateEnum(Enum):
    """
    VpStateEnum

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

    vp_initialized = 0

    vp_modifying = 1

    vp_ready = 2

    vp_mgd_down = 3

    vp_deleting = 4

    vp_deleted = 5

    vp_state_unknown = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VpStateEnum']


class VpTrafShapingEnum(Enum):
    """
    VpTrafShapingEnum

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

    vp_cbr = 1

    vp_vbr_nrt = 2

    vp_vbr_rt = 3

    vp_abr = 4

    vp_ubr_plus = 5

    vp_ubr = 6

    vp_traf_shaping_unknown = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['VpTrafShapingEnum']



class AtmVcm(object):
    """
    ATM VCM operational data
    
    .. attribute:: nodes
    
    	Contains all the nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes>`
    
    

    """

    _prefix = 'atm-vcm-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = AtmVcm.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Contains all the nodes
        
        .. attribute:: node
        
        	The node on which ATM Interfaces/VCs/VPs are located
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node>`
        
        

        """

        _prefix = 'atm-vcm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_name = None
                self.cell_packs = AtmVcm.Nodes.Node.CellPacks()
                self.cell_packs.parent = self
                self.class_links = AtmVcm.Nodes.Node.ClassLinks()
                self.class_links.parent = self
                self.interfaces = AtmVcm.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.pvps = AtmVcm.Nodes.Node.Pvps()
                self.pvps.parent = self
                self.vcs = AtmVcm.Nodes.Node.Vcs()
                self.vcs.parent = self
                self.vp_tunnels = AtmVcm.Nodes.Node.VpTunnels()
                self.vp_tunnels.parent = self


            class Vcs(object):
                """
                Contains all VC information for node
                
                .. attribute:: vc
                
                	All VC information on a node
                	**type**\: list of    :py:class:`Vc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Vcs.Vc>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vc = YList()
                    self.vc.parent = self
                    self.vc.name = 'vc'


                class Vc(object):
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
                    	**type**\:   :py:class:`VcInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevelEnum>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation type
                    	**type**\:   :py:class:`VcEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncapEnum>`
                    
                    .. attribute:: internal_state
                    
                    	VC Internal state
                    	**type**\:   :py:class:`VcStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcStateEnum>`
                    
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
                    	**type**\:   :py:class:`VcInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevelEnum>`
                    
                    .. attribute:: receive_mtu
                    
                    	Receive MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: shape
                    
                    	ATM VC traffic shaping type
                    	**type**\:   :py:class:`VcTrafShapingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShapingEnum>`
                    
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
                    	**type**\:   :py:class:`VcTestModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTestModeEnum>`
                    
                    .. attribute:: transmit_mtu
                    
                    	Transmit MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	VC Type
                    	**type**\:   :py:class:`VcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEnum>`
                    
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
                        self.parent = None
                        self.interface_name = None
                        self.amin_status = None
                        self.burst_rate = None
                        self.cell_packing_data = AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData()
                        self.cell_packing_data.parent = self
                        self.encaps_inherit_level = None
                        self.encapsulation = None
                        self.internal_state = None
                        self.last_state_change_time = None
                        self.main_interface = None
                        self.oper_status = None
                        self.peak_cell_rate = None
                        self.qos_inherit_level = None
                        self.receive_mtu = None
                        self.shape = None
                        self.sub_interface = None
                        self.sustained_cell_rate = None
                        self.test_mode = None
                        self.transmit_mtu = None
                        self.type = None
                        self.vc_interface = None
                        self.vc_on_p2p_sub_interface = None
                        self.vc_onvp_tunnel = None
                        self.vci = None
                        self.vci_xr = None
                        self.vpi = None
                        self.vpi_xr = None


                    class CellPackingData(object):
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
                            self.parent = None
                            self.local_max_cells_packed_per_packet = None
                            self.max_cell_packed_timeout = None
                            self.negotiated_max_cells_packed_per_packet = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:cell-packing-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_max_cells_packed_per_packet is not None:
                                return True

                            if self.max_cell_packed_timeout is not None:
                                return True

                            if self.negotiated_max_cells_packed_per_packet is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                            return meta._meta_table['AtmVcm.Nodes.Node.Vcs.Vc.CellPackingData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:vc[Cisco-IOS-XR-atm-vcm-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.amin_status is not None:
                            return True

                        if self.burst_rate is not None:
                            return True

                        if self.cell_packing_data is not None and self.cell_packing_data._has_data():
                            return True

                        if self.encaps_inherit_level is not None:
                            return True

                        if self.encapsulation is not None:
                            return True

                        if self.internal_state is not None:
                            return True

                        if self.last_state_change_time is not None:
                            return True

                        if self.main_interface is not None:
                            return True

                        if self.oper_status is not None:
                            return True

                        if self.peak_cell_rate is not None:
                            return True

                        if self.qos_inherit_level is not None:
                            return True

                        if self.receive_mtu is not None:
                            return True

                        if self.shape is not None:
                            return True

                        if self.sub_interface is not None:
                            return True

                        if self.sustained_cell_rate is not None:
                            return True

                        if self.test_mode is not None:
                            return True

                        if self.transmit_mtu is not None:
                            return True

                        if self.type is not None:
                            return True

                        if self.vc_interface is not None:
                            return True

                        if self.vc_on_p2p_sub_interface is not None:
                            return True

                        if self.vc_onvp_tunnel is not None:
                            return True

                        if self.vci is not None:
                            return True

                        if self.vci_xr is not None:
                            return True

                        if self.vpi is not None:
                            return True

                        if self.vpi_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                        return meta._meta_table['AtmVcm.Nodes.Node.Vcs.Vc']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:vcs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vc is not None:
                        for child_ref in self.vc:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                    return meta._meta_table['AtmVcm.Nodes.Node.Vcs']['meta_info']


            class CellPacks(object):
                """
                Contains all cell packing information for node
                
                .. attribute:: cell_pack
                
                	All cell packing information on a node
                	**type**\: list of    :py:class:`CellPack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.CellPacks.CellPack>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.cell_pack = YList()
                    self.cell_pack.parent = self
                    self.cell_pack.name = 'cell_pack'


                class CellPack(object):
                    """
                    All cell packing information on a node
                    
                    .. attribute:: cell_packing
                    
                    	Cell packing specific data
                    	**type**\:   :py:class:`CellPacking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking>`
                    
                    .. attribute:: cell_packing_mode
                    
                    	ATM cell packing mode
                    	**type**\:   :py:class:`VcCellPackingModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcCellPackingModeEnum>`
                    
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
                        self.parent = None
                        self.cell_packing = AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking()
                        self.cell_packing.parent = self
                        self.cell_packing_mode = None
                        self.interface_name = None
                        self.pci = None
                        self.received_average_cells_packets = None
                        self.sent_cells_packets = None
                        self.sub_interface_name = None
                        self.vci = None
                        self.vpi = None


                    class CellPacking(object):
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
                            self.parent = None
                            self.local_max_cells_packed_per_packet = None
                            self.max_cell_packed_timeout = None
                            self.negotiated_max_cells_packed_per_packet = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:cell-packing'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_max_cells_packed_per_packet is not None:
                                return True

                            if self.max_cell_packed_timeout is not None:
                                return True

                            if self.negotiated_max_cells_packed_per_packet is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                            return meta._meta_table['AtmVcm.Nodes.Node.CellPacks.CellPack.CellPacking']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:cell-pack'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.cell_packing is not None and self.cell_packing._has_data():
                            return True

                        if self.cell_packing_mode is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.pci is not None:
                            return True

                        if self.received_average_cells_packets is not None:
                            return True

                        if self.sent_cells_packets is not None:
                            return True

                        if self.sub_interface_name is not None:
                            return True

                        if self.vci is not None:
                            return True

                        if self.vpi is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                        return meta._meta_table['AtmVcm.Nodes.Node.CellPacks.CellPack']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:cell-packs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.cell_pack is not None:
                        for child_ref in self.cell_pack:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                    return meta._meta_table['AtmVcm.Nodes.Node.CellPacks']['meta_info']


            class Pvps(object):
                """
                Contains all L2 PVP information for node
                
                .. attribute:: pvp
                
                	All L2 PVP information on a node
                	**type**\: list of    :py:class:`Pvp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Pvps.Pvp>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.pvp = YList()
                    self.pvp.parent = self
                    self.pvp.name = 'pvp'


                class Pvp(object):
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
                    	**type**\:   :py:class:`VcInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevelEnum>`
                    
                    .. attribute:: encapsulation
                    
                    	Encapsulation type
                    	**type**\:   :py:class:`VcEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncapEnum>`
                    
                    .. attribute:: internal_state
                    
                    	VC Internal state
                    	**type**\:   :py:class:`VcStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcStateEnum>`
                    
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
                    	**type**\:   :py:class:`VcInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevelEnum>`
                    
                    .. attribute:: receive_mtu
                    
                    	Receive MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: shape
                    
                    	ATM VC traffic shaping type
                    	**type**\:   :py:class:`VcTrafShapingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShapingEnum>`
                    
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
                    	**type**\:   :py:class:`VcTestModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTestModeEnum>`
                    
                    .. attribute:: transmit_mtu
                    
                    	Transmit MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	VC Type
                    	**type**\:   :py:class:`VcEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEnum>`
                    
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
                        self.parent = None
                        self.interface_name = None
                        self.amin_status = None
                        self.burst_rate = None
                        self.cell_packing_data = AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData()
                        self.cell_packing_data.parent = self
                        self.encaps_inherit_level = None
                        self.encapsulation = None
                        self.internal_state = None
                        self.last_state_change_time = None
                        self.main_interface = None
                        self.oper_status = None
                        self.peak_cell_rate = None
                        self.qos_inherit_level = None
                        self.receive_mtu = None
                        self.shape = None
                        self.sub_interface = None
                        self.sustained_cell_rate = None
                        self.test_mode = None
                        self.transmit_mtu = None
                        self.type = None
                        self.vc_interface = None
                        self.vc_on_p2p_sub_interface = None
                        self.vc_onvp_tunnel = None
                        self.vci_xr = None
                        self.vpi = None
                        self.vpi_xr = None


                    class CellPackingData(object):
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
                            self.parent = None
                            self.local_max_cells_packed_per_packet = None
                            self.max_cell_packed_timeout = None
                            self.negotiated_max_cells_packed_per_packet = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:cell-packing-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_max_cells_packed_per_packet is not None:
                                return True

                            if self.max_cell_packed_timeout is not None:
                                return True

                            if self.negotiated_max_cells_packed_per_packet is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                            return meta._meta_table['AtmVcm.Nodes.Node.Pvps.Pvp.CellPackingData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:pvp[Cisco-IOS-XR-atm-vcm-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.amin_status is not None:
                            return True

                        if self.burst_rate is not None:
                            return True

                        if self.cell_packing_data is not None and self.cell_packing_data._has_data():
                            return True

                        if self.encaps_inherit_level is not None:
                            return True

                        if self.encapsulation is not None:
                            return True

                        if self.internal_state is not None:
                            return True

                        if self.last_state_change_time is not None:
                            return True

                        if self.main_interface is not None:
                            return True

                        if self.oper_status is not None:
                            return True

                        if self.peak_cell_rate is not None:
                            return True

                        if self.qos_inherit_level is not None:
                            return True

                        if self.receive_mtu is not None:
                            return True

                        if self.shape is not None:
                            return True

                        if self.sub_interface is not None:
                            return True

                        if self.sustained_cell_rate is not None:
                            return True

                        if self.test_mode is not None:
                            return True

                        if self.transmit_mtu is not None:
                            return True

                        if self.type is not None:
                            return True

                        if self.vc_interface is not None:
                            return True

                        if self.vc_on_p2p_sub_interface is not None:
                            return True

                        if self.vc_onvp_tunnel is not None:
                            return True

                        if self.vci_xr is not None:
                            return True

                        if self.vpi is not None:
                            return True

                        if self.vpi_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                        return meta._meta_table['AtmVcm.Nodes.Node.Pvps.Pvp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:pvps'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.pvp is not None:
                        for child_ref in self.pvp:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                    return meta._meta_table['AtmVcm.Nodes.Node.Pvps']['meta_info']


            class ClassLinks(object):
                """
                Contains all class link information for node
                
                .. attribute:: class_link
                
                	All ATM VC information on a node
                	**type**\: list of    :py:class:`ClassLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.ClassLinks.ClassLink>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.class_link = YList()
                    self.class_link.parent = self
                    self.class_link.name = 'class_link'


                class ClassLink(object):
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
                        self.parent = None
                        self.vpi = None
                        self.oam_config = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig()
                        self.oam_config.parent = self
                        self.sub_interface_name = None
                        self.vc_class_not_supported = AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported()
                        self.vc_class_not_supported.parent = self
                        self.vci = None


                    class VcClassNotSupported(object):
                        """
                        Not supported VC class
                        
                        .. attribute:: encapsulation_not_supported
                        
                        	Encapsulation type not supported
                        	**type**\:   :py:class:`VcEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncapEnum>`
                        
                        .. attribute:: not_supported_inherit_level
                        
                        	NotSupportedInheritLevel
                        	**type**\:   :py:class:`VcInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevelEnum>`
                        
                        

                        """

                        _prefix = 'atm-vcm-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.encapsulation_not_supported = None
                            self.not_supported_inherit_level = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:vc-class-not-supported'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.encapsulation_not_supported is not None:
                                return True

                            if self.not_supported_inherit_level is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                            return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.VcClassNotSupported']['meta_info']


                    class OamConfig(object):
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
                            self.parent = None
                            self.ais_rdi = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi()
                            self.ais_rdi.parent = self
                            self.class_link_encapsulation = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation()
                            self.class_link_encapsulation.parent = self
                            self.class_link_shaping = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping()
                            self.class_link_shaping.parent = self
                            self.oam_pvc = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc()
                            self.oam_pvc.parent = self
                            self.oam_retry = AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry()
                            self.oam_retry.parent = self


                        class ClassLinkShaping(object):
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
                            	**type**\:   :py:class:`VcInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevelEnum>`
                            
                            .. attribute:: shaping_type
                            
                            	ATM VC traffic shaping type
                            	**type**\:   :py:class:`VcTrafShapingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcTrafShapingEnum>`
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.average_output_rate = None
                                self.burst_output_rate = None
                                self.peak_output_rate = None
                                self.shaping_inherit_level = None
                                self.shaping_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:class-link-shaping'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.average_output_rate is not None:
                                    return True

                                if self.burst_output_rate is not None:
                                    return True

                                if self.peak_output_rate is not None:
                                    return True

                                if self.shaping_inherit_level is not None:
                                    return True

                                if self.shaping_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                                return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkShaping']['meta_info']


                        class ClassLinkEncapsulation(object):
                            """
                            Encapsulation details of VC class
                            
                            .. attribute:: encapsulation_inherit_level
                            
                            	Encapsulation inherit level
                            	**type**\:   :py:class:`VcInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcInheritLevelEnum>`
                            
                            .. attribute:: encapsulation_type
                            
                            	Encapsulation type
                            	**type**\:   :py:class:`VcEncapEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcEncapEnum>`
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.encapsulation_inherit_level = None
                                self.encapsulation_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:class-link-encapsulation'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.encapsulation_inherit_level is not None:
                                    return True

                                if self.encapsulation_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                                return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.ClassLinkEncapsulation']['meta_info']


                        class OamPvc(object):
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
                            	**type**\:   :py:class:`ClassLinkOamInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevelEnum>`
                            
                            .. attribute:: manage_level
                            
                            	Manage Level
                            	**type**\:   :py:class:`VcManageLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcManageLevelEnum>`
                            
                            .. attribute:: pvc_frequency
                            
                            	PVC Frequency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ais_rdi_failure = None
                                self.keep_vc_up = None
                                self.manage_inherit_level = None
                                self.manage_level = None
                                self.pvc_frequency = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:oam-pvc'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ais_rdi_failure is not None:
                                    return True

                                if self.keep_vc_up is not None:
                                    return True

                                if self.manage_inherit_level is not None:
                                    return True

                                if self.manage_level is not None:
                                    return True

                                if self.pvc_frequency is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                                return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamPvc']['meta_info']


                        class OamRetry(object):
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
                            	**type**\:   :py:class:`ClassLinkOamInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevelEnum>`
                            
                            .. attribute:: retry_up_count
                            
                            	Retry Count
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'atm-vcm-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.down_count = None
                                self.retry_frequency = None
                                self.retry_inherit_level = None
                                self.retry_up_count = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:oam-retry'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.down_count is not None:
                                    return True

                                if self.retry_frequency is not None:
                                    return True

                                if self.retry_inherit_level is not None:
                                    return True

                                if self.retry_up_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                                return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.OamRetry']['meta_info']


                        class AisRdi(object):
                            """
                            AIS RDI details of a VC class
                            
                            .. attribute:: ais_rdi_inherit_level
                            
                            	AIS RDI inherit level
                            	**type**\:   :py:class:`ClassLinkOamInheritLevelEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.ClassLinkOamInheritLevelEnum>`
                            
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
                                self.parent = None
                                self.ais_rdi_inherit_level = None
                                self.ais_rdi_up_count = None
                                self.ais_rdi_up_time = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:ais-rdi'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ais_rdi_inherit_level is not None:
                                    return True

                                if self.ais_rdi_up_count is not None:
                                    return True

                                if self.ais_rdi_up_time is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                                return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig.AisRdi']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:oam-config'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ais_rdi is not None and self.ais_rdi._has_data():
                                return True

                            if self.class_link_encapsulation is not None and self.class_link_encapsulation._has_data():
                                return True

                            if self.class_link_shaping is not None and self.class_link_shaping._has_data():
                                return True

                            if self.oam_pvc is not None and self.oam_pvc._has_data():
                                return True

                            if self.oam_retry is not None and self.oam_retry._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                            return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink.OamConfig']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.vpi is None:
                            raise YPYModelError('Key property vpi is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:class-link[Cisco-IOS-XR-atm-vcm-oper:vpi = ' + str(self.vpi) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vpi is not None:
                            return True

                        if self.oam_config is not None and self.oam_config._has_data():
                            return True

                        if self.sub_interface_name is not None:
                            return True

                        if self.vc_class_not_supported is not None and self.vc_class_not_supported._has_data():
                            return True

                        if self.vci is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                        return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks.ClassLink']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:class-links'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.class_link is not None:
                        for child_ref in self.class_link:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                    return meta._meta_table['AtmVcm.Nodes.Node.ClassLinks']['meta_info']


            class Interfaces(object):
                """
                Contains all Interface information for node
                
                .. attribute:: interface
                
                	ATM Interface data
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
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
                    	**type**\:   :py:class:`VcmPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VcmPortEnum>`
                    
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
                        self.parent = None
                        self.interface_name = None
                        self.cell_packing_data = AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData()
                        self.cell_packing_data.parent = self
                        self.configured_layer2pv_cs = None
                        self.configured_layer2pv_ps = None
                        self.configured_layer3pv_cs = None
                        self.configured_layer3vp_tunnels = None
                        self.currently_failing_layer2pv_cs = None
                        self.currently_failing_layer2pv_ps = None
                        self.currently_failing_layer3pv_cs = None
                        self.currently_failing_layer3vp_tunnels = None
                        self.ilmi_vci = None
                        self.ilmi_vpi = None
                        self.l2_cell_packing_count = None
                        self.main_interface = None
                        self.port_type = None
                        self.pvc_failures = None
                        self.pvc_failures_trap_enable = None
                        self.pvc_notification_interval = None


                    class CellPackingData(object):
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
                            self.parent = None
                            self.local_max_cells_packed_per_packet = None
                            self.max_cell_packed_timeout = None
                            self.negotiated_max_cells_packed_per_packet = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:cell-packing-data'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.local_max_cells_packed_per_packet is not None:
                                return True

                            if self.max_cell_packed_timeout is not None:
                                return True

                            if self.negotiated_max_cells_packed_per_packet is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                            return meta._meta_table['AtmVcm.Nodes.Node.Interfaces.Interface.CellPackingData']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:interface[Cisco-IOS-XR-atm-vcm-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.cell_packing_data is not None and self.cell_packing_data._has_data():
                            return True

                        if self.configured_layer2pv_cs is not None:
                            return True

                        if self.configured_layer2pv_ps is not None:
                            return True

                        if self.configured_layer3pv_cs is not None:
                            return True

                        if self.configured_layer3vp_tunnels is not None:
                            return True

                        if self.currently_failing_layer2pv_cs is not None:
                            return True

                        if self.currently_failing_layer2pv_ps is not None:
                            return True

                        if self.currently_failing_layer3pv_cs is not None:
                            return True

                        if self.currently_failing_layer3vp_tunnels is not None:
                            return True

                        if self.ilmi_vci is not None:
                            return True

                        if self.ilmi_vpi is not None:
                            return True

                        if self.l2_cell_packing_count is not None:
                            return True

                        if self.main_interface is not None:
                            return True

                        if self.port_type is not None:
                            return True

                        if self.pvc_failures is not None:
                            return True

                        if self.pvc_failures_trap_enable is not None:
                            return True

                        if self.pvc_notification_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                        return meta._meta_table['AtmVcm.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                    return meta._meta_table['AtmVcm.Nodes.Node.Interfaces']['meta_info']


            class VpTunnels(object):
                """
                Contains all VP\-tunnel information for node
                
                .. attribute:: vp_tunnel
                
                	All VP\-tunnel information on a node
                	**type**\: list of    :py:class:`VpTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.AtmVcm.Nodes.Node.VpTunnels.VpTunnel>`
                
                

                """

                _prefix = 'atm-vcm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vp_tunnel = YList()
                    self.vp_tunnel.parent = self
                    self.vp_tunnel.name = 'vp_tunnel'


                class VpTunnel(object):
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
                    	**type**\:   :py:class:`VpStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VpStateEnum>`
                    
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
                    	**type**\:   :py:class:`VpTrafShapingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_vcm_oper.VpTrafShapingEnum>`
                    
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
                        self.parent = None
                        self.interface_name = None
                        self.amin_status = None
                        self.burst_rate = None
                        self.data_vc_count = None
                        self.f4oam_enabled = None
                        self.internal_state = None
                        self.last_vp_state_change_time = None
                        self.main_interface = None
                        self.oper_status = None
                        self.peak_cell_rate = None
                        self.shape = None
                        self.sustained_cell_rate = None
                        self.vp_interface = None
                        self.vpi = None
                        self.vpi_xr = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:vp-tunnel[Cisco-IOS-XR-atm-vcm-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.amin_status is not None:
                            return True

                        if self.burst_rate is not None:
                            return True

                        if self.data_vc_count is not None:
                            return True

                        if self.f4oam_enabled is not None:
                            return True

                        if self.internal_state is not None:
                            return True

                        if self.last_vp_state_change_time is not None:
                            return True

                        if self.main_interface is not None:
                            return True

                        if self.oper_status is not None:
                            return True

                        if self.peak_cell_rate is not None:
                            return True

                        if self.shape is not None:
                            return True

                        if self.sustained_cell_rate is not None:
                            return True

                        if self.vp_interface is not None:
                            return True

                        if self.vpi is not None:
                            return True

                        if self.vpi_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                        return meta._meta_table['AtmVcm.Nodes.Node.VpTunnels.VpTunnel']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-atm-vcm-oper:vp-tunnels'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vp_tunnel is not None:
                        for child_ref in self.vp_tunnel:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                    return meta._meta_table['AtmVcm.Nodes.Node.VpTunnels']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-atm-vcm-oper:atm-vcm/Cisco-IOS-XR-atm-vcm-oper:nodes/Cisco-IOS-XR-atm-vcm-oper:node[Cisco-IOS-XR-atm-vcm-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.cell_packs is not None and self.cell_packs._has_data():
                    return True

                if self.class_links is not None and self.class_links._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.pvps is not None and self.pvps._has_data():
                    return True

                if self.vcs is not None and self.vcs._has_data():
                    return True

                if self.vp_tunnels is not None and self.vp_tunnels._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
                return meta._meta_table['AtmVcm.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-atm-vcm-oper:atm-vcm/Cisco-IOS-XR-atm-vcm-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
            return meta._meta_table['AtmVcm.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-atm-vcm-oper:atm-vcm'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_vcm_oper as meta
        return meta._meta_table['AtmVcm']['meta_info']


