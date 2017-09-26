""" Cisco_IOS_XR_infra_xtc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc package operational data.

This module contains definitions
for the following management objects\:
  pce\-lsp\-data\: PCE LSP's data
  pce\-peer\: pce peer
  pce\-topology\: pce topology
  pce\: pce

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LspSetup(Enum):
    """
    LspSetup

    LSP setup type

    .. data:: setup_rsvp = 0

    	LSP is established using RSVP-TE

    .. data:: setup_sr = 1

    	LSP is established using SR-TE

    .. data:: setup_unknown = 2

    	Unknown LSP establishment method

    """

    setup_rsvp = Enum.YLeaf(0, "setup-rsvp")

    setup_sr = Enum.YLeaf(1, "setup-sr")

    setup_unknown = Enum.YLeaf(2, "setup-unknown")


class LspState(Enum):
    """
    LspState

    LSP setup type

    .. data:: lsp_down = 0

    	LSP is down

    .. data:: lsp_up = 1

    	LSP is up

    """

    lsp_down = Enum.YLeaf(0, "lsp-down")

    lsp_up = Enum.YLeaf(1, "lsp-up")


class PceAfId(Enum):
    """
    PceAfId

    Pce af id

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    none = Enum.YLeaf(0, "none")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class PceAsso(Enum):
    """
    PceAsso

    Pce asso

    .. data:: unknown = 0

    	Unknown type

    .. data:: link = 1

    	LINK

    .. data:: node = 2

    	NODE

    .. data:: srlg = 3

    	SRLG

    """

    unknown = Enum.YLeaf(0, "unknown")

    link = Enum.YLeaf(1, "link")

    node = Enum.YLeaf(2, "node")

    srlg = Enum.YLeaf(3, "srlg")


class PceCspfRc(Enum):
    """
    PceCspfRc

    PCE CSPF Result Code

    .. data:: pce_cspf_not_set = 0

    	Not set

    .. data:: pce_cspf_src_not_found = 1

    	Source not found

    .. data:: pce_cspf_dst_not_found = 2

    	Destination not found

    .. data:: pce_cspf_second_src_not_found = 3

    	Second source not found

    .. data:: pce_cspf_second_dst_not_found = 4

    	Second destination not found

    .. data:: pce_cspf_no_mem = 5

    	No memory

    .. data:: pce_cspf_ex_path_not_resolved = 6

    	Second path not resolved

    .. data:: pce_cspf_no_path = 7

    	No path

    .. data:: pce_cspf_sp_success = 8

    	Shortest path success

    .. data:: pce_cspf_error = 9

    	Error

    .. data:: pce_cspf_fallback_srlg_node_node = 10

    	Fallback from SRLG-NODE to NODE

    .. data:: pce_cspf_fallback_srlg_node_link = 11

    	Fallback from SRLG-NODE to LINK

    .. data:: pce_cspf_fallback_srlg_node_sp = 12

    	Fallback from SRLG-NODE to SP

    .. data:: pce_cspf_fallback_node_link = 13

    	Fallback from NODE to LINK

    .. data:: pce_cspf_fallback_link_sp = 14

    	Fallback from LINK to SP

    .. data:: pce_cspf_fallback_node_sp = 15

    	Fallback from NODE to SP

    .. data:: pce_cspf_fallback_srlg_link = 16

    	Fallback from SRLG to LINK

    .. data:: pce_cspf_fallback_srlg_sp = 17

    	Fallback from SRLG to SP

    .. data:: pce_cspf_dp_success = 18

    	Disjoint path success

    """

    pce_cspf_not_set = Enum.YLeaf(0, "pce-cspf-not-set")

    pce_cspf_src_not_found = Enum.YLeaf(1, "pce-cspf-src-not-found")

    pce_cspf_dst_not_found = Enum.YLeaf(2, "pce-cspf-dst-not-found")

    pce_cspf_second_src_not_found = Enum.YLeaf(3, "pce-cspf-second-src-not-found")

    pce_cspf_second_dst_not_found = Enum.YLeaf(4, "pce-cspf-second-dst-not-found")

    pce_cspf_no_mem = Enum.YLeaf(5, "pce-cspf-no-mem")

    pce_cspf_ex_path_not_resolved = Enum.YLeaf(6, "pce-cspf-ex-path-not-resolved")

    pce_cspf_no_path = Enum.YLeaf(7, "pce-cspf-no-path")

    pce_cspf_sp_success = Enum.YLeaf(8, "pce-cspf-sp-success")

    pce_cspf_error = Enum.YLeaf(9, "pce-cspf-error")

    pce_cspf_fallback_srlg_node_node = Enum.YLeaf(10, "pce-cspf-fallback-srlg-node-node")

    pce_cspf_fallback_srlg_node_link = Enum.YLeaf(11, "pce-cspf-fallback-srlg-node-link")

    pce_cspf_fallback_srlg_node_sp = Enum.YLeaf(12, "pce-cspf-fallback-srlg-node-sp")

    pce_cspf_fallback_node_link = Enum.YLeaf(13, "pce-cspf-fallback-node-link")

    pce_cspf_fallback_link_sp = Enum.YLeaf(14, "pce-cspf-fallback-link-sp")

    pce_cspf_fallback_node_sp = Enum.YLeaf(15, "pce-cspf-fallback-node-sp")

    pce_cspf_fallback_srlg_link = Enum.YLeaf(16, "pce-cspf-fallback-srlg-link")

    pce_cspf_fallback_srlg_sp = Enum.YLeaf(17, "pce-cspf-fallback-srlg-sp")

    pce_cspf_dp_success = Enum.YLeaf(18, "pce-cspf-dp-success")


class PceHeadendSwap(Enum):
    """
    PceHeadendSwap

    PCE Headends Swap Code

    .. data:: pcehs_none = 0

    	Headends not swapped

    .. data:: pcehs_plain = 1

    	Headends swapped

    .. data:: pcehs_rwi = 2

    	Headends swapped with increment

    """

    pcehs_none = Enum.YLeaf(0, "pcehs-none")

    pcehs_plain = Enum.YLeaf(1, "pcehs-plain")

    pcehs_rwi = Enum.YLeaf(2, "pcehs-rwi")


class PceIgpInfoId(Enum):
    """
    PceIgpInfoId

    IGP IDs

    .. data:: isis = 1

    	ISIS

    .. data:: ospf = 2

    	OSPF

    .. data:: bgp = 3

    	BGP

    """

    isis = Enum.YLeaf(1, "isis")

    ospf = Enum.YLeaf(2, "ospf")

    bgp = Enum.YLeaf(3, "bgp")


class PceProto(Enum):
    """
    PceProto

    PCE peer protocol

    .. data:: pcep = 0

    	PCE protocol

    .. data:: netconf = 1

    	Netconf protocol

    """

    pcep = Enum.YLeaf(0, "pcep")

    netconf = Enum.YLeaf(1, "netconf")


class PceRro(Enum):
    """
    PceRro

    PCE RRO type

    .. data:: rro_type_ipv4_address = 0

    	IPv4 Address

    .. data:: rro_type_mpls_label = 1

    	MPLS Label

    .. data:: rro_type_sripv4_node_sid = 2

    	Segment Routing IPv4 Node SID

    .. data:: rro_type_sripv4_adjacency_sid = 3

    	Segment Routing IPv4 Adjacency SID

    .. data:: rro_type_sr_nai_null = 4

    	Segment Routing with NAI null

    """

    rro_type_ipv4_address = Enum.YLeaf(0, "rro-type-ipv4-address")

    rro_type_mpls_label = Enum.YLeaf(1, "rro-type-mpls-label")

    rro_type_sripv4_node_sid = Enum.YLeaf(2, "rro-type-sripv4-node-sid")

    rro_type_sripv4_adjacency_sid = Enum.YLeaf(3, "rro-type-sripv4-adjacency-sid")

    rro_type_sr_nai_null = Enum.YLeaf(4, "rro-type-sr-nai-null")


class PceSrSid(Enum):
    """
    PceSrSid

    PCE SR SID type

    .. data:: ipv4_node_sid = 0

    	IPv4 Node SID

    .. data:: ipv4_adjacency_sid = 1

    	IPv4 Adjacency SID

    .. data:: unknown_sid = 2

    	Unknown SID

    """

    ipv4_node_sid = Enum.YLeaf(0, "ipv4-node-sid")

    ipv4_adjacency_sid = Enum.YLeaf(1, "ipv4-adjacency-sid")

    unknown_sid = Enum.YLeaf(2, "unknown-sid")


class PcepLspState(Enum):
    """
    PcepLspState

    PCEP operation protocol

    .. data:: lsp_down = 0

    	LSP is down

    .. data:: lsp_up = 1

    	LSP is up

    .. data:: lsp_active = 2

    	LSP is active (carrying traffic)

    .. data:: lsp_going_down = 3

    	LSP is going down

    .. data:: lsp_being_signaled = 4

    	LSP is being signaled

    """

    lsp_down = Enum.YLeaf(0, "lsp-down")

    lsp_up = Enum.YLeaf(1, "lsp-up")

    lsp_active = Enum.YLeaf(2, "lsp-active")

    lsp_going_down = Enum.YLeaf(3, "lsp-going-down")

    lsp_being_signaled = Enum.YLeaf(4, "lsp-being-signaled")


class PcepState(Enum):
    """
    PcepState

    PCEP State

    .. data:: tcp_close = 0

    	TCP close

    .. data:: tcp_listen = 1

    	TCP listen

    .. data:: tcp_connect = 2

    	TCP connect

    .. data:: pcep_closed = 3

    	PCEP closed

    .. data:: pcep_opening = 4

    	PCEP opening

    .. data:: pcep_open = 5

    	PCEP open

    """

    tcp_close = Enum.YLeaf(0, "tcp-close")

    tcp_listen = Enum.YLeaf(1, "tcp-listen")

    tcp_connect = Enum.YLeaf(2, "tcp-connect")

    pcep_closed = Enum.YLeaf(3, "pcep-closed")

    pcep_opening = Enum.YLeaf(4, "pcep-opening")

    pcep_open = Enum.YLeaf(5, "pcep-open")


class Sid(Enum):
    """
    Sid

    SID Types

    .. data:: sr_protected_adj_sid = 1

    	Protected Adjacency SID

    .. data:: sr_unprotected_adj_sid = 2

    	Unprotected Adjacency SID

    .. data:: sr_bgp_egress_peer_engineering_sid = 3

    	BGP egress peer engineering SID

    .. data:: sr_reqular_prefix_sid = 4

    	Regular prefix SID

    .. data:: sr_strict_prefix_sid = 5

    	Strict prefix SID

    """

    sr_protected_adj_sid = Enum.YLeaf(1, "sr-protected-adj-sid")

    sr_unprotected_adj_sid = Enum.YLeaf(2, "sr-unprotected-adj-sid")

    sr_bgp_egress_peer_engineering_sid = Enum.YLeaf(3, "sr-bgp-egress-peer-engineering-sid")

    sr_reqular_prefix_sid = Enum.YLeaf(4, "sr-reqular-prefix-sid")

    sr_strict_prefix_sid = Enum.YLeaf(5, "sr-strict-prefix-sid")



class Pce(Entity):
    """
    pce
    
    .. attribute:: association_infos
    
    	Associaition database in XTC
    	**type**\:   :py:class:`AssociationInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos>`
    
    .. attribute:: cspf
    
    	CSPF path info
    	**type**\:   :py:class:`Cspf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf>`
    
    .. attribute:: lsp_summary
    
    	LSP summary database in XTC
    	**type**\:   :py:class:`LspSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary>`
    
    .. attribute:: peer_detail_infos
    
    	Detailed peers database in XTC
    	**type**\:   :py:class:`PeerDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos>`
    
    .. attribute:: peer_infos
    
    	Peers database in XTC
    	**type**\:   :py:class:`PeerInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos>`
    
    .. attribute:: prefix_infos
    
    	Prefixes database in XTC
    	**type**\:   :py:class:`PrefixInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos>`
    
    .. attribute:: topology_nodes
    
    	Node database in XTC
    	**type**\:   :py:class:`TopologyNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes>`
    
    .. attribute:: topology_summary
    
    	Node summary database in XTC
    	**type**\:   :py:class:`TopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologySummary>`
    
    .. attribute:: tunnel_detail_infos
    
    	Detailed tunnel database in XTC
    	**type**\:   :py:class:`TunnelDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos>`
    
    .. attribute:: tunnel_infos
    
    	Tunnel database in XTC
    	**type**\:   :py:class:`TunnelInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2017-06-26'

    def __init__(self):
        super(Pce, self).__init__()
        self._top_entity = None

        self.yang_name = "pce"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"association-infos" : ("association_infos", Pce.AssociationInfos), "cspf" : ("cspf", Pce.Cspf), "lsp-summary" : ("lsp_summary", Pce.LspSummary), "peer-detail-infos" : ("peer_detail_infos", Pce.PeerDetailInfos), "peer-infos" : ("peer_infos", Pce.PeerInfos), "prefix-infos" : ("prefix_infos", Pce.PrefixInfos), "topology-nodes" : ("topology_nodes", Pce.TopologyNodes), "topology-summary" : ("topology_summary", Pce.TopologySummary), "tunnel-detail-infos" : ("tunnel_detail_infos", Pce.TunnelDetailInfos), "tunnel-infos" : ("tunnel_infos", Pce.TunnelInfos)}
        self._child_list_classes = {}

        self.association_infos = Pce.AssociationInfos()
        self.association_infos.parent = self
        self._children_name_map["association_infos"] = "association-infos"
        self._children_yang_names.add("association-infos")

        self.cspf = Pce.Cspf()
        self.cspf.parent = self
        self._children_name_map["cspf"] = "cspf"
        self._children_yang_names.add("cspf")

        self.lsp_summary = Pce.LspSummary()
        self.lsp_summary.parent = self
        self._children_name_map["lsp_summary"] = "lsp-summary"
        self._children_yang_names.add("lsp-summary")

        self.peer_detail_infos = Pce.PeerDetailInfos()
        self.peer_detail_infos.parent = self
        self._children_name_map["peer_detail_infos"] = "peer-detail-infos"
        self._children_yang_names.add("peer-detail-infos")

        self.peer_infos = Pce.PeerInfos()
        self.peer_infos.parent = self
        self._children_name_map["peer_infos"] = "peer-infos"
        self._children_yang_names.add("peer-infos")

        self.prefix_infos = Pce.PrefixInfos()
        self.prefix_infos.parent = self
        self._children_name_map["prefix_infos"] = "prefix-infos"
        self._children_yang_names.add("prefix-infos")

        self.topology_nodes = Pce.TopologyNodes()
        self.topology_nodes.parent = self
        self._children_name_map["topology_nodes"] = "topology-nodes"
        self._children_yang_names.add("topology-nodes")

        self.topology_summary = Pce.TopologySummary()
        self.topology_summary.parent = self
        self._children_name_map["topology_summary"] = "topology-summary"
        self._children_yang_names.add("topology-summary")

        self.tunnel_detail_infos = Pce.TunnelDetailInfos()
        self.tunnel_detail_infos.parent = self
        self._children_name_map["tunnel_detail_infos"] = "tunnel-detail-infos"
        self._children_yang_names.add("tunnel-detail-infos")

        self.tunnel_infos = Pce.TunnelInfos()
        self.tunnel_infos.parent = self
        self._children_name_map["tunnel_infos"] = "tunnel-infos"
        self._children_yang_names.add("tunnel-infos")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce"


    class AssociationInfos(Entity):
        """
        Associaition database in XTC
        
        .. attribute:: association_info
        
        	PCE Association information
        	**type**\: list of    :py:class:`AssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos.AssociationInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.AssociationInfos, self).__init__()

            self.yang_name = "association-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"association-info" : ("association_info", Pce.AssociationInfos.AssociationInfo)}

            self.association_info = YList(self)
            self._segment_path = lambda: "association-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.AssociationInfos, [], name, value)


        class AssociationInfo(Entity):
            """
            PCE Association information
            
            .. attribute:: group_id  <key>
            
            	Group ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: association_id
            
            	Association ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: association_lsp
            
            	Association LSP Info
            	**type**\: list of    :py:class:`AssociationLsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos.AssociationInfo.AssociationLsp>`
            
            .. attribute:: association_source
            
            	Association Source
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: association_type
            
            	Association Type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: headends_swapped
            
            	Headends Swapped
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: status
            
            	Association Status
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: strict
            
            	Association Strict Mode
            	**type**\:  bool
            
            .. attribute:: sub_id
            
            	Sub ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: type
            
            	Type
            	**type**\:   :py:class:`PceAsso <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAsso>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.AssociationInfos.AssociationInfo, self).__init__()

                self.yang_name = "association-info"
                self.yang_parent_name = "association-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"association-lsp" : ("association_lsp", Pce.AssociationInfos.AssociationInfo.AssociationLsp)}

                self.group_id = YLeaf(YType.int32, "group-id")

                self.association_id = YLeaf(YType.uint32, "association-id")

                self.association_source = YLeaf(YType.str, "association-source")

                self.association_type = YLeaf(YType.uint32, "association-type")

                self.headends_swapped = YLeaf(YType.uint32, "headends-swapped")

                self.status = YLeaf(YType.uint32, "status")

                self.strict = YLeaf(YType.boolean, "strict")

                self.sub_id = YLeaf(YType.int32, "sub-id")

                self.type = YLeaf(YType.enumeration, "type")

                self.association_lsp = YList(self)
                self._segment_path = lambda: "association-info" + "[group-id='" + self.group_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/association-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.AssociationInfos.AssociationInfo, ['group_id', 'association_id', 'association_source', 'association_type', 'headends_swapped', 'status', 'strict', 'sub_id', 'type'], name, value)


            class AssociationLsp(Entity):
                """
                Association LSP Info
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pcc_address
                
                	PCC address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: pce_based
                
                	PCE Based
                	**type**\:  bool
                
                .. attribute:: plsp_id
                
                	PLSP ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: tunnel_name
                
                	Tunnel Name
                	**type**\:  str
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.AssociationInfos.AssociationInfo.AssociationLsp, self).__init__()

                    self.yang_name = "association-lsp"
                    self.yang_parent_name = "association-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.lspid = YLeaf(YType.uint32, "lspid")

                    self.pcc_address = YLeaf(YType.str, "pcc-address")

                    self.pce_based = YLeaf(YType.boolean, "pce-based")

                    self.plsp_id = YLeaf(YType.uint32, "plsp-id")

                    self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")

                    self.tunnel_name = YLeaf(YType.str, "tunnel-name")
                    self._segment_path = lambda: "association-lsp"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.AssociationInfos.AssociationInfo.AssociationLsp, ['lspid', 'pcc_address', 'pce_based', 'plsp_id', 'tunnel_id', 'tunnel_name'], name, value)


    class Cspf(Entity):
        """
        CSPF path info
        
        .. attribute:: cspf_paths
        
        	This table models the path calculation capabilities in XTC.A GET operation for the complete table will return no entries
        	**type**\:   :py:class:`CspfPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.Cspf, self).__init__()

            self.yang_name = "cspf"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"cspf-paths" : ("cspf_paths", Pce.Cspf.CspfPaths)}
            self._child_list_classes = {}

            self.cspf_paths = Pce.Cspf.CspfPaths()
            self.cspf_paths.parent = self
            self._children_name_map["cspf_paths"] = "cspf-paths"
            self._children_yang_names.add("cspf-paths")
            self._segment_path = lambda: "cspf"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()


        class CspfPaths(Entity):
            """
            This table models the path calculation
            capabilities in XTC.A GET operation for the
            complete table will return no entries.
            
            .. attribute:: cspf_path
            
            	A GET operation on this class returns the path 
            	**type**\: list of    :py:class:`CspfPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.Cspf.CspfPaths, self).__init__()

                self.yang_name = "cspf-paths"
                self.yang_parent_name = "cspf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"cspf-path" : ("cspf_path", Pce.Cspf.CspfPaths.CspfPath)}

                self.cspf_path = YList(self)
                self._segment_path = lambda: "cspf-paths"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/cspf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.Cspf.CspfPaths, [], name, value)


            class CspfPath(Entity):
                """
                A GET operation on this class returns the path
                .
                
                .. attribute:: af  <key>
                
                	Address Family
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: source1  <key>
                
                	Source of path 1
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: destination1  <key>
                
                	Destination of path 1
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: metric_type  <key>
                
                	Metric type
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: source2  <key>
                
                	Source of path 2
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: destination2  <key>
                
                	Destination of path 2
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: disjoint_level  <key>
                
                	Disjointness level
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: disjoint_strict  <key>
                
                	Strict disjointness required
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: shortest_path  <key>
                
                	Whether path 1 or 2 should be shortest
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: cspf_result
                
                	CSPF Result
                	**type**\:   :py:class:`PceCspfRc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceCspfRc>`
                
                .. attribute:: headends_swapped
                
                	Headends swapped
                	**type**\:   :py:class:`PceHeadendSwap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceHeadendSwap>`
                
                .. attribute:: output_path
                
                	Output PCE paths
                	**type**\: list of    :py:class:`OutputPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath.OutputPath>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.Cspf.CspfPaths.CspfPath, self).__init__()

                    self.yang_name = "cspf-path"
                    self.yang_parent_name = "cspf-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"output-path" : ("output_path", Pce.Cspf.CspfPaths.CspfPath.OutputPath)}

                    self.af = YLeaf(YType.int32, "af")

                    self.source1 = YLeaf(YType.str, "source1")

                    self.destination1 = YLeaf(YType.str, "destination1")

                    self.metric_type = YLeaf(YType.int32, "metric-type")

                    self.source2 = YLeaf(YType.str, "source2")

                    self.destination2 = YLeaf(YType.str, "destination2")

                    self.disjoint_level = YLeaf(YType.int32, "disjoint-level")

                    self.disjoint_strict = YLeaf(YType.int32, "disjoint-strict")

                    self.shortest_path = YLeaf(YType.int32, "shortest-path")

                    self.cspf_result = YLeaf(YType.enumeration, "cspf-result")

                    self.headends_swapped = YLeaf(YType.enumeration, "headends-swapped")

                    self.output_path = YList(self)
                    self._segment_path = lambda: "cspf-path" + "[af='" + self.af.get() + "']" + "[source1='" + self.source1.get() + "']" + "[destination1='" + self.destination1.get() + "']" + "[metric-type='" + self.metric_type.get() + "']" + "[source2='" + self.source2.get() + "']" + "[destination2='" + self.destination2.get() + "']" + "[disjoint-level='" + self.disjoint_level.get() + "']" + "[disjoint-strict='" + self.disjoint_strict.get() + "']" + "[shortest-path='" + self.shortest_path.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/cspf/cspf-paths/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath, ['af', 'source1', 'destination1', 'metric_type', 'source2', 'destination2', 'disjoint_level', 'disjoint_strict', 'shortest_path', 'cspf_result', 'headends_swapped'], name, value)


                class OutputPath(Entity):
                    """
                    Output PCE paths
                    
                    .. attribute:: cost
                    
                    	Cost
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: destination
                    
                    	Destination of path
                    	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination>`
                    
                    .. attribute:: hops
                    
                    	Hop addresses
                    	**type**\: list of    :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath.OutputPath.Hops>`
                    
                    .. attribute:: source
                    
                    	Source of path
                    	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.Cspf.CspfPaths.CspfPath.OutputPath, self).__init__()

                        self.yang_name = "output-path"
                        self.yang_parent_name = "cspf-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"destination" : ("destination", Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination), "source" : ("source", Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source)}
                        self._child_list_classes = {"hops" : ("hops", Pce.Cspf.CspfPaths.CspfPath.OutputPath.Hops)}

                        self.cost = YLeaf(YType.uint64, "cost")

                        self.destination = Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination()
                        self.destination.parent = self
                        self._children_name_map["destination"] = "destination"
                        self._children_yang_names.add("destination")

                        self.source = Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source()
                        self.source.parent = self
                        self._children_name_map["source"] = "source"
                        self._children_yang_names.add("source")

                        self.hops = YList(self)
                        self._segment_path = lambda: "output-path"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath.OutputPath, ['cost'], name, value)


                    class Destination(Entity):
                        """
                        Destination of path
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination, self).__init__()

                            self.yang_name = "destination"
                            self.yang_parent_name = "output-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "destination"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination, ['af_name', 'ipv4', 'ipv6'], name, value)


                    class Hops(Entity):
                        """
                        Hop addresses
                        
                        .. attribute:: address_family
                        
                        	Address Family
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 prefix
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 prefix
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Hops, self).__init__()

                            self.yang_name = "hops"
                            self.yang_parent_name = "output-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address_family = YLeaf(YType.uint8, "address-family")

                            self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                            self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")
                            self._segment_path = lambda: "hops"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Hops, ['address_family', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                    class Source(Entity):
                        """
                        Source of path
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "output-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "source"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source, ['af_name', 'ipv4', 'ipv6'], name, value)


    class LspSummary(Entity):
        """
        LSP summary database in XTC
        
        .. attribute:: all_ls_ps
        
        	Summary for all peers
        	**type**\:   :py:class:`AllLsPs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.AllLsPs>`
        
        .. attribute:: peer_ls_ps_info
        
        	Number of LSPs for specific peer
        	**type**\: list of    :py:class:`PeerLsPsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.PeerLsPsInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.LspSummary, self).__init__()

            self.yang_name = "lsp-summary"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"all-ls-ps" : ("all_ls_ps", Pce.LspSummary.AllLsPs)}
            self._child_list_classes = {"peer-ls-ps-info" : ("peer_ls_ps_info", Pce.LspSummary.PeerLsPsInfo)}

            self.all_ls_ps = Pce.LspSummary.AllLsPs()
            self.all_ls_ps.parent = self
            self._children_name_map["all_ls_ps"] = "all-ls-ps"
            self._children_yang_names.add("all-ls-ps")

            self.peer_ls_ps_info = YList(self)
            self._segment_path = lambda: "lsp-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.LspSummary, [], name, value)


        class AllLsPs(Entity):
            """
            Summary for all peers
            
            .. attribute:: admin_up_ls_ps
            
            	Number of administratively up LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: all_ls_ps
            
            	Number of all LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvp_ls_ps
            
            	Number of LSPs with RSVP setup type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sr_ls_ps
            
            	Number of LSPs with Segment routing setup type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_ls_ps
            
            	Number of operational LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.LspSummary.AllLsPs, self).__init__()

                self.yang_name = "all-ls-ps"
                self.yang_parent_name = "lsp-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.admin_up_ls_ps = YLeaf(YType.uint32, "admin-up-ls-ps")

                self.all_ls_ps = YLeaf(YType.uint32, "all-ls-ps")

                self.rsvp_ls_ps = YLeaf(YType.uint32, "rsvp-ls-ps")

                self.sr_ls_ps = YLeaf(YType.uint32, "sr-ls-ps")

                self.up_ls_ps = YLeaf(YType.uint32, "up-ls-ps")
                self._segment_path = lambda: "all-ls-ps"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/lsp-summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.LspSummary.AllLsPs, ['admin_up_ls_ps', 'all_ls_ps', 'rsvp_ls_ps', 'sr_ls_ps', 'up_ls_ps'], name, value)


        class PeerLsPsInfo(Entity):
            """
            Number of LSPs for specific peer
            
            .. attribute:: lsp_summary
            
            	Number of LSPs for specific peer
            	**type**\:   :py:class:`LspSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.PeerLsPsInfo.LspSummary>`
            
            .. attribute:: peer_address
            
            	Peer IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.LspSummary.PeerLsPsInfo, self).__init__()

                self.yang_name = "peer-ls-ps-info"
                self.yang_parent_name = "lsp-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"lsp-summary" : ("lsp_summary", Pce.LspSummary.PeerLsPsInfo.LspSummary)}
                self._child_list_classes = {}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.lsp_summary = Pce.LspSummary.PeerLsPsInfo.LspSummary()
                self.lsp_summary.parent = self
                self._children_name_map["lsp_summary"] = "lsp-summary"
                self._children_yang_names.add("lsp-summary")
                self._segment_path = lambda: "peer-ls-ps-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/lsp-summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.LspSummary.PeerLsPsInfo, ['peer_address'], name, value)


            class LspSummary(Entity):
                """
                Number of LSPs for specific peer
                
                .. attribute:: admin_up_ls_ps
                
                	Number of administratively up LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: all_ls_ps
                
                	Number of all LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rsvp_ls_ps
                
                	Number of LSPs with RSVP setup type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sr_ls_ps
                
                	Number of LSPs with Segment routing setup type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_ls_ps
                
                	Number of operational LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.LspSummary.PeerLsPsInfo.LspSummary, self).__init__()

                    self.yang_name = "lsp-summary"
                    self.yang_parent_name = "peer-ls-ps-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.admin_up_ls_ps = YLeaf(YType.uint32, "admin-up-ls-ps")

                    self.all_ls_ps = YLeaf(YType.uint32, "all-ls-ps")

                    self.rsvp_ls_ps = YLeaf(YType.uint32, "rsvp-ls-ps")

                    self.sr_ls_ps = YLeaf(YType.uint32, "sr-ls-ps")

                    self.up_ls_ps = YLeaf(YType.uint32, "up-ls-ps")
                    self._segment_path = lambda: "lsp-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/lsp-summary/peer-ls-ps-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.LspSummary.PeerLsPsInfo.LspSummary, ['admin_up_ls_ps', 'all_ls_ps', 'rsvp_ls_ps', 'sr_ls_ps', 'up_ls_ps'], name, value)


    class PeerDetailInfos(Entity):
        """
        Detailed peers database in XTC
        
        .. attribute:: peer_detail_info
        
        	Detailed PCE peer information
        	**type**\: list of    :py:class:`PeerDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.PeerDetailInfos, self).__init__()

            self.yang_name = "peer-detail-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"peer-detail-info" : ("peer_detail_info", Pce.PeerDetailInfos.PeerDetailInfo)}

            self.peer_detail_info = YList(self)
            self._segment_path = lambda: "peer-detail-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.PeerDetailInfos, [], name, value)


        class PeerDetailInfo(Entity):
            """
            Detailed PCE peer information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: detail_pcep_information
            
            	Detailed PCE protocol information
            	**type**\:   :py:class:`DetailPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation>`
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:   :py:class:`PceProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProto>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.PeerDetailInfos.PeerDetailInfo, self).__init__()

                self.yang_name = "peer-detail-info"
                self.yang_parent_name = "peer-detail-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"detail-pcep-information" : ("detail_pcep_information", Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation)}
                self._child_list_classes = {}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.peer_address_xr = YLeaf(YType.str, "peer-address-xr")

                self.peer_protocol = YLeaf(YType.enumeration, "peer-protocol")

                self.detail_pcep_information = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation()
                self.detail_pcep_information.parent = self
                self._children_name_map["detail_pcep_information"] = "detail-pcep-information"
                self._children_yang_names.add("detail-pcep-information")
                self._segment_path = lambda: "peer-detail-info" + "[peer-address='" + self.peer_address.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/peer-detail-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo, ['peer_address', 'peer_address_xr', 'peer_protocol'], name, value)


            class DetailPcepInformation(Entity):
                """
                Detailed PCE protocol information
                
                .. attribute:: brief_pcep_information
                
                	Brief PCE protocol information
                	**type**\:   :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation>`
                
                .. attribute:: error
                
                	Error (for display only)
                	**type**\:  str
                
                .. attribute:: keepalives
                
                	Keepalive count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: keychain_enabled
                
                	Keychain based Authentication Enabled
                	**type**\:  bool
                
                .. attribute:: last_error_rx
                
                	Last PCError received
                	**type**\:   :py:class:`LastErrorRx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx>`
                
                .. attribute:: last_error_tx
                
                	Last PCError sent
                	**type**\:   :py:class:`LastErrorTx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx>`
                
                .. attribute:: local_session_id
                
                	Local PCEP session ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: maximum_dead_interval
                
                	Maximum dead interval for the peer
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: md5_enabled
                
                	MD5 Authentication Enabled
                	**type**\:  bool
                
                .. attribute:: minimum_keepalive_interval
                
                	Minimum keepalive interval for the peer
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: negotiated_dead_time
                
                	Negotiated DT
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_local_keepalive
                
                	Negotiated KA
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_remote_keepalive
                
                	Negotiated KA
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_rx
                
                	PCEErr Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_tx
                
                	PCEErr Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_rx
                
                	PCEInit Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_tx
                
                	PCEInit Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_keepalive_rx
                
                	PCE Keepalive Rx
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_keepalive_tx
                
                	PCE Keepalive Tx
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_open_rx
                
                	PCEOpen Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_open_tx
                
                	PCEOpen Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_rx
                
                	PCERep Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_tx
                
                	PCERep Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_rx
                
                	PCERpt Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_tx
                
                	PCERpt Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_rx
                
                	PCEReq Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_tx
                
                	PCEReq Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_rx
                
                	PCEUpd Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_tx
                
                	PCEUpd Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pcep_up_time
                
                	PCEP Up Time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_session_id
                
                	Remote PCEP session ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: speaker_id
                
                	Speaker Entity ID
                	**type**\:  str
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation, self).__init__()

                    self.yang_name = "detail-pcep-information"
                    self.yang_parent_name = "peer-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"brief-pcep-information" : ("brief_pcep_information", Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation), "last-error-rx" : ("last_error_rx", Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx), "last-error-tx" : ("last_error_tx", Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx)}
                    self._child_list_classes = {}

                    self.error = YLeaf(YType.str, "error")

                    self.keepalives = YLeaf(YType.uint32, "keepalives")

                    self.keychain_enabled = YLeaf(YType.boolean, "keychain-enabled")

                    self.local_session_id = YLeaf(YType.uint8, "local-session-id")

                    self.maximum_dead_interval = YLeaf(YType.uint8, "maximum-dead-interval")

                    self.md5_enabled = YLeaf(YType.boolean, "md5-enabled")

                    self.minimum_keepalive_interval = YLeaf(YType.uint8, "minimum-keepalive-interval")

                    self.negotiated_dead_time = YLeaf(YType.uint32, "negotiated-dead-time")

                    self.negotiated_local_keepalive = YLeaf(YType.uint32, "negotiated-local-keepalive")

                    self.negotiated_remote_keepalive = YLeaf(YType.uint32, "negotiated-remote-keepalive")

                    self.pce_error_rx = YLeaf(YType.uint32, "pce-error-rx")

                    self.pce_error_tx = YLeaf(YType.uint32, "pce-error-tx")

                    self.pce_initiate_rx = YLeaf(YType.uint32, "pce-initiate-rx")

                    self.pce_initiate_tx = YLeaf(YType.uint32, "pce-initiate-tx")

                    self.pce_keepalive_rx = YLeaf(YType.uint64, "pce-keepalive-rx")

                    self.pce_keepalive_tx = YLeaf(YType.uint64, "pce-keepalive-tx")

                    self.pce_open_rx = YLeaf(YType.uint32, "pce-open-rx")

                    self.pce_open_tx = YLeaf(YType.uint32, "pce-open-tx")

                    self.pce_reply_rx = YLeaf(YType.uint32, "pce-reply-rx")

                    self.pce_reply_tx = YLeaf(YType.uint32, "pce-reply-tx")

                    self.pce_report_rx = YLeaf(YType.uint32, "pce-report-rx")

                    self.pce_report_tx = YLeaf(YType.uint32, "pce-report-tx")

                    self.pce_request_rx = YLeaf(YType.uint32, "pce-request-rx")

                    self.pce_request_tx = YLeaf(YType.uint32, "pce-request-tx")

                    self.pce_update_rx = YLeaf(YType.uint32, "pce-update-rx")

                    self.pce_update_tx = YLeaf(YType.uint32, "pce-update-tx")

                    self.pcep_up_time = YLeaf(YType.uint32, "pcep-up-time")

                    self.remote_session_id = YLeaf(YType.uint8, "remote-session-id")

                    self.speaker_id = YLeaf(YType.str, "speaker-id")

                    self.brief_pcep_information = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation()
                    self.brief_pcep_information.parent = self
                    self._children_name_map["brief_pcep_information"] = "brief-pcep-information"
                    self._children_yang_names.add("brief-pcep-information")

                    self.last_error_rx = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx()
                    self.last_error_rx.parent = self
                    self._children_name_map["last_error_rx"] = "last-error-rx"
                    self._children_yang_names.add("last-error-rx")

                    self.last_error_tx = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx()
                    self.last_error_tx.parent = self
                    self._children_name_map["last_error_tx"] = "last-error-tx"
                    self._children_yang_names.add("last-error-tx")
                    self._segment_path = lambda: "detail-pcep-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation, ['error', 'keepalives', 'keychain_enabled', 'local_session_id', 'maximum_dead_interval', 'md5_enabled', 'minimum_keepalive_interval', 'negotiated_dead_time', 'negotiated_local_keepalive', 'negotiated_remote_keepalive', 'pce_error_rx', 'pce_error_tx', 'pce_initiate_rx', 'pce_initiate_tx', 'pce_keepalive_rx', 'pce_keepalive_tx', 'pce_open_rx', 'pce_open_tx', 'pce_reply_rx', 'pce_reply_tx', 'pce_report_rx', 'pce_report_tx', 'pce_request_rx', 'pce_request_tx', 'pce_update_rx', 'pce_update_tx', 'pcep_up_time', 'remote_session_id', 'speaker_id'], name, value)


                class BriefPcepInformation(Entity):
                    """
                    Brief PCE protocol information
                    
                    .. attribute:: capability_db_version
                    
                    	DB version capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_delta_sync
                    
                    	Delta Synchronization capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_instantiate
                    
                    	Instantiation capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_segment_routing
                    
                    	Segment Routing capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_triggered_sync
                    
                    	Triggered Synchronization capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_update
                    
                    	Update capability
                    	**type**\:  bool
                    
                    .. attribute:: pcep_state
                    
                    	PCEP State
                    	**type**\:   :py:class:`PcepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepState>`
                    
                    .. attribute:: stateful
                    
                    	Stateful
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation, self).__init__()

                        self.yang_name = "brief-pcep-information"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.capability_db_version = YLeaf(YType.boolean, "capability-db-version")

                        self.capability_delta_sync = YLeaf(YType.boolean, "capability-delta-sync")

                        self.capability_instantiate = YLeaf(YType.boolean, "capability-instantiate")

                        self.capability_segment_routing = YLeaf(YType.boolean, "capability-segment-routing")

                        self.capability_triggered_sync = YLeaf(YType.boolean, "capability-triggered-sync")

                        self.capability_update = YLeaf(YType.boolean, "capability-update")

                        self.pcep_state = YLeaf(YType.enumeration, "pcep-state")

                        self.stateful = YLeaf(YType.boolean, "stateful")
                        self._segment_path = lambda: "brief-pcep-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation, ['capability_db_version', 'capability_delta_sync', 'capability_instantiate', 'capability_segment_routing', 'capability_triggered_sync', 'capability_update', 'pcep_state', 'stateful'], name, value)


                class LastErrorRx(Entity):
                    """
                    Last PCError received
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx, self).__init__()

                        self.yang_name = "last-error-rx"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.pc_error_type = YLeaf(YType.uint8, "pc-error-type")

                        self.pc_error_value = YLeaf(YType.uint8, "pc-error-value")
                        self._segment_path = lambda: "last-error-rx"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx, ['pc_error_type', 'pc_error_value'], name, value)


                class LastErrorTx(Entity):
                    """
                    Last PCError sent
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx, self).__init__()

                        self.yang_name = "last-error-tx"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.pc_error_type = YLeaf(YType.uint8, "pc-error-type")

                        self.pc_error_value = YLeaf(YType.uint8, "pc-error-value")
                        self._segment_path = lambda: "last-error-tx"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx, ['pc_error_type', 'pc_error_value'], name, value)


    class PeerInfos(Entity):
        """
        Peers database in XTC
        
        .. attribute:: peer_info
        
        	PCE peer information
        	**type**\: list of    :py:class:`PeerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos.PeerInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.PeerInfos, self).__init__()

            self.yang_name = "peer-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"peer-info" : ("peer_info", Pce.PeerInfos.PeerInfo)}

            self.peer_info = YList(self)
            self._segment_path = lambda: "peer-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.PeerInfos, [], name, value)


        class PeerInfo(Entity):
            """
            PCE peer information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: brief_pcep_information
            
            	PCE protocol information
            	**type**\:   :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos.PeerInfo.BriefPcepInformation>`
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:   :py:class:`PceProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProto>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.PeerInfos.PeerInfo, self).__init__()

                self.yang_name = "peer-info"
                self.yang_parent_name = "peer-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"brief-pcep-information" : ("brief_pcep_information", Pce.PeerInfos.PeerInfo.BriefPcepInformation)}
                self._child_list_classes = {}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.peer_address_xr = YLeaf(YType.str, "peer-address-xr")

                self.peer_protocol = YLeaf(YType.enumeration, "peer-protocol")

                self.brief_pcep_information = Pce.PeerInfos.PeerInfo.BriefPcepInformation()
                self.brief_pcep_information.parent = self
                self._children_name_map["brief_pcep_information"] = "brief-pcep-information"
                self._children_yang_names.add("brief-pcep-information")
                self._segment_path = lambda: "peer-info" + "[peer-address='" + self.peer_address.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/peer-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.PeerInfos.PeerInfo, ['peer_address', 'peer_address_xr', 'peer_protocol'], name, value)


            class BriefPcepInformation(Entity):
                """
                PCE protocol information
                
                .. attribute:: capability_db_version
                
                	DB version capability
                	**type**\:  bool
                
                .. attribute:: capability_delta_sync
                
                	Delta Synchronization capability
                	**type**\:  bool
                
                .. attribute:: capability_instantiate
                
                	Instantiation capability
                	**type**\:  bool
                
                .. attribute:: capability_segment_routing
                
                	Segment Routing capability
                	**type**\:  bool
                
                .. attribute:: capability_triggered_sync
                
                	Triggered Synchronization capability
                	**type**\:  bool
                
                .. attribute:: capability_update
                
                	Update capability
                	**type**\:  bool
                
                .. attribute:: pcep_state
                
                	PCEP State
                	**type**\:   :py:class:`PcepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepState>`
                
                .. attribute:: stateful
                
                	Stateful
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.PeerInfos.PeerInfo.BriefPcepInformation, self).__init__()

                    self.yang_name = "brief-pcep-information"
                    self.yang_parent_name = "peer-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.capability_db_version = YLeaf(YType.boolean, "capability-db-version")

                    self.capability_delta_sync = YLeaf(YType.boolean, "capability-delta-sync")

                    self.capability_instantiate = YLeaf(YType.boolean, "capability-instantiate")

                    self.capability_segment_routing = YLeaf(YType.boolean, "capability-segment-routing")

                    self.capability_triggered_sync = YLeaf(YType.boolean, "capability-triggered-sync")

                    self.capability_update = YLeaf(YType.boolean, "capability-update")

                    self.pcep_state = YLeaf(YType.enumeration, "pcep-state")

                    self.stateful = YLeaf(YType.boolean, "stateful")
                    self._segment_path = lambda: "brief-pcep-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PeerInfos.PeerInfo.BriefPcepInformation, ['capability_db_version', 'capability_delta_sync', 'capability_instantiate', 'capability_segment_routing', 'capability_triggered_sync', 'capability_update', 'pcep_state', 'stateful'], name, value)


    class PrefixInfos(Entity):
        """
        Prefixes database in XTC
        
        .. attribute:: prefix_info
        
        	PCE prefix information
        	**type**\: list of    :py:class:`PrefixInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.PrefixInfos, self).__init__()

            self.yang_name = "prefix-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"prefix-info" : ("prefix_info", Pce.PrefixInfos.PrefixInfo)}

            self.prefix_info = YList(self)
            self._segment_path = lambda: "prefix-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.PrefixInfos, [], name, value)


        class PrefixInfo(Entity):
            """
            PCE prefix information
            
            .. attribute:: node_identifier  <key>
            
            	Node ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: address
            
            	Prefix address
            	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.Address>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:   :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.PrefixInfos.PrefixInfo, self).__init__()

                self.yang_name = "prefix-info"
                self.yang_parent_name = "prefix-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"node-protocol-identifier" : ("node_protocol_identifier", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier)}
                self._child_list_classes = {"address" : ("address", Pce.PrefixInfos.PrefixInfo.Address)}

                self.node_identifier = YLeaf(YType.int32, "node-identifier")

                self.node_identifier_xr = YLeaf(YType.uint32, "node-identifier-xr")

                self.node_protocol_identifier = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"
                self._children_yang_names.add("node-protocol-identifier")

                self.address = YList(self)
                self._segment_path = lambda: "prefix-info" + "[node-identifier='" + self.node_identifier.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/prefix-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.PrefixInfos.PrefixInfo, ['node_identifier', 'node_identifier_xr'], name, value)


            class Address(Entity):
                """
                Prefix address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.PrefixInfos.PrefixInfo.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.ipv4 = YLeaf(YType.str, "ipv4")

                    self.ipv6 = YLeaf(YType.str, "ipv6")
                    self._segment_path = lambda: "address"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.Address, ['af_name', 'ipv4', 'ipv6'], name, value)


            class NodeProtocolIdentifier(Entity):
                """
                Node protocol identifier
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\:  bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\:  bool
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\:  str
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"igp-information" : ("igp_information", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation), "srgb-information" : ("srgb_information", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation)}

                    self.ipv4_bgp_router_id = YLeaf(YType.str, "ipv4-bgp-router-id")

                    self.ipv4_bgp_router_id_set = YLeaf(YType.boolean, "ipv4-bgp-router-id-set")

                    self.ipv4te_router_id = YLeaf(YType.str, "ipv4te-router-id")

                    self.ipv4te_router_id_set = YLeaf(YType.boolean, "ipv4te-router-id-set")

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.igp_information = YList(self)
                    self.srgb_information = YList(self)
                    self._segment_path = lambda: "node-protocol-identifier"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, ['ipv4_bgp_router_id', 'ipv4_bgp_router_id_set', 'ipv4te_router_id', 'ipv4te_router_id_set', 'node_name'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp" : ("igp", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp)}
                        self._child_list_classes = {}

                        self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.igp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "igp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp), "isis" : ("isis", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis), "ospf" : ("ospf", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                class SrgbInformation(Entity):
                    """
                    SRGB information
                    
                    .. attribute:: igp_srgb
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation, self).__init__()

                        self.yang_name = "srgb-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp-srgb" : ("igp_srgb", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb)}
                        self._child_list_classes = {}

                        self.size = YLeaf(YType.uint32, "size")

                        self.start = YLeaf(YType.uint32, "start")

                        self.igp_srgb = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                        self.igp_srgb.parent = self
                        self._children_name_map["igp_srgb"] = "igp-srgb"
                        self._children_yang_names.add("igp-srgb")
                        self._segment_path = lambda: "srgb-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation, ['size', 'start'], name, value)


                    class IgpSrgb(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb, self).__init__()

                            self.yang_name = "igp-srgb"
                            self.yang_parent_name = "srgb-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp), "isis" : ("isis", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis), "ospf" : ("ospf", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp-srgb"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, ['area', 'router_id'], name, value)


    class TopologyNodes(Entity):
        """
        Node database in XTC
        
        .. attribute:: topology_node
        
        	Node information
        	**type**\: list of    :py:class:`TopologyNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.TopologyNodes, self).__init__()

            self.yang_name = "topology-nodes"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"topology-node" : ("topology_node", Pce.TopologyNodes.TopologyNode)}

            self.topology_node = YList(self)
            self._segment_path = lambda: "topology-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.TopologyNodes, [], name, value)


        class TopologyNode(Entity):
            """
            Node information
            
            .. attribute:: node_identifier  <key>
            
            	Node Identifier
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipv4_link
            
            	IPv4 Link information
            	**type**\: list of    :py:class:`Ipv4Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link>`
            
            .. attribute:: ipv6_link
            
            	IPv6 Link information
            	**type**\: list of    :py:class:`Ipv6Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:   :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier>`
            
            .. attribute:: overload
            
            	Node Overload Bit
            	**type**\:  bool
            
            .. attribute:: prefix_sid
            
            	Prefix SIDs
            	**type**\: list of    :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.PrefixSid>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.TopologyNodes.TopologyNode, self).__init__()

                self.yang_name = "topology-node"
                self.yang_parent_name = "topology-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"node-protocol-identifier" : ("node_protocol_identifier", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier)}
                self._child_list_classes = {"ipv4-link" : ("ipv4_link", Pce.TopologyNodes.TopologyNode.Ipv4Link), "ipv6-link" : ("ipv6_link", Pce.TopologyNodes.TopologyNode.Ipv6Link), "prefix-sid" : ("prefix_sid", Pce.TopologyNodes.TopologyNode.PrefixSid)}

                self.node_identifier = YLeaf(YType.int32, "node-identifier")

                self.node_identifier_xr = YLeaf(YType.uint32, "node-identifier-xr")

                self.overload = YLeaf(YType.boolean, "overload")

                self.node_protocol_identifier = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"
                self._children_yang_names.add("node-protocol-identifier")

                self.ipv4_link = YList(self)
                self.ipv6_link = YList(self)
                self.prefix_sid = YList(self)
                self._segment_path = lambda: "topology-node" + "[node-identifier='" + self.node_identifier.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/topology-nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.TopologyNodes.TopologyNode, ['node_identifier', 'node_identifier_xr', 'overload'], name, value)


            class Ipv4Link(Entity):
                """
                IPv4 Link information
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of    :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid>`
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:   :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation>`
                
                .. attribute:: local_ipv4_address
                
                	Local IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_ipv4_address
                
                	Remote IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:   :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: srlgs
                
                	SRLG Values
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link, self).__init__()

                    self.yang_name = "ipv4-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"local-igp-information" : ("local_igp_information", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation), "remote-node-protocol-identifier" : ("remote_node_protocol_identifier", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier)}
                    self._child_list_classes = {"adjacency-sid" : ("adjacency_sid", Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid)}

                    self.igp_metric = YLeaf(YType.uint32, "igp-metric")

                    self.local_ipv4_address = YLeaf(YType.str, "local-ipv4-address")

                    self.max_reservable_bandwidth = YLeaf(YType.uint64, "max-reservable-bandwidth")

                    self.maximum_link_bandwidth = YLeaf(YType.uint64, "maximum-link-bandwidth")

                    self.remote_ipv4_address = YLeaf(YType.str, "remote-ipv4-address")

                    self.srlgs = YLeafList(YType.uint32, "srlgs")

                    self.te_metric = YLeaf(YType.uint32, "te-metric")

                    self.local_igp_information = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"
                    self._children_yang_names.add("local-igp-information")

                    self.remote_node_protocol_identifier = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"
                    self._children_yang_names.add("remote-node-protocol-identifier")

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv4-link"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link, ['igp_metric', 'local_ipv4_address', 'max_reservable_bandwidth', 'maximum_link_bandwidth', 'remote_ipv4_address', 'srlgs', 'te_metric'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\:  bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\:  bool
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\:  bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\:  bool
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\:  bool
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:   :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sid-prefix" : ("sid_prefix", Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix)}
                        self._child_list_classes = {}

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.eflag = YLeaf(YType.boolean, "eflag")

                        self.lflag = YLeaf(YType.boolean, "lflag")

                        self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                        self.nflag = YLeaf(YType.boolean, "nflag")

                        self.pflag = YLeaf(YType.boolean, "pflag")

                        self.rflag = YLeaf(YType.boolean, "rflag")

                        self.sid_type = YLeaf(YType.enumeration, "sid-type")

                        self.vflag = YLeaf(YType.boolean, "vflag")

                        self.sid_prefix = Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._children_yang_names.add("sid-prefix")
                        self._segment_path = lambda: "adjacency-sid"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, ['domain_identifier', 'eflag', 'lflag', 'mpls_label', 'nflag', 'pflag', 'rflag', 'sid_type', 'vflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "sid-prefix"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp" : ("igp", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp)}
                        self._child_list_classes = {}

                        self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.igp = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "local-igp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp), "isis" : ("isis", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis), "ospf" : ("ospf", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                class RemoteNodeProtocolIdentifier(Entity):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\:  str
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"igp-information" : ("igp_information", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation), "srgb-information" : ("srgb_information", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation)}

                        self.ipv4_bgp_router_id = YLeaf(YType.str, "ipv4-bgp-router-id")

                        self.ipv4_bgp_router_id_set = YLeaf(YType.boolean, "ipv4-bgp-router-id-set")

                        self.ipv4te_router_id = YLeaf(YType.str, "ipv4te-router-id")

                        self.ipv4te_router_id_set = YLeaf(YType.boolean, "ipv4te-router-id-set")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.igp_information = YList(self)
                        self.srgb_information = YList(self)
                        self._segment_path = lambda: "remote-node-protocol-identifier"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, ['ipv4_bgp_router_id', 'ipv4_bgp_router_id_set', 'ipv4te_router_id', 'ipv4te_router_id_set', 'node_name'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"igp" : ("igp", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp)}
                            self._child_list_classes = {}

                            self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                            self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                            self.igp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._children_yang_names.add("igp")
                            self._segment_path = lambda: "igp-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp" : ("bgp", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp), "isis" : ("isis", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis), "ospf" : ("ospf", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf)}
                                self._child_list_classes = {}

                                self.igp_id = YLeaf(YType.enumeration, "igp-id")

                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._children_yang_names.add("bgp")

                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"
                                self._children_yang_names.add("isis")

                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"
                                self._children_yang_names.add("ospf")
                                self._segment_path = lambda: "igp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "bgp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.system_id = YLeaf(YType.str, "system-id")
                                    self._segment_path = lambda: "isis"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area = YLeaf(YType.uint32, "area")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "ospf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                    class SrgbInformation(Entity):
                        """
                        SRGB information
                        
                        .. attribute:: igp_srgb
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation, self).__init__()

                            self.yang_name = "srgb-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"igp-srgb" : ("igp_srgb", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb)}
                            self._child_list_classes = {}

                            self.size = YLeaf(YType.uint32, "size")

                            self.start = YLeaf(YType.uint32, "start")

                            self.igp_srgb = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                            self.igp_srgb.parent = self
                            self._children_name_map["igp_srgb"] = "igp-srgb"
                            self._children_yang_names.add("igp-srgb")
                            self._segment_path = lambda: "srgb-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation, ['size', 'start'], name, value)


                        class IgpSrgb(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb, self).__init__()

                                self.yang_name = "igp-srgb"
                                self.yang_parent_name = "srgb-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp" : ("bgp", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp), "isis" : ("isis", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis), "ospf" : ("ospf", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf)}
                                self._child_list_classes = {}

                                self.igp_id = YLeaf(YType.enumeration, "igp-id")

                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._children_yang_names.add("bgp")

                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"
                                self._children_yang_names.add("isis")

                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"
                                self._children_yang_names.add("ospf")
                                self._segment_path = lambda: "igp-srgb"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb, ['igp_id'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "bgp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, ['confed_asn', 'router_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.system_id = YLeaf(YType.str, "system-id")
                                    self._segment_path = lambda: "isis"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, ['level', 'system_id'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area = YLeaf(YType.uint32, "area")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "ospf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, ['area', 'router_id'], name, value)


            class Ipv6Link(Entity):
                """
                IPv6 Link information
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of    :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid>`
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:   :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation>`
                
                .. attribute:: local_ipv6_address
                
                	Local IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_ipv6_address
                
                	Remote IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:   :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link, self).__init__()

                    self.yang_name = "ipv6-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"local-igp-information" : ("local_igp_information", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation), "remote-node-protocol-identifier" : ("remote_node_protocol_identifier", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier)}
                    self._child_list_classes = {"adjacency-sid" : ("adjacency_sid", Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid)}

                    self.igp_metric = YLeaf(YType.uint32, "igp-metric")

                    self.local_ipv6_address = YLeaf(YType.str, "local-ipv6-address")

                    self.max_reservable_bandwidth = YLeaf(YType.uint64, "max-reservable-bandwidth")

                    self.maximum_link_bandwidth = YLeaf(YType.uint64, "maximum-link-bandwidth")

                    self.remote_ipv6_address = YLeaf(YType.str, "remote-ipv6-address")

                    self.te_metric = YLeaf(YType.uint32, "te-metric")

                    self.local_igp_information = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"
                    self._children_yang_names.add("local-igp-information")

                    self.remote_node_protocol_identifier = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"
                    self._children_yang_names.add("remote-node-protocol-identifier")

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv6-link"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link, ['igp_metric', 'local_ipv6_address', 'max_reservable_bandwidth', 'maximum_link_bandwidth', 'remote_ipv6_address', 'te_metric'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\:  bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\:  bool
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\:  bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\:  bool
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\:  bool
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:   :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sid-prefix" : ("sid_prefix", Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix)}
                        self._child_list_classes = {}

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.eflag = YLeaf(YType.boolean, "eflag")

                        self.lflag = YLeaf(YType.boolean, "lflag")

                        self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                        self.nflag = YLeaf(YType.boolean, "nflag")

                        self.pflag = YLeaf(YType.boolean, "pflag")

                        self.rflag = YLeaf(YType.boolean, "rflag")

                        self.sid_type = YLeaf(YType.enumeration, "sid-type")

                        self.vflag = YLeaf(YType.boolean, "vflag")

                        self.sid_prefix = Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._children_yang_names.add("sid-prefix")
                        self._segment_path = lambda: "adjacency-sid"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, ['domain_identifier', 'eflag', 'lflag', 'mpls_label', 'nflag', 'pflag', 'rflag', 'sid_type', 'vflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "sid-prefix"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp" : ("igp", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp)}
                        self._child_list_classes = {}

                        self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.igp = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "local-igp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp), "isis" : ("isis", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis), "ospf" : ("ospf", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                class RemoteNodeProtocolIdentifier(Entity):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\:  str
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"igp-information" : ("igp_information", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation), "srgb-information" : ("srgb_information", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation)}

                        self.ipv4_bgp_router_id = YLeaf(YType.str, "ipv4-bgp-router-id")

                        self.ipv4_bgp_router_id_set = YLeaf(YType.boolean, "ipv4-bgp-router-id-set")

                        self.ipv4te_router_id = YLeaf(YType.str, "ipv4te-router-id")

                        self.ipv4te_router_id_set = YLeaf(YType.boolean, "ipv4te-router-id-set")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.igp_information = YList(self)
                        self.srgb_information = YList(self)
                        self._segment_path = lambda: "remote-node-protocol-identifier"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, ['ipv4_bgp_router_id', 'ipv4_bgp_router_id_set', 'ipv4te_router_id', 'ipv4te_router_id_set', 'node_name'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"igp" : ("igp", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp)}
                            self._child_list_classes = {}

                            self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                            self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                            self.igp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._children_yang_names.add("igp")
                            self._segment_path = lambda: "igp-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp" : ("bgp", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp), "isis" : ("isis", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis), "ospf" : ("ospf", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf)}
                                self._child_list_classes = {}

                                self.igp_id = YLeaf(YType.enumeration, "igp-id")

                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._children_yang_names.add("bgp")

                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"
                                self._children_yang_names.add("isis")

                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"
                                self._children_yang_names.add("ospf")
                                self._segment_path = lambda: "igp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "bgp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.system_id = YLeaf(YType.str, "system-id")
                                    self._segment_path = lambda: "isis"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area = YLeaf(YType.uint32, "area")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "ospf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                    class SrgbInformation(Entity):
                        """
                        SRGB information
                        
                        .. attribute:: igp_srgb
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation, self).__init__()

                            self.yang_name = "srgb-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"igp-srgb" : ("igp_srgb", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb)}
                            self._child_list_classes = {}

                            self.size = YLeaf(YType.uint32, "size")

                            self.start = YLeaf(YType.uint32, "start")

                            self.igp_srgb = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                            self.igp_srgb.parent = self
                            self._children_name_map["igp_srgb"] = "igp-srgb"
                            self._children_yang_names.add("igp-srgb")
                            self._segment_path = lambda: "srgb-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation, ['size', 'start'], name, value)


                        class IgpSrgb(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb, self).__init__()

                                self.yang_name = "igp-srgb"
                                self.yang_parent_name = "srgb-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp" : ("bgp", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp), "isis" : ("isis", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis), "ospf" : ("ospf", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf)}
                                self._child_list_classes = {}

                                self.igp_id = YLeaf(YType.enumeration, "igp-id")

                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._children_yang_names.add("bgp")

                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"
                                self._children_yang_names.add("isis")

                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"
                                self._children_yang_names.add("ospf")
                                self._segment_path = lambda: "igp-srgb"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb, ['igp_id'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "bgp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, ['confed_asn', 'router_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.system_id = YLeaf(YType.str, "system-id")
                                    self._segment_path = lambda: "isis"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, ['level', 'system_id'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area = YLeaf(YType.uint32, "area")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "ospf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, ['area', 'router_id'], name, value)


            class NodeProtocolIdentifier(Entity):
                """
                Node protocol identifier
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\:  bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\:  bool
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\:  str
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"igp-information" : ("igp_information", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation), "srgb-information" : ("srgb_information", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation)}

                    self.ipv4_bgp_router_id = YLeaf(YType.str, "ipv4-bgp-router-id")

                    self.ipv4_bgp_router_id_set = YLeaf(YType.boolean, "ipv4-bgp-router-id-set")

                    self.ipv4te_router_id = YLeaf(YType.str, "ipv4te-router-id")

                    self.ipv4te_router_id_set = YLeaf(YType.boolean, "ipv4te-router-id-set")

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.igp_information = YList(self)
                    self.srgb_information = YList(self)
                    self._segment_path = lambda: "node-protocol-identifier"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier, ['ipv4_bgp_router_id', 'ipv4_bgp_router_id_set', 'ipv4te_router_id', 'ipv4te_router_id_set', 'node_name'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp" : ("igp", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp)}
                        self._child_list_classes = {}

                        self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.igp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "igp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp), "isis" : ("isis", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis), "ospf" : ("ospf", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                class SrgbInformation(Entity):
                    """
                    SRGB information
                    
                    .. attribute:: igp_srgb
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation, self).__init__()

                        self.yang_name = "srgb-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp-srgb" : ("igp_srgb", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb)}
                        self._child_list_classes = {}

                        self.size = YLeaf(YType.uint32, "size")

                        self.start = YLeaf(YType.uint32, "start")

                        self.igp_srgb = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                        self.igp_srgb.parent = self
                        self._children_name_map["igp_srgb"] = "igp-srgb"
                        self._children_yang_names.add("igp-srgb")
                        self._segment_path = lambda: "srgb-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation, ['size', 'start'], name, value)


                    class IgpSrgb(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb, self).__init__()

                            self.yang_name = "igp-srgb"
                            self.yang_parent_name = "srgb-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp), "isis" : ("isis", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis), "ospf" : ("ospf", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp-srgb"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, ['area', 'router_id'], name, value)


            class PrefixSid(Entity):
                """
                Prefix SIDs
                
                .. attribute:: domain_identifier
                
                	Domain identifier
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: eflag
                
                	E Flag
                	**type**\:  bool
                
                .. attribute:: lflag
                
                	L Flag
                	**type**\:  bool
                
                .. attribute:: mpls_label
                
                	MPLS Label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nflag
                
                	N Flag
                	**type**\:  bool
                
                .. attribute:: pflag
                
                	P Flag
                	**type**\:  bool
                
                .. attribute:: rflag
                
                	R Flag
                	**type**\:  bool
                
                .. attribute:: sid_prefix
                
                	Prefix
                	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix>`
                
                .. attribute:: sid_type
                
                	SID Type
                	**type**\:   :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                
                .. attribute:: vflag
                
                	V Flag
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.TopologyNodes.TopologyNode.PrefixSid, self).__init__()

                    self.yang_name = "prefix-sid"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"sid-prefix" : ("sid_prefix", Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix)}
                    self._child_list_classes = {}

                    self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                    self.eflag = YLeaf(YType.boolean, "eflag")

                    self.lflag = YLeaf(YType.boolean, "lflag")

                    self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                    self.nflag = YLeaf(YType.boolean, "nflag")

                    self.pflag = YLeaf(YType.boolean, "pflag")

                    self.rflag = YLeaf(YType.boolean, "rflag")

                    self.sid_type = YLeaf(YType.enumeration, "sid-type")

                    self.vflag = YLeaf(YType.boolean, "vflag")

                    self.sid_prefix = Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix()
                    self.sid_prefix.parent = self
                    self._children_name_map["sid_prefix"] = "sid-prefix"
                    self._children_yang_names.add("sid-prefix")
                    self._segment_path = lambda: "prefix-sid"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.PrefixSid, ['domain_identifier', 'eflag', 'lflag', 'mpls_label', 'nflag', 'pflag', 'rflag', 'sid_type', 'vflag'], name, value)


                class SidPrefix(Entity):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix, self).__init__()

                        self.yang_name = "sid-prefix"
                        self.yang_parent_name = "prefix-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.ipv4 = YLeaf(YType.str, "ipv4")

                        self.ipv6 = YLeaf(YType.str, "ipv6")
                        self._segment_path = lambda: "sid-prefix"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.PrefixSid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


    class TopologySummary(Entity):
        """
        Node summary database in XTC
        
        .. attribute:: adjacency_sids
        
        	Number of total adjacency SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: epe_links
        
        	Number of EPE links
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: epesids
        
        	Number of total EPE SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: links
        
        	Number of links
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: lookup_nodes
        
        	Number of lookup nodes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: nodes
        
        	Number of PCE nodes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefix_sids
        
        	Number of total prefix SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefixes
        
        	Number of prefixes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: protected_adjacency_sids
        
        	Number of protected adjacency SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: regular_prefix_sids
        
        	Number of reguar prefix SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stats_topology_update
        
        	Statistics on topology update
        	**type**\:   :py:class:`StatsTopologyUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologySummary.StatsTopologyUpdate>`
        
        .. attribute:: strict_prefix_sids
        
        	Number of strict prefix SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: topology_consistent
        
        	True if topology is consistent
        	**type**\:  bool
        
        .. attribute:: un_protected_adjacency_sids
        
        	Number of unprotected adjacency SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.TopologySummary, self).__init__()

            self.yang_name = "topology-summary"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"stats-topology-update" : ("stats_topology_update", Pce.TopologySummary.StatsTopologyUpdate)}
            self._child_list_classes = {}

            self.adjacency_sids = YLeaf(YType.uint32, "adjacency-sids")

            self.epe_links = YLeaf(YType.uint32, "epe-links")

            self.epesids = YLeaf(YType.uint32, "epesids")

            self.links = YLeaf(YType.uint32, "links")

            self.lookup_nodes = YLeaf(YType.uint32, "lookup-nodes")

            self.nodes = YLeaf(YType.uint32, "nodes")

            self.prefix_sids = YLeaf(YType.uint32, "prefix-sids")

            self.prefixes = YLeaf(YType.uint32, "prefixes")

            self.protected_adjacency_sids = YLeaf(YType.uint32, "protected-adjacency-sids")

            self.regular_prefix_sids = YLeaf(YType.uint32, "regular-prefix-sids")

            self.strict_prefix_sids = YLeaf(YType.uint32, "strict-prefix-sids")

            self.topology_consistent = YLeaf(YType.boolean, "topology-consistent")

            self.un_protected_adjacency_sids = YLeaf(YType.uint32, "un-protected-adjacency-sids")

            self.stats_topology_update = Pce.TopologySummary.StatsTopologyUpdate()
            self.stats_topology_update.parent = self
            self._children_name_map["stats_topology_update"] = "stats-topology-update"
            self._children_yang_names.add("stats-topology-update")
            self._segment_path = lambda: "topology-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.TopologySummary, ['adjacency_sids', 'epe_links', 'epesids', 'links', 'lookup_nodes', 'nodes', 'prefix_sids', 'prefixes', 'protected_adjacency_sids', 'regular_prefix_sids', 'strict_prefix_sids', 'topology_consistent', 'un_protected_adjacency_sids'], name, value)


        class StatsTopologyUpdate(Entity):
            """
            Statistics on topology update
            
            .. attribute:: num_links_added
            
            	Number of links added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_links_deleted
            
            	Number of links deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_added
            
            	Number of nodes added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_deleted
            
            	Number of nodes deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_added
            
            	Number of prefixes added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_deleted
            
            	Number of prefixes deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.TopologySummary.StatsTopologyUpdate, self).__init__()

                self.yang_name = "stats-topology-update"
                self.yang_parent_name = "topology-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.num_links_added = YLeaf(YType.uint32, "num-links-added")

                self.num_links_deleted = YLeaf(YType.uint32, "num-links-deleted")

                self.num_nodes_added = YLeaf(YType.uint32, "num-nodes-added")

                self.num_nodes_deleted = YLeaf(YType.uint32, "num-nodes-deleted")

                self.num_prefixes_added = YLeaf(YType.uint32, "num-prefixes-added")

                self.num_prefixes_deleted = YLeaf(YType.uint32, "num-prefixes-deleted")
                self._segment_path = lambda: "stats-topology-update"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/topology-summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.TopologySummary.StatsTopologyUpdate, ['num_links_added', 'num_links_deleted', 'num_nodes_added', 'num_nodes_deleted', 'num_prefixes_added', 'num_prefixes_deleted'], name, value)


    class TunnelDetailInfos(Entity):
        """
        Detailed tunnel database in XTC
        
        .. attribute:: tunnel_detail_info
        
        	Detailed tunnel information
        	**type**\: list of    :py:class:`TunnelDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.TunnelDetailInfos, self).__init__()

            self.yang_name = "tunnel-detail-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel-detail-info" : ("tunnel_detail_info", Pce.TunnelDetailInfos.TunnelDetailInfo)}

            self.tunnel_detail_info = YList(self)
            self._segment_path = lambda: "tunnel-detail-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.TunnelDetailInfos, [], name, value)


        class TunnelDetailInfo(Entity):
            """
            Detailed tunnel information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: plsp_id  <key>
            
            	PCEP LSP ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tunnel_name  <key>
            
            	Tunnel name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: detail_lsp_information
            
            	Detail LSP information
            	**type**\: list of    :py:class:`DetailLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation>`
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: private_lsp_information
            
            	Private LSP information
            	**type**\:   :py:class:`PrivateLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation>`
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.TunnelDetailInfos.TunnelDetailInfo, self).__init__()

                self.yang_name = "tunnel-detail-info"
                self.yang_parent_name = "tunnel-detail-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"private-lsp-information" : ("private_lsp_information", Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation)}
                self._child_list_classes = {"detail-lsp-information" : ("detail_lsp_information", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation)}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.plsp_id = YLeaf(YType.int32, "plsp-id")

                self.tunnel_name = YLeaf(YType.str, "tunnel-name")

                self.pcc_address = YLeaf(YType.str, "pcc-address")

                self.tunnel_name_xr = YLeaf(YType.str, "tunnel-name-xr")

                self.private_lsp_information = Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation()
                self.private_lsp_information.parent = self
                self._children_name_map["private_lsp_information"] = "private-lsp-information"
                self._children_yang_names.add("private-lsp-information")

                self.detail_lsp_information = YList(self)
                self._segment_path = lambda: "tunnel-detail-info" + "[peer-address='" + self.peer_address.get() + "']" + "[plsp-id='" + self.plsp_id.get() + "']" + "[tunnel-name='" + self.tunnel_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/tunnel-detail-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo, ['peer_address', 'plsp_id', 'tunnel_name', 'pcc_address', 'tunnel_name_xr'], name, value)


            class DetailLspInformation(Entity):
                """
                Detail LSP information
                
                .. attribute:: actual_bandwidth
                
                	Actual bandwidth utilized in the data\-plane
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: actual_bandwidth_specified
                
                	True if router notifies actual bandwidth
                	**type**\:  bool
                
                .. attribute:: brief_lsp_information
                
                	Brief LSP information
                	**type**\:   :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation>`
                
                .. attribute:: computing_pce
                
                	Computing PCE
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: er_os
                
                	Paths
                	**type**\:   :py:class:`ErOs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs>`
                
                .. attribute:: lsp_association_info
                
                	LSP association information
                	**type**\:   :py:class:`LspAssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo>`
                
                .. attribute:: lsp_attributes
                
                	LSP attributes
                	**type**\:   :py:class:`LspAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes>`
                
                .. attribute:: lsp_role
                
                	LSP Role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsppcep_information
                
                	PCEP related LSP information
                	**type**\:   :py:class:`LsppcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation>`
                
                .. attribute:: reporting_pcc_address
                
                	Reporting PCC address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: rro
                
                	RRO
                	**type**\: list of    :py:class:`Rro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro>`
                
                .. attribute:: signaled_bandwidth
                
                	Signaled Bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: signaled_bandwidth_specified
                
                	True if router notifies signal bandwidth
                	**type**\:  bool
                
                .. attribute:: srlg_info
                
                	List of SLRGs used by LSP
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_sync_pce
                
                	State\-sync PCE
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: sub_delegated_pce
                
                	Sub delegated PCE
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation, self).__init__()

                    self.yang_name = "detail-lsp-information"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"brief-lsp-information" : ("brief_lsp_information", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation), "er-os" : ("er_os", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs), "lsp-association-info" : ("lsp_association_info", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo), "lsp-attributes" : ("lsp_attributes", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes), "lsppcep-information" : ("lsppcep_information", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation)}
                    self._child_list_classes = {"rro" : ("rro", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro)}

                    self.actual_bandwidth = YLeaf(YType.uint64, "actual-bandwidth")

                    self.actual_bandwidth_specified = YLeaf(YType.boolean, "actual-bandwidth-specified")

                    self.computing_pce = YLeaf(YType.uint32, "computing-pce")

                    self.lsp_role = YLeaf(YType.uint32, "lsp-role")

                    self.reporting_pcc_address = YLeaf(YType.str, "reporting-pcc-address")

                    self.signaled_bandwidth = YLeaf(YType.uint64, "signaled-bandwidth")

                    self.signaled_bandwidth_specified = YLeaf(YType.boolean, "signaled-bandwidth-specified")

                    self.srlg_info = YLeafList(YType.uint32, "srlg-info")

                    self.state_sync_pce = YLeaf(YType.str, "state-sync-pce")

                    self.sub_delegated_pce = YLeaf(YType.str, "sub-delegated-pce")

                    self.brief_lsp_information = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation()
                    self.brief_lsp_information.parent = self
                    self._children_name_map["brief_lsp_information"] = "brief-lsp-information"
                    self._children_yang_names.add("brief-lsp-information")

                    self.er_os = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs()
                    self.er_os.parent = self
                    self._children_name_map["er_os"] = "er-os"
                    self._children_yang_names.add("er-os")

                    self.lsp_association_info = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo()
                    self.lsp_association_info.parent = self
                    self._children_name_map["lsp_association_info"] = "lsp-association-info"
                    self._children_yang_names.add("lsp-association-info")

                    self.lsp_attributes = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes()
                    self.lsp_attributes.parent = self
                    self._children_name_map["lsp_attributes"] = "lsp-attributes"
                    self._children_yang_names.add("lsp-attributes")

                    self.lsppcep_information = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation()
                    self.lsppcep_information.parent = self
                    self._children_name_map["lsppcep_information"] = "lsppcep-information"
                    self._children_yang_names.add("lsppcep-information")

                    self.rro = YList(self)
                    self._segment_path = lambda: "detail-lsp-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation, ['actual_bandwidth', 'actual_bandwidth_specified', 'computing_pce', 'lsp_role', 'reporting_pcc_address', 'signaled_bandwidth', 'signaled_bandwidth_specified', 'srlg_info', 'state_sync_pce', 'sub_delegated_pce'], name, value)


                class BriefLspInformation(Entity):
                    """
                    Brief LSP information
                    
                    .. attribute:: administrative_state
                    
                    	Admin state
                    	**type**\:   :py:class:`LspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspState>`
                    
                    .. attribute:: binding_sid
                    
                    	Binding SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: lsp_setup_type
                    
                    	LSP Setup Type
                    	**type**\:   :py:class:`LspSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetup>`
                    
                    .. attribute:: lspid
                    
                    	LSP ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: operational_state
                    
                    	Operational state
                    	**type**\:   :py:class:`PcepLspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspState>`
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation, self).__init__()

                        self.yang_name = "brief-lsp-information"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.administrative_state = YLeaf(YType.enumeration, "administrative-state")

                        self.binding_sid = YLeaf(YType.uint32, "binding-sid")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.lsp_setup_type = YLeaf(YType.enumeration, "lsp-setup-type")

                        self.lspid = YLeaf(YType.uint32, "lspid")

                        self.operational_state = YLeaf(YType.enumeration, "operational-state")

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")
                        self._segment_path = lambda: "brief-lsp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation, ['administrative_state', 'binding_sid', 'destination_address', 'lsp_setup_type', 'lspid', 'operational_state', 'source_address', 'tunnel_id'], name, value)


                class ErOs(Entity):
                    """
                    Paths
                    
                    .. attribute:: computed_hop_list_time
                    
                    	Computed Hop List Time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_type
                    
                    	Computed Metric Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_value
                    
                    	Computed Metric Value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_rsvp_path
                    
                    	Computed RSVP path
                    	**type**\: list of    :py:class:`ComputedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath>`
                    
                    .. attribute:: computed_sr_path
                    
                    	Computed SR path
                    	**type**\: list of    :py:class:`ComputedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath>`
                    
                    .. attribute:: reported_metric_type
                    
                    	Reported Metric Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_metric_value
                    
                    	Reported Metric Value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_rsvp_path
                    
                    	Reported RSVP path
                    	**type**\: list of    :py:class:`ReportedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath>`
                    
                    .. attribute:: reported_sr_path
                    
                    	Reported SR path
                    	**type**\: list of    :py:class:`ReportedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs, self).__init__()

                        self.yang_name = "er-os"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"computed-rsvp-path" : ("computed_rsvp_path", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath), "computed-sr-path" : ("computed_sr_path", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath), "reported-rsvp-path" : ("reported_rsvp_path", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath), "reported-sr-path" : ("reported_sr_path", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath)}

                        self.computed_hop_list_time = YLeaf(YType.uint32, "computed-hop-list-time")

                        self.computed_metric_type = YLeaf(YType.uint32, "computed-metric-type")

                        self.computed_metric_value = YLeaf(YType.uint32, "computed-metric-value")

                        self.reported_metric_type = YLeaf(YType.uint32, "reported-metric-type")

                        self.reported_metric_value = YLeaf(YType.uint32, "reported-metric-value")

                        self.computed_rsvp_path = YList(self)
                        self.computed_sr_path = YList(self)
                        self.reported_rsvp_path = YList(self)
                        self.reported_sr_path = YList(self)
                        self._segment_path = lambda: "er-os"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs, ['computed_hop_list_time', 'computed_metric_type', 'computed_metric_value', 'reported_metric_type', 'reported_metric_value'], name, value)


                    class ComputedRsvpPath(Entity):
                        """
                        Computed RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath, self).__init__()

                            self.yang_name = "computed-rsvp-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.hop_address = YLeaf(YType.str, "hop-address")
                            self._segment_path = lambda: "computed-rsvp-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath, ['hop_address'], name, value)


                    class ComputedSrPath(Entity):
                        """
                        Computed SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath, self).__init__()

                            self.yang_name = "computed-sr-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_addr = YLeaf(YType.str, "local-addr")

                            self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                            self.remote_addr = YLeaf(YType.str, "remote-addr")

                            self.sid_type = YLeaf(YType.enumeration, "sid-type")
                            self._segment_path = lambda: "computed-sr-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath, ['local_addr', 'mpls_label', 'remote_addr', 'sid_type'], name, value)


                    class ReportedRsvpPath(Entity):
                        """
                        Reported RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath, self).__init__()

                            self.yang_name = "reported-rsvp-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.hop_address = YLeaf(YType.str, "hop-address")
                            self._segment_path = lambda: "reported-rsvp-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath, ['hop_address'], name, value)


                    class ReportedSrPath(Entity):
                        """
                        Reported SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath, self).__init__()

                            self.yang_name = "reported-sr-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_addr = YLeaf(YType.str, "local-addr")

                            self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                            self.remote_addr = YLeaf(YType.str, "remote-addr")

                            self.sid_type = YLeaf(YType.enumeration, "sid-type")
                            self._segment_path = lambda: "reported-sr-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath, ['local_addr', 'mpls_label', 'remote_addr', 'sid_type'], name, value)


                class LspAssociationInfo(Entity):
                    """
                    LSP association information
                    
                    .. attribute:: association_id
                    
                    	Association ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: association_source
                    
                    	Association Source
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: association_type
                    
                    	Association Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo, self).__init__()

                        self.yang_name = "lsp-association-info"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.association_id = YLeaf(YType.uint32, "association-id")

                        self.association_source = YLeaf(YType.str, "association-source")

                        self.association_type = YLeaf(YType.uint32, "association-type")
                        self._segment_path = lambda: "lsp-association-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo, ['association_id', 'association_source', 'association_type'], name, value)


                class LspAttributes(Entity):
                    """
                    LSP attributes
                    
                    .. attribute:: affinity_exclude_any
                    
                    	Affinity exclude any
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_all
                    
                    	Affinity include all
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_any
                    
                    	Affinity include any
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_priority
                    
                    	Hold Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_protection
                    
                    	True, if local protection is desired
                    	**type**\:  bool
                    
                    .. attribute:: setup_priority
                    
                    	Setup Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes, self).__init__()

                        self.yang_name = "lsp-attributes"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.affinity_exclude_any = YLeaf(YType.uint32, "affinity-exclude-any")

                        self.affinity_include_all = YLeaf(YType.uint32, "affinity-include-all")

                        self.affinity_include_any = YLeaf(YType.uint32, "affinity-include-any")

                        self.hold_priority = YLeaf(YType.uint8, "hold-priority")

                        self.local_protection = YLeaf(YType.boolean, "local-protection")

                        self.setup_priority = YLeaf(YType.uint8, "setup-priority")
                        self._segment_path = lambda: "lsp-attributes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes, ['affinity_exclude_any', 'affinity_include_all', 'affinity_include_any', 'hold_priority', 'local_protection', 'setup_priority'], name, value)


                class LsppcepInformation(Entity):
                    """
                    PCEP related LSP information
                    
                    .. attribute:: pcep_flag_a
                    
                    	PCEP LSP admin flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_d
                    
                    	PCEP LSP delegation flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_o
                    
                    	PCEP LSP operation flag
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pcep_flag_r
                    
                    	PCEP LSP remove flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_s
                    
                    	PCEP LSP state\-sync flag
                    	**type**\:  bool
                    
                    .. attribute:: pcepid
                    
                    	PCE protocol identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rsvp_error
                    
                    	RSVP error info
                    	**type**\:   :py:class:`RsvpError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation, self).__init__()

                        self.yang_name = "lsppcep-information"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"rsvp-error" : ("rsvp_error", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError)}
                        self._child_list_classes = {}

                        self.pcep_flag_a = YLeaf(YType.boolean, "pcep-flag-a")

                        self.pcep_flag_d = YLeaf(YType.boolean, "pcep-flag-d")

                        self.pcep_flag_o = YLeaf(YType.uint8, "pcep-flag-o")

                        self.pcep_flag_r = YLeaf(YType.boolean, "pcep-flag-r")

                        self.pcep_flag_s = YLeaf(YType.boolean, "pcep-flag-s")

                        self.pcepid = YLeaf(YType.uint32, "pcepid")

                        self.rsvp_error = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError()
                        self.rsvp_error.parent = self
                        self._children_name_map["rsvp_error"] = "rsvp-error"
                        self._children_yang_names.add("rsvp-error")
                        self._segment_path = lambda: "lsppcep-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation, ['pcep_flag_a', 'pcep_flag_d', 'pcep_flag_o', 'pcep_flag_r', 'pcep_flag_s', 'pcepid'], name, value)


                    class RsvpError(Entity):
                        """
                        RSVP error info
                        
                        .. attribute:: error_code
                        
                        	RSVP error code
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_flags
                        
                        	RSVP error flags
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_value
                        
                        	RSVP error value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: node_address
                        
                        	RSVP error node address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError, self).__init__()

                            self.yang_name = "rsvp-error"
                            self.yang_parent_name = "lsppcep-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error_code = YLeaf(YType.uint8, "error-code")

                            self.error_flags = YLeaf(YType.uint8, "error-flags")

                            self.error_value = YLeaf(YType.uint16, "error-value")

                            self.node_address = YLeaf(YType.str, "node-address")
                            self._segment_path = lambda: "rsvp-error"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError, ['error_code', 'error_flags', 'error_value', 'node_address'], name, value)


                class Rro(Entity):
                    """
                    RRO
                    
                    .. attribute:: flags
                    
                    	RRO Flags
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address of RRO
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mpls_label
                    
                    	MPLS label of RRO
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rro_type
                    
                    	RRO Type
                    	**type**\:   :py:class:`PceRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceRro>`
                    
                    .. attribute:: sr_rro
                    
                    	Segment Routing RRO info
                    	**type**\:   :py:class:`SrRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro, self).__init__()

                        self.yang_name = "rro"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sr-rro" : ("sr_rro", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro)}
                        self._child_list_classes = {}

                        self.flags = YLeaf(YType.uint8, "flags")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                        self.rro_type = YLeaf(YType.enumeration, "rro-type")

                        self.sr_rro = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro()
                        self.sr_rro.parent = self
                        self._children_name_map["sr_rro"] = "sr-rro"
                        self._children_yang_names.add("sr-rro")
                        self._segment_path = lambda: "rro"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro, ['flags', 'ipv4_address', 'mpls_label', 'rro_type'], name, value)


                    class SrRro(Entity):
                        """
                        Segment Routing RRO info
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro, self).__init__()

                            self.yang_name = "sr-rro"
                            self.yang_parent_name = "rro"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_addr = YLeaf(YType.str, "local-addr")

                            self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                            self.remote_addr = YLeaf(YType.str, "remote-addr")

                            self.sid_type = YLeaf(YType.enumeration, "sid-type")
                            self._segment_path = lambda: "sr-rro"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro, ['local_addr', 'mpls_label', 'remote_addr', 'sid_type'], name, value)


            class PrivateLspInformation(Entity):
                """
                Private LSP information
                
                .. attribute:: event_buffer
                
                	LSP Event buffer
                	**type**\: list of    :py:class:`EventBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation, self).__init__()

                    self.yang_name = "private-lsp-information"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"event-buffer" : ("event_buffer", Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer)}

                    self.event_buffer = YList(self)
                    self._segment_path = lambda: "private-lsp-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation, [], name, value)


                class EventBuffer(Entity):
                    """
                    LSP Event buffer
                    
                    .. attribute:: event_message
                    
                    	Event message
                    	**type**\:  str
                    
                    .. attribute:: time_stamp
                    
                    	Event time, relative to Jan 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer, self).__init__()

                        self.yang_name = "event-buffer"
                        self.yang_parent_name = "private-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.event_message = YLeaf(YType.str, "event-message")

                        self.time_stamp = YLeaf(YType.uint32, "time-stamp")
                        self._segment_path = lambda: "event-buffer"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer, ['event_message', 'time_stamp'], name, value)


    class TunnelInfos(Entity):
        """
        Tunnel database in XTC
        
        .. attribute:: tunnel_info
        
        	Tunnel information
        	**type**\: list of    :py:class:`TunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(Pce.TunnelInfos, self).__init__()

            self.yang_name = "tunnel-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel-info" : ("tunnel_info", Pce.TunnelInfos.TunnelInfo)}

            self.tunnel_info = YList(self)
            self._segment_path = lambda: "tunnel-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.TunnelInfos, [], name, value)


        class TunnelInfo(Entity):
            """
            Tunnel information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: plsp_id  <key>
            
            	PCEP LSP ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tunnel_name  <key>
            
            	Tunnel name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: brief_lsp_information
            
            	Brief LSP information
            	**type**\: list of    :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo.BriefLspInformation>`
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(Pce.TunnelInfos.TunnelInfo, self).__init__()

                self.yang_name = "tunnel-info"
                self.yang_parent_name = "tunnel-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"brief-lsp-information" : ("brief_lsp_information", Pce.TunnelInfos.TunnelInfo.BriefLspInformation)}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.plsp_id = YLeaf(YType.int32, "plsp-id")

                self.tunnel_name = YLeaf(YType.str, "tunnel-name")

                self.pcc_address = YLeaf(YType.str, "pcc-address")

                self.tunnel_name_xr = YLeaf(YType.str, "tunnel-name-xr")

                self.brief_lsp_information = YList(self)
                self._segment_path = lambda: "tunnel-info" + "[peer-address='" + self.peer_address.get() + "']" + "[plsp-id='" + self.plsp_id.get() + "']" + "[tunnel-name='" + self.tunnel_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/tunnel-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.TunnelInfos.TunnelInfo, ['peer_address', 'plsp_id', 'tunnel_name', 'pcc_address', 'tunnel_name_xr'], name, value)


            class BriefLspInformation(Entity):
                """
                Brief LSP information
                
                .. attribute:: administrative_state
                
                	Admin state
                	**type**\:   :py:class:`LspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspState>`
                
                .. attribute:: binding_sid
                
                	Binding SID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_address
                
                	Destination address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: lsp_setup_type
                
                	LSP Setup Type
                	**type**\:   :py:class:`LspSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetup>`
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_state
                
                	Operational state
                	**type**\:   :py:class:`PcepLspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspState>`
                
                .. attribute:: source_address
                
                	Source address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(Pce.TunnelInfos.TunnelInfo.BriefLspInformation, self).__init__()

                    self.yang_name = "brief-lsp-information"
                    self.yang_parent_name = "tunnel-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.administrative_state = YLeaf(YType.enumeration, "administrative-state")

                    self.binding_sid = YLeaf(YType.uint32, "binding-sid")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.lsp_setup_type = YLeaf(YType.enumeration, "lsp-setup-type")

                    self.lspid = YLeaf(YType.uint32, "lspid")

                    self.operational_state = YLeaf(YType.enumeration, "operational-state")

                    self.source_address = YLeaf(YType.str, "source-address")

                    self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")
                    self._segment_path = lambda: "brief-lsp-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TunnelInfos.TunnelInfo.BriefLspInformation, ['administrative_state', 'binding_sid', 'destination_address', 'lsp_setup_type', 'lspid', 'operational_state', 'source_address', 'tunnel_id'], name, value)

    def clone_ptr(self):
        self._top_entity = Pce()
        return self._top_entity

class PceLspData(Entity):
    """
    PCE LSP's data
    
    .. attribute:: lsp_summary
    
    	LSP summary database in XTC
    	**type**\:   :py:class:`LspSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary>`
    
    .. attribute:: tunnel_detail_infos
    
    	Detailed tunnel database in XTC
    	**type**\:   :py:class:`TunnelDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos>`
    
    .. attribute:: tunnel_infos
    
    	Tunnel database in XTC
    	**type**\:   :py:class:`TunnelInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2017-06-26'

    def __init__(self):
        super(PceLspData, self).__init__()
        self._top_entity = None

        self.yang_name = "pce-lsp-data"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"lsp-summary" : ("lsp_summary", PceLspData.LspSummary), "tunnel-detail-infos" : ("tunnel_detail_infos", PceLspData.TunnelDetailInfos), "tunnel-infos" : ("tunnel_infos", PceLspData.TunnelInfos)}
        self._child_list_classes = {}

        self.lsp_summary = PceLspData.LspSummary()
        self.lsp_summary.parent = self
        self._children_name_map["lsp_summary"] = "lsp-summary"
        self._children_yang_names.add("lsp-summary")

        self.tunnel_detail_infos = PceLspData.TunnelDetailInfos()
        self.tunnel_detail_infos.parent = self
        self._children_name_map["tunnel_detail_infos"] = "tunnel-detail-infos"
        self._children_yang_names.add("tunnel-detail-infos")

        self.tunnel_infos = PceLspData.TunnelInfos()
        self.tunnel_infos.parent = self
        self._children_name_map["tunnel_infos"] = "tunnel-infos"
        self._children_yang_names.add("tunnel-infos")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data"


    class LspSummary(Entity):
        """
        LSP summary database in XTC
        
        .. attribute:: all_ls_ps
        
        	Summary for all peers
        	**type**\:   :py:class:`AllLsPs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.AllLsPs>`
        
        .. attribute:: peer_ls_ps_info
        
        	Number of LSPs for specific peer
        	**type**\: list of    :py:class:`PeerLsPsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.PeerLsPsInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(PceLspData.LspSummary, self).__init__()

            self.yang_name = "lsp-summary"
            self.yang_parent_name = "pce-lsp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"all-ls-ps" : ("all_ls_ps", PceLspData.LspSummary.AllLsPs)}
            self._child_list_classes = {"peer-ls-ps-info" : ("peer_ls_ps_info", PceLspData.LspSummary.PeerLsPsInfo)}

            self.all_ls_ps = PceLspData.LspSummary.AllLsPs()
            self.all_ls_ps.parent = self
            self._children_name_map["all_ls_ps"] = "all-ls-ps"
            self._children_yang_names.add("all-ls-ps")

            self.peer_ls_ps_info = YList(self)
            self._segment_path = lambda: "lsp-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PceLspData.LspSummary, [], name, value)


        class AllLsPs(Entity):
            """
            Summary for all peers
            
            .. attribute:: admin_up_ls_ps
            
            	Number of administratively up LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: all_ls_ps
            
            	Number of all LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvp_ls_ps
            
            	Number of LSPs with RSVP setup type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sr_ls_ps
            
            	Number of LSPs with Segment routing setup type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_ls_ps
            
            	Number of operational LSPs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PceLspData.LspSummary.AllLsPs, self).__init__()

                self.yang_name = "all-ls-ps"
                self.yang_parent_name = "lsp-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.admin_up_ls_ps = YLeaf(YType.uint32, "admin-up-ls-ps")

                self.all_ls_ps = YLeaf(YType.uint32, "all-ls-ps")

                self.rsvp_ls_ps = YLeaf(YType.uint32, "rsvp-ls-ps")

                self.sr_ls_ps = YLeaf(YType.uint32, "sr-ls-ps")

                self.up_ls_ps = YLeaf(YType.uint32, "up-ls-ps")
                self._segment_path = lambda: "all-ls-ps"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/lsp-summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PceLspData.LspSummary.AllLsPs, ['admin_up_ls_ps', 'all_ls_ps', 'rsvp_ls_ps', 'sr_ls_ps', 'up_ls_ps'], name, value)


        class PeerLsPsInfo(Entity):
            """
            Number of LSPs for specific peer
            
            .. attribute:: lsp_summary
            
            	Number of LSPs for specific peer
            	**type**\:   :py:class:`LspSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.PeerLsPsInfo.LspSummary>`
            
            .. attribute:: peer_address
            
            	Peer IPv4 address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PceLspData.LspSummary.PeerLsPsInfo, self).__init__()

                self.yang_name = "peer-ls-ps-info"
                self.yang_parent_name = "lsp-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"lsp-summary" : ("lsp_summary", PceLspData.LspSummary.PeerLsPsInfo.LspSummary)}
                self._child_list_classes = {}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.lsp_summary = PceLspData.LspSummary.PeerLsPsInfo.LspSummary()
                self.lsp_summary.parent = self
                self._children_name_map["lsp_summary"] = "lsp-summary"
                self._children_yang_names.add("lsp-summary")
                self._segment_path = lambda: "peer-ls-ps-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/lsp-summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PceLspData.LspSummary.PeerLsPsInfo, ['peer_address'], name, value)


            class LspSummary(Entity):
                """
                Number of LSPs for specific peer
                
                .. attribute:: admin_up_ls_ps
                
                	Number of administratively up LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: all_ls_ps
                
                	Number of all LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: rsvp_ls_ps
                
                	Number of LSPs with RSVP setup type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sr_ls_ps
                
                	Number of LSPs with Segment routing setup type
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_ls_ps
                
                	Number of operational LSPs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceLspData.LspSummary.PeerLsPsInfo.LspSummary, self).__init__()

                    self.yang_name = "lsp-summary"
                    self.yang_parent_name = "peer-ls-ps-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.admin_up_ls_ps = YLeaf(YType.uint32, "admin-up-ls-ps")

                    self.all_ls_ps = YLeaf(YType.uint32, "all-ls-ps")

                    self.rsvp_ls_ps = YLeaf(YType.uint32, "rsvp-ls-ps")

                    self.sr_ls_ps = YLeaf(YType.uint32, "sr-ls-ps")

                    self.up_ls_ps = YLeaf(YType.uint32, "up-ls-ps")
                    self._segment_path = lambda: "lsp-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/lsp-summary/peer-ls-ps-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.LspSummary.PeerLsPsInfo.LspSummary, ['admin_up_ls_ps', 'all_ls_ps', 'rsvp_ls_ps', 'sr_ls_ps', 'up_ls_ps'], name, value)


    class TunnelDetailInfos(Entity):
        """
        Detailed tunnel database in XTC
        
        .. attribute:: tunnel_detail_info
        
        	Detailed tunnel information
        	**type**\: list of    :py:class:`TunnelDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(PceLspData.TunnelDetailInfos, self).__init__()

            self.yang_name = "tunnel-detail-infos"
            self.yang_parent_name = "pce-lsp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel-detail-info" : ("tunnel_detail_info", PceLspData.TunnelDetailInfos.TunnelDetailInfo)}

            self.tunnel_detail_info = YList(self)
            self._segment_path = lambda: "tunnel-detail-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PceLspData.TunnelDetailInfos, [], name, value)


        class TunnelDetailInfo(Entity):
            """
            Detailed tunnel information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: plsp_id  <key>
            
            	PCEP LSP ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tunnel_name  <key>
            
            	Tunnel name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: detail_lsp_information
            
            	Detail LSP information
            	**type**\: list of    :py:class:`DetailLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation>`
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: private_lsp_information
            
            	Private LSP information
            	**type**\:   :py:class:`PrivateLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation>`
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PceLspData.TunnelDetailInfos.TunnelDetailInfo, self).__init__()

                self.yang_name = "tunnel-detail-info"
                self.yang_parent_name = "tunnel-detail-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"private-lsp-information" : ("private_lsp_information", PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation)}
                self._child_list_classes = {"detail-lsp-information" : ("detail_lsp_information", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation)}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.plsp_id = YLeaf(YType.int32, "plsp-id")

                self.tunnel_name = YLeaf(YType.str, "tunnel-name")

                self.pcc_address = YLeaf(YType.str, "pcc-address")

                self.tunnel_name_xr = YLeaf(YType.str, "tunnel-name-xr")

                self.private_lsp_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation()
                self.private_lsp_information.parent = self
                self._children_name_map["private_lsp_information"] = "private-lsp-information"
                self._children_yang_names.add("private-lsp-information")

                self.detail_lsp_information = YList(self)
                self._segment_path = lambda: "tunnel-detail-info" + "[peer-address='" + self.peer_address.get() + "']" + "[plsp-id='" + self.plsp_id.get() + "']" + "[tunnel-name='" + self.tunnel_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/tunnel-detail-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo, ['peer_address', 'plsp_id', 'tunnel_name', 'pcc_address', 'tunnel_name_xr'], name, value)


            class DetailLspInformation(Entity):
                """
                Detail LSP information
                
                .. attribute:: actual_bandwidth
                
                	Actual bandwidth utilized in the data\-plane
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: actual_bandwidth_specified
                
                	True if router notifies actual bandwidth
                	**type**\:  bool
                
                .. attribute:: brief_lsp_information
                
                	Brief LSP information
                	**type**\:   :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation>`
                
                .. attribute:: computing_pce
                
                	Computing PCE
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: er_os
                
                	Paths
                	**type**\:   :py:class:`ErOs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs>`
                
                .. attribute:: lsp_association_info
                
                	LSP association information
                	**type**\:   :py:class:`LspAssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo>`
                
                .. attribute:: lsp_attributes
                
                	LSP attributes
                	**type**\:   :py:class:`LspAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes>`
                
                .. attribute:: lsp_role
                
                	LSP Role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsppcep_information
                
                	PCEP related LSP information
                	**type**\:   :py:class:`LsppcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation>`
                
                .. attribute:: reporting_pcc_address
                
                	Reporting PCC address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: rro
                
                	RRO
                	**type**\: list of    :py:class:`Rro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro>`
                
                .. attribute:: signaled_bandwidth
                
                	Signaled Bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: signaled_bandwidth_specified
                
                	True if router notifies signal bandwidth
                	**type**\:  bool
                
                .. attribute:: srlg_info
                
                	List of SLRGs used by LSP
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_sync_pce
                
                	State\-sync PCE
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: sub_delegated_pce
                
                	Sub delegated PCE
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation, self).__init__()

                    self.yang_name = "detail-lsp-information"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"brief-lsp-information" : ("brief_lsp_information", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation), "er-os" : ("er_os", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs), "lsp-association-info" : ("lsp_association_info", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo), "lsp-attributes" : ("lsp_attributes", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes), "lsppcep-information" : ("lsppcep_information", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation)}
                    self._child_list_classes = {"rro" : ("rro", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro)}

                    self.actual_bandwidth = YLeaf(YType.uint64, "actual-bandwidth")

                    self.actual_bandwidth_specified = YLeaf(YType.boolean, "actual-bandwidth-specified")

                    self.computing_pce = YLeaf(YType.uint32, "computing-pce")

                    self.lsp_role = YLeaf(YType.uint32, "lsp-role")

                    self.reporting_pcc_address = YLeaf(YType.str, "reporting-pcc-address")

                    self.signaled_bandwidth = YLeaf(YType.uint64, "signaled-bandwidth")

                    self.signaled_bandwidth_specified = YLeaf(YType.boolean, "signaled-bandwidth-specified")

                    self.srlg_info = YLeafList(YType.uint32, "srlg-info")

                    self.state_sync_pce = YLeaf(YType.str, "state-sync-pce")

                    self.sub_delegated_pce = YLeaf(YType.str, "sub-delegated-pce")

                    self.brief_lsp_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation()
                    self.brief_lsp_information.parent = self
                    self._children_name_map["brief_lsp_information"] = "brief-lsp-information"
                    self._children_yang_names.add("brief-lsp-information")

                    self.er_os = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs()
                    self.er_os.parent = self
                    self._children_name_map["er_os"] = "er-os"
                    self._children_yang_names.add("er-os")

                    self.lsp_association_info = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo()
                    self.lsp_association_info.parent = self
                    self._children_name_map["lsp_association_info"] = "lsp-association-info"
                    self._children_yang_names.add("lsp-association-info")

                    self.lsp_attributes = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes()
                    self.lsp_attributes.parent = self
                    self._children_name_map["lsp_attributes"] = "lsp-attributes"
                    self._children_yang_names.add("lsp-attributes")

                    self.lsppcep_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation()
                    self.lsppcep_information.parent = self
                    self._children_name_map["lsppcep_information"] = "lsppcep-information"
                    self._children_yang_names.add("lsppcep-information")

                    self.rro = YList(self)
                    self._segment_path = lambda: "detail-lsp-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation, ['actual_bandwidth', 'actual_bandwidth_specified', 'computing_pce', 'lsp_role', 'reporting_pcc_address', 'signaled_bandwidth', 'signaled_bandwidth_specified', 'srlg_info', 'state_sync_pce', 'sub_delegated_pce'], name, value)


                class BriefLspInformation(Entity):
                    """
                    Brief LSP information
                    
                    .. attribute:: administrative_state
                    
                    	Admin state
                    	**type**\:   :py:class:`LspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspState>`
                    
                    .. attribute:: binding_sid
                    
                    	Binding SID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: lsp_setup_type
                    
                    	LSP Setup Type
                    	**type**\:   :py:class:`LspSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetup>`
                    
                    .. attribute:: lspid
                    
                    	LSP ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: operational_state
                    
                    	Operational state
                    	**type**\:   :py:class:`PcepLspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspState>`
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation, self).__init__()

                        self.yang_name = "brief-lsp-information"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.administrative_state = YLeaf(YType.enumeration, "administrative-state")

                        self.binding_sid = YLeaf(YType.uint32, "binding-sid")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.lsp_setup_type = YLeaf(YType.enumeration, "lsp-setup-type")

                        self.lspid = YLeaf(YType.uint32, "lspid")

                        self.operational_state = YLeaf(YType.enumeration, "operational-state")

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")
                        self._segment_path = lambda: "brief-lsp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation, ['administrative_state', 'binding_sid', 'destination_address', 'lsp_setup_type', 'lspid', 'operational_state', 'source_address', 'tunnel_id'], name, value)


                class ErOs(Entity):
                    """
                    Paths
                    
                    .. attribute:: computed_hop_list_time
                    
                    	Computed Hop List Time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_type
                    
                    	Computed Metric Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_value
                    
                    	Computed Metric Value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_rsvp_path
                    
                    	Computed RSVP path
                    	**type**\: list of    :py:class:`ComputedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath>`
                    
                    .. attribute:: computed_sr_path
                    
                    	Computed SR path
                    	**type**\: list of    :py:class:`ComputedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath>`
                    
                    .. attribute:: reported_metric_type
                    
                    	Reported Metric Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_metric_value
                    
                    	Reported Metric Value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_rsvp_path
                    
                    	Reported RSVP path
                    	**type**\: list of    :py:class:`ReportedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath>`
                    
                    .. attribute:: reported_sr_path
                    
                    	Reported SR path
                    	**type**\: list of    :py:class:`ReportedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs, self).__init__()

                        self.yang_name = "er-os"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"computed-rsvp-path" : ("computed_rsvp_path", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath), "computed-sr-path" : ("computed_sr_path", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath), "reported-rsvp-path" : ("reported_rsvp_path", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath), "reported-sr-path" : ("reported_sr_path", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath)}

                        self.computed_hop_list_time = YLeaf(YType.uint32, "computed-hop-list-time")

                        self.computed_metric_type = YLeaf(YType.uint32, "computed-metric-type")

                        self.computed_metric_value = YLeaf(YType.uint32, "computed-metric-value")

                        self.reported_metric_type = YLeaf(YType.uint32, "reported-metric-type")

                        self.reported_metric_value = YLeaf(YType.uint32, "reported-metric-value")

                        self.computed_rsvp_path = YList(self)
                        self.computed_sr_path = YList(self)
                        self.reported_rsvp_path = YList(self)
                        self.reported_sr_path = YList(self)
                        self._segment_path = lambda: "er-os"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs, ['computed_hop_list_time', 'computed_metric_type', 'computed_metric_value', 'reported_metric_type', 'reported_metric_value'], name, value)


                    class ComputedRsvpPath(Entity):
                        """
                        Computed RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath, self).__init__()

                            self.yang_name = "computed-rsvp-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.hop_address = YLeaf(YType.str, "hop-address")
                            self._segment_path = lambda: "computed-rsvp-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath, ['hop_address'], name, value)


                    class ComputedSrPath(Entity):
                        """
                        Computed SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath, self).__init__()

                            self.yang_name = "computed-sr-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_addr = YLeaf(YType.str, "local-addr")

                            self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                            self.remote_addr = YLeaf(YType.str, "remote-addr")

                            self.sid_type = YLeaf(YType.enumeration, "sid-type")
                            self._segment_path = lambda: "computed-sr-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath, ['local_addr', 'mpls_label', 'remote_addr', 'sid_type'], name, value)


                    class ReportedRsvpPath(Entity):
                        """
                        Reported RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath, self).__init__()

                            self.yang_name = "reported-rsvp-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.hop_address = YLeaf(YType.str, "hop-address")
                            self._segment_path = lambda: "reported-rsvp-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath, ['hop_address'], name, value)


                    class ReportedSrPath(Entity):
                        """
                        Reported SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath, self).__init__()

                            self.yang_name = "reported-sr-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_addr = YLeaf(YType.str, "local-addr")

                            self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                            self.remote_addr = YLeaf(YType.str, "remote-addr")

                            self.sid_type = YLeaf(YType.enumeration, "sid-type")
                            self._segment_path = lambda: "reported-sr-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath, ['local_addr', 'mpls_label', 'remote_addr', 'sid_type'], name, value)


                class LspAssociationInfo(Entity):
                    """
                    LSP association information
                    
                    .. attribute:: association_id
                    
                    	Association ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: association_source
                    
                    	Association Source
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: association_type
                    
                    	Association Type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo, self).__init__()

                        self.yang_name = "lsp-association-info"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.association_id = YLeaf(YType.uint32, "association-id")

                        self.association_source = YLeaf(YType.str, "association-source")

                        self.association_type = YLeaf(YType.uint32, "association-type")
                        self._segment_path = lambda: "lsp-association-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo, ['association_id', 'association_source', 'association_type'], name, value)


                class LspAttributes(Entity):
                    """
                    LSP attributes
                    
                    .. attribute:: affinity_exclude_any
                    
                    	Affinity exclude any
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_all
                    
                    	Affinity include all
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_any
                    
                    	Affinity include any
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hold_priority
                    
                    	Hold Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_protection
                    
                    	True, if local protection is desired
                    	**type**\:  bool
                    
                    .. attribute:: setup_priority
                    
                    	Setup Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes, self).__init__()

                        self.yang_name = "lsp-attributes"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.affinity_exclude_any = YLeaf(YType.uint32, "affinity-exclude-any")

                        self.affinity_include_all = YLeaf(YType.uint32, "affinity-include-all")

                        self.affinity_include_any = YLeaf(YType.uint32, "affinity-include-any")

                        self.hold_priority = YLeaf(YType.uint8, "hold-priority")

                        self.local_protection = YLeaf(YType.boolean, "local-protection")

                        self.setup_priority = YLeaf(YType.uint8, "setup-priority")
                        self._segment_path = lambda: "lsp-attributes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes, ['affinity_exclude_any', 'affinity_include_all', 'affinity_include_any', 'hold_priority', 'local_protection', 'setup_priority'], name, value)


                class LsppcepInformation(Entity):
                    """
                    PCEP related LSP information
                    
                    .. attribute:: pcep_flag_a
                    
                    	PCEP LSP admin flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_d
                    
                    	PCEP LSP delegation flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_o
                    
                    	PCEP LSP operation flag
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pcep_flag_r
                    
                    	PCEP LSP remove flag
                    	**type**\:  bool
                    
                    .. attribute:: pcep_flag_s
                    
                    	PCEP LSP state\-sync flag
                    	**type**\:  bool
                    
                    .. attribute:: pcepid
                    
                    	PCE protocol identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rsvp_error
                    
                    	RSVP error info
                    	**type**\:   :py:class:`RsvpError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation, self).__init__()

                        self.yang_name = "lsppcep-information"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"rsvp-error" : ("rsvp_error", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError)}
                        self._child_list_classes = {}

                        self.pcep_flag_a = YLeaf(YType.boolean, "pcep-flag-a")

                        self.pcep_flag_d = YLeaf(YType.boolean, "pcep-flag-d")

                        self.pcep_flag_o = YLeaf(YType.uint8, "pcep-flag-o")

                        self.pcep_flag_r = YLeaf(YType.boolean, "pcep-flag-r")

                        self.pcep_flag_s = YLeaf(YType.boolean, "pcep-flag-s")

                        self.pcepid = YLeaf(YType.uint32, "pcepid")

                        self.rsvp_error = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError()
                        self.rsvp_error.parent = self
                        self._children_name_map["rsvp_error"] = "rsvp-error"
                        self._children_yang_names.add("rsvp-error")
                        self._segment_path = lambda: "lsppcep-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation, ['pcep_flag_a', 'pcep_flag_d', 'pcep_flag_o', 'pcep_flag_r', 'pcep_flag_s', 'pcepid'], name, value)


                    class RsvpError(Entity):
                        """
                        RSVP error info
                        
                        .. attribute:: error_code
                        
                        	RSVP error code
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_flags
                        
                        	RSVP error flags
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_value
                        
                        	RSVP error value
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: node_address
                        
                        	RSVP error node address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError, self).__init__()

                            self.yang_name = "rsvp-error"
                            self.yang_parent_name = "lsppcep-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.error_code = YLeaf(YType.uint8, "error-code")

                            self.error_flags = YLeaf(YType.uint8, "error-flags")

                            self.error_value = YLeaf(YType.uint16, "error-value")

                            self.node_address = YLeaf(YType.str, "node-address")
                            self._segment_path = lambda: "rsvp-error"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError, ['error_code', 'error_flags', 'error_value', 'node_address'], name, value)


                class Rro(Entity):
                    """
                    RRO
                    
                    .. attribute:: flags
                    
                    	RRO Flags
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address of RRO
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mpls_label
                    
                    	MPLS label of RRO
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rro_type
                    
                    	RRO Type
                    	**type**\:   :py:class:`PceRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceRro>`
                    
                    .. attribute:: sr_rro
                    
                    	Segment Routing RRO info
                    	**type**\:   :py:class:`SrRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro, self).__init__()

                        self.yang_name = "rro"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sr-rro" : ("sr_rro", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro)}
                        self._child_list_classes = {}

                        self.flags = YLeaf(YType.uint8, "flags")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                        self.rro_type = YLeaf(YType.enumeration, "rro-type")

                        self.sr_rro = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro()
                        self.sr_rro.parent = self
                        self._children_name_map["sr_rro"] = "sr-rro"
                        self._children_yang_names.add("sr-rro")
                        self._segment_path = lambda: "rro"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro, ['flags', 'ipv4_address', 'mpls_label', 'rro_type'], name, value)


                    class SrRro(Entity):
                        """
                        Segment Routing RRO info
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:   :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro, self).__init__()

                            self.yang_name = "sr-rro"
                            self.yang_parent_name = "rro"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_addr = YLeaf(YType.str, "local-addr")

                            self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                            self.remote_addr = YLeaf(YType.str, "remote-addr")

                            self.sid_type = YLeaf(YType.enumeration, "sid-type")
                            self._segment_path = lambda: "sr-rro"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro, ['local_addr', 'mpls_label', 'remote_addr', 'sid_type'], name, value)


            class PrivateLspInformation(Entity):
                """
                Private LSP information
                
                .. attribute:: event_buffer
                
                	LSP Event buffer
                	**type**\: list of    :py:class:`EventBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation, self).__init__()

                    self.yang_name = "private-lsp-information"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"event-buffer" : ("event_buffer", PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer)}

                    self.event_buffer = YList(self)
                    self._segment_path = lambda: "private-lsp-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation, [], name, value)


                class EventBuffer(Entity):
                    """
                    LSP Event buffer
                    
                    .. attribute:: event_message
                    
                    	Event message
                    	**type**\:  str
                    
                    .. attribute:: time_stamp
                    
                    	Event time, relative to Jan 1, 1970
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer, self).__init__()

                        self.yang_name = "event-buffer"
                        self.yang_parent_name = "private-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.event_message = YLeaf(YType.str, "event-message")

                        self.time_stamp = YLeaf(YType.uint32, "time-stamp")
                        self._segment_path = lambda: "event-buffer"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer, ['event_message', 'time_stamp'], name, value)


    class TunnelInfos(Entity):
        """
        Tunnel database in XTC
        
        .. attribute:: tunnel_info
        
        	Tunnel information
        	**type**\: list of    :py:class:`TunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(PceLspData.TunnelInfos, self).__init__()

            self.yang_name = "tunnel-infos"
            self.yang_parent_name = "pce-lsp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel-info" : ("tunnel_info", PceLspData.TunnelInfos.TunnelInfo)}

            self.tunnel_info = YList(self)
            self._segment_path = lambda: "tunnel-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PceLspData.TunnelInfos, [], name, value)


        class TunnelInfo(Entity):
            """
            Tunnel information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: plsp_id  <key>
            
            	PCEP LSP ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tunnel_name  <key>
            
            	Tunnel name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: brief_lsp_information
            
            	Brief LSP information
            	**type**\: list of    :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation>`
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PceLspData.TunnelInfos.TunnelInfo, self).__init__()

                self.yang_name = "tunnel-info"
                self.yang_parent_name = "tunnel-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"brief-lsp-information" : ("brief_lsp_information", PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation)}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.plsp_id = YLeaf(YType.int32, "plsp-id")

                self.tunnel_name = YLeaf(YType.str, "tunnel-name")

                self.pcc_address = YLeaf(YType.str, "pcc-address")

                self.tunnel_name_xr = YLeaf(YType.str, "tunnel-name-xr")

                self.brief_lsp_information = YList(self)
                self._segment_path = lambda: "tunnel-info" + "[peer-address='" + self.peer_address.get() + "']" + "[plsp-id='" + self.plsp_id.get() + "']" + "[tunnel-name='" + self.tunnel_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/tunnel-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PceLspData.TunnelInfos.TunnelInfo, ['peer_address', 'plsp_id', 'tunnel_name', 'pcc_address', 'tunnel_name_xr'], name, value)


            class BriefLspInformation(Entity):
                """
                Brief LSP information
                
                .. attribute:: administrative_state
                
                	Admin state
                	**type**\:   :py:class:`LspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspState>`
                
                .. attribute:: binding_sid
                
                	Binding SID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_address
                
                	Destination address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: lsp_setup_type
                
                	LSP Setup Type
                	**type**\:   :py:class:`LspSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetup>`
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: operational_state
                
                	Operational state
                	**type**\:   :py:class:`PcepLspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspState>`
                
                .. attribute:: source_address
                
                	Source address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation, self).__init__()

                    self.yang_name = "brief-lsp-information"
                    self.yang_parent_name = "tunnel-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.administrative_state = YLeaf(YType.enumeration, "administrative-state")

                    self.binding_sid = YLeaf(YType.uint32, "binding-sid")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.lsp_setup_type = YLeaf(YType.enumeration, "lsp-setup-type")

                    self.lspid = YLeaf(YType.uint32, "lspid")

                    self.operational_state = YLeaf(YType.enumeration, "operational-state")

                    self.source_address = YLeaf(YType.str, "source-address")

                    self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")
                    self._segment_path = lambda: "brief-lsp-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation, ['administrative_state', 'binding_sid', 'destination_address', 'lsp_setup_type', 'lspid', 'operational_state', 'source_address', 'tunnel_id'], name, value)

    def clone_ptr(self):
        self._top_entity = PceLspData()
        return self._top_entity

class PcePeer(Entity):
    """
    pce peer
    
    .. attribute:: peer_detail_infos
    
    	Detailed peers database in XTC
    	**type**\:   :py:class:`PeerDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos>`
    
    .. attribute:: peer_infos
    
    	Peers database in XTC
    	**type**\:   :py:class:`PeerInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2017-06-26'

    def __init__(self):
        super(PcePeer, self).__init__()
        self._top_entity = None

        self.yang_name = "pce-peer"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"peer-detail-infos" : ("peer_detail_infos", PcePeer.PeerDetailInfos), "peer-infos" : ("peer_infos", PcePeer.PeerInfos)}
        self._child_list_classes = {}

        self.peer_detail_infos = PcePeer.PeerDetailInfos()
        self.peer_detail_infos.parent = self
        self._children_name_map["peer_detail_infos"] = "peer-detail-infos"
        self._children_yang_names.add("peer-detail-infos")

        self.peer_infos = PcePeer.PeerInfos()
        self.peer_infos.parent = self
        self._children_name_map["peer_infos"] = "peer-infos"
        self._children_yang_names.add("peer-infos")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer"


    class PeerDetailInfos(Entity):
        """
        Detailed peers database in XTC
        
        .. attribute:: peer_detail_info
        
        	Detailed PCE peer information
        	**type**\: list of    :py:class:`PeerDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(PcePeer.PeerDetailInfos, self).__init__()

            self.yang_name = "peer-detail-infos"
            self.yang_parent_name = "pce-peer"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"peer-detail-info" : ("peer_detail_info", PcePeer.PeerDetailInfos.PeerDetailInfo)}

            self.peer_detail_info = YList(self)
            self._segment_path = lambda: "peer-detail-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PcePeer.PeerDetailInfos, [], name, value)


        class PeerDetailInfo(Entity):
            """
            Detailed PCE peer information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: detail_pcep_information
            
            	Detailed PCE protocol information
            	**type**\:   :py:class:`DetailPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation>`
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:   :py:class:`PceProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProto>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PcePeer.PeerDetailInfos.PeerDetailInfo, self).__init__()

                self.yang_name = "peer-detail-info"
                self.yang_parent_name = "peer-detail-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"detail-pcep-information" : ("detail_pcep_information", PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation)}
                self._child_list_classes = {}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.peer_address_xr = YLeaf(YType.str, "peer-address-xr")

                self.peer_protocol = YLeaf(YType.enumeration, "peer-protocol")

                self.detail_pcep_information = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation()
                self.detail_pcep_information.parent = self
                self._children_name_map["detail_pcep_information"] = "detail-pcep-information"
                self._children_yang_names.add("detail-pcep-information")
                self._segment_path = lambda: "peer-detail-info" + "[peer-address='" + self.peer_address.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer/peer-detail-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo, ['peer_address', 'peer_address_xr', 'peer_protocol'], name, value)


            class DetailPcepInformation(Entity):
                """
                Detailed PCE protocol information
                
                .. attribute:: brief_pcep_information
                
                	Brief PCE protocol information
                	**type**\:   :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation>`
                
                .. attribute:: error
                
                	Error (for display only)
                	**type**\:  str
                
                .. attribute:: keepalives
                
                	Keepalive count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: keychain_enabled
                
                	Keychain based Authentication Enabled
                	**type**\:  bool
                
                .. attribute:: last_error_rx
                
                	Last PCError received
                	**type**\:   :py:class:`LastErrorRx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx>`
                
                .. attribute:: last_error_tx
                
                	Last PCError sent
                	**type**\:   :py:class:`LastErrorTx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx>`
                
                .. attribute:: local_session_id
                
                	Local PCEP session ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: maximum_dead_interval
                
                	Maximum dead interval for the peer
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: md5_enabled
                
                	MD5 Authentication Enabled
                	**type**\:  bool
                
                .. attribute:: minimum_keepalive_interval
                
                	Minimum keepalive interval for the peer
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: negotiated_dead_time
                
                	Negotiated DT
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_local_keepalive
                
                	Negotiated KA
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_remote_keepalive
                
                	Negotiated KA
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_rx
                
                	PCEErr Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_tx
                
                	PCEErr Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_rx
                
                	PCEInit Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_tx
                
                	PCEInit Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_keepalive_rx
                
                	PCE Keepalive Rx
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_keepalive_tx
                
                	PCE Keepalive Tx
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_open_rx
                
                	PCEOpen Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_open_tx
                
                	PCEOpen Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_rx
                
                	PCERep Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_tx
                
                	PCERep Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_rx
                
                	PCERpt Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_tx
                
                	PCERpt Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_rx
                
                	PCEReq Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_tx
                
                	PCEReq Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_rx
                
                	PCEUpd Rx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_tx
                
                	PCEUpd Tx
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pcep_up_time
                
                	PCEP Up Time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_session_id
                
                	Remote PCEP session ID
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: speaker_id
                
                	Speaker Entity ID
                	**type**\:  str
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation, self).__init__()

                    self.yang_name = "detail-pcep-information"
                    self.yang_parent_name = "peer-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"brief-pcep-information" : ("brief_pcep_information", PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation), "last-error-rx" : ("last_error_rx", PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx), "last-error-tx" : ("last_error_tx", PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx)}
                    self._child_list_classes = {}

                    self.error = YLeaf(YType.str, "error")

                    self.keepalives = YLeaf(YType.uint32, "keepalives")

                    self.keychain_enabled = YLeaf(YType.boolean, "keychain-enabled")

                    self.local_session_id = YLeaf(YType.uint8, "local-session-id")

                    self.maximum_dead_interval = YLeaf(YType.uint8, "maximum-dead-interval")

                    self.md5_enabled = YLeaf(YType.boolean, "md5-enabled")

                    self.minimum_keepalive_interval = YLeaf(YType.uint8, "minimum-keepalive-interval")

                    self.negotiated_dead_time = YLeaf(YType.uint32, "negotiated-dead-time")

                    self.negotiated_local_keepalive = YLeaf(YType.uint32, "negotiated-local-keepalive")

                    self.negotiated_remote_keepalive = YLeaf(YType.uint32, "negotiated-remote-keepalive")

                    self.pce_error_rx = YLeaf(YType.uint32, "pce-error-rx")

                    self.pce_error_tx = YLeaf(YType.uint32, "pce-error-tx")

                    self.pce_initiate_rx = YLeaf(YType.uint32, "pce-initiate-rx")

                    self.pce_initiate_tx = YLeaf(YType.uint32, "pce-initiate-tx")

                    self.pce_keepalive_rx = YLeaf(YType.uint64, "pce-keepalive-rx")

                    self.pce_keepalive_tx = YLeaf(YType.uint64, "pce-keepalive-tx")

                    self.pce_open_rx = YLeaf(YType.uint32, "pce-open-rx")

                    self.pce_open_tx = YLeaf(YType.uint32, "pce-open-tx")

                    self.pce_reply_rx = YLeaf(YType.uint32, "pce-reply-rx")

                    self.pce_reply_tx = YLeaf(YType.uint32, "pce-reply-tx")

                    self.pce_report_rx = YLeaf(YType.uint32, "pce-report-rx")

                    self.pce_report_tx = YLeaf(YType.uint32, "pce-report-tx")

                    self.pce_request_rx = YLeaf(YType.uint32, "pce-request-rx")

                    self.pce_request_tx = YLeaf(YType.uint32, "pce-request-tx")

                    self.pce_update_rx = YLeaf(YType.uint32, "pce-update-rx")

                    self.pce_update_tx = YLeaf(YType.uint32, "pce-update-tx")

                    self.pcep_up_time = YLeaf(YType.uint32, "pcep-up-time")

                    self.remote_session_id = YLeaf(YType.uint8, "remote-session-id")

                    self.speaker_id = YLeaf(YType.str, "speaker-id")

                    self.brief_pcep_information = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation()
                    self.brief_pcep_information.parent = self
                    self._children_name_map["brief_pcep_information"] = "brief-pcep-information"
                    self._children_yang_names.add("brief-pcep-information")

                    self.last_error_rx = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx()
                    self.last_error_rx.parent = self
                    self._children_name_map["last_error_rx"] = "last-error-rx"
                    self._children_yang_names.add("last-error-rx")

                    self.last_error_tx = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx()
                    self.last_error_tx.parent = self
                    self._children_name_map["last_error_tx"] = "last-error-tx"
                    self._children_yang_names.add("last-error-tx")
                    self._segment_path = lambda: "detail-pcep-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation, ['error', 'keepalives', 'keychain_enabled', 'local_session_id', 'maximum_dead_interval', 'md5_enabled', 'minimum_keepalive_interval', 'negotiated_dead_time', 'negotiated_local_keepalive', 'negotiated_remote_keepalive', 'pce_error_rx', 'pce_error_tx', 'pce_initiate_rx', 'pce_initiate_tx', 'pce_keepalive_rx', 'pce_keepalive_tx', 'pce_open_rx', 'pce_open_tx', 'pce_reply_rx', 'pce_reply_tx', 'pce_report_rx', 'pce_report_tx', 'pce_request_rx', 'pce_request_tx', 'pce_update_rx', 'pce_update_tx', 'pcep_up_time', 'remote_session_id', 'speaker_id'], name, value)


                class BriefPcepInformation(Entity):
                    """
                    Brief PCE protocol information
                    
                    .. attribute:: capability_db_version
                    
                    	DB version capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_delta_sync
                    
                    	Delta Synchronization capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_instantiate
                    
                    	Instantiation capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_segment_routing
                    
                    	Segment Routing capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_triggered_sync
                    
                    	Triggered Synchronization capability
                    	**type**\:  bool
                    
                    .. attribute:: capability_update
                    
                    	Update capability
                    	**type**\:  bool
                    
                    .. attribute:: pcep_state
                    
                    	PCEP State
                    	**type**\:   :py:class:`PcepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepState>`
                    
                    .. attribute:: stateful
                    
                    	Stateful
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation, self).__init__()

                        self.yang_name = "brief-pcep-information"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.capability_db_version = YLeaf(YType.boolean, "capability-db-version")

                        self.capability_delta_sync = YLeaf(YType.boolean, "capability-delta-sync")

                        self.capability_instantiate = YLeaf(YType.boolean, "capability-instantiate")

                        self.capability_segment_routing = YLeaf(YType.boolean, "capability-segment-routing")

                        self.capability_triggered_sync = YLeaf(YType.boolean, "capability-triggered-sync")

                        self.capability_update = YLeaf(YType.boolean, "capability-update")

                        self.pcep_state = YLeaf(YType.enumeration, "pcep-state")

                        self.stateful = YLeaf(YType.boolean, "stateful")
                        self._segment_path = lambda: "brief-pcep-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation, ['capability_db_version', 'capability_delta_sync', 'capability_instantiate', 'capability_segment_routing', 'capability_triggered_sync', 'capability_update', 'pcep_state', 'stateful'], name, value)


                class LastErrorRx(Entity):
                    """
                    Last PCError received
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx, self).__init__()

                        self.yang_name = "last-error-rx"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.pc_error_type = YLeaf(YType.uint8, "pc-error-type")

                        self.pc_error_value = YLeaf(YType.uint8, "pc-error-value")
                        self._segment_path = lambda: "last-error-rx"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx, ['pc_error_type', 'pc_error_value'], name, value)


                class LastErrorTx(Entity):
                    """
                    Last PCError sent
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx, self).__init__()

                        self.yang_name = "last-error-tx"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.pc_error_type = YLeaf(YType.uint8, "pc-error-type")

                        self.pc_error_value = YLeaf(YType.uint8, "pc-error-value")
                        self._segment_path = lambda: "last-error-tx"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx, ['pc_error_type', 'pc_error_value'], name, value)


    class PeerInfos(Entity):
        """
        Peers database in XTC
        
        .. attribute:: peer_info
        
        	PCE peer information
        	**type**\: list of    :py:class:`PeerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos.PeerInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(PcePeer.PeerInfos, self).__init__()

            self.yang_name = "peer-infos"
            self.yang_parent_name = "pce-peer"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"peer-info" : ("peer_info", PcePeer.PeerInfos.PeerInfo)}

            self.peer_info = YList(self)
            self._segment_path = lambda: "peer-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PcePeer.PeerInfos, [], name, value)


        class PeerInfo(Entity):
            """
            PCE peer information
            
            .. attribute:: peer_address  <key>
            
            	Peer Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: brief_pcep_information
            
            	PCE protocol information
            	**type**\:   :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos.PeerInfo.BriefPcepInformation>`
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:   :py:class:`PceProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProto>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PcePeer.PeerInfos.PeerInfo, self).__init__()

                self.yang_name = "peer-info"
                self.yang_parent_name = "peer-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"brief-pcep-information" : ("brief_pcep_information", PcePeer.PeerInfos.PeerInfo.BriefPcepInformation)}
                self._child_list_classes = {}

                self.peer_address = YLeaf(YType.str, "peer-address")

                self.peer_address_xr = YLeaf(YType.str, "peer-address-xr")

                self.peer_protocol = YLeaf(YType.enumeration, "peer-protocol")

                self.brief_pcep_information = PcePeer.PeerInfos.PeerInfo.BriefPcepInformation()
                self.brief_pcep_information.parent = self
                self._children_name_map["brief_pcep_information"] = "brief-pcep-information"
                self._children_yang_names.add("brief-pcep-information")
                self._segment_path = lambda: "peer-info" + "[peer-address='" + self.peer_address.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer/peer-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PcePeer.PeerInfos.PeerInfo, ['peer_address', 'peer_address_xr', 'peer_protocol'], name, value)


            class BriefPcepInformation(Entity):
                """
                PCE protocol information
                
                .. attribute:: capability_db_version
                
                	DB version capability
                	**type**\:  bool
                
                .. attribute:: capability_delta_sync
                
                	Delta Synchronization capability
                	**type**\:  bool
                
                .. attribute:: capability_instantiate
                
                	Instantiation capability
                	**type**\:  bool
                
                .. attribute:: capability_segment_routing
                
                	Segment Routing capability
                	**type**\:  bool
                
                .. attribute:: capability_triggered_sync
                
                	Triggered Synchronization capability
                	**type**\:  bool
                
                .. attribute:: capability_update
                
                	Update capability
                	**type**\:  bool
                
                .. attribute:: pcep_state
                
                	PCEP State
                	**type**\:   :py:class:`PcepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepState>`
                
                .. attribute:: stateful
                
                	Stateful
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PcePeer.PeerInfos.PeerInfo.BriefPcepInformation, self).__init__()

                    self.yang_name = "brief-pcep-information"
                    self.yang_parent_name = "peer-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.capability_db_version = YLeaf(YType.boolean, "capability-db-version")

                    self.capability_delta_sync = YLeaf(YType.boolean, "capability-delta-sync")

                    self.capability_instantiate = YLeaf(YType.boolean, "capability-instantiate")

                    self.capability_segment_routing = YLeaf(YType.boolean, "capability-segment-routing")

                    self.capability_triggered_sync = YLeaf(YType.boolean, "capability-triggered-sync")

                    self.capability_update = YLeaf(YType.boolean, "capability-update")

                    self.pcep_state = YLeaf(YType.enumeration, "pcep-state")

                    self.stateful = YLeaf(YType.boolean, "stateful")
                    self._segment_path = lambda: "brief-pcep-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(PcePeer.PeerInfos.PeerInfo.BriefPcepInformation, ['capability_db_version', 'capability_delta_sync', 'capability_instantiate', 'capability_segment_routing', 'capability_triggered_sync', 'capability_update', 'pcep_state', 'stateful'], name, value)

    def clone_ptr(self):
        self._top_entity = PcePeer()
        return self._top_entity

class PceTopology(Entity):
    """
    pce topology
    
    .. attribute:: prefix_infos
    
    	Prefixes database in XTC
    	**type**\:   :py:class:`PrefixInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos>`
    
    .. attribute:: topology_nodes
    
    	Node database in XTC
    	**type**\:   :py:class:`TopologyNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes>`
    
    .. attribute:: topology_summary
    
    	Node summary database in XTC
    	**type**\:   :py:class:`TopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologySummary>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2017-06-26'

    def __init__(self):
        super(PceTopology, self).__init__()
        self._top_entity = None

        self.yang_name = "pce-topology"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"prefix-infos" : ("prefix_infos", PceTopology.PrefixInfos), "topology-nodes" : ("topology_nodes", PceTopology.TopologyNodes), "topology-summary" : ("topology_summary", PceTopology.TopologySummary)}
        self._child_list_classes = {}

        self.prefix_infos = PceTopology.PrefixInfos()
        self.prefix_infos.parent = self
        self._children_name_map["prefix_infos"] = "prefix-infos"
        self._children_yang_names.add("prefix-infos")

        self.topology_nodes = PceTopology.TopologyNodes()
        self.topology_nodes.parent = self
        self._children_name_map["topology_nodes"] = "topology-nodes"
        self._children_yang_names.add("topology-nodes")

        self.topology_summary = PceTopology.TopologySummary()
        self.topology_summary.parent = self
        self._children_name_map["topology_summary"] = "topology-summary"
        self._children_yang_names.add("topology-summary")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology"


    class PrefixInfos(Entity):
        """
        Prefixes database in XTC
        
        .. attribute:: prefix_info
        
        	PCE prefix information
        	**type**\: list of    :py:class:`PrefixInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(PceTopology.PrefixInfos, self).__init__()

            self.yang_name = "prefix-infos"
            self.yang_parent_name = "pce-topology"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"prefix-info" : ("prefix_info", PceTopology.PrefixInfos.PrefixInfo)}

            self.prefix_info = YList(self)
            self._segment_path = lambda: "prefix-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PceTopology.PrefixInfos, [], name, value)


        class PrefixInfo(Entity):
            """
            PCE prefix information
            
            .. attribute:: node_identifier  <key>
            
            	Node ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: address
            
            	Prefix address
            	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.Address>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:   :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PceTopology.PrefixInfos.PrefixInfo, self).__init__()

                self.yang_name = "prefix-info"
                self.yang_parent_name = "prefix-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"node-protocol-identifier" : ("node_protocol_identifier", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier)}
                self._child_list_classes = {"address" : ("address", PceTopology.PrefixInfos.PrefixInfo.Address)}

                self.node_identifier = YLeaf(YType.int32, "node-identifier")

                self.node_identifier_xr = YLeaf(YType.uint32, "node-identifier-xr")

                self.node_protocol_identifier = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"
                self._children_yang_names.add("node-protocol-identifier")

                self.address = YList(self)
                self._segment_path = lambda: "prefix-info" + "[node-identifier='" + self.node_identifier.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/prefix-infos/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo, ['node_identifier', 'node_identifier_xr'], name, value)


            class Address(Entity):
                """
                Prefix address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceTopology.PrefixInfos.PrefixInfo.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.ipv4 = YLeaf(YType.str, "ipv4")

                    self.ipv6 = YLeaf(YType.str, "ipv6")
                    self._segment_path = lambda: "address"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.Address, ['af_name', 'ipv4', 'ipv6'], name, value)


            class NodeProtocolIdentifier(Entity):
                """
                Node protocol identifier
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\:  bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\:  bool
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\:  str
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"igp-information" : ("igp_information", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation), "srgb-information" : ("srgb_information", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation)}

                    self.ipv4_bgp_router_id = YLeaf(YType.str, "ipv4-bgp-router-id")

                    self.ipv4_bgp_router_id_set = YLeaf(YType.boolean, "ipv4-bgp-router-id-set")

                    self.ipv4te_router_id = YLeaf(YType.str, "ipv4te-router-id")

                    self.ipv4te_router_id_set = YLeaf(YType.boolean, "ipv4te-router-id-set")

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.igp_information = YList(self)
                    self.srgb_information = YList(self)
                    self._segment_path = lambda: "node-protocol-identifier"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, ['ipv4_bgp_router_id', 'ipv4_bgp_router_id_set', 'ipv4te_router_id', 'ipv4te_router_id_set', 'node_name'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp" : ("igp", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp)}
                        self._child_list_classes = {}

                        self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.igp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "igp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp), "isis" : ("isis", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis), "ospf" : ("ospf", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                class SrgbInformation(Entity):
                    """
                    SRGB information
                    
                    .. attribute:: igp_srgb
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation, self).__init__()

                        self.yang_name = "srgb-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp-srgb" : ("igp_srgb", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb)}
                        self._child_list_classes = {}

                        self.size = YLeaf(YType.uint32, "size")

                        self.start = YLeaf(YType.uint32, "start")

                        self.igp_srgb = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                        self.igp_srgb.parent = self
                        self._children_name_map["igp_srgb"] = "igp-srgb"
                        self._children_yang_names.add("igp-srgb")
                        self._segment_path = lambda: "srgb-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation, ['size', 'start'], name, value)


                    class IgpSrgb(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb, self).__init__()

                            self.yang_name = "igp-srgb"
                            self.yang_parent_name = "srgb-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp), "isis" : ("isis", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis), "ospf" : ("ospf", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp-srgb"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, ['area', 'router_id'], name, value)


    class TopologyNodes(Entity):
        """
        Node database in XTC
        
        .. attribute:: topology_node
        
        	Node information
        	**type**\: list of    :py:class:`TopologyNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(PceTopology.TopologyNodes, self).__init__()

            self.yang_name = "topology-nodes"
            self.yang_parent_name = "pce-topology"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"topology-node" : ("topology_node", PceTopology.TopologyNodes.TopologyNode)}

            self.topology_node = YList(self)
            self._segment_path = lambda: "topology-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PceTopology.TopologyNodes, [], name, value)


        class TopologyNode(Entity):
            """
            Node information
            
            .. attribute:: node_identifier  <key>
            
            	Node Identifier
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ipv4_link
            
            	IPv4 Link information
            	**type**\: list of    :py:class:`Ipv4Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link>`
            
            .. attribute:: ipv6_link
            
            	IPv6 Link information
            	**type**\: list of    :py:class:`Ipv6Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:   :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier>`
            
            .. attribute:: overload
            
            	Node Overload Bit
            	**type**\:  bool
            
            .. attribute:: prefix_sid
            
            	Prefix SIDs
            	**type**\: list of    :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.PrefixSid>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PceTopology.TopologyNodes.TopologyNode, self).__init__()

                self.yang_name = "topology-node"
                self.yang_parent_name = "topology-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"node-protocol-identifier" : ("node_protocol_identifier", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier)}
                self._child_list_classes = {"ipv4-link" : ("ipv4_link", PceTopology.TopologyNodes.TopologyNode.Ipv4Link), "ipv6-link" : ("ipv6_link", PceTopology.TopologyNodes.TopologyNode.Ipv6Link), "prefix-sid" : ("prefix_sid", PceTopology.TopologyNodes.TopologyNode.PrefixSid)}

                self.node_identifier = YLeaf(YType.int32, "node-identifier")

                self.node_identifier_xr = YLeaf(YType.uint32, "node-identifier-xr")

                self.overload = YLeaf(YType.boolean, "overload")

                self.node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"
                self._children_yang_names.add("node-protocol-identifier")

                self.ipv4_link = YList(self)
                self.ipv6_link = YList(self)
                self.prefix_sid = YList(self)
                self._segment_path = lambda: "topology-node" + "[node-identifier='" + self.node_identifier.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/topology-nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode, ['node_identifier', 'node_identifier_xr', 'overload'], name, value)


            class Ipv4Link(Entity):
                """
                IPv4 Link information
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of    :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid>`
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:   :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation>`
                
                .. attribute:: local_ipv4_address
                
                	Local IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_ipv4_address
                
                	Remote IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:   :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: srlgs
                
                	SRLG Values
                	**type**\:  list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link, self).__init__()

                    self.yang_name = "ipv4-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"local-igp-information" : ("local_igp_information", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation), "remote-node-protocol-identifier" : ("remote_node_protocol_identifier", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier)}
                    self._child_list_classes = {"adjacency-sid" : ("adjacency_sid", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid)}

                    self.igp_metric = YLeaf(YType.uint32, "igp-metric")

                    self.local_ipv4_address = YLeaf(YType.str, "local-ipv4-address")

                    self.max_reservable_bandwidth = YLeaf(YType.uint64, "max-reservable-bandwidth")

                    self.maximum_link_bandwidth = YLeaf(YType.uint64, "maximum-link-bandwidth")

                    self.remote_ipv4_address = YLeaf(YType.str, "remote-ipv4-address")

                    self.srlgs = YLeafList(YType.uint32, "srlgs")

                    self.te_metric = YLeaf(YType.uint32, "te-metric")

                    self.local_igp_information = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"
                    self._children_yang_names.add("local-igp-information")

                    self.remote_node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"
                    self._children_yang_names.add("remote-node-protocol-identifier")

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv4-link"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link, ['igp_metric', 'local_ipv4_address', 'max_reservable_bandwidth', 'maximum_link_bandwidth', 'remote_ipv4_address', 'srlgs', 'te_metric'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\:  bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\:  bool
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\:  bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\:  bool
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\:  bool
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:   :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sid-prefix" : ("sid_prefix", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix)}
                        self._child_list_classes = {}

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.eflag = YLeaf(YType.boolean, "eflag")

                        self.lflag = YLeaf(YType.boolean, "lflag")

                        self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                        self.nflag = YLeaf(YType.boolean, "nflag")

                        self.pflag = YLeaf(YType.boolean, "pflag")

                        self.rflag = YLeaf(YType.boolean, "rflag")

                        self.sid_type = YLeaf(YType.enumeration, "sid-type")

                        self.vflag = YLeaf(YType.boolean, "vflag")

                        self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._children_yang_names.add("sid-prefix")
                        self._segment_path = lambda: "adjacency-sid"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, ['domain_identifier', 'eflag', 'lflag', 'mpls_label', 'nflag', 'pflag', 'rflag', 'sid_type', 'vflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "sid-prefix"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp" : ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp)}
                        self._child_list_classes = {}

                        self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "local-igp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp), "isis" : ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis), "ospf" : ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                class RemoteNodeProtocolIdentifier(Entity):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\:  str
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"igp-information" : ("igp_information", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation), "srgb-information" : ("srgb_information", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation)}

                        self.ipv4_bgp_router_id = YLeaf(YType.str, "ipv4-bgp-router-id")

                        self.ipv4_bgp_router_id_set = YLeaf(YType.boolean, "ipv4-bgp-router-id-set")

                        self.ipv4te_router_id = YLeaf(YType.str, "ipv4te-router-id")

                        self.ipv4te_router_id_set = YLeaf(YType.boolean, "ipv4te-router-id-set")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.igp_information = YList(self)
                        self.srgb_information = YList(self)
                        self._segment_path = lambda: "remote-node-protocol-identifier"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, ['ipv4_bgp_router_id', 'ipv4_bgp_router_id_set', 'ipv4te_router_id', 'ipv4te_router_id_set', 'node_name'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"igp" : ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp)}
                            self._child_list_classes = {}

                            self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                            self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                            self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._children_yang_names.add("igp")
                            self._segment_path = lambda: "igp-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp" : ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp), "isis" : ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis), "ospf" : ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf)}
                                self._child_list_classes = {}

                                self.igp_id = YLeaf(YType.enumeration, "igp-id")

                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._children_yang_names.add("bgp")

                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"
                                self._children_yang_names.add("isis")

                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"
                                self._children_yang_names.add("ospf")
                                self._segment_path = lambda: "igp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "bgp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.system_id = YLeaf(YType.str, "system-id")
                                    self._segment_path = lambda: "isis"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area = YLeaf(YType.uint32, "area")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "ospf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                    class SrgbInformation(Entity):
                        """
                        SRGB information
                        
                        .. attribute:: igp_srgb
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation, self).__init__()

                            self.yang_name = "srgb-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"igp-srgb" : ("igp_srgb", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb)}
                            self._child_list_classes = {}

                            self.size = YLeaf(YType.uint32, "size")

                            self.start = YLeaf(YType.uint32, "start")

                            self.igp_srgb = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                            self.igp_srgb.parent = self
                            self._children_name_map["igp_srgb"] = "igp-srgb"
                            self._children_yang_names.add("igp-srgb")
                            self._segment_path = lambda: "srgb-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation, ['size', 'start'], name, value)


                        class IgpSrgb(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb, self).__init__()

                                self.yang_name = "igp-srgb"
                                self.yang_parent_name = "srgb-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp" : ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp), "isis" : ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis), "ospf" : ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf)}
                                self._child_list_classes = {}

                                self.igp_id = YLeaf(YType.enumeration, "igp-id")

                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._children_yang_names.add("bgp")

                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"
                                self._children_yang_names.add("isis")

                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"
                                self._children_yang_names.add("ospf")
                                self._segment_path = lambda: "igp-srgb"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb, ['igp_id'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "bgp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, ['confed_asn', 'router_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.system_id = YLeaf(YType.str, "system-id")
                                    self._segment_path = lambda: "isis"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, ['level', 'system_id'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area = YLeaf(YType.uint32, "area")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "ospf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, ['area', 'router_id'], name, value)


            class Ipv6Link(Entity):
                """
                IPv6 Link information
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of    :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid>`
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:   :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation>`
                
                .. attribute:: local_ipv6_address
                
                	Local IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_ipv6_address
                
                	Remote IPv6 address
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:   :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link, self).__init__()

                    self.yang_name = "ipv6-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"local-igp-information" : ("local_igp_information", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation), "remote-node-protocol-identifier" : ("remote_node_protocol_identifier", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier)}
                    self._child_list_classes = {"adjacency-sid" : ("adjacency_sid", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid)}

                    self.igp_metric = YLeaf(YType.uint32, "igp-metric")

                    self.local_ipv6_address = YLeaf(YType.str, "local-ipv6-address")

                    self.max_reservable_bandwidth = YLeaf(YType.uint64, "max-reservable-bandwidth")

                    self.maximum_link_bandwidth = YLeaf(YType.uint64, "maximum-link-bandwidth")

                    self.remote_ipv6_address = YLeaf(YType.str, "remote-ipv6-address")

                    self.te_metric = YLeaf(YType.uint32, "te-metric")

                    self.local_igp_information = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"
                    self._children_yang_names.add("local-igp-information")

                    self.remote_node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"
                    self._children_yang_names.add("remote-node-protocol-identifier")

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv6-link"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link, ['igp_metric', 'local_ipv6_address', 'max_reservable_bandwidth', 'maximum_link_bandwidth', 'remote_ipv6_address', 'te_metric'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\:  bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\:  bool
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\:  bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\:  bool
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\:  bool
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:   :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sid-prefix" : ("sid_prefix", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix)}
                        self._child_list_classes = {}

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.eflag = YLeaf(YType.boolean, "eflag")

                        self.lflag = YLeaf(YType.boolean, "lflag")

                        self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                        self.nflag = YLeaf(YType.boolean, "nflag")

                        self.pflag = YLeaf(YType.boolean, "pflag")

                        self.rflag = YLeaf(YType.boolean, "rflag")

                        self.sid_type = YLeaf(YType.enumeration, "sid-type")

                        self.vflag = YLeaf(YType.boolean, "vflag")

                        self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._children_yang_names.add("sid-prefix")
                        self._segment_path = lambda: "adjacency-sid"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, ['domain_identifier', 'eflag', 'lflag', 'mpls_label', 'nflag', 'pflag', 'rflag', 'sid_type', 'vflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")
                            self._segment_path = lambda: "sid-prefix"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp" : ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp)}
                        self._child_list_classes = {}

                        self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "local-igp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp), "isis" : ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis), "ospf" : ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                class RemoteNodeProtocolIdentifier(Entity):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\:  bool
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\:  str
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"igp-information" : ("igp_information", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation), "srgb-information" : ("srgb_information", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation)}

                        self.ipv4_bgp_router_id = YLeaf(YType.str, "ipv4-bgp-router-id")

                        self.ipv4_bgp_router_id_set = YLeaf(YType.boolean, "ipv4-bgp-router-id-set")

                        self.ipv4te_router_id = YLeaf(YType.str, "ipv4te-router-id")

                        self.ipv4te_router_id_set = YLeaf(YType.boolean, "ipv4te-router-id-set")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.igp_information = YList(self)
                        self.srgb_information = YList(self)
                        self._segment_path = lambda: "remote-node-protocol-identifier"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, ['ipv4_bgp_router_id', 'ipv4_bgp_router_id_set', 'ipv4te_router_id', 'ipv4te_router_id_set', 'node_name'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"igp" : ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp)}
                            self._child_list_classes = {}

                            self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                            self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                            self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._children_yang_names.add("igp")
                            self._segment_path = lambda: "igp-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp" : ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp), "isis" : ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis), "ospf" : ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf)}
                                self._child_list_classes = {}

                                self.igp_id = YLeaf(YType.enumeration, "igp-id")

                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._children_yang_names.add("bgp")

                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"
                                self._children_yang_names.add("isis")

                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"
                                self._children_yang_names.add("ospf")
                                self._segment_path = lambda: "igp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "bgp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.system_id = YLeaf(YType.str, "system-id")
                                    self._segment_path = lambda: "isis"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area = YLeaf(YType.uint32, "area")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "ospf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                    class SrgbInformation(Entity):
                        """
                        SRGB information
                        
                        .. attribute:: igp_srgb
                        
                        	IGP\-specific information
                        	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation, self).__init__()

                            self.yang_name = "srgb-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"igp-srgb" : ("igp_srgb", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb)}
                            self._child_list_classes = {}

                            self.size = YLeaf(YType.uint32, "size")

                            self.start = YLeaf(YType.uint32, "start")

                            self.igp_srgb = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                            self.igp_srgb.parent = self
                            self._children_name_map["igp_srgb"] = "igp-srgb"
                            self._children_yang_names.add("igp-srgb")
                            self._segment_path = lambda: "srgb-information"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation, ['size', 'start'], name, value)


                        class IgpSrgb(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb, self).__init__()

                                self.yang_name = "igp-srgb"
                                self.yang_parent_name = "srgb-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp" : ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp), "isis" : ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis), "ospf" : ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf)}
                                self._child_list_classes = {}

                                self.igp_id = YLeaf(YType.enumeration, "igp-id")

                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._children_yang_names.add("bgp")

                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"
                                self._children_yang_names.add("isis")

                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"
                                self._children_yang_names.add("ospf")
                                self._segment_path = lambda: "igp-srgb"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb, ['igp_id'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "bgp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, ['confed_asn', 'router_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.system_id = YLeaf(YType.str, "system-id")
                                    self._segment_path = lambda: "isis"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, ['level', 'system_id'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-06-26'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp-srgb"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.area = YLeaf(YType.uint32, "area")

                                    self.router_id = YLeaf(YType.str, "router-id")
                                    self._segment_path = lambda: "ospf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, ['area', 'router_id'], name, value)


            class NodeProtocolIdentifier(Entity):
                """
                Node protocol identifier
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of    :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\:  bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\:  bool
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\:  str
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of    :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"igp-information" : ("igp_information", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation), "srgb-information" : ("srgb_information", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation)}

                    self.ipv4_bgp_router_id = YLeaf(YType.str, "ipv4-bgp-router-id")

                    self.ipv4_bgp_router_id_set = YLeaf(YType.boolean, "ipv4-bgp-router-id-set")

                    self.ipv4te_router_id = YLeaf(YType.str, "ipv4te-router-id")

                    self.ipv4te_router_id_set = YLeaf(YType.boolean, "ipv4te-router-id-set")

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.igp_information = YList(self)
                    self.srgb_information = YList(self)
                    self._segment_path = lambda: "node-protocol-identifier"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier, ['ipv4_bgp_router_id', 'ipv4_bgp_router_id_set', 'ipv4te_router_id', 'ipv4te_router_id_set', 'node_name'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp" : ("igp", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp)}
                        self._child_list_classes = {}

                        self.autonomous_system_number = YLeaf(YType.uint32, "autonomous-system-number")

                        self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                        self.igp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")
                        self._segment_path = lambda: "igp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, ['autonomous_system_number', 'domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp), "isis" : ("isis", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis), "ospf" : ("ospf", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['area', 'router_id'], name, value)


                class SrgbInformation(Entity):
                    """
                    SRGB information
                    
                    .. attribute:: igp_srgb
                    
                    	IGP\-specific information
                    	**type**\:   :py:class:`IgpSrgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb>`
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation, self).__init__()

                        self.yang_name = "srgb-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"igp-srgb" : ("igp_srgb", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb)}
                        self._child_list_classes = {}

                        self.size = YLeaf(YType.uint32, "size")

                        self.start = YLeaf(YType.uint32, "start")

                        self.igp_srgb = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb()
                        self.igp_srgb.parent = self
                        self._children_name_map["igp_srgb"] = "igp-srgb"
                        self._children_yang_names.add("igp-srgb")
                        self._segment_path = lambda: "srgb-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation, ['size', 'start'], name, value)


                    class IgpSrgb(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:   :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:   :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-06-26'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb, self).__init__()

                            self.yang_name = "igp-srgb"
                            self.yang_parent_name = "srgb-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bgp" : ("bgp", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp), "isis" : ("isis", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis), "ospf" : ("ospf", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf)}
                            self._child_list_classes = {}

                            self.igp_id = YLeaf(YType.enumeration, "igp-id")

                            self.bgp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._children_yang_names.add("bgp")

                            self.isis = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"
                            self._children_yang_names.add("isis")

                            self.ospf = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"
                            self._children_yang_names.add("ospf")
                            self._segment_path = lambda: "igp-srgb"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb, ['igp_id'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.confed_asn = YLeaf(YType.uint32, "confed-asn")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "bgp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Bgp, ['confed_asn', 'router_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.uint32, "level")

                                self.system_id = YLeaf(YType.str, "system-id")
                                self._segment_path = lambda: "isis"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Isis, ['level', 'system_id'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-06-26'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp-srgb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.area = YLeaf(YType.uint32, "area")

                                self.router_id = YLeaf(YType.str, "router-id")
                                self._segment_path = lambda: "ospf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.IgpSrgb.Ospf, ['area', 'router_id'], name, value)


            class PrefixSid(Entity):
                """
                Prefix SIDs
                
                .. attribute:: domain_identifier
                
                	Domain identifier
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: eflag
                
                	E Flag
                	**type**\:  bool
                
                .. attribute:: lflag
                
                	L Flag
                	**type**\:  bool
                
                .. attribute:: mpls_label
                
                	MPLS Label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nflag
                
                	N Flag
                	**type**\:  bool
                
                .. attribute:: pflag
                
                	P Flag
                	**type**\:  bool
                
                .. attribute:: rflag
                
                	R Flag
                	**type**\:  bool
                
                .. attribute:: sid_prefix
                
                	Prefix
                	**type**\:   :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix>`
                
                .. attribute:: sid_type
                
                	SID Type
                	**type**\:   :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                
                .. attribute:: vflag
                
                	V Flag
                	**type**\:  bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-06-26'

                def __init__(self):
                    super(PceTopology.TopologyNodes.TopologyNode.PrefixSid, self).__init__()

                    self.yang_name = "prefix-sid"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"sid-prefix" : ("sid_prefix", PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix)}
                    self._child_list_classes = {}

                    self.domain_identifier = YLeaf(YType.uint64, "domain-identifier")

                    self.eflag = YLeaf(YType.boolean, "eflag")

                    self.lflag = YLeaf(YType.boolean, "lflag")

                    self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                    self.nflag = YLeaf(YType.boolean, "nflag")

                    self.pflag = YLeaf(YType.boolean, "pflag")

                    self.rflag = YLeaf(YType.boolean, "rflag")

                    self.sid_type = YLeaf(YType.enumeration, "sid-type")

                    self.vflag = YLeaf(YType.boolean, "vflag")

                    self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix()
                    self.sid_prefix.parent = self
                    self._children_name_map["sid_prefix"] = "sid-prefix"
                    self._children_yang_names.add("sid-prefix")
                    self._segment_path = lambda: "prefix-sid"

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.PrefixSid, ['domain_identifier', 'eflag', 'lflag', 'mpls_label', 'nflag', 'pflag', 'rflag', 'sid_type', 'vflag'], name, value)


                class SidPrefix(Entity):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:   :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-06-26'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix, self).__init__()

                        self.yang_name = "sid-prefix"
                        self.yang_parent_name = "prefix-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.ipv4 = YLeaf(YType.str, "ipv4")

                        self.ipv6 = YLeaf(YType.str, "ipv6")
                        self._segment_path = lambda: "sid-prefix"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.PrefixSid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


    class TopologySummary(Entity):
        """
        Node summary database in XTC
        
        .. attribute:: adjacency_sids
        
        	Number of total adjacency SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: epe_links
        
        	Number of EPE links
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: epesids
        
        	Number of total EPE SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: links
        
        	Number of links
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: lookup_nodes
        
        	Number of lookup nodes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: nodes
        
        	Number of PCE nodes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefix_sids
        
        	Number of total prefix SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefixes
        
        	Number of prefixes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: protected_adjacency_sids
        
        	Number of protected adjacency SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: regular_prefix_sids
        
        	Number of reguar prefix SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: stats_topology_update
        
        	Statistics on topology update
        	**type**\:   :py:class:`StatsTopologyUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologySummary.StatsTopologyUpdate>`
        
        .. attribute:: strict_prefix_sids
        
        	Number of strict prefix SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: topology_consistent
        
        	True if topology is consistent
        	**type**\:  bool
        
        .. attribute:: un_protected_adjacency_sids
        
        	Number of unprotected adjacency SIDs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-06-26'

        def __init__(self):
            super(PceTopology.TopologySummary, self).__init__()

            self.yang_name = "topology-summary"
            self.yang_parent_name = "pce-topology"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"stats-topology-update" : ("stats_topology_update", PceTopology.TopologySummary.StatsTopologyUpdate)}
            self._child_list_classes = {}

            self.adjacency_sids = YLeaf(YType.uint32, "adjacency-sids")

            self.epe_links = YLeaf(YType.uint32, "epe-links")

            self.epesids = YLeaf(YType.uint32, "epesids")

            self.links = YLeaf(YType.uint32, "links")

            self.lookup_nodes = YLeaf(YType.uint32, "lookup-nodes")

            self.nodes = YLeaf(YType.uint32, "nodes")

            self.prefix_sids = YLeaf(YType.uint32, "prefix-sids")

            self.prefixes = YLeaf(YType.uint32, "prefixes")

            self.protected_adjacency_sids = YLeaf(YType.uint32, "protected-adjacency-sids")

            self.regular_prefix_sids = YLeaf(YType.uint32, "regular-prefix-sids")

            self.strict_prefix_sids = YLeaf(YType.uint32, "strict-prefix-sids")

            self.topology_consistent = YLeaf(YType.boolean, "topology-consistent")

            self.un_protected_adjacency_sids = YLeaf(YType.uint32, "un-protected-adjacency-sids")

            self.stats_topology_update = PceTopology.TopologySummary.StatsTopologyUpdate()
            self.stats_topology_update.parent = self
            self._children_name_map["stats_topology_update"] = "stats-topology-update"
            self._children_yang_names.add("stats-topology-update")
            self._segment_path = lambda: "topology-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PceTopology.TopologySummary, ['adjacency_sids', 'epe_links', 'epesids', 'links', 'lookup_nodes', 'nodes', 'prefix_sids', 'prefixes', 'protected_adjacency_sids', 'regular_prefix_sids', 'strict_prefix_sids', 'topology_consistent', 'un_protected_adjacency_sids'], name, value)


        class StatsTopologyUpdate(Entity):
            """
            Statistics on topology update
            
            .. attribute:: num_links_added
            
            	Number of links added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_links_deleted
            
            	Number of links deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_added
            
            	Number of nodes added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_deleted
            
            	Number of nodes deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_added
            
            	Number of prefixes added
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_deleted
            
            	Number of prefixes deleted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-06-26'

            def __init__(self):
                super(PceTopology.TopologySummary.StatsTopologyUpdate, self).__init__()

                self.yang_name = "stats-topology-update"
                self.yang_parent_name = "topology-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.num_links_added = YLeaf(YType.uint32, "num-links-added")

                self.num_links_deleted = YLeaf(YType.uint32, "num-links-deleted")

                self.num_nodes_added = YLeaf(YType.uint32, "num-nodes-added")

                self.num_nodes_deleted = YLeaf(YType.uint32, "num-nodes-deleted")

                self.num_prefixes_added = YLeaf(YType.uint32, "num-prefixes-added")

                self.num_prefixes_deleted = YLeaf(YType.uint32, "num-prefixes-deleted")
                self._segment_path = lambda: "stats-topology-update"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/topology-summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PceTopology.TopologySummary.StatsTopologyUpdate, ['num_links_added', 'num_links_deleted', 'num_nodes_added', 'num_nodes_deleted', 'num_prefixes_added', 'num_prefixes_deleted'], name, value)

    def clone_ptr(self):
        self._top_entity = PceTopology()
        return self._top_entity

