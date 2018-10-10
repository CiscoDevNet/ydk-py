""" Cisco_IOS_XR_lmp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lmp package operational data.

This module contains definitions
for the following management objects\:
  lmp\: Main common UCP/OLM operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OlmAddrTypeId(Enum):
    """
    OlmAddrTypeId (Enum Class)

    OLM Link Address Type

    .. data:: unknown_address = 0

    	Unknown address type

    .. data:: ipv4 = 101

    	IPv4 address type

    .. data:: ipv6 = 102

    	IPv6 address type

    .. data:: unnumbered = 103

    	Unnumberedaddress type

    """

    unknown_address = Enum.YLeaf(0, "unknown-address")

    ipv4 = Enum.YLeaf(101, "ipv4")

    ipv6 = Enum.YLeaf(102, "ipv6")

    unnumbered = Enum.YLeaf(103, "unnumbered")


class OlmCompLinkImState(Enum):
    """
    OlmCompLinkImState (Enum Class)

    The OLM Component link IM state

    .. data:: comp_link_im_state_oir = 0

    	OIR removed

    .. data:: comp_link_im_state_down = 1

    	Down

    .. data:: comp_link_im_state_admin_down = 2

    	Admin Down

    .. data:: comp_link_im_state_up = 3

    	Up

    .. data:: comp_link_im_state_unknown = 4

    	Unknown

    """

    comp_link_im_state_oir = Enum.YLeaf(0, "comp-link-im-state-oir")

    comp_link_im_state_down = Enum.YLeaf(1, "comp-link-im-state-down")

    comp_link_im_state_admin_down = Enum.YLeaf(2, "comp-link-im-state-admin-down")

    comp_link_im_state_up = Enum.YLeaf(3, "comp-link-im-state-up")

    comp_link_im_state_unknown = Enum.YLeaf(4, "comp-link-im-state-unknown")


class OlmCompLinkLmpState(Enum):
    """
    OlmCompLinkLmpState (Enum Class)

    The OLM Component link LMP state

    .. data:: comp_link_lmp_state_down = 0

    	Down

    .. data:: comp_link_lmp_state_test = 1

    	Test

    .. data:: comp_link_lmp_state_passive_test = 2

    	Pasv Test

    .. data:: comp_link_lmp_state_up_free = 3

    	Up Free

    .. data:: comp_link_lmp_state_up_allocated = 4

    	Up Allocated

    .. data:: comp_link_lmp_state_unknown = 5

    	Unknown/Invalid

    """

    comp_link_lmp_state_down = Enum.YLeaf(0, "comp-link-lmp-state-down")

    comp_link_lmp_state_test = Enum.YLeaf(1, "comp-link-lmp-state-test")

    comp_link_lmp_state_passive_test = Enum.YLeaf(2, "comp-link-lmp-state-passive-test")

    comp_link_lmp_state_up_free = Enum.YLeaf(3, "comp-link-lmp-state-up-free")

    comp_link_lmp_state_up_allocated = Enum.YLeaf(4, "comp-link-lmp-state-up-allocated")

    comp_link_lmp_state_unknown = Enum.YLeaf(5, "comp-link-lmp-state-unknown")


class OlmCompLinkLmpStatus(Enum):
    """
    OlmCompLinkLmpStatus (Enum Class)

    The component link LMP status

    .. data:: comp_link_lmp_status_if_id_mismatch = 0

    	Component link IF ID mismatch

    .. data:: comp_link_lmp_status_switch_cap_mismatch = 1

    	Component link switching capability ID mismatch

    """

    comp_link_lmp_status_if_id_mismatch = Enum.YLeaf(0, "comp-link-lmp-status-if-id-mismatch")

    comp_link_lmp_status_switch_cap_mismatch = Enum.YLeaf(1, "comp-link-lmp-status-switch-cap-mismatch")


class OlmLinkEncoding(Enum):
    """
    OlmLinkEncoding (Enum Class)

    LMP link encoding type as defined in [RFC3471]

    .. data:: none = 0

    	None

    .. data:: packet = 1

    	Packet

    .. data:: ethernet = 2

    	Ethernet

    .. data:: ansi_etsi_pdh = 3

    	ANSI/ETSI PDH

    .. data:: reserved1 = 4

    	Reserved

    .. data:: sdh_sonet = 5

    	SDH ITU-T G.707 / SONET ANSI T1.105

    .. data:: reserved2 = 6

    	Reserved

    .. data:: digital_wrapper = 7

    	Digital Wrapper

    .. data:: lambda_ = 8

    	Lambda (photonic)

    .. data:: fiber = 9

    	Fiber

    .. data:: reserved3 = 10

    	Reserved

    .. data:: fiber_channel = 11

    	FiberChannel

    .. data:: lencode_unknown = 12

    	Unknown

    """

    none = Enum.YLeaf(0, "none")

    packet = Enum.YLeaf(1, "packet")

    ethernet = Enum.YLeaf(2, "ethernet")

    ansi_etsi_pdh = Enum.YLeaf(3, "ansi-etsi-pdh")

    reserved1 = Enum.YLeaf(4, "reserved1")

    sdh_sonet = Enum.YLeaf(5, "sdh-sonet")

    reserved2 = Enum.YLeaf(6, "reserved2")

    digital_wrapper = Enum.YLeaf(7, "digital-wrapper")

    lambda_ = Enum.YLeaf(8, "lambda")

    fiber = Enum.YLeaf(9, "fiber")

    reserved3 = Enum.YLeaf(10, "reserved3")

    fiber_channel = Enum.YLeaf(11, "fiber-channel")

    lencode_unknown = Enum.YLeaf(12, "lencode-unknown")


class OlmMuxCap(Enum):
    """
    OlmMuxCap (Enum Class)

    Multiplexing capability

    .. data:: psc1 = 0

    	PSC 1

    .. data:: psc2 = 1

    	PSC 2

    .. data:: psc3 = 2

    	PSC 3

    .. data:: psc4 = 3

    	PSC 4

    .. data:: l2sc = 4

    	L2SC

    .. data:: tdm = 5

    	TDM

    .. data:: lsc = 6

    	LSC

    .. data:: fsc = 7

    	FSC

    .. data:: unknown_mux_cap = 8

    	Unknown Mux Cap

    """

    psc1 = Enum.YLeaf(0, "psc1")

    psc2 = Enum.YLeaf(1, "psc2")

    psc3 = Enum.YLeaf(2, "psc3")

    psc4 = Enum.YLeaf(3, "psc4")

    l2sc = Enum.YLeaf(4, "l2sc")

    tdm = Enum.YLeaf(5, "tdm")

    lsc = Enum.YLeaf(6, "lsc")

    fsc = Enum.YLeaf(7, "fsc")

    unknown_mux_cap = Enum.YLeaf(8, "unknown-mux-cap")


class OlmObjectOwner(Enum):
    """
    OlmObjectOwner (Enum Class)

    The OLM object owner

    .. data:: unknown = 0

    	Unknown owner

    .. data:: ouni = 1

    	OIF OUNI

    .. data:: gmpls_nni = 2

    	GMPLS NNI

    .. data:: gmpls_uni = 3

    	GMPLS UNI

    """

    unknown = Enum.YLeaf(0, "unknown")

    ouni = Enum.YLeaf(1, "ouni")

    gmpls_nni = Enum.YLeaf(2, "gmpls-nni")

    gmpls_uni = Enum.YLeaf(3, "gmpls-uni")


class OlmRouterId(Enum):
    """
    OlmRouterId (Enum Class)

    The OLM router ID type

    .. data:: not_configured = 0

    	No router ID configured

    .. data:: global_ = 1

    	Global router ID

    .. data:: protocol_based_address = 2

    	Protocol based CLIrouter ID configured

    .. data:: interface = 3

    	Protocol based CLI I/Frouter ID configured

    .. data:: network_element = 4

    	Protocol based CLI I/F routerID configured on

    	I/F that is not known to the system

    .. data:: unknown_type = 5

    	Unknown

    """

    not_configured = Enum.YLeaf(0, "not-configured")

    global_ = Enum.YLeaf(1, "global")

    protocol_based_address = Enum.YLeaf(2, "protocol-based-address")

    interface = Enum.YLeaf(3, "interface")

    network_element = Enum.YLeaf(4, "network-element")

    unknown_type = Enum.YLeaf(5, "unknown-type")


class Olmipcc(Enum):
    """
    Olmipcc (Enum Class)

    The OLM IPCC type

    .. data:: ipcc_type_global_routed = 0

    	Global routed IPCC

    .. data:: ipcc_type_global_if_bound = 1

    	Global I/F bound IPCC

    .. data:: ipcc_type_ldcc_sdcc = 2

    	SDCC/LDCC in fiber in band type IPCC

    .. data:: ipcc_type_unknown = 3

    	Unknown IPCC type

    """

    ipcc_type_global_routed = Enum.YLeaf(0, "ipcc-type-global-routed")

    ipcc_type_global_if_bound = Enum.YLeaf(1, "ipcc-type-global-if-bound")

    ipcc_type_ldcc_sdcc = Enum.YLeaf(2, "ipcc-type-ldcc-sdcc")

    ipcc_type_unknown = Enum.YLeaf(3, "ipcc-type-unknown")


class OlmipccState(Enum):
    """
    OlmipccState (Enum Class)

    The OLM IPCC state

    .. data:: ipcc_state_oir_removed = 0

    	OIR Removed

    .. data:: ipcc_state_admin_down = 1

    	OOS

    .. data:: ipcc_state_down = 2

    	Down

    .. data:: ipcc_state_cfg_send = 3

    	ConfigSend

    .. data:: ipcc_state_cfg_rcv = 4

    	ConfigReceive

    .. data:: ipcc_state_active = 5

    	Active

    .. data:: ipcc_state_up = 6

    	Up

    .. data:: ipcc_state_going_down = 7

    	Going Down

    .. data:: ipcc_state_unknown = 8

    	Unknown/Invalid

    """

    ipcc_state_oir_removed = Enum.YLeaf(0, "ipcc-state-oir-removed")

    ipcc_state_admin_down = Enum.YLeaf(1, "ipcc-state-admin-down")

    ipcc_state_down = Enum.YLeaf(2, "ipcc-state-down")

    ipcc_state_cfg_send = Enum.YLeaf(3, "ipcc-state-cfg-send")

    ipcc_state_cfg_rcv = Enum.YLeaf(4, "ipcc-state-cfg-rcv")

    ipcc_state_active = Enum.YLeaf(5, "ipcc-state-active")

    ipcc_state_up = Enum.YLeaf(6, "ipcc-state-up")

    ipcc_state_going_down = Enum.YLeaf(7, "ipcc-state-going-down")

    ipcc_state_unknown = Enum.YLeaf(8, "ipcc-state-unknown")


class OlmteLinkLmpState(Enum):
    """
    OlmteLinkLmpState (Enum Class)

    The OLM TE link LMP state

    .. data:: te_link_lmp_state_down = 0

    	Down

    .. data:: te_link_lmp_state_init = 1

    	Init

    .. data:: te_link_lmp_state_up = 2

    	Up

    .. data:: te_link_lmp_state_degraded = 3

    	Degraded

    .. data:: te_link_lmp_state_unknown = 4

    	Unknown/Invalid

    """

    te_link_lmp_state_down = Enum.YLeaf(0, "te-link-lmp-state-down")

    te_link_lmp_state_init = Enum.YLeaf(1, "te-link-lmp-state-init")

    te_link_lmp_state_up = Enum.YLeaf(2, "te-link-lmp-state-up")

    te_link_lmp_state_degraded = Enum.YLeaf(3, "te-link-lmp-state-degraded")

    te_link_lmp_state_unknown = Enum.YLeaf(4, "te-link-lmp-state-unknown")



class Lmp(Entity):
    """
    Main common UCP/OLM operational data
    
    .. attribute:: global_status
    
    	Global OLM process information
    	**type**\:  :py:class:`GlobalStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GlobalStatus>`
    
    .. attribute:: clients
    
    	UCP OLM clients container class
    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.Clients>`
    
    .. attribute:: gmpls_uni
    
    	GMPLS UNI specific OLM/LMP configuration
    	**type**\:  :py:class:`GmplsUni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni>`
    
    .. attribute:: component_link_ids
    
    	UCP OLM component link ID container class
    	**type**\:  :py:class:`ComponentLinkIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.ComponentLinkIds>`
    
    

    """

    _prefix = 'lmp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Lmp, self).__init__()
        self._top_entity = None

        self.yang_name = "lmp"
        self.yang_parent_name = "Cisco-IOS-XR-lmp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("global-status", ("global_status", Lmp.GlobalStatus)), ("clients", ("clients", Lmp.Clients)), ("gmpls-uni", ("gmpls_uni", Lmp.GmplsUni)), ("component-link-ids", ("component_link_ids", Lmp.ComponentLinkIds))])
        self._leafs = OrderedDict()

        self.global_status = Lmp.GlobalStatus()
        self.global_status.parent = self
        self._children_name_map["global_status"] = "global-status"

        self.clients = Lmp.Clients()
        self.clients.parent = self
        self._children_name_map["clients"] = "clients"

        self.gmpls_uni = Lmp.GmplsUni()
        self.gmpls_uni.parent = self
        self._children_name_map["gmpls_uni"] = "gmpls-uni"

        self.component_link_ids = Lmp.ComponentLinkIds()
        self.component_link_ids.parent = self
        self._children_name_map["component_link_ids"] = "component-link-ids"
        self._segment_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Lmp, [], name, value)


    class GlobalStatus(Entity):
        """
        Global OLM process information
        
        .. attribute:: local_ouni_lmp_node_id
        
        	Local OUNI LMP Node ID
        	**type**\:  :py:class:`LocalOuniLmpNodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GlobalStatus.LocalOuniLmpNodeId>`
        
        .. attribute:: local_mpls_te_lmp_node_id
        
        	MPLS TE LMP Node ID
        	**type**\:  :py:class:`LocalMplsTeLmpNodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GlobalStatus.LocalMplsTeLmpNodeId>`
        
        .. attribute:: local_gmpls_uni_lmp_node_id
        
        	GMPLS UNI LMP Node ID
        	**type**\:  :py:class:`LocalGmplsUniLmpNodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GlobalStatus.LocalGmplsUniLmpNodeId>`
        
        .. attribute:: local_ouni_lmp_node_id_interface
        
        	Local OUNI LMP Node ID I/F
        	**type**\: str
        
        .. attribute:: local_ouni_lmp_node_id_type
        
        	Local OUNI LMP Node ID type
        	**type**\:  :py:class:`OlmRouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmRouterId>`
        
        .. attribute:: is_ouni_config_exist
        
        	TRUE if any OLM OUNI config exists
        	**type**\: bool
        
        .. attribute:: is_gmpls_nni_config_exist
        
        	TRUE if any OLM/LNP GMPLS NNI config exists
        	**type**\: bool
        
        .. attribute:: is_gmpls_uni_config_exist
        
        	TRUE if any OLM/LMP GMPLS UNI config exists
        	**type**\: bool
        
        

        """

        _prefix = 'lmp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lmp.GlobalStatus, self).__init__()

            self.yang_name = "global-status"
            self.yang_parent_name = "lmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("local-ouni-lmp-node-id", ("local_ouni_lmp_node_id", Lmp.GlobalStatus.LocalOuniLmpNodeId)), ("local-mpls-te-lmp-node-id", ("local_mpls_te_lmp_node_id", Lmp.GlobalStatus.LocalMplsTeLmpNodeId)), ("local-gmpls-uni-lmp-node-id", ("local_gmpls_uni_lmp_node_id", Lmp.GlobalStatus.LocalGmplsUniLmpNodeId))])
            self._leafs = OrderedDict([
                ('local_ouni_lmp_node_id_interface', (YLeaf(YType.str, 'local-ouni-lmp-node-id-interface'), ['str'])),
                ('local_ouni_lmp_node_id_type', (YLeaf(YType.enumeration, 'local-ouni-lmp-node-id-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmRouterId', '')])),
                ('is_ouni_config_exist', (YLeaf(YType.boolean, 'is-ouni-config-exist'), ['bool'])),
                ('is_gmpls_nni_config_exist', (YLeaf(YType.boolean, 'is-gmpls-nni-config-exist'), ['bool'])),
                ('is_gmpls_uni_config_exist', (YLeaf(YType.boolean, 'is-gmpls-uni-config-exist'), ['bool'])),
            ])
            self.local_ouni_lmp_node_id_interface = None
            self.local_ouni_lmp_node_id_type = None
            self.is_ouni_config_exist = None
            self.is_gmpls_nni_config_exist = None
            self.is_gmpls_uni_config_exist = None

            self.local_ouni_lmp_node_id = Lmp.GlobalStatus.LocalOuniLmpNodeId()
            self.local_ouni_lmp_node_id.parent = self
            self._children_name_map["local_ouni_lmp_node_id"] = "local-ouni-lmp-node-id"

            self.local_mpls_te_lmp_node_id = Lmp.GlobalStatus.LocalMplsTeLmpNodeId()
            self.local_mpls_te_lmp_node_id.parent = self
            self._children_name_map["local_mpls_te_lmp_node_id"] = "local-mpls-te-lmp-node-id"

            self.local_gmpls_uni_lmp_node_id = Lmp.GlobalStatus.LocalGmplsUniLmpNodeId()
            self.local_gmpls_uni_lmp_node_id.parent = self
            self._children_name_map["local_gmpls_uni_lmp_node_id"] = "local-gmpls-uni-lmp-node-id"
            self._segment_path = lambda: "global-status"
            self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lmp.GlobalStatus, ['local_ouni_lmp_node_id_interface', 'local_ouni_lmp_node_id_type', 'is_ouni_config_exist', 'is_gmpls_nni_config_exist', 'is_gmpls_uni_config_exist'], name, value)


        class LocalOuniLmpNodeId(Entity):
            """
            Local OUNI LMP Node ID
            
            .. attribute:: address
            
            	Address Union
            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GlobalStatus.LocalOuniLmpNodeId.Address>`
            
            

            """

            _prefix = 'lmp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.GlobalStatus.LocalOuniLmpNodeId, self).__init__()

                self.yang_name = "local-ouni-lmp-node-id"
                self.yang_parent_name = "global-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("address", ("address", Lmp.GlobalStatus.LocalOuniLmpNodeId.Address))])
                self._leafs = OrderedDict()

                self.address = Lmp.GlobalStatus.LocalOuniLmpNodeId.Address()
                self.address.parent = self
                self._children_name_map["address"] = "address"
                self._segment_path = lambda: "local-ouni-lmp-node-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/global-status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.GlobalStatus.LocalOuniLmpNodeId, [], name, value)


            class Address(Entity):
                """
                Address Union
                
                .. attribute:: address_type
                
                	AddressType
                	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                
                .. attribute:: ipv4_address
                
                	IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: unnumbered_address
                
                	Unnumberedaddress
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lmp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lmp.GlobalStatus.LocalOuniLmpNodeId.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "local-ouni-lmp-node-id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                        ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                    ])
                    self.address_type = None
                    self.ipv4_address = None
                    self.ipv6_address = None
                    self.unnumbered_address = None
                    self._segment_path = lambda: "address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/global-status/local-ouni-lmp-node-id/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lmp.GlobalStatus.LocalOuniLmpNodeId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


        class LocalMplsTeLmpNodeId(Entity):
            """
            MPLS TE LMP Node ID
            
            .. attribute:: address
            
            	Address Union
            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GlobalStatus.LocalMplsTeLmpNodeId.Address>`
            
            

            """

            _prefix = 'lmp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.GlobalStatus.LocalMplsTeLmpNodeId, self).__init__()

                self.yang_name = "local-mpls-te-lmp-node-id"
                self.yang_parent_name = "global-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("address", ("address", Lmp.GlobalStatus.LocalMplsTeLmpNodeId.Address))])
                self._leafs = OrderedDict()

                self.address = Lmp.GlobalStatus.LocalMplsTeLmpNodeId.Address()
                self.address.parent = self
                self._children_name_map["address"] = "address"
                self._segment_path = lambda: "local-mpls-te-lmp-node-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/global-status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.GlobalStatus.LocalMplsTeLmpNodeId, [], name, value)


            class Address(Entity):
                """
                Address Union
                
                .. attribute:: address_type
                
                	AddressType
                	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                
                .. attribute:: ipv4_address
                
                	IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: unnumbered_address
                
                	Unnumberedaddress
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lmp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lmp.GlobalStatus.LocalMplsTeLmpNodeId.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "local-mpls-te-lmp-node-id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                        ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                    ])
                    self.address_type = None
                    self.ipv4_address = None
                    self.ipv6_address = None
                    self.unnumbered_address = None
                    self._segment_path = lambda: "address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/global-status/local-mpls-te-lmp-node-id/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lmp.GlobalStatus.LocalMplsTeLmpNodeId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


        class LocalGmplsUniLmpNodeId(Entity):
            """
            GMPLS UNI LMP Node ID
            
            .. attribute:: address
            
            	Address Union
            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GlobalStatus.LocalGmplsUniLmpNodeId.Address>`
            
            

            """

            _prefix = 'lmp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.GlobalStatus.LocalGmplsUniLmpNodeId, self).__init__()

                self.yang_name = "local-gmpls-uni-lmp-node-id"
                self.yang_parent_name = "global-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("address", ("address", Lmp.GlobalStatus.LocalGmplsUniLmpNodeId.Address))])
                self._leafs = OrderedDict()

                self.address = Lmp.GlobalStatus.LocalGmplsUniLmpNodeId.Address()
                self.address.parent = self
                self._children_name_map["address"] = "address"
                self._segment_path = lambda: "local-gmpls-uni-lmp-node-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/global-status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.GlobalStatus.LocalGmplsUniLmpNodeId, [], name, value)


            class Address(Entity):
                """
                Address Union
                
                .. attribute:: address_type
                
                	AddressType
                	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                
                .. attribute:: ipv4_address
                
                	IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: unnumbered_address
                
                	Unnumberedaddress
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lmp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lmp.GlobalStatus.LocalGmplsUniLmpNodeId.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "local-gmpls-uni-lmp-node-id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                        ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                    ])
                    self.address_type = None
                    self.ipv4_address = None
                    self.ipv6_address = None
                    self.unnumbered_address = None
                    self._segment_path = lambda: "address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/global-status/local-gmpls-uni-lmp-node-id/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lmp.GlobalStatus.LocalGmplsUniLmpNodeId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


    class Clients(Entity):
        """
        UCP OLM clients container class
        
        .. attribute:: client
        
        	Information on a particular OLM API client
        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.Clients.Client>`
        
        

        """

        _prefix = 'lmp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lmp.Clients, self).__init__()

            self.yang_name = "clients"
            self.yang_parent_name = "lmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("client", ("client", Lmp.Clients.Client))])
            self._leafs = OrderedDict()

            self.client = YList(self)
            self._segment_path = lambda: "clients"
            self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lmp.Clients, [], name, value)


        class Client(Entity):
            """
            Information on a particular OLM API client
            
            .. attribute:: client_name  (key)
            
            	Client name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: connected_time
            
            	The time the clientconnected in sec
            	**type**\:  :py:class:`ConnectedTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.Clients.Client.ConnectedTime>`
            
            .. attribute:: node_name
            
            	The RP name that the clientprocess is running on
            	**type**\: str
            
            

            """

            _prefix = 'lmp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.Clients.Client, self).__init__()

                self.yang_name = "client"
                self.yang_parent_name = "clients"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['client_name']
                self._child_classes = OrderedDict([("connected-time", ("connected_time", Lmp.Clients.Client.ConnectedTime))])
                self._leafs = OrderedDict([
                    ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.client_name = None
                self.node_name = None

                self.connected_time = Lmp.Clients.Client.ConnectedTime()
                self.connected_time.parent = self
                self._children_name_map["connected_time"] = "connected-time"
                self._segment_path = lambda: "client" + "[client-name='" + str(self.client_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/clients/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.Clients.Client, ['client_name', 'node_name'], name, value)


            class ConnectedTime(Entity):
                """
                The time the clientconnected in sec
                
                .. attribute:: time_connected
                
                	The time the clientconnected in sec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lmp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lmp.Clients.Client.ConnectedTime, self).__init__()

                    self.yang_name = "connected-time"
                    self.yang_parent_name = "client"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_connected', (YLeaf(YType.uint32, 'time-connected'), ['int'])),
                    ])
                    self.time_connected = None
                    self._segment_path = lambda: "connected-time"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lmp.Clients.Client.ConnectedTime, ['time_connected'], name, value)


    class GmplsUni(Entity):
        """
        GMPLS UNI specific OLM/LMP configuration
        
        .. attribute:: te_links
        
        	UCP OLM TE Links container class
        	**type**\:  :py:class:`TeLinks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks>`
        
        .. attribute:: neighbors
        
        	UCP OLM neighbors container class
        	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors>`
        
        

        """

        _prefix = 'lmp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lmp.GmplsUni, self).__init__()

            self.yang_name = "gmpls-uni"
            self.yang_parent_name = "lmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("te-links", ("te_links", Lmp.GmplsUni.TeLinks)), ("neighbors", ("neighbors", Lmp.GmplsUni.Neighbors))])
            self._leafs = OrderedDict()

            self.te_links = Lmp.GmplsUni.TeLinks()
            self.te_links.parent = self
            self._children_name_map["te_links"] = "te-links"

            self.neighbors = Lmp.GmplsUni.Neighbors()
            self.neighbors.parent = self
            self._children_name_map["neighbors"] = "neighbors"
            self._segment_path = lambda: "gmpls-uni"
            self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lmp.GmplsUni, [], name, value)


        class TeLinks(Entity):
            """
            UCP OLM TE Links container class
            
            .. attribute:: te_link
            
            	Information on a particular OLM TE Link
            	**type**\: list of  		 :py:class:`TeLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink>`
            
            

            """

            _prefix = 'lmp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.GmplsUni.TeLinks, self).__init__()

                self.yang_name = "te-links"
                self.yang_parent_name = "gmpls-uni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("te-link", ("te_link", Lmp.GmplsUni.TeLinks.TeLink))])
                self._leafs = OrderedDict()

                self.te_link = YList(self)
                self._segment_path = lambda: "te-links"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/gmpls-uni/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.GmplsUni.TeLinks, [], name, value)


            class TeLink(Entity):
                """
                Information on a particular OLM TE Link
                
                .. attribute:: controller_name  (key)
                
                	Controller name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: local_link_id
                
                	The local datalink ID
                	**type**\:  :py:class:`LocalLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId>`
                
                .. attribute:: remote_link_id
                
                	The remote datalink ID
                	**type**\:  :py:class:`RemoteLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId>`
                
                .. attribute:: local_te_link_id
                
                	Local TE\-Link ID/ TNA address
                	**type**\:  :py:class:`LocalTeLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId>`
                
                .. attribute:: remote_te_link_id
                
                	Remote TE\-Link ID/ TNA address
                	**type**\:  :py:class:`RemoteTeLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId>`
                
                .. attribute:: neighbor_address
                
                	The address of the neighbor
                	**type**\:  :py:class:`NeighborAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress>`
                
                .. attribute:: remote_ipcc_address
                
                	The remote node's IPCC address
                	**type**\:  :py:class:`RemoteIpccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress>`
                
                .. attribute:: interface_name
                
                	Interface forOLM info
                	**type**\: str
                
                .. attribute:: protocol_owner
                
                	Protocol owningthis te\-link
                	**type**\:  :py:class:`OlmObjectOwner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmObjectOwner>`
                
                .. attribute:: neighbor_name
                
                	The name of the neighbor
                	**type**\: str
                
                .. attribute:: ipcc_id
                
                	The IPCC ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ipc_ctype
                
                	OLM IPCC type
                	**type**\:  :py:class:`Olmipcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Olmipcc>`
                
                .. attribute:: ipcc_name
                
                	The name ofthe IPCC associated with the TE Link
                	**type**\: str
                
                .. attribute:: local_mux_cap
                
                	The local mux capability
                	**type**\:  :py:class:`OlmMuxCap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmMuxCap>`
                
                .. attribute:: remote_mux_cap
                
                	The remote mux capability
                	**type**\:  :py:class:`OlmMuxCap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmMuxCap>`
                
                .. attribute:: im_state
                
                	data link IM state
                	**type**\:  :py:class:`OlmCompLinkImState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmCompLinkImState>`
                
                .. attribute:: lmp_state
                
                	data link LMP state
                	**type**\:  :py:class:`OlmCompLinkLmpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmCompLinkLmpState>`
                
                .. attribute:: te_link_lmp_state
                
                	TE LinkLMP state
                	**type**\:  :py:class:`OlmteLinkLmpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmteLinkLmpState>`
                
                .. attribute:: gmpls_te_link_local_minimum_bandwidth
                
                	GMPLS localminimum B/W in bytes/sec
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte/s
                
                .. attribute:: gmpls_te_link_local_maximum_bandwidth
                
                	GMPLS localmaximum B/W in bytes/sec
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte/s
                
                .. attribute:: gmpls_te_link_neighbor_minimum_bandwidth
                
                	GMPLSneighbor minimum B/W in bytes/sec
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte/s
                
                .. attribute:: gmpls_te_link_neighbor_maximum_bandwidth
                
                	GMPLSneighbor maximum B/W in bytes/sec
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte/s
                
                .. attribute:: gmpls_te_link_local_encoding_type
                
                	GMPLS locallink encoding type
                	**type**\:  :py:class:`OlmLinkEncoding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmLinkEncoding>`
                
                .. attribute:: gmpls_te_link_neighbor_encoding_type
                
                	GMPLS neighborlink encoding type
                	**type**\:  :py:class:`OlmLinkEncoding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmLinkEncoding>`
                
                .. attribute:: is_lmp_enabled
                
                	Is LMP enabledon this TE link
                	**type**\: bool
                
                .. attribute:: lmp_transmit_msg_id
                
                	LMP transmitmessage ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lmp_receive_msg_id
                
                	LMP receivemessage ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lmp_comp_link_status
                
                	Component link LMP status indicators
                	**type**\: list of   :py:class:`OlmCompLinkLmpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmCompLinkLmpStatus>`
                
                

                """

                _prefix = 'lmp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lmp.GmplsUni.TeLinks.TeLink, self).__init__()

                    self.yang_name = "te-link"
                    self.yang_parent_name = "te-links"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['controller_name']
                    self._child_classes = OrderedDict([("local-link-id", ("local_link_id", Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId)), ("remote-link-id", ("remote_link_id", Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId)), ("local-te-link-id", ("local_te_link_id", Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId)), ("remote-te-link-id", ("remote_te_link_id", Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId)), ("neighbor-address", ("neighbor_address", Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress)), ("remote-ipcc-address", ("remote_ipcc_address", Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress))])
                    self._leafs = OrderedDict([
                        ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('protocol_owner', (YLeaf(YType.enumeration, 'protocol-owner'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmObjectOwner', '')])),
                        ('neighbor_name', (YLeaf(YType.str, 'neighbor-name'), ['str'])),
                        ('ipcc_id', (YLeaf(YType.uint32, 'ipcc-id'), ['int'])),
                        ('ipc_ctype', (YLeaf(YType.enumeration, 'ipc-ctype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'Olmipcc', '')])),
                        ('ipcc_name', (YLeaf(YType.str, 'ipcc-name'), ['str'])),
                        ('local_mux_cap', (YLeaf(YType.enumeration, 'local-mux-cap'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmMuxCap', '')])),
                        ('remote_mux_cap', (YLeaf(YType.enumeration, 'remote-mux-cap'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmMuxCap', '')])),
                        ('im_state', (YLeaf(YType.enumeration, 'im-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmCompLinkImState', '')])),
                        ('lmp_state', (YLeaf(YType.enumeration, 'lmp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmCompLinkLmpState', '')])),
                        ('te_link_lmp_state', (YLeaf(YType.enumeration, 'te-link-lmp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmteLinkLmpState', '')])),
                        ('gmpls_te_link_local_minimum_bandwidth', (YLeaf(YType.uint64, 'gmpls-te-link-local-minimum-bandwidth'), ['int'])),
                        ('gmpls_te_link_local_maximum_bandwidth', (YLeaf(YType.uint64, 'gmpls-te-link-local-maximum-bandwidth'), ['int'])),
                        ('gmpls_te_link_neighbor_minimum_bandwidth', (YLeaf(YType.uint64, 'gmpls-te-link-neighbor-minimum-bandwidth'), ['int'])),
                        ('gmpls_te_link_neighbor_maximum_bandwidth', (YLeaf(YType.uint64, 'gmpls-te-link-neighbor-maximum-bandwidth'), ['int'])),
                        ('gmpls_te_link_local_encoding_type', (YLeaf(YType.enumeration, 'gmpls-te-link-local-encoding-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmLinkEncoding', '')])),
                        ('gmpls_te_link_neighbor_encoding_type', (YLeaf(YType.enumeration, 'gmpls-te-link-neighbor-encoding-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmLinkEncoding', '')])),
                        ('is_lmp_enabled', (YLeaf(YType.boolean, 'is-lmp-enabled'), ['bool'])),
                        ('lmp_transmit_msg_id', (YLeaf(YType.uint32, 'lmp-transmit-msg-id'), ['int'])),
                        ('lmp_receive_msg_id', (YLeaf(YType.uint32, 'lmp-receive-msg-id'), ['int'])),
                        ('lmp_comp_link_status', (YLeafList(YType.enumeration, 'lmp-comp-link-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmCompLinkLmpStatus', '')])),
                    ])
                    self.controller_name = None
                    self.interface_name = None
                    self.protocol_owner = None
                    self.neighbor_name = None
                    self.ipcc_id = None
                    self.ipc_ctype = None
                    self.ipcc_name = None
                    self.local_mux_cap = None
                    self.remote_mux_cap = None
                    self.im_state = None
                    self.lmp_state = None
                    self.te_link_lmp_state = None
                    self.gmpls_te_link_local_minimum_bandwidth = None
                    self.gmpls_te_link_local_maximum_bandwidth = None
                    self.gmpls_te_link_neighbor_minimum_bandwidth = None
                    self.gmpls_te_link_neighbor_maximum_bandwidth = None
                    self.gmpls_te_link_local_encoding_type = None
                    self.gmpls_te_link_neighbor_encoding_type = None
                    self.is_lmp_enabled = None
                    self.lmp_transmit_msg_id = None
                    self.lmp_receive_msg_id = None
                    self.lmp_comp_link_status = []

                    self.local_link_id = Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId()
                    self.local_link_id.parent = self
                    self._children_name_map["local_link_id"] = "local-link-id"

                    self.remote_link_id = Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId()
                    self.remote_link_id.parent = self
                    self._children_name_map["remote_link_id"] = "remote-link-id"

                    self.local_te_link_id = Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId()
                    self.local_te_link_id.parent = self
                    self._children_name_map["local_te_link_id"] = "local-te-link-id"

                    self.remote_te_link_id = Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId()
                    self.remote_te_link_id.parent = self
                    self._children_name_map["remote_te_link_id"] = "remote-te-link-id"

                    self.neighbor_address = Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress()
                    self.neighbor_address.parent = self
                    self._children_name_map["neighbor_address"] = "neighbor-address"

                    self.remote_ipcc_address = Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress()
                    self.remote_ipcc_address.parent = self
                    self._children_name_map["remote_ipcc_address"] = "remote-ipcc-address"
                    self._segment_path = lambda: "te-link" + "[controller-name='" + str(self.controller_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/gmpls-uni/te-links/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink, ['controller_name', 'interface_name', 'protocol_owner', 'neighbor_name', 'ipcc_id', 'ipc_ctype', 'ipcc_name', 'local_mux_cap', 'remote_mux_cap', 'im_state', 'lmp_state', 'te_link_lmp_state', 'gmpls_te_link_local_minimum_bandwidth', 'gmpls_te_link_local_maximum_bandwidth', 'gmpls_te_link_neighbor_minimum_bandwidth', 'gmpls_te_link_neighbor_maximum_bandwidth', 'gmpls_te_link_local_encoding_type', 'gmpls_te_link_neighbor_encoding_type', 'is_lmp_enabled', 'lmp_transmit_msg_id', 'lmp_receive_msg_id', 'lmp_comp_link_status'], name, value)


                class LocalLinkId(Entity):
                    """
                    The local datalink ID
                    
                    .. attribute:: address
                    
                    	Address Union
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId.Address>`
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId, self).__init__()

                        self.yang_name = "local-link-id"
                        self.yang_parent_name = "te-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId.Address))])
                        self._leafs = OrderedDict()

                        self.address = Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "local-link-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId, [], name, value)


                    class Address(Entity):
                        """
                        Address Union
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: unnumbered_address
                        
                        	Unnumberedaddress
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "local-link-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                            ])
                            self.address_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self.unnumbered_address = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.LocalLinkId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                class RemoteLinkId(Entity):
                    """
                    The remote datalink ID
                    
                    .. attribute:: address
                    
                    	Address Union
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId.Address>`
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId, self).__init__()

                        self.yang_name = "remote-link-id"
                        self.yang_parent_name = "te-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId.Address))])
                        self._leafs = OrderedDict()

                        self.address = Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "remote-link-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId, [], name, value)


                    class Address(Entity):
                        """
                        Address Union
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: unnumbered_address
                        
                        	Unnumberedaddress
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "remote-link-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                            ])
                            self.address_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self.unnumbered_address = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.RemoteLinkId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                class LocalTeLinkId(Entity):
                    """
                    Local TE\-Link ID/ TNA address
                    
                    .. attribute:: address
                    
                    	Address Union
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId.Address>`
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId, self).__init__()

                        self.yang_name = "local-te-link-id"
                        self.yang_parent_name = "te-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId.Address))])
                        self._leafs = OrderedDict()

                        self.address = Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "local-te-link-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId, [], name, value)


                    class Address(Entity):
                        """
                        Address Union
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: unnumbered_address
                        
                        	Unnumberedaddress
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "local-te-link-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                            ])
                            self.address_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self.unnumbered_address = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.LocalTeLinkId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                class RemoteTeLinkId(Entity):
                    """
                    Remote TE\-Link ID/ TNA address
                    
                    .. attribute:: address
                    
                    	Address Union
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId.Address>`
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId, self).__init__()

                        self.yang_name = "remote-te-link-id"
                        self.yang_parent_name = "te-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId.Address))])
                        self._leafs = OrderedDict()

                        self.address = Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "remote-te-link-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId, [], name, value)


                    class Address(Entity):
                        """
                        Address Union
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: unnumbered_address
                        
                        	Unnumberedaddress
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "remote-te-link-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                            ])
                            self.address_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self.unnumbered_address = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.RemoteTeLinkId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                class NeighborAddress(Entity):
                    """
                    The address of the neighbor
                    
                    .. attribute:: address
                    
                    	Address Union
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress.Address>`
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress, self).__init__()

                        self.yang_name = "neighbor-address"
                        self.yang_parent_name = "te-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress.Address))])
                        self._leafs = OrderedDict()

                        self.address = Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "neighbor-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress, [], name, value)


                    class Address(Entity):
                        """
                        Address Union
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: unnumbered_address
                        
                        	Unnumberedaddress
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "neighbor-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                            ])
                            self.address_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self.unnumbered_address = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.NeighborAddress.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                class RemoteIpccAddress(Entity):
                    """
                    The remote node's IPCC address
                    
                    .. attribute:: address
                    
                    	Address Union
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress.Address>`
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress, self).__init__()

                        self.yang_name = "remote-ipcc-address"
                        self.yang_parent_name = "te-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress.Address))])
                        self._leafs = OrderedDict()

                        self.address = Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "remote-ipcc-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress, [], name, value)


                    class Address(Entity):
                        """
                        Address Union
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: unnumbered_address
                        
                        	Unnumberedaddress
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "remote-ipcc-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                            ])
                            self.address_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self.unnumbered_address = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.TeLinks.TeLink.RemoteIpccAddress.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


        class Neighbors(Entity):
            """
            UCP OLM neighbors container class
            
            .. attribute:: neighbor
            
            	Information on a particular OLM neighbor
            	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor>`
            
            

            """

            _prefix = 'lmp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.GmplsUni.Neighbors, self).__init__()

                self.yang_name = "neighbors"
                self.yang_parent_name = "gmpls-uni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("neighbor", ("neighbor", Lmp.GmplsUni.Neighbors.Neighbor))])
                self._leafs = OrderedDict()

                self.neighbor = YList(self)
                self._segment_path = lambda: "neighbors"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/gmpls-uni/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.GmplsUni.Neighbors, [], name, value)


            class Neighbor(Entity):
                """
                Information on a particular OLM neighbor
                
                .. attribute:: neighbor_name  (key)
                
                	Neighbor name
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: neighbor_address
                
                	The remote node ID of the neighbor
                	**type**\:  :py:class:`NeighborAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress>`
                
                .. attribute:: protocol_owner
                
                	Protocol owningthis neighbor
                	**type**\:  :py:class:`OlmObjectOwner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmObjectOwner>`
                
                .. attribute:: ipcc_id
                
                	The global active IPCCfor this neighbor
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_lmp_enabled
                
                	Is LMP enabled on this neighbor [DEPRECATED]
                	**type**\: bool
                
                .. attribute:: is_lmp_config_disabled
                
                	Are LMP hellos disabled through configuration for this neighbor [DEPRECATED]
                	**type**\: bool
                
                .. attribute:: lmp_transmit_msg_id
                
                	LMP transmit message ID [DEPRECATED]
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lmp_receive_msg_id
                
                	LMP receive message ID [DEPRECATED]
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lmp_link_sum_transmit_packets
                
                	LMP link summary transmit packet count [DEPRECATED]
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lmp_link_sum_receive_packets
                
                	LMP link summary receive packet count[DEPRECATED]
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_link
                
                	A list of TE Links connected to this neighbor
                	**type**\: list of  		 :py:class:`TeLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink>`
                
                .. attribute:: ipcc
                
                	A list of IPCCs connected to this neighbor
                	**type**\: list of  		 :py:class:`Ipcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.Ipcc>`
                
                

                """

                _prefix = 'lmp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Lmp.GmplsUni.Neighbors.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "neighbors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['neighbor_name']
                    self._child_classes = OrderedDict([("neighbor-address", ("neighbor_address", Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress)), ("te-link", ("te_link", Lmp.GmplsUni.Neighbors.Neighbor.TeLink)), ("ipcc", ("ipcc", Lmp.GmplsUni.Neighbors.Neighbor.Ipcc))])
                    self._leafs = OrderedDict([
                        ('neighbor_name', (YLeaf(YType.str, 'neighbor-name'), ['str'])),
                        ('protocol_owner', (YLeaf(YType.enumeration, 'protocol-owner'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmObjectOwner', '')])),
                        ('ipcc_id', (YLeaf(YType.uint32, 'ipcc-id'), ['int'])),
                        ('is_lmp_enabled', (YLeaf(YType.boolean, 'is-lmp-enabled'), ['bool'])),
                        ('is_lmp_config_disabled', (YLeaf(YType.boolean, 'is-lmp-config-disabled'), ['bool'])),
                        ('lmp_transmit_msg_id', (YLeaf(YType.uint32, 'lmp-transmit-msg-id'), ['int'])),
                        ('lmp_receive_msg_id', (YLeaf(YType.uint32, 'lmp-receive-msg-id'), ['int'])),
                        ('lmp_link_sum_transmit_packets', (YLeaf(YType.uint32, 'lmp-link-sum-transmit-packets'), ['int'])),
                        ('lmp_link_sum_receive_packets', (YLeaf(YType.uint32, 'lmp-link-sum-receive-packets'), ['int'])),
                    ])
                    self.neighbor_name = None
                    self.protocol_owner = None
                    self.ipcc_id = None
                    self.is_lmp_enabled = None
                    self.is_lmp_config_disabled = None
                    self.lmp_transmit_msg_id = None
                    self.lmp_receive_msg_id = None
                    self.lmp_link_sum_transmit_packets = None
                    self.lmp_link_sum_receive_packets = None

                    self.neighbor_address = Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress()
                    self.neighbor_address.parent = self
                    self._children_name_map["neighbor_address"] = "neighbor-address"

                    self.te_link = YList(self)
                    self.ipcc = YList(self)
                    self._segment_path = lambda: "neighbor" + "[neighbor-name='" + str(self.neighbor_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/gmpls-uni/neighbors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor, ['neighbor_name', 'protocol_owner', 'ipcc_id', 'is_lmp_enabled', 'is_lmp_config_disabled', 'lmp_transmit_msg_id', 'lmp_receive_msg_id', 'lmp_link_sum_transmit_packets', 'lmp_link_sum_receive_packets'], name, value)


                class NeighborAddress(Entity):
                    """
                    The remote node ID of the neighbor
                    
                    .. attribute:: address
                    
                    	Address Union
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress.Address>`
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress, self).__init__()

                        self.yang_name = "neighbor-address"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress.Address))])
                        self._leafs = OrderedDict()

                        self.address = Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "neighbor-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress, [], name, value)


                    class Address(Entity):
                        """
                        Address Union
                        
                        .. attribute:: address_type
                        
                        	AddressType
                        	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: unnumbered_address
                        
                        	Unnumberedaddress
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "neighbor-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                            ])
                            self.address_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self.unnumbered_address = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.NeighborAddress.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                class TeLink(Entity):
                    """
                    A list of TE Links connected to this neighbor
                    
                    .. attribute:: local_link_id
                    
                    	The local datalink ID
                    	**type**\:  :py:class:`LocalLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId>`
                    
                    .. attribute:: remote_link_id
                    
                    	The remote datalink ID
                    	**type**\:  :py:class:`RemoteLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId>`
                    
                    .. attribute:: local_te_link_id
                    
                    	Local TE\-Link ID/ TNA address
                    	**type**\:  :py:class:`LocalTeLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId>`
                    
                    .. attribute:: remote_te_link_id
                    
                    	Remote TE\-Link ID/ TNA address
                    	**type**\:  :py:class:`RemoteTeLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId>`
                    
                    .. attribute:: neighbor_address
                    
                    	The address of the neighbor
                    	**type**\:  :py:class:`NeighborAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress>`
                    
                    .. attribute:: remote_ipcc_address
                    
                    	The remote node's IPCC address
                    	**type**\:  :py:class:`RemoteIpccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress>`
                    
                    .. attribute:: interface_name
                    
                    	Interface forOLM info
                    	**type**\: str
                    
                    .. attribute:: protocol_owner
                    
                    	Protocol owningthis te\-link
                    	**type**\:  :py:class:`OlmObjectOwner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmObjectOwner>`
                    
                    .. attribute:: neighbor_name
                    
                    	The name of the neighbor
                    	**type**\: str
                    
                    .. attribute:: ipcc_id
                    
                    	The IPCC ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipc_ctype
                    
                    	OLM IPCC type
                    	**type**\:  :py:class:`Olmipcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Olmipcc>`
                    
                    .. attribute:: ipcc_name
                    
                    	The name ofthe IPCC associated with the TE Link
                    	**type**\: str
                    
                    .. attribute:: local_mux_cap
                    
                    	The local mux capability
                    	**type**\:  :py:class:`OlmMuxCap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmMuxCap>`
                    
                    .. attribute:: remote_mux_cap
                    
                    	The remote mux capability
                    	**type**\:  :py:class:`OlmMuxCap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmMuxCap>`
                    
                    .. attribute:: im_state
                    
                    	data link IM state
                    	**type**\:  :py:class:`OlmCompLinkImState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmCompLinkImState>`
                    
                    .. attribute:: lmp_state
                    
                    	data link LMP state
                    	**type**\:  :py:class:`OlmCompLinkLmpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmCompLinkLmpState>`
                    
                    .. attribute:: te_link_lmp_state
                    
                    	TE LinkLMP state
                    	**type**\:  :py:class:`OlmteLinkLmpState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmteLinkLmpState>`
                    
                    .. attribute:: gmpls_te_link_local_minimum_bandwidth
                    
                    	GMPLS localminimum B/W in bytes/sec
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte/s
                    
                    .. attribute:: gmpls_te_link_local_maximum_bandwidth
                    
                    	GMPLS localmaximum B/W in bytes/sec
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte/s
                    
                    .. attribute:: gmpls_te_link_neighbor_minimum_bandwidth
                    
                    	GMPLSneighbor minimum B/W in bytes/sec
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte/s
                    
                    .. attribute:: gmpls_te_link_neighbor_maximum_bandwidth
                    
                    	GMPLSneighbor maximum B/W in bytes/sec
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte/s
                    
                    .. attribute:: gmpls_te_link_local_encoding_type
                    
                    	GMPLS locallink encoding type
                    	**type**\:  :py:class:`OlmLinkEncoding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmLinkEncoding>`
                    
                    .. attribute:: gmpls_te_link_neighbor_encoding_type
                    
                    	GMPLS neighborlink encoding type
                    	**type**\:  :py:class:`OlmLinkEncoding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmLinkEncoding>`
                    
                    .. attribute:: is_lmp_enabled
                    
                    	Is LMP enabledon this TE link
                    	**type**\: bool
                    
                    .. attribute:: lmp_transmit_msg_id
                    
                    	LMP transmitmessage ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_receive_msg_id
                    
                    	LMP receivemessage ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_comp_link_status
                    
                    	Component link LMP status indicators
                    	**type**\: list of   :py:class:`OlmCompLinkLmpStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmCompLinkLmpStatus>`
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink, self).__init__()

                        self.yang_name = "te-link"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("local-link-id", ("local_link_id", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId)), ("remote-link-id", ("remote_link_id", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId)), ("local-te-link-id", ("local_te_link_id", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId)), ("remote-te-link-id", ("remote_te_link_id", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId)), ("neighbor-address", ("neighbor_address", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress)), ("remote-ipcc-address", ("remote_ipcc_address", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('protocol_owner', (YLeaf(YType.enumeration, 'protocol-owner'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmObjectOwner', '')])),
                            ('neighbor_name', (YLeaf(YType.str, 'neighbor-name'), ['str'])),
                            ('ipcc_id', (YLeaf(YType.uint32, 'ipcc-id'), ['int'])),
                            ('ipc_ctype', (YLeaf(YType.enumeration, 'ipc-ctype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'Olmipcc', '')])),
                            ('ipcc_name', (YLeaf(YType.str, 'ipcc-name'), ['str'])),
                            ('local_mux_cap', (YLeaf(YType.enumeration, 'local-mux-cap'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmMuxCap', '')])),
                            ('remote_mux_cap', (YLeaf(YType.enumeration, 'remote-mux-cap'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmMuxCap', '')])),
                            ('im_state', (YLeaf(YType.enumeration, 'im-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmCompLinkImState', '')])),
                            ('lmp_state', (YLeaf(YType.enumeration, 'lmp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmCompLinkLmpState', '')])),
                            ('te_link_lmp_state', (YLeaf(YType.enumeration, 'te-link-lmp-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmteLinkLmpState', '')])),
                            ('gmpls_te_link_local_minimum_bandwidth', (YLeaf(YType.uint64, 'gmpls-te-link-local-minimum-bandwidth'), ['int'])),
                            ('gmpls_te_link_local_maximum_bandwidth', (YLeaf(YType.uint64, 'gmpls-te-link-local-maximum-bandwidth'), ['int'])),
                            ('gmpls_te_link_neighbor_minimum_bandwidth', (YLeaf(YType.uint64, 'gmpls-te-link-neighbor-minimum-bandwidth'), ['int'])),
                            ('gmpls_te_link_neighbor_maximum_bandwidth', (YLeaf(YType.uint64, 'gmpls-te-link-neighbor-maximum-bandwidth'), ['int'])),
                            ('gmpls_te_link_local_encoding_type', (YLeaf(YType.enumeration, 'gmpls-te-link-local-encoding-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmLinkEncoding', '')])),
                            ('gmpls_te_link_neighbor_encoding_type', (YLeaf(YType.enumeration, 'gmpls-te-link-neighbor-encoding-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmLinkEncoding', '')])),
                            ('is_lmp_enabled', (YLeaf(YType.boolean, 'is-lmp-enabled'), ['bool'])),
                            ('lmp_transmit_msg_id', (YLeaf(YType.uint32, 'lmp-transmit-msg-id'), ['int'])),
                            ('lmp_receive_msg_id', (YLeaf(YType.uint32, 'lmp-receive-msg-id'), ['int'])),
                            ('lmp_comp_link_status', (YLeafList(YType.enumeration, 'lmp-comp-link-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmCompLinkLmpStatus', '')])),
                        ])
                        self.interface_name = None
                        self.protocol_owner = None
                        self.neighbor_name = None
                        self.ipcc_id = None
                        self.ipc_ctype = None
                        self.ipcc_name = None
                        self.local_mux_cap = None
                        self.remote_mux_cap = None
                        self.im_state = None
                        self.lmp_state = None
                        self.te_link_lmp_state = None
                        self.gmpls_te_link_local_minimum_bandwidth = None
                        self.gmpls_te_link_local_maximum_bandwidth = None
                        self.gmpls_te_link_neighbor_minimum_bandwidth = None
                        self.gmpls_te_link_neighbor_maximum_bandwidth = None
                        self.gmpls_te_link_local_encoding_type = None
                        self.gmpls_te_link_neighbor_encoding_type = None
                        self.is_lmp_enabled = None
                        self.lmp_transmit_msg_id = None
                        self.lmp_receive_msg_id = None
                        self.lmp_comp_link_status = []

                        self.local_link_id = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId()
                        self.local_link_id.parent = self
                        self._children_name_map["local_link_id"] = "local-link-id"

                        self.remote_link_id = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId()
                        self.remote_link_id.parent = self
                        self._children_name_map["remote_link_id"] = "remote-link-id"

                        self.local_te_link_id = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId()
                        self.local_te_link_id.parent = self
                        self._children_name_map["local_te_link_id"] = "local-te-link-id"

                        self.remote_te_link_id = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId()
                        self.remote_te_link_id.parent = self
                        self._children_name_map["remote_te_link_id"] = "remote-te-link-id"

                        self.neighbor_address = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress()
                        self.neighbor_address.parent = self
                        self._children_name_map["neighbor_address"] = "neighbor-address"

                        self.remote_ipcc_address = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress()
                        self.remote_ipcc_address.parent = self
                        self._children_name_map["remote_ipcc_address"] = "remote-ipcc-address"
                        self._segment_path = lambda: "te-link"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink, ['interface_name', 'protocol_owner', 'neighbor_name', 'ipcc_id', 'ipc_ctype', 'ipcc_name', 'local_mux_cap', 'remote_mux_cap', 'im_state', 'lmp_state', 'te_link_lmp_state', 'gmpls_te_link_local_minimum_bandwidth', 'gmpls_te_link_local_maximum_bandwidth', 'gmpls_te_link_neighbor_minimum_bandwidth', 'gmpls_te_link_neighbor_maximum_bandwidth', 'gmpls_te_link_local_encoding_type', 'gmpls_te_link_neighbor_encoding_type', 'is_lmp_enabled', 'lmp_transmit_msg_id', 'lmp_receive_msg_id', 'lmp_comp_link_status'], name, value)


                    class LocalLinkId(Entity):
                        """
                        The local datalink ID
                        
                        .. attribute:: address
                        
                        	Address Union
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId.Address>`
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId, self).__init__()

                            self.yang_name = "local-link-id"
                            self.yang_parent_name = "te-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId.Address))])
                            self._leafs = OrderedDict()

                            self.address = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "local-link-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId, [], name, value)


                        class Address(Entity):
                            """
                            Address Union
                            
                            .. attribute:: address_type
                            
                            	AddressType
                            	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: unnumbered_address
                            
                            	Unnumberedaddress
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lmp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "local-link-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                                ])
                                self.address_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.unnumbered_address = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalLinkId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                    class RemoteLinkId(Entity):
                        """
                        The remote datalink ID
                        
                        .. attribute:: address
                        
                        	Address Union
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId.Address>`
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId, self).__init__()

                            self.yang_name = "remote-link-id"
                            self.yang_parent_name = "te-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId.Address))])
                            self._leafs = OrderedDict()

                            self.address = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "remote-link-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId, [], name, value)


                        class Address(Entity):
                            """
                            Address Union
                            
                            .. attribute:: address_type
                            
                            	AddressType
                            	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: unnumbered_address
                            
                            	Unnumberedaddress
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lmp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "remote-link-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                                ])
                                self.address_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.unnumbered_address = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteLinkId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                    class LocalTeLinkId(Entity):
                        """
                        Local TE\-Link ID/ TNA address
                        
                        .. attribute:: address
                        
                        	Address Union
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId.Address>`
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId, self).__init__()

                            self.yang_name = "local-te-link-id"
                            self.yang_parent_name = "te-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId.Address))])
                            self._leafs = OrderedDict()

                            self.address = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "local-te-link-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId, [], name, value)


                        class Address(Entity):
                            """
                            Address Union
                            
                            .. attribute:: address_type
                            
                            	AddressType
                            	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: unnumbered_address
                            
                            	Unnumberedaddress
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lmp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "local-te-link-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                                ])
                                self.address_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.unnumbered_address = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.LocalTeLinkId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                    class RemoteTeLinkId(Entity):
                        """
                        Remote TE\-Link ID/ TNA address
                        
                        .. attribute:: address
                        
                        	Address Union
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId.Address>`
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId, self).__init__()

                            self.yang_name = "remote-te-link-id"
                            self.yang_parent_name = "te-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId.Address))])
                            self._leafs = OrderedDict()

                            self.address = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "remote-te-link-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId, [], name, value)


                        class Address(Entity):
                            """
                            Address Union
                            
                            .. attribute:: address_type
                            
                            	AddressType
                            	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: unnumbered_address
                            
                            	Unnumberedaddress
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lmp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "remote-te-link-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                                ])
                                self.address_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.unnumbered_address = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteTeLinkId.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                    class NeighborAddress(Entity):
                        """
                        The address of the neighbor
                        
                        .. attribute:: address
                        
                        	Address Union
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress.Address>`
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress, self).__init__()

                            self.yang_name = "neighbor-address"
                            self.yang_parent_name = "te-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress.Address))])
                            self._leafs = OrderedDict()

                            self.address = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "neighbor-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress, [], name, value)


                        class Address(Entity):
                            """
                            Address Union
                            
                            .. attribute:: address_type
                            
                            	AddressType
                            	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: unnumbered_address
                            
                            	Unnumberedaddress
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lmp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "neighbor-address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                                ])
                                self.address_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.unnumbered_address = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.NeighborAddress.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                    class RemoteIpccAddress(Entity):
                        """
                        The remote node's IPCC address
                        
                        .. attribute:: address
                        
                        	Address Union
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress.Address>`
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress, self).__init__()

                            self.yang_name = "remote-ipcc-address"
                            self.yang_parent_name = "te-link"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress.Address))])
                            self._leafs = OrderedDict()

                            self.address = Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "remote-ipcc-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress, [], name, value)


                        class Address(Entity):
                            """
                            Address Union
                            
                            .. attribute:: address_type
                            
                            	AddressType
                            	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: unnumbered_address
                            
                            	Unnumberedaddress
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lmp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "remote-ipcc-address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                                ])
                                self.address_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.unnumbered_address = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.TeLink.RemoteIpccAddress.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                class Ipcc(Entity):
                    """
                    A list of IPCCs connected to this neighbor
                    
                    .. attribute:: remote_ipcc_address
                    
                    	The remote node'sIPCC address
                    	**type**\:  :py:class:`RemoteIpccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress>`
                    
                    .. attribute:: source_ip_cc_address
                    
                    	The local IPCC address
                    	**type**\:  :py:class:`SourceIpCcAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress>`
                    
                    .. attribute:: ipcc_id
                    
                    	Global active IPCCfor this neighbor
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipc_ctype
                    
                    	OLM IPCC type
                    	**type**\:  :py:class:`Olmipcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Olmipcc>`
                    
                    .. attribute:: interface_name
                    
                    	The interface name forI/F IPCCs
                    	**type**\: str
                    
                    .. attribute:: neighbor_name
                    
                    	Neighbor name of theIPCCs neighbor
                    	**type**\: str
                    
                    .. attribute:: ipcc_state
                    
                    	OLM IPCC master state
                    	**type**\:  :py:class:`OlmipccState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmipccState>`
                    
                    .. attribute:: lmp_hello_interval
                    
                    	LMP hello send interval in msec [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_interval_minimum
                    
                    	LMP minimum acceptable hello send interval [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_interval_maximum
                    
                    	LMP maximum acceptable hello send interval [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_dead_interval
                    
                    	LMP hello dead interval [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_dead_interval_minimum
                    
                    	LMP minimum acceptable hello dead interval [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_dead_interval_maximum
                    
                    	LMP maximum acceptable hello dead interval [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_transmit_packets
                    
                    	LMP hello transmit packet count[DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_receive_packets
                    
                    	LMP hello receive packet count [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_transmit_packet_sequence_number
                    
                    	LMP hello transmit packet sequence number [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_hello_receive_packet_sequence_number
                    
                    	LMP hello receive packet sequence number[DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_transmit_msg_id
                    
                    	LMP transmit message ID[DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_receive_msg_id
                    
                    	LMP receive message ID[DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_link_sum_transmit_packets
                    
                    	LMP link summary transmit packet count [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lmp_link_sum_receive_packets
                    
                    	LMP link summary receive packet count [DEPRECATED]
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'lmp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc, self).__init__()

                        self.yang_name = "ipcc"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("remote-ipcc-address", ("remote_ipcc_address", Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress)), ("source-ip-cc-address", ("source_ip_cc_address", Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress))])
                        self._leafs = OrderedDict([
                            ('ipcc_id', (YLeaf(YType.uint32, 'ipcc-id'), ['int'])),
                            ('ipc_ctype', (YLeaf(YType.enumeration, 'ipc-ctype'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'Olmipcc', '')])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('neighbor_name', (YLeaf(YType.str, 'neighbor-name'), ['str'])),
                            ('ipcc_state', (YLeaf(YType.enumeration, 'ipcc-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmipccState', '')])),
                            ('lmp_hello_interval', (YLeaf(YType.uint32, 'lmp-hello-interval'), ['int'])),
                            ('lmp_hello_interval_minimum', (YLeaf(YType.uint32, 'lmp-hello-interval-minimum'), ['int'])),
                            ('lmp_hello_interval_maximum', (YLeaf(YType.uint32, 'lmp-hello-interval-maximum'), ['int'])),
                            ('lmp_hello_dead_interval', (YLeaf(YType.uint32, 'lmp-hello-dead-interval'), ['int'])),
                            ('lmp_hello_dead_interval_minimum', (YLeaf(YType.uint32, 'lmp-hello-dead-interval-minimum'), ['int'])),
                            ('lmp_hello_dead_interval_maximum', (YLeaf(YType.uint32, 'lmp-hello-dead-interval-maximum'), ['int'])),
                            ('lmp_hello_transmit_packets', (YLeaf(YType.uint32, 'lmp-hello-transmit-packets'), ['int'])),
                            ('lmp_hello_receive_packets', (YLeaf(YType.uint32, 'lmp-hello-receive-packets'), ['int'])),
                            ('lmp_hello_transmit_packet_sequence_number', (YLeaf(YType.uint32, 'lmp-hello-transmit-packet-sequence-number'), ['int'])),
                            ('lmp_hello_receive_packet_sequence_number', (YLeaf(YType.uint32, 'lmp-hello-receive-packet-sequence-number'), ['int'])),
                            ('lmp_transmit_msg_id', (YLeaf(YType.uint32, 'lmp-transmit-msg-id'), ['int'])),
                            ('lmp_receive_msg_id', (YLeaf(YType.uint32, 'lmp-receive-msg-id'), ['int'])),
                            ('lmp_link_sum_transmit_packets', (YLeaf(YType.uint32, 'lmp-link-sum-transmit-packets'), ['int'])),
                            ('lmp_link_sum_receive_packets', (YLeaf(YType.uint32, 'lmp-link-sum-receive-packets'), ['int'])),
                        ])
                        self.ipcc_id = None
                        self.ipc_ctype = None
                        self.interface_name = None
                        self.neighbor_name = None
                        self.ipcc_state = None
                        self.lmp_hello_interval = None
                        self.lmp_hello_interval_minimum = None
                        self.lmp_hello_interval_maximum = None
                        self.lmp_hello_dead_interval = None
                        self.lmp_hello_dead_interval_minimum = None
                        self.lmp_hello_dead_interval_maximum = None
                        self.lmp_hello_transmit_packets = None
                        self.lmp_hello_receive_packets = None
                        self.lmp_hello_transmit_packet_sequence_number = None
                        self.lmp_hello_receive_packet_sequence_number = None
                        self.lmp_transmit_msg_id = None
                        self.lmp_receive_msg_id = None
                        self.lmp_link_sum_transmit_packets = None
                        self.lmp_link_sum_receive_packets = None

                        self.remote_ipcc_address = Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress()
                        self.remote_ipcc_address.parent = self
                        self._children_name_map["remote_ipcc_address"] = "remote-ipcc-address"

                        self.source_ip_cc_address = Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress()
                        self.source_ip_cc_address.parent = self
                        self._children_name_map["source_ip_cc_address"] = "source-ip-cc-address"
                        self._segment_path = lambda: "ipcc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc, ['ipcc_id', 'ipc_ctype', 'interface_name', 'neighbor_name', 'ipcc_state', 'lmp_hello_interval', 'lmp_hello_interval_minimum', 'lmp_hello_interval_maximum', 'lmp_hello_dead_interval', 'lmp_hello_dead_interval_minimum', 'lmp_hello_dead_interval_maximum', 'lmp_hello_transmit_packets', 'lmp_hello_receive_packets', 'lmp_hello_transmit_packet_sequence_number', 'lmp_hello_receive_packet_sequence_number', 'lmp_transmit_msg_id', 'lmp_receive_msg_id', 'lmp_link_sum_transmit_packets', 'lmp_link_sum_receive_packets'], name, value)


                    class RemoteIpccAddress(Entity):
                        """
                        The remote node'sIPCC address
                        
                        .. attribute:: address
                        
                        	Address Union
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress.Address>`
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress, self).__init__()

                            self.yang_name = "remote-ipcc-address"
                            self.yang_parent_name = "ipcc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress.Address))])
                            self._leafs = OrderedDict()

                            self.address = Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "remote-ipcc-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress, [], name, value)


                        class Address(Entity):
                            """
                            Address Union
                            
                            .. attribute:: address_type
                            
                            	AddressType
                            	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: unnumbered_address
                            
                            	Unnumberedaddress
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lmp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "remote-ipcc-address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                                ])
                                self.address_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.unnumbered_address = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.RemoteIpccAddress.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


                    class SourceIpCcAddress(Entity):
                        """
                        The local IPCC address
                        
                        .. attribute:: address
                        
                        	Address Union
                        	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress.Address>`
                        
                        

                        """

                        _prefix = 'lmp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress, self).__init__()

                            self.yang_name = "source-ip-cc-address"
                            self.yang_parent_name = "ipcc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("address", ("address", Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress.Address))])
                            self._leafs = OrderedDict()

                            self.address = Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress.Address()
                            self.address.parent = self
                            self._children_name_map["address"] = "address"
                            self._segment_path = lambda: "source-ip-cc-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress, [], name, value)


                        class Address(Entity):
                            """
                            Address Union
                            
                            .. attribute:: address_type
                            
                            	AddressType
                            	**type**\:  :py:class:`OlmAddrTypeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.OlmAddrTypeId>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: unnumbered_address
                            
                            	Unnumberedaddress
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'lmp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "source-ip-cc-address"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address_type', (YLeaf(YType.enumeration, 'address-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper', 'OlmAddrTypeId', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('unnumbered_address', (YLeaf(YType.uint32, 'unnumbered-address'), ['int'])),
                                ])
                                self.address_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.unnumbered_address = None
                                self._segment_path = lambda: "address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Lmp.GmplsUni.Neighbors.Neighbor.Ipcc.SourceIpCcAddress.Address, ['address_type', 'ipv4_address', 'ipv6_address', 'unnumbered_address'], name, value)


    class ComponentLinkIds(Entity):
        """
        UCP OLM component link ID container class
        
        .. attribute:: component_link_id
        
        	Retrieve the LMP component link ID for a given controller
        	**type**\: list of  		 :py:class:`ComponentLinkId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lmp_oper.Lmp.ComponentLinkIds.ComponentLinkId>`
        
        

        """

        _prefix = 'lmp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Lmp.ComponentLinkIds, self).__init__()

            self.yang_name = "component-link-ids"
            self.yang_parent_name = "lmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("component-link-id", ("component_link_id", Lmp.ComponentLinkIds.ComponentLinkId))])
            self._leafs = OrderedDict()

            self.component_link_id = YList(self)
            self._segment_path = lambda: "component-link-ids"
            self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Lmp.ComponentLinkIds, [], name, value)


        class ComponentLinkId(Entity):
            """
            Retrieve the LMP component link ID for a given
            controller
            
            .. attribute:: controller_name  (key)
            
            	Controller name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: component_interface_id
            
            	LMP component link ID for an I/F
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'lmp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Lmp.ComponentLinkIds.ComponentLinkId, self).__init__()

                self.yang_name = "component-link-id"
                self.yang_parent_name = "component-link-ids"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['controller_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('controller_name', (YLeaf(YType.str, 'controller-name'), ['str'])),
                    ('component_interface_id', (YLeaf(YType.uint32, 'component-interface-id'), ['int'])),
                ])
                self.controller_name = None
                self.component_interface_id = None
                self._segment_path = lambda: "component-link-id" + "[controller-name='" + str(self.controller_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lmp-oper:lmp/component-link-ids/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Lmp.ComponentLinkIds.ComponentLinkId, ['controller_name', 'component_interface_id'], name, value)

    def clone_ptr(self):
        self._top_entity = Lmp()
        return self._top_entity

