""" Cisco_IOS_XR_infra_xtc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc package operational data.

This module contains definitions
for the following management objects\:
  pce\-lsp\-data\: PCE LSP's data
  pce\-peer\: pce peer
  pce\-topology\: pce topology
  pce\: pce

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LspSetup(Enum):
    """
    LspSetup (Enum Class)

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
    LspState (Enum Class)

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
    PceAfId (Enum Class)

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
    PceAsso (Enum Class)

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
    PceCspfRc (Enum Class)

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
    PceHeadendSwap (Enum Class)

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
    PceIgpInfoId (Enum Class)

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
    PceProto (Enum Class)

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
    PceRro (Enum Class)

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
    PceSrSid (Enum Class)

    PCE SR SID type

    .. data:: ipv4_node_sid = 0

    	IPv4 Node SID

    .. data:: ipv4_adjacency_sid = 1

    	IPv4 Adjacency SID

    .. data:: ipv6_node_sid = 2

    	IPv6 Node SID

    .. data:: ipv6_adjacency_sid = 3

    	IPv6 Adjacency SID

    .. data:: unknown_sid = 4

    	Unknown SID

    """

    ipv4_node_sid = Enum.YLeaf(0, "ipv4-node-sid")

    ipv4_adjacency_sid = Enum.YLeaf(1, "ipv4-adjacency-sid")

    ipv6_node_sid = Enum.YLeaf(2, "ipv6-node-sid")

    ipv6_adjacency_sid = Enum.YLeaf(3, "ipv6-adjacency-sid")

    unknown_sid = Enum.YLeaf(4, "unknown-sid")


class PcepLspState(Enum):
    """
    PcepLspState (Enum Class)

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
    PcepState (Enum Class)

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
    Sid (Enum Class)

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



class PceLspData(Entity):
    """
    PCE LSP's data
    
    .. attribute:: tunnel_infos
    
    	Tunnel database in XTC
    	**type**\:  :py:class:`TunnelInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos>`
    
    .. attribute:: lsp_summary
    
    	LSP summary database in XTC
    	**type**\:  :py:class:`LspSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary>`
    
    .. attribute:: tunnel_detail_infos
    
    	Detailed tunnel database in XTC
    	**type**\:  :py:class:`TunnelDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(PceLspData, self).__init__()
        self._top_entity = None

        self.yang_name = "pce-lsp-data"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("tunnel-infos", ("tunnel_infos", PceLspData.TunnelInfos)), ("lsp-summary", ("lsp_summary", PceLspData.LspSummary)), ("tunnel-detail-infos", ("tunnel_detail_infos", PceLspData.TunnelDetailInfos))])
        self._leafs = OrderedDict()

        self.tunnel_infos = PceLspData.TunnelInfos()
        self.tunnel_infos.parent = self
        self._children_name_map["tunnel_infos"] = "tunnel-infos"

        self.lsp_summary = PceLspData.LspSummary()
        self.lsp_summary.parent = self
        self._children_name_map["lsp_summary"] = "lsp-summary"

        self.tunnel_detail_infos = PceLspData.TunnelDetailInfos()
        self.tunnel_detail_infos.parent = self
        self._children_name_map["tunnel_detail_infos"] = "tunnel-detail-infos"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PceLspData, [], name, value)


    class TunnelInfos(Entity):
        """
        Tunnel database in XTC
        
        .. attribute:: tunnel_info
        
        	Tunnel information
        	**type**\: list of  		 :py:class:`TunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PceLspData.TunnelInfos, self).__init__()

            self.yang_name = "tunnel-infos"
            self.yang_parent_name = "pce-lsp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel-info", ("tunnel_info", PceLspData.TunnelInfos.TunnelInfo))])
            self._leafs = OrderedDict()

            self.tunnel_info = YList(self)
            self._segment_path = lambda: "tunnel-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PceLspData.TunnelInfos, [], name, value)


        class TunnelInfo(Entity):
            """
            Tunnel information
            
            .. attribute:: peer_address  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: plsp_id  (key)
            
            	PCEP LSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tunnel_name  (key)
            
            	Tunnel name
            	**type**\: str
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo.PccAddress>`
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\: str
            
            .. attribute:: brief_lsp_information
            
            	Brief LSP information
            	**type**\: list of  		 :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PceLspData.TunnelInfos.TunnelInfo, self).__init__()

                self.yang_name = "tunnel-info"
                self.yang_parent_name = "tunnel-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_address','plsp_id','tunnel_name']
                self._child_classes = OrderedDict([("pcc-address", ("pcc_address", PceLspData.TunnelInfos.TunnelInfo.PccAddress)), ("brief-lsp-information", ("brief_lsp_information", PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation))])
                self._leafs = OrderedDict([
                    ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str','str'])),
                    ('plsp_id', (YLeaf(YType.uint32, 'plsp-id'), ['int'])),
                    ('tunnel_name', (YLeaf(YType.str, 'tunnel-name'), ['str'])),
                    ('tunnel_name_xr', (YLeaf(YType.str, 'tunnel-name-xr'), ['str'])),
                ])
                self.peer_address = None
                self.plsp_id = None
                self.tunnel_name = None
                self.tunnel_name_xr = None

                self.pcc_address = PceLspData.TunnelInfos.TunnelInfo.PccAddress()
                self.pcc_address.parent = self
                self._children_name_map["pcc_address"] = "pcc-address"

                self.brief_lsp_information = YList(self)
                self._segment_path = lambda: "tunnel-info" + "[peer-address='" + str(self.peer_address) + "']" + "[plsp-id='" + str(self.plsp_id) + "']" + "[tunnel-name='" + str(self.tunnel_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/tunnel-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PceLspData.TunnelInfos.TunnelInfo, ['peer_address', 'plsp_id', 'tunnel_name', u'tunnel_name_xr'], name, value)


            class PccAddress(Entity):
                """
                PCC address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceLspData.TunnelInfos.TunnelInfo.PccAddress, self).__init__()

                    self.yang_name = "pcc-address"
                    self.yang_parent_name = "tunnel-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "pcc-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.TunnelInfos.TunnelInfo.PccAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class BriefLspInformation(Entity):
                """
                Brief LSP information
                
                .. attribute:: source_address
                
                	Source address
                	**type**\:  :py:class:`SourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress>`
                
                .. attribute:: destination_address
                
                	Destination address
                	**type**\:  :py:class:`DestinationAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress>`
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: binding_sid
                
                	Binding SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsp_setup_type
                
                	LSP Setup Type
                	**type**\:  :py:class:`LspSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetup>`
                
                .. attribute:: operational_state
                
                	Operational state
                	**type**\:  :py:class:`PcepLspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspState>`
                
                .. attribute:: administrative_state
                
                	Admin state
                	**type**\:  :py:class:`LspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspState>`
                
                .. attribute:: msd
                
                	Maximum SID Depth
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation, self).__init__()

                    self.yang_name = "brief-lsp-information"
                    self.yang_parent_name = "tunnel-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("source-address", ("source_address", PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress)), ("destination-address", ("destination_address", PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress))])
                    self._leafs = OrderedDict([
                        ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                        ('lspid', (YLeaf(YType.uint32, 'lspid'), ['int'])),
                        ('binding_sid', (YLeaf(YType.uint32, 'binding-sid'), ['int'])),
                        ('lsp_setup_type', (YLeaf(YType.enumeration, 'lsp-setup-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspSetup', '')])),
                        ('operational_state', (YLeaf(YType.enumeration, 'operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepLspState', '')])),
                        ('administrative_state', (YLeaf(YType.enumeration, 'administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspState', '')])),
                        ('msd', (YLeaf(YType.uint32, 'msd'), ['int'])),
                    ])
                    self.tunnel_id = None
                    self.lspid = None
                    self.binding_sid = None
                    self.lsp_setup_type = None
                    self.operational_state = None
                    self.administrative_state = None
                    self.msd = None

                    self.source_address = PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress()
                    self.source_address.parent = self
                    self._children_name_map["source_address"] = "source-address"

                    self.destination_address = PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress()
                    self.destination_address.parent = self
                    self._children_name_map["destination_address"] = "destination-address"
                    self._segment_path = lambda: "brief-lsp-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation, [u'tunnel_id', u'lspid', u'binding_sid', u'lsp_setup_type', u'operational_state', u'administrative_state', u'msd'], name, value)


                class SourceAddress(Entity):
                    """
                    Source address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress, self).__init__()

                        self.yang_name = "source-address"
                        self.yang_parent_name = "brief-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "source-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class DestinationAddress(Entity):
                    """
                    Destination address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress, self).__init__()

                        self.yang_name = "destination-address"
                        self.yang_parent_name = "brief-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "destination-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


    class LspSummary(Entity):
        """
        LSP summary database in XTC
        
        .. attribute:: all_ls_ps
        
        	Summary for all peers
        	**type**\:  :py:class:`AllLsPs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.AllLsPs>`
        
        .. attribute:: peer_ls_ps_info
        
        	Number of LSPs for specific peer
        	**type**\: list of  		 :py:class:`PeerLsPsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.PeerLsPsInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PceLspData.LspSummary, self).__init__()

            self.yang_name = "lsp-summary"
            self.yang_parent_name = "pce-lsp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("all-ls-ps", ("all_ls_ps", PceLspData.LspSummary.AllLsPs)), ("peer-ls-ps-info", ("peer_ls_ps_info", PceLspData.LspSummary.PeerLsPsInfo))])
            self._leafs = OrderedDict()

            self.all_ls_ps = PceLspData.LspSummary.AllLsPs()
            self.all_ls_ps.parent = self
            self._children_name_map["all_ls_ps"] = "all-ls-ps"

            self.peer_ls_ps_info = YList(self)
            self._segment_path = lambda: "lsp-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PceLspData.LspSummary, [], name, value)


        class AllLsPs(Entity):
            """
            Summary for all peers
            
            .. attribute:: all_ls_ps
            
            	Number of all LSPs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_ls_ps
            
            	Number of operational LSPs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: admin_up_ls_ps
            
            	Number of administratively up LSPs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sr_ls_ps
            
            	Number of LSPs with Segment routing setup type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvp_ls_ps
            
            	Number of LSPs with RSVP setup type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PceLspData.LspSummary.AllLsPs, self).__init__()

                self.yang_name = "all-ls-ps"
                self.yang_parent_name = "lsp-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('all_ls_ps', (YLeaf(YType.uint32, 'all-ls-ps'), ['int'])),
                    ('up_ls_ps', (YLeaf(YType.uint32, 'up-ls-ps'), ['int'])),
                    ('admin_up_ls_ps', (YLeaf(YType.uint32, 'admin-up-ls-ps'), ['int'])),
                    ('sr_ls_ps', (YLeaf(YType.uint32, 'sr-ls-ps'), ['int'])),
                    ('rsvp_ls_ps', (YLeaf(YType.uint32, 'rsvp-ls-ps'), ['int'])),
                ])
                self.all_ls_ps = None
                self.up_ls_ps = None
                self.admin_up_ls_ps = None
                self.sr_ls_ps = None
                self.rsvp_ls_ps = None
                self._segment_path = lambda: "all-ls-ps"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/lsp-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PceLspData.LspSummary.AllLsPs, [u'all_ls_ps', u'up_ls_ps', u'admin_up_ls_ps', u'sr_ls_ps', u'rsvp_ls_ps'], name, value)


        class PeerLsPsInfo(Entity):
            """
            Number of LSPs for specific peer
            
            .. attribute:: lsp_summary
            
            	Number of LSPs for specific peer
            	**type**\:  :py:class:`LspSummary_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.PeerLsPsInfo.LspSummary_>`
            
            .. attribute:: peer_address
            
            	Peer address
            	**type**\:  :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.LspSummary.PeerLsPsInfo.PeerAddress>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PceLspData.LspSummary.PeerLsPsInfo, self).__init__()

                self.yang_name = "peer-ls-ps-info"
                self.yang_parent_name = "lsp-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("lsp-summary", ("lsp_summary", PceLspData.LspSummary.PeerLsPsInfo.LspSummary_)), ("peer-address", ("peer_address", PceLspData.LspSummary.PeerLsPsInfo.PeerAddress))])
                self._leafs = OrderedDict()

                self.lsp_summary = PceLspData.LspSummary.PeerLsPsInfo.LspSummary_()
                self.lsp_summary.parent = self
                self._children_name_map["lsp_summary"] = "lsp-summary"

                self.peer_address = PceLspData.LspSummary.PeerLsPsInfo.PeerAddress()
                self.peer_address.parent = self
                self._children_name_map["peer_address"] = "peer-address"
                self._segment_path = lambda: "peer-ls-ps-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/lsp-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PceLspData.LspSummary.PeerLsPsInfo, [], name, value)


            class LspSummary_(Entity):
                """
                Number of LSPs for specific peer
                
                .. attribute:: all_ls_ps
                
                	Number of all LSPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_ls_ps
                
                	Number of operational LSPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: admin_up_ls_ps
                
                	Number of administratively up LSPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sr_ls_ps
                
                	Number of LSPs with Segment routing setup type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rsvp_ls_ps
                
                	Number of LSPs with RSVP setup type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceLspData.LspSummary.PeerLsPsInfo.LspSummary_, self).__init__()

                    self.yang_name = "lsp-summary"
                    self.yang_parent_name = "peer-ls-ps-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('all_ls_ps', (YLeaf(YType.uint32, 'all-ls-ps'), ['int'])),
                        ('up_ls_ps', (YLeaf(YType.uint32, 'up-ls-ps'), ['int'])),
                        ('admin_up_ls_ps', (YLeaf(YType.uint32, 'admin-up-ls-ps'), ['int'])),
                        ('sr_ls_ps', (YLeaf(YType.uint32, 'sr-ls-ps'), ['int'])),
                        ('rsvp_ls_ps', (YLeaf(YType.uint32, 'rsvp-ls-ps'), ['int'])),
                    ])
                    self.all_ls_ps = None
                    self.up_ls_ps = None
                    self.admin_up_ls_ps = None
                    self.sr_ls_ps = None
                    self.rsvp_ls_ps = None
                    self._segment_path = lambda: "lsp-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/lsp-summary/peer-ls-ps-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.LspSummary.PeerLsPsInfo.LspSummary_, [u'all_ls_ps', u'up_ls_ps', u'admin_up_ls_ps', u'sr_ls_ps', u'rsvp_ls_ps'], name, value)


            class PeerAddress(Entity):
                """
                Peer address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceLspData.LspSummary.PeerLsPsInfo.PeerAddress, self).__init__()

                    self.yang_name = "peer-address"
                    self.yang_parent_name = "peer-ls-ps-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "peer-address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/lsp-summary/peer-ls-ps-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.LspSummary.PeerLsPsInfo.PeerAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


    class TunnelDetailInfos(Entity):
        """
        Detailed tunnel database in XTC
        
        .. attribute:: tunnel_detail_info
        
        	Detailed tunnel information
        	**type**\: list of  		 :py:class:`TunnelDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PceLspData.TunnelDetailInfos, self).__init__()

            self.yang_name = "tunnel-detail-infos"
            self.yang_parent_name = "pce-lsp-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel-detail-info", ("tunnel_detail_info", PceLspData.TunnelDetailInfos.TunnelDetailInfo))])
            self._leafs = OrderedDict()

            self.tunnel_detail_info = YList(self)
            self._segment_path = lambda: "tunnel-detail-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PceLspData.TunnelDetailInfos, [], name, value)


        class TunnelDetailInfo(Entity):
            """
            Detailed tunnel information
            
            .. attribute:: peer_address  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: plsp_id  (key)
            
            	PCEP LSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tunnel_name  (key)
            
            	Tunnel name
            	**type**\: str
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.PccAddress>`
            
            .. attribute:: private_lsp_information
            
            	Private LSP information
            	**type**\:  :py:class:`PrivateLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation>`
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\: str
            
            .. attribute:: xtc_controlled
            
            	Allow XTC reoptimizations
            	**type**\: bool
            
            .. attribute:: color
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: detail_lsp_information
            
            	Detail LSP information
            	**type**\: list of  		 :py:class:`DetailLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PceLspData.TunnelDetailInfos.TunnelDetailInfo, self).__init__()

                self.yang_name = "tunnel-detail-info"
                self.yang_parent_name = "tunnel-detail-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_address','plsp_id','tunnel_name']
                self._child_classes = OrderedDict([("pcc-address", ("pcc_address", PceLspData.TunnelDetailInfos.TunnelDetailInfo.PccAddress)), ("private-lsp-information", ("private_lsp_information", PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation)), ("detail-lsp-information", ("detail_lsp_information", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation))])
                self._leafs = OrderedDict([
                    ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str','str'])),
                    ('plsp_id', (YLeaf(YType.uint32, 'plsp-id'), ['int'])),
                    ('tunnel_name', (YLeaf(YType.str, 'tunnel-name'), ['str'])),
                    ('tunnel_name_xr', (YLeaf(YType.str, 'tunnel-name-xr'), ['str'])),
                    ('xtc_controlled', (YLeaf(YType.boolean, 'xtc-controlled'), ['bool'])),
                    ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                ])
                self.peer_address = None
                self.plsp_id = None
                self.tunnel_name = None
                self.tunnel_name_xr = None
                self.xtc_controlled = None
                self.color = None

                self.pcc_address = PceLspData.TunnelDetailInfos.TunnelDetailInfo.PccAddress()
                self.pcc_address.parent = self
                self._children_name_map["pcc_address"] = "pcc-address"

                self.private_lsp_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation()
                self.private_lsp_information.parent = self
                self._children_name_map["private_lsp_information"] = "private-lsp-information"

                self.detail_lsp_information = YList(self)
                self._segment_path = lambda: "tunnel-detail-info" + "[peer-address='" + str(self.peer_address) + "']" + "[plsp-id='" + str(self.plsp_id) + "']" + "[tunnel-name='" + str(self.tunnel_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-lsp-data/tunnel-detail-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo, ['peer_address', 'plsp_id', 'tunnel_name', u'tunnel_name_xr', u'xtc_controlled', u'color'], name, value)


            class PccAddress(Entity):
                """
                PCC address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PccAddress, self).__init__()

                    self.yang_name = "pcc-address"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "pcc-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PccAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class PrivateLspInformation(Entity):
                """
                Private LSP information
                
                .. attribute:: event_buffer
                
                	LSP Event buffer
                	**type**\: list of  		 :py:class:`EventBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation, self).__init__()

                    self.yang_name = "private-lsp-information"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("event-buffer", ("event_buffer", PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer))])
                    self._leafs = OrderedDict()

                    self.event_buffer = YList(self)
                    self._segment_path = lambda: "private-lsp-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation, [], name, value)


                class EventBuffer(Entity):
                    """
                    LSP Event buffer
                    
                    .. attribute:: event_id
                    
                    	Event ID in range 1 \- 0xFFFFFFFF. 0 is invalid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: event_message
                    
                    	Event message
                    	**type**\: str
                    
                    .. attribute:: time_stamp
                    
                    	Event time, relative to Jan 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer, self).__init__()

                        self.yang_name = "event-buffer"
                        self.yang_parent_name = "private-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('event_id', (YLeaf(YType.uint32, 'event-id'), ['int'])),
                            ('event_message', (YLeaf(YType.str, 'event-message'), ['str'])),
                            ('time_stamp', (YLeaf(YType.uint32, 'time-stamp'), ['int'])),
                        ])
                        self.event_id = None
                        self.event_message = None
                        self.time_stamp = None
                        self._segment_path = lambda: "event-buffer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer, [u'event_id', u'event_message', u'time_stamp'], name, value)


            class DetailLspInformation(Entity):
                """
                Detail LSP information
                
                .. attribute:: brief_lsp_information
                
                	Brief LSP information
                	**type**\:  :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation>`
                
                .. attribute:: er_os
                
                	Paths
                	**type**\:  :py:class:`ErOs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs>`
                
                .. attribute:: lsppcep_information
                
                	PCEP related LSP information
                	**type**\:  :py:class:`LsppcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation>`
                
                .. attribute:: lsp_association_info
                
                	LSP association information
                	**type**\:  :py:class:`LspAssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo>`
                
                .. attribute:: lsp_attributes
                
                	LSP attributes
                	**type**\:  :py:class:`LspAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes>`
                
                .. attribute:: sub_delegated_pce
                
                	Sub delegated PCE
                	**type**\:  :py:class:`SubDelegatedPce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce>`
                
                .. attribute:: state_sync_pce
                
                	State\-sync PCE
                	**type**\:  :py:class:`StateSyncPce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce>`
                
                .. attribute:: reporting_pcc_address
                
                	Reporting PCC address
                	**type**\:  :py:class:`ReportingPccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress>`
                
                .. attribute:: signaled_bandwidth_specified
                
                	True if router notifies signal bandwidth
                	**type**\: bool
                
                .. attribute:: signaled_bandwidth
                
                	Signaled Bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: actual_bandwidth_specified
                
                	True if router notifies actual bandwidth
                	**type**\: bool
                
                .. attribute:: actual_bandwidth
                
                	Actual bandwidth utilized in the data\-plane
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: lsp_role
                
                	LSP Role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: computing_pce
                
                	Computing PCE
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: srlg_info
                
                	List of SLRGs used by LSP
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: rro
                
                	RRO
                	**type**\: list of  		 :py:class:`Rro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation, self).__init__()

                    self.yang_name = "detail-lsp-information"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("brief-lsp-information", ("brief_lsp_information", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation)), ("er-os", ("er_os", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs)), ("lsppcep-information", ("lsppcep_information", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation)), ("lsp-association-info", ("lsp_association_info", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo)), ("lsp-attributes", ("lsp_attributes", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes)), ("sub-delegated-pce", ("sub_delegated_pce", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce)), ("state-sync-pce", ("state_sync_pce", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce)), ("reporting-pcc-address", ("reporting_pcc_address", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress)), ("rro", ("rro", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro))])
                    self._leafs = OrderedDict([
                        ('signaled_bandwidth_specified', (YLeaf(YType.boolean, 'signaled-bandwidth-specified'), ['bool'])),
                        ('signaled_bandwidth', (YLeaf(YType.uint64, 'signaled-bandwidth'), ['int'])),
                        ('actual_bandwidth_specified', (YLeaf(YType.boolean, 'actual-bandwidth-specified'), ['bool'])),
                        ('actual_bandwidth', (YLeaf(YType.uint64, 'actual-bandwidth'), ['int'])),
                        ('lsp_role', (YLeaf(YType.uint32, 'lsp-role'), ['int'])),
                        ('computing_pce', (YLeaf(YType.uint32, 'computing-pce'), ['int'])),
                        ('srlg_info', (YLeafList(YType.uint32, 'srlg-info'), ['int'])),
                    ])
                    self.signaled_bandwidth_specified = None
                    self.signaled_bandwidth = None
                    self.actual_bandwidth_specified = None
                    self.actual_bandwidth = None
                    self.lsp_role = None
                    self.computing_pce = None
                    self.srlg_info = []

                    self.brief_lsp_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation()
                    self.brief_lsp_information.parent = self
                    self._children_name_map["brief_lsp_information"] = "brief-lsp-information"

                    self.er_os = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs()
                    self.er_os.parent = self
                    self._children_name_map["er_os"] = "er-os"

                    self.lsppcep_information = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation()
                    self.lsppcep_information.parent = self
                    self._children_name_map["lsppcep_information"] = "lsppcep-information"

                    self.lsp_association_info = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo()
                    self.lsp_association_info.parent = self
                    self._children_name_map["lsp_association_info"] = "lsp-association-info"

                    self.lsp_attributes = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes()
                    self.lsp_attributes.parent = self
                    self._children_name_map["lsp_attributes"] = "lsp-attributes"

                    self.sub_delegated_pce = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce()
                    self.sub_delegated_pce.parent = self
                    self._children_name_map["sub_delegated_pce"] = "sub-delegated-pce"

                    self.state_sync_pce = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce()
                    self.state_sync_pce.parent = self
                    self._children_name_map["state_sync_pce"] = "state-sync-pce"

                    self.reporting_pcc_address = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress()
                    self.reporting_pcc_address.parent = self
                    self._children_name_map["reporting_pcc_address"] = "reporting-pcc-address"

                    self.rro = YList(self)
                    self._segment_path = lambda: "detail-lsp-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation, [u'signaled_bandwidth_specified', u'signaled_bandwidth', u'actual_bandwidth_specified', u'actual_bandwidth', u'lsp_role', u'computing_pce', u'srlg_info'], name, value)


                class BriefLspInformation(Entity):
                    """
                    Brief LSP information
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\:  :py:class:`SourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress>`
                    
                    .. attribute:: destination_address
                    
                    	Destination address
                    	**type**\:  :py:class:`DestinationAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress>`
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lspid
                    
                    	LSP ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_sid
                    
                    	Binding SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lsp_setup_type
                    
                    	LSP Setup Type
                    	**type**\:  :py:class:`LspSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetup>`
                    
                    .. attribute:: operational_state
                    
                    	Operational state
                    	**type**\:  :py:class:`PcepLspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspState>`
                    
                    .. attribute:: administrative_state
                    
                    	Admin state
                    	**type**\:  :py:class:`LspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspState>`
                    
                    .. attribute:: msd
                    
                    	Maximum SID Depth
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation, self).__init__()

                        self.yang_name = "brief-lsp-information"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("source-address", ("source_address", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress)), ("destination-address", ("destination_address", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress))])
                        self._leafs = OrderedDict([
                            ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                            ('lspid', (YLeaf(YType.uint32, 'lspid'), ['int'])),
                            ('binding_sid', (YLeaf(YType.uint32, 'binding-sid'), ['int'])),
                            ('lsp_setup_type', (YLeaf(YType.enumeration, 'lsp-setup-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspSetup', '')])),
                            ('operational_state', (YLeaf(YType.enumeration, 'operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepLspState', '')])),
                            ('administrative_state', (YLeaf(YType.enumeration, 'administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspState', '')])),
                            ('msd', (YLeaf(YType.uint32, 'msd'), ['int'])),
                        ])
                        self.tunnel_id = None
                        self.lspid = None
                        self.binding_sid = None
                        self.lsp_setup_type = None
                        self.operational_state = None
                        self.administrative_state = None
                        self.msd = None

                        self.source_address = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress()
                        self.source_address.parent = self
                        self._children_name_map["source_address"] = "source-address"

                        self.destination_address = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress()
                        self.destination_address.parent = self
                        self._children_name_map["destination_address"] = "destination-address"
                        self._segment_path = lambda: "brief-lsp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation, [u'tunnel_id', u'lspid', u'binding_sid', u'lsp_setup_type', u'operational_state', u'administrative_state', u'msd'], name, value)


                    class SourceAddress(Entity):
                        """
                        Source address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress, self).__init__()

                            self.yang_name = "source-address"
                            self.yang_parent_name = "brief-lsp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "source-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


                    class DestinationAddress(Entity):
                        """
                        Destination address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress, self).__init__()

                            self.yang_name = "destination-address"
                            self.yang_parent_name = "brief-lsp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "destination-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class ErOs(Entity):
                    """
                    Paths
                    
                    .. attribute:: reported_metric_type
                    
                    	Reported Metric Type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_metric_value
                    
                    	Reported Metric Value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_type
                    
                    	Computed Metric Type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_value
                    
                    	Computed Metric Value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_hop_list_time
                    
                    	Computed Hop List Time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_rsvp_path
                    
                    	Reported RSVP path
                    	**type**\: list of  		 :py:class:`ReportedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath>`
                    
                    .. attribute:: reported_sr_path
                    
                    	Reported SR path
                    	**type**\: list of  		 :py:class:`ReportedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath>`
                    
                    .. attribute:: computed_rsvp_path
                    
                    	Computed RSVP path
                    	**type**\: list of  		 :py:class:`ComputedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath>`
                    
                    .. attribute:: computed_sr_path
                    
                    	Computed SR path
                    	**type**\: list of  		 :py:class:`ComputedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs, self).__init__()

                        self.yang_name = "er-os"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("reported-rsvp-path", ("reported_rsvp_path", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath)), ("reported-sr-path", ("reported_sr_path", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath)), ("computed-rsvp-path", ("computed_rsvp_path", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath)), ("computed-sr-path", ("computed_sr_path", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath))])
                        self._leafs = OrderedDict([
                            ('reported_metric_type', (YLeaf(YType.uint32, 'reported-metric-type'), ['int'])),
                            ('reported_metric_value', (YLeaf(YType.uint32, 'reported-metric-value'), ['int'])),
                            ('computed_metric_type', (YLeaf(YType.uint32, 'computed-metric-type'), ['int'])),
                            ('computed_metric_value', (YLeaf(YType.uint32, 'computed-metric-value'), ['int'])),
                            ('computed_hop_list_time', (YLeaf(YType.uint32, 'computed-hop-list-time'), ['int'])),
                        ])
                        self.reported_metric_type = None
                        self.reported_metric_value = None
                        self.computed_metric_type = None
                        self.computed_metric_value = None
                        self.computed_hop_list_time = None

                        self.reported_rsvp_path = YList(self)
                        self.reported_sr_path = YList(self)
                        self.computed_rsvp_path = YList(self)
                        self.computed_sr_path = YList(self)
                        self._segment_path = lambda: "er-os"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs, [u'reported_metric_type', u'reported_metric_value', u'computed_metric_type', u'computed_metric_value', u'computed_hop_list_time'], name, value)


                    class ReportedRsvpPath(Entity):
                        """
                        Reported RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath, self).__init__()

                            self.yang_name = "reported-rsvp-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                            ])
                            self.hop_address = None
                            self._segment_path = lambda: "reported-rsvp-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath, [u'hop_address'], name, value)


                    class ReportedSrPath(Entity):
                        """
                        Reported SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  :py:class:`LocalAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr>`
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  :py:class:`RemoteAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr>`
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath, self).__init__()

                            self.yang_name = "reported-sr-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-addr", ("local_addr", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr)), ("remote-addr", ("remote_addr", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSid', '')])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.sid_type = None
                            self.mpls_label = None

                            self.local_addr = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr()
                            self.local_addr.parent = self
                            self._children_name_map["local_addr"] = "local-addr"

                            self.remote_addr = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr()
                            self.remote_addr.parent = self
                            self._children_name_map["remote_addr"] = "remote-addr"
                            self._segment_path = lambda: "reported-sr-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath, [u'sid_type', u'mpls_label'], name, value)


                        class LocalAddr(Entity):
                            """
                            Local Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr, self).__init__()

                                self.yang_name = "local-addr"
                                self.yang_parent_name = "reported-sr-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "local-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                        class RemoteAddr(Entity):
                            """
                            Remote Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr, self).__init__()

                                self.yang_name = "remote-addr"
                                self.yang_parent_name = "reported-sr-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "remote-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                    class ComputedRsvpPath(Entity):
                        """
                        Computed RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath, self).__init__()

                            self.yang_name = "computed-rsvp-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                            ])
                            self.hop_address = None
                            self._segment_path = lambda: "computed-rsvp-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath, [u'hop_address'], name, value)


                    class ComputedSrPath(Entity):
                        """
                        Computed SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  :py:class:`LocalAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr>`
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  :py:class:`RemoteAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr>`
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath, self).__init__()

                            self.yang_name = "computed-sr-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-addr", ("local_addr", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr)), ("remote-addr", ("remote_addr", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSid', '')])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.sid_type = None
                            self.mpls_label = None

                            self.local_addr = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr()
                            self.local_addr.parent = self
                            self._children_name_map["local_addr"] = "local-addr"

                            self.remote_addr = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr()
                            self.remote_addr.parent = self
                            self._children_name_map["remote_addr"] = "remote-addr"
                            self._segment_path = lambda: "computed-sr-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath, [u'sid_type', u'mpls_label'], name, value)


                        class LocalAddr(Entity):
                            """
                            Local Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr, self).__init__()

                                self.yang_name = "local-addr"
                                self.yang_parent_name = "computed-sr-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "local-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                        class RemoteAddr(Entity):
                            """
                            Remote Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr, self).__init__()

                                self.yang_name = "remote-addr"
                                self.yang_parent_name = "computed-sr-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "remote-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class LsppcepInformation(Entity):
                    """
                    PCEP related LSP information
                    
                    .. attribute:: rsvp_error
                    
                    	RSVP error info
                    	**type**\:  :py:class:`RsvpError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError>`
                    
                    .. attribute:: pcepid
                    
                    	PCE protocol identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pcep_flag_d
                    
                    	PCEP LSP delegation flag
                    	**type**\: bool
                    
                    .. attribute:: pcep_flag_s
                    
                    	PCEP LSP state\-sync flag
                    	**type**\: bool
                    
                    .. attribute:: pcep_flag_r
                    
                    	PCEP LSP remove flag
                    	**type**\: bool
                    
                    .. attribute:: pcep_flag_a
                    
                    	PCEP LSP admin flag
                    	**type**\: bool
                    
                    .. attribute:: pcep_flag_o
                    
                    	PCEP LSP operation flag
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pcep_flag_c
                    
                    	PCEP LSP initiated flag
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation, self).__init__()

                        self.yang_name = "lsppcep-information"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rsvp-error", ("rsvp_error", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError))])
                        self._leafs = OrderedDict([
                            ('pcepid', (YLeaf(YType.uint32, 'pcepid'), ['int'])),
                            ('pcep_flag_d', (YLeaf(YType.boolean, 'pcep-flag-d'), ['bool'])),
                            ('pcep_flag_s', (YLeaf(YType.boolean, 'pcep-flag-s'), ['bool'])),
                            ('pcep_flag_r', (YLeaf(YType.boolean, 'pcep-flag-r'), ['bool'])),
                            ('pcep_flag_a', (YLeaf(YType.boolean, 'pcep-flag-a'), ['bool'])),
                            ('pcep_flag_o', (YLeaf(YType.uint8, 'pcep-flag-o'), ['int'])),
                            ('pcep_flag_c', (YLeaf(YType.uint8, 'pcep-flag-c'), ['int'])),
                        ])
                        self.pcepid = None
                        self.pcep_flag_d = None
                        self.pcep_flag_s = None
                        self.pcep_flag_r = None
                        self.pcep_flag_a = None
                        self.pcep_flag_o = None
                        self.pcep_flag_c = None

                        self.rsvp_error = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError()
                        self.rsvp_error.parent = self
                        self._children_name_map["rsvp_error"] = "rsvp-error"
                        self._segment_path = lambda: "lsppcep-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation, [u'pcepid', u'pcep_flag_d', u'pcep_flag_s', u'pcep_flag_r', u'pcep_flag_a', u'pcep_flag_o', u'pcep_flag_c'], name, value)


                    class RsvpError(Entity):
                        """
                        RSVP error info
                        
                        .. attribute:: node_address
                        
                        	RSVP error node address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: error_flags
                        
                        	RSVP error flags
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_code
                        
                        	RSVP error code
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_value
                        
                        	RSVP error value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError, self).__init__()

                            self.yang_name = "rsvp-error"
                            self.yang_parent_name = "lsppcep-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_address', (YLeaf(YType.str, 'node-address'), ['str'])),
                                ('error_flags', (YLeaf(YType.uint8, 'error-flags'), ['int'])),
                                ('error_code', (YLeaf(YType.uint8, 'error-code'), ['int'])),
                                ('error_value', (YLeaf(YType.uint16, 'error-value'), ['int'])),
                            ])
                            self.node_address = None
                            self.error_flags = None
                            self.error_code = None
                            self.error_value = None
                            self._segment_path = lambda: "rsvp-error"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError, [u'node_address', u'error_flags', u'error_code', u'error_value'], name, value)


                class LspAssociationInfo(Entity):
                    """
                    LSP association information
                    
                    .. attribute:: association_source
                    
                    	Association Source
                    	**type**\:  :py:class:`AssociationSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource>`
                    
                    .. attribute:: association_type
                    
                    	Association Type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: association_id
                    
                    	Association ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo, self).__init__()

                        self.yang_name = "lsp-association-info"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("association-source", ("association_source", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource))])
                        self._leafs = OrderedDict([
                            ('association_type', (YLeaf(YType.uint32, 'association-type'), ['int'])),
                            ('association_id', (YLeaf(YType.uint32, 'association-id'), ['int'])),
                        ])
                        self.association_type = None
                        self.association_id = None

                        self.association_source = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource()
                        self.association_source.parent = self
                        self._children_name_map["association_source"] = "association-source"
                        self._segment_path = lambda: "lsp-association-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo, [u'association_type', u'association_id'], name, value)


                    class AssociationSource(Entity):
                        """
                        Association Source
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource, self).__init__()

                            self.yang_name = "association-source"
                            self.yang_parent_name = "lsp-association-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "association-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class LspAttributes(Entity):
                    """
                    LSP attributes
                    
                    .. attribute:: affinity_exclude_any
                    
                    	Affinity exclude any
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_any
                    
                    	Affinity include any
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_all
                    
                    	Affinity include all
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: setup_priority
                    
                    	Setup Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: hold_priority
                    
                    	Hold Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_protection
                    
                    	True, if local protection is desired
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes, self).__init__()

                        self.yang_name = "lsp-attributes"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('affinity_exclude_any', (YLeaf(YType.uint32, 'affinity-exclude-any'), ['int'])),
                            ('affinity_include_any', (YLeaf(YType.uint32, 'affinity-include-any'), ['int'])),
                            ('affinity_include_all', (YLeaf(YType.uint32, 'affinity-include-all'), ['int'])),
                            ('setup_priority', (YLeaf(YType.uint8, 'setup-priority'), ['int'])),
                            ('hold_priority', (YLeaf(YType.uint8, 'hold-priority'), ['int'])),
                            ('local_protection', (YLeaf(YType.boolean, 'local-protection'), ['bool'])),
                        ])
                        self.affinity_exclude_any = None
                        self.affinity_include_any = None
                        self.affinity_include_all = None
                        self.setup_priority = None
                        self.hold_priority = None
                        self.local_protection = None
                        self._segment_path = lambda: "lsp-attributes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes, [u'affinity_exclude_any', u'affinity_include_any', u'affinity_include_all', u'setup_priority', u'hold_priority', u'local_protection'], name, value)


                class SubDelegatedPce(Entity):
                    """
                    Sub delegated PCE
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce, self).__init__()

                        self.yang_name = "sub-delegated-pce"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "sub-delegated-pce"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class StateSyncPce(Entity):
                    """
                    State\-sync PCE
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce, self).__init__()

                        self.yang_name = "state-sync-pce"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "state-sync-pce"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class ReportingPccAddress(Entity):
                    """
                    Reporting PCC address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress, self).__init__()

                        self.yang_name = "reporting-pcc-address"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "reporting-pcc-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class Rro(Entity):
                    """
                    RRO
                    
                    .. attribute:: sr_rro
                    
                    	Segment Routing RRO info
                    	**type**\:  :py:class:`SrRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro>`
                    
                    .. attribute:: rro_type
                    
                    	RRO Type
                    	**type**\:  :py:class:`PceRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceRro>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address of RRO
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mpls_label
                    
                    	MPLS label of RRO
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flags
                    
                    	RRO Flags
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro, self).__init__()

                        self.yang_name = "rro"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sr-rro", ("sr_rro", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro))])
                        self._leafs = OrderedDict([
                            ('rro_type', (YLeaf(YType.enumeration, 'rro-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceRro', '')])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ('flags', (YLeaf(YType.uint8, 'flags'), ['int'])),
                        ])
                        self.rro_type = None
                        self.ipv4_address = None
                        self.mpls_label = None
                        self.flags = None

                        self.sr_rro = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro()
                        self.sr_rro.parent = self
                        self._children_name_map["sr_rro"] = "sr-rro"
                        self._segment_path = lambda: "rro"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro, [u'rro_type', u'ipv4_address', u'mpls_label', u'flags'], name, value)


                    class SrRro(Entity):
                        """
                        Segment Routing RRO info
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  :py:class:`LocalAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr>`
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  :py:class:`RemoteAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr>`
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro, self).__init__()

                            self.yang_name = "sr-rro"
                            self.yang_parent_name = "rro"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-addr", ("local_addr", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr)), ("remote-addr", ("remote_addr", PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSid', '')])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.sid_type = None
                            self.mpls_label = None

                            self.local_addr = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr()
                            self.local_addr.parent = self
                            self._children_name_map["local_addr"] = "local-addr"

                            self.remote_addr = PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr()
                            self.remote_addr.parent = self
                            self._children_name_map["remote_addr"] = "remote-addr"
                            self._segment_path = lambda: "sr-rro"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro, [u'sid_type', u'mpls_label'], name, value)


                        class LocalAddr(Entity):
                            """
                            Local Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr, self).__init__()

                                self.yang_name = "local-addr"
                                self.yang_parent_name = "sr-rro"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "local-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                        class RemoteAddr(Entity):
                            """
                            Remote Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr, self).__init__()

                                self.yang_name = "remote-addr"
                                self.yang_parent_name = "sr-rro"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "remote-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceLspData.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)

    def clone_ptr(self):
        self._top_entity = PceLspData()
        return self._top_entity

class PcePeer(Entity):
    """
    pce peer
    
    .. attribute:: peer_detail_infos
    
    	Detailed peers database in XTC
    	**type**\:  :py:class:`PeerDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos>`
    
    .. attribute:: peer_infos
    
    	Peers database in XTC
    	**type**\:  :py:class:`PeerInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(PcePeer, self).__init__()
        self._top_entity = None

        self.yang_name = "pce-peer"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("peer-detail-infos", ("peer_detail_infos", PcePeer.PeerDetailInfos)), ("peer-infos", ("peer_infos", PcePeer.PeerInfos))])
        self._leafs = OrderedDict()

        self.peer_detail_infos = PcePeer.PeerDetailInfos()
        self.peer_detail_infos.parent = self
        self._children_name_map["peer_detail_infos"] = "peer-detail-infos"

        self.peer_infos = PcePeer.PeerInfos()
        self.peer_infos.parent = self
        self._children_name_map["peer_infos"] = "peer-infos"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PcePeer, [], name, value)


    class PeerDetailInfos(Entity):
        """
        Detailed peers database in XTC
        
        .. attribute:: peer_detail_info
        
        	Detailed PCE peer information
        	**type**\: list of  		 :py:class:`PeerDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PcePeer.PeerDetailInfos, self).__init__()

            self.yang_name = "peer-detail-infos"
            self.yang_parent_name = "pce-peer"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("peer-detail-info", ("peer_detail_info", PcePeer.PeerDetailInfos.PeerDetailInfo))])
            self._leafs = OrderedDict()

            self.peer_detail_info = YList(self)
            self._segment_path = lambda: "peer-detail-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PcePeer.PeerDetailInfos, [], name, value)


        class PeerDetailInfo(Entity):
            """
            Detailed PCE peer information
            
            .. attribute:: peer_address  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  :py:class:`PeerAddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.PeerAddressXr>`
            
            .. attribute:: detail_pcep_information
            
            	Detailed PCE protocol information
            	**type**\:  :py:class:`DetailPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation>`
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:  :py:class:`PceProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProto>`
            
            .. attribute:: max_sid_depth
            
            	Maximum SID Depth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PcePeer.PeerDetailInfos.PeerDetailInfo, self).__init__()

                self.yang_name = "peer-detail-info"
                self.yang_parent_name = "peer-detail-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_address']
                self._child_classes = OrderedDict([("peer-address-xr", ("peer_address_xr", PcePeer.PeerDetailInfos.PeerDetailInfo.PeerAddressXr)), ("detail-pcep-information", ("detail_pcep_information", PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation))])
                self._leafs = OrderedDict([
                    ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str','str'])),
                    ('peer_protocol', (YLeaf(YType.enumeration, 'peer-protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceProto', '')])),
                    ('max_sid_depth', (YLeaf(YType.uint32, 'max-sid-depth'), ['int'])),
                ])
                self.peer_address = None
                self.peer_protocol = None
                self.max_sid_depth = None

                self.peer_address_xr = PcePeer.PeerDetailInfos.PeerDetailInfo.PeerAddressXr()
                self.peer_address_xr.parent = self
                self._children_name_map["peer_address_xr"] = "peer-address-xr"

                self.detail_pcep_information = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation()
                self.detail_pcep_information.parent = self
                self._children_name_map["detail_pcep_information"] = "detail-pcep-information"
                self._segment_path = lambda: "peer-detail-info" + "[peer-address='" + str(self.peer_address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer/peer-detail-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo, ['peer_address', u'peer_protocol', u'max_sid_depth'], name, value)


            class PeerAddressXr(Entity):
                """
                Peer address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PcePeer.PeerDetailInfos.PeerDetailInfo.PeerAddressXr, self).__init__()

                    self.yang_name = "peer-address-xr"
                    self.yang_parent_name = "peer-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "peer-address-xr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.PeerAddressXr, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class DetailPcepInformation(Entity):
                """
                Detailed PCE protocol information
                
                .. attribute:: brief_pcep_information
                
                	Brief PCE protocol information
                	**type**\:  :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation>`
                
                .. attribute:: last_error_rx
                
                	Last PCError received
                	**type**\:  :py:class:`LastErrorRx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx>`
                
                .. attribute:: last_error_tx
                
                	Last PCError sent
                	**type**\:  :py:class:`LastErrorTx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx>`
                
                .. attribute:: error
                
                	Error (for display only)
                	**type**\: str
                
                .. attribute:: speaker_id
                
                	Speaker Entity ID
                	**type**\: str
                
                .. attribute:: pcep_up_time
                
                	PCEP Up Time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: keepalives
                
                	Keepalive count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: md5_enabled
                
                	MD5 Authentication Enabled
                	**type**\: bool
                
                .. attribute:: keychain_enabled
                
                	Keychain based Authentication Enabled
                	**type**\: bool
                
                .. attribute:: negotiated_local_keepalive
                
                	Negotiated KA
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_remote_keepalive
                
                	Negotiated KA
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_dead_time
                
                	Negotiated DT
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_rx
                
                	PCEReq Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_tx
                
                	PCEReq Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_rx
                
                	PCERep Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_tx
                
                	PCERep Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_rx
                
                	PCEErr Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_tx
                
                	PCEErr Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_open_tx
                
                	PCEOpen Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_open_rx
                
                	PCEOpen Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_rx
                
                	PCERpt Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_tx
                
                	PCERpt Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_rx
                
                	PCEUpd Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_tx
                
                	PCEUpd Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_rx
                
                	PCEInit Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_tx
                
                	PCEInit Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_keepalive_tx
                
                	PCE Keepalive Tx
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_keepalive_rx
                
                	PCE Keepalive Rx
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: local_session_id
                
                	Local PCEP session ID
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: remote_session_id
                
                	Remote PCEP session ID
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: minimum_keepalive_interval
                
                	Minimum keepalive interval for the peer
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: maximum_dead_interval
                
                	Maximum dead interval for the peer
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: max_sid_depth
                
                	Maximum number of labels the peer can impose
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation, self).__init__()

                    self.yang_name = "detail-pcep-information"
                    self.yang_parent_name = "peer-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("brief-pcep-information", ("brief_pcep_information", PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation)), ("last-error-rx", ("last_error_rx", PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx)), ("last-error-tx", ("last_error_tx", PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx))])
                    self._leafs = OrderedDict([
                        ('error', (YLeaf(YType.str, 'error'), ['str'])),
                        ('speaker_id', (YLeaf(YType.str, 'speaker-id'), ['str'])),
                        ('pcep_up_time', (YLeaf(YType.uint32, 'pcep-up-time'), ['int'])),
                        ('keepalives', (YLeaf(YType.uint32, 'keepalives'), ['int'])),
                        ('md5_enabled', (YLeaf(YType.boolean, 'md5-enabled'), ['bool'])),
                        ('keychain_enabled', (YLeaf(YType.boolean, 'keychain-enabled'), ['bool'])),
                        ('negotiated_local_keepalive', (YLeaf(YType.uint32, 'negotiated-local-keepalive'), ['int'])),
                        ('negotiated_remote_keepalive', (YLeaf(YType.uint32, 'negotiated-remote-keepalive'), ['int'])),
                        ('negotiated_dead_time', (YLeaf(YType.uint32, 'negotiated-dead-time'), ['int'])),
                        ('pce_request_rx', (YLeaf(YType.uint32, 'pce-request-rx'), ['int'])),
                        ('pce_request_tx', (YLeaf(YType.uint32, 'pce-request-tx'), ['int'])),
                        ('pce_reply_rx', (YLeaf(YType.uint32, 'pce-reply-rx'), ['int'])),
                        ('pce_reply_tx', (YLeaf(YType.uint32, 'pce-reply-tx'), ['int'])),
                        ('pce_error_rx', (YLeaf(YType.uint32, 'pce-error-rx'), ['int'])),
                        ('pce_error_tx', (YLeaf(YType.uint32, 'pce-error-tx'), ['int'])),
                        ('pce_open_tx', (YLeaf(YType.uint32, 'pce-open-tx'), ['int'])),
                        ('pce_open_rx', (YLeaf(YType.uint32, 'pce-open-rx'), ['int'])),
                        ('pce_report_rx', (YLeaf(YType.uint32, 'pce-report-rx'), ['int'])),
                        ('pce_report_tx', (YLeaf(YType.uint32, 'pce-report-tx'), ['int'])),
                        ('pce_update_rx', (YLeaf(YType.uint32, 'pce-update-rx'), ['int'])),
                        ('pce_update_tx', (YLeaf(YType.uint32, 'pce-update-tx'), ['int'])),
                        ('pce_initiate_rx', (YLeaf(YType.uint32, 'pce-initiate-rx'), ['int'])),
                        ('pce_initiate_tx', (YLeaf(YType.uint32, 'pce-initiate-tx'), ['int'])),
                        ('pce_keepalive_tx', (YLeaf(YType.uint64, 'pce-keepalive-tx'), ['int'])),
                        ('pce_keepalive_rx', (YLeaf(YType.uint64, 'pce-keepalive-rx'), ['int'])),
                        ('local_session_id', (YLeaf(YType.uint8, 'local-session-id'), ['int'])),
                        ('remote_session_id', (YLeaf(YType.uint8, 'remote-session-id'), ['int'])),
                        ('minimum_keepalive_interval', (YLeaf(YType.uint8, 'minimum-keepalive-interval'), ['int'])),
                        ('maximum_dead_interval', (YLeaf(YType.uint8, 'maximum-dead-interval'), ['int'])),
                        ('max_sid_depth', (YLeaf(YType.uint8, 'max-sid-depth'), ['int'])),
                    ])
                    self.error = None
                    self.speaker_id = None
                    self.pcep_up_time = None
                    self.keepalives = None
                    self.md5_enabled = None
                    self.keychain_enabled = None
                    self.negotiated_local_keepalive = None
                    self.negotiated_remote_keepalive = None
                    self.negotiated_dead_time = None
                    self.pce_request_rx = None
                    self.pce_request_tx = None
                    self.pce_reply_rx = None
                    self.pce_reply_tx = None
                    self.pce_error_rx = None
                    self.pce_error_tx = None
                    self.pce_open_tx = None
                    self.pce_open_rx = None
                    self.pce_report_rx = None
                    self.pce_report_tx = None
                    self.pce_update_rx = None
                    self.pce_update_tx = None
                    self.pce_initiate_rx = None
                    self.pce_initiate_tx = None
                    self.pce_keepalive_tx = None
                    self.pce_keepalive_rx = None
                    self.local_session_id = None
                    self.remote_session_id = None
                    self.minimum_keepalive_interval = None
                    self.maximum_dead_interval = None
                    self.max_sid_depth = None

                    self.brief_pcep_information = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation()
                    self.brief_pcep_information.parent = self
                    self._children_name_map["brief_pcep_information"] = "brief-pcep-information"

                    self.last_error_rx = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx()
                    self.last_error_rx.parent = self
                    self._children_name_map["last_error_rx"] = "last-error-rx"

                    self.last_error_tx = PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx()
                    self.last_error_tx.parent = self
                    self._children_name_map["last_error_tx"] = "last-error-tx"
                    self._segment_path = lambda: "detail-pcep-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation, [u'error', u'speaker_id', u'pcep_up_time', u'keepalives', u'md5_enabled', u'keychain_enabled', u'negotiated_local_keepalive', u'negotiated_remote_keepalive', u'negotiated_dead_time', u'pce_request_rx', u'pce_request_tx', u'pce_reply_rx', u'pce_reply_tx', u'pce_error_rx', u'pce_error_tx', u'pce_open_tx', u'pce_open_rx', u'pce_report_rx', u'pce_report_tx', u'pce_update_rx', u'pce_update_tx', u'pce_initiate_rx', u'pce_initiate_tx', u'pce_keepalive_tx', u'pce_keepalive_rx', u'local_session_id', u'remote_session_id', u'minimum_keepalive_interval', u'maximum_dead_interval', u'max_sid_depth'], name, value)


                class BriefPcepInformation(Entity):
                    """
                    Brief PCE protocol information
                    
                    .. attribute:: pcep_state
                    
                    	PCEP State
                    	**type**\:  :py:class:`PcepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepState>`
                    
                    .. attribute:: stateful
                    
                    	Stateful
                    	**type**\: bool
                    
                    .. attribute:: capability_update
                    
                    	Update capability
                    	**type**\: bool
                    
                    .. attribute:: capability_instantiate
                    
                    	Instantiation capability
                    	**type**\: bool
                    
                    .. attribute:: capability_segment_routing
                    
                    	Segment Routing capability
                    	**type**\: bool
                    
                    .. attribute:: capability_triggered_sync
                    
                    	Triggered Synchronization capability
                    	**type**\: bool
                    
                    .. attribute:: capability_db_version
                    
                    	DB version capability
                    	**type**\: bool
                    
                    .. attribute:: capability_delta_sync
                    
                    	Delta Synchronization capability
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation, self).__init__()

                        self.yang_name = "brief-pcep-information"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pcep_state', (YLeaf(YType.enumeration, 'pcep-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepState', '')])),
                            ('stateful', (YLeaf(YType.boolean, 'stateful'), ['bool'])),
                            ('capability_update', (YLeaf(YType.boolean, 'capability-update'), ['bool'])),
                            ('capability_instantiate', (YLeaf(YType.boolean, 'capability-instantiate'), ['bool'])),
                            ('capability_segment_routing', (YLeaf(YType.boolean, 'capability-segment-routing'), ['bool'])),
                            ('capability_triggered_sync', (YLeaf(YType.boolean, 'capability-triggered-sync'), ['bool'])),
                            ('capability_db_version', (YLeaf(YType.boolean, 'capability-db-version'), ['bool'])),
                            ('capability_delta_sync', (YLeaf(YType.boolean, 'capability-delta-sync'), ['bool'])),
                        ])
                        self.pcep_state = None
                        self.stateful = None
                        self.capability_update = None
                        self.capability_instantiate = None
                        self.capability_segment_routing = None
                        self.capability_triggered_sync = None
                        self.capability_db_version = None
                        self.capability_delta_sync = None
                        self._segment_path = lambda: "brief-pcep-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation, [u'pcep_state', u'stateful', u'capability_update', u'capability_instantiate', u'capability_segment_routing', u'capability_triggered_sync', u'capability_db_version', u'capability_delta_sync'], name, value)


                class LastErrorRx(Entity):
                    """
                    Last PCError received
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx, self).__init__()

                        self.yang_name = "last-error-rx"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pc_error_type', (YLeaf(YType.uint8, 'pc-error-type'), ['int'])),
                            ('pc_error_value', (YLeaf(YType.uint8, 'pc-error-value'), ['int'])),
                        ])
                        self.pc_error_type = None
                        self.pc_error_value = None
                        self._segment_path = lambda: "last-error-rx"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx, [u'pc_error_type', u'pc_error_value'], name, value)


                class LastErrorTx(Entity):
                    """
                    Last PCError sent
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx, self).__init__()

                        self.yang_name = "last-error-tx"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pc_error_type', (YLeaf(YType.uint8, 'pc-error-type'), ['int'])),
                            ('pc_error_value', (YLeaf(YType.uint8, 'pc-error-value'), ['int'])),
                        ])
                        self.pc_error_type = None
                        self.pc_error_value = None
                        self._segment_path = lambda: "last-error-tx"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PcePeer.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx, [u'pc_error_type', u'pc_error_value'], name, value)


    class PeerInfos(Entity):
        """
        Peers database in XTC
        
        .. attribute:: peer_info
        
        	PCE peer information
        	**type**\: list of  		 :py:class:`PeerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos.PeerInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PcePeer.PeerInfos, self).__init__()

            self.yang_name = "peer-infos"
            self.yang_parent_name = "pce-peer"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("peer-info", ("peer_info", PcePeer.PeerInfos.PeerInfo))])
            self._leafs = OrderedDict()

            self.peer_info = YList(self)
            self._segment_path = lambda: "peer-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PcePeer.PeerInfos, [], name, value)


        class PeerInfo(Entity):
            """
            PCE peer information
            
            .. attribute:: peer_address  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  :py:class:`PeerAddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos.PeerInfo.PeerAddressXr>`
            
            .. attribute:: brief_pcep_information
            
            	PCE protocol information
            	**type**\:  :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcePeer.PeerInfos.PeerInfo.BriefPcepInformation>`
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:  :py:class:`PceProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProto>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PcePeer.PeerInfos.PeerInfo, self).__init__()

                self.yang_name = "peer-info"
                self.yang_parent_name = "peer-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_address']
                self._child_classes = OrderedDict([("peer-address-xr", ("peer_address_xr", PcePeer.PeerInfos.PeerInfo.PeerAddressXr)), ("brief-pcep-information", ("brief_pcep_information", PcePeer.PeerInfos.PeerInfo.BriefPcepInformation))])
                self._leafs = OrderedDict([
                    ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str','str'])),
                    ('peer_protocol', (YLeaf(YType.enumeration, 'peer-protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceProto', '')])),
                ])
                self.peer_address = None
                self.peer_protocol = None

                self.peer_address_xr = PcePeer.PeerInfos.PeerInfo.PeerAddressXr()
                self.peer_address_xr.parent = self
                self._children_name_map["peer_address_xr"] = "peer-address-xr"

                self.brief_pcep_information = PcePeer.PeerInfos.PeerInfo.BriefPcepInformation()
                self.brief_pcep_information.parent = self
                self._children_name_map["brief_pcep_information"] = "brief-pcep-information"
                self._segment_path = lambda: "peer-info" + "[peer-address='" + str(self.peer_address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-peer/peer-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PcePeer.PeerInfos.PeerInfo, ['peer_address', u'peer_protocol'], name, value)


            class PeerAddressXr(Entity):
                """
                Peer address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PcePeer.PeerInfos.PeerInfo.PeerAddressXr, self).__init__()

                    self.yang_name = "peer-address-xr"
                    self.yang_parent_name = "peer-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "peer-address-xr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PcePeer.PeerInfos.PeerInfo.PeerAddressXr, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class BriefPcepInformation(Entity):
                """
                PCE protocol information
                
                .. attribute:: pcep_state
                
                	PCEP State
                	**type**\:  :py:class:`PcepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepState>`
                
                .. attribute:: stateful
                
                	Stateful
                	**type**\: bool
                
                .. attribute:: capability_update
                
                	Update capability
                	**type**\: bool
                
                .. attribute:: capability_instantiate
                
                	Instantiation capability
                	**type**\: bool
                
                .. attribute:: capability_segment_routing
                
                	Segment Routing capability
                	**type**\: bool
                
                .. attribute:: capability_triggered_sync
                
                	Triggered Synchronization capability
                	**type**\: bool
                
                .. attribute:: capability_db_version
                
                	DB version capability
                	**type**\: bool
                
                .. attribute:: capability_delta_sync
                
                	Delta Synchronization capability
                	**type**\: bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PcePeer.PeerInfos.PeerInfo.BriefPcepInformation, self).__init__()

                    self.yang_name = "brief-pcep-information"
                    self.yang_parent_name = "peer-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('pcep_state', (YLeaf(YType.enumeration, 'pcep-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepState', '')])),
                        ('stateful', (YLeaf(YType.boolean, 'stateful'), ['bool'])),
                        ('capability_update', (YLeaf(YType.boolean, 'capability-update'), ['bool'])),
                        ('capability_instantiate', (YLeaf(YType.boolean, 'capability-instantiate'), ['bool'])),
                        ('capability_segment_routing', (YLeaf(YType.boolean, 'capability-segment-routing'), ['bool'])),
                        ('capability_triggered_sync', (YLeaf(YType.boolean, 'capability-triggered-sync'), ['bool'])),
                        ('capability_db_version', (YLeaf(YType.boolean, 'capability-db-version'), ['bool'])),
                        ('capability_delta_sync', (YLeaf(YType.boolean, 'capability-delta-sync'), ['bool'])),
                    ])
                    self.pcep_state = None
                    self.stateful = None
                    self.capability_update = None
                    self.capability_instantiate = None
                    self.capability_segment_routing = None
                    self.capability_triggered_sync = None
                    self.capability_db_version = None
                    self.capability_delta_sync = None
                    self._segment_path = lambda: "brief-pcep-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PcePeer.PeerInfos.PeerInfo.BriefPcepInformation, [u'pcep_state', u'stateful', u'capability_update', u'capability_instantiate', u'capability_segment_routing', u'capability_triggered_sync', u'capability_db_version', u'capability_delta_sync'], name, value)

    def clone_ptr(self):
        self._top_entity = PcePeer()
        return self._top_entity

class PceTopology(Entity):
    """
    pce topology
    
    .. attribute:: topology_summary
    
    	Node summary database in XTC
    	**type**\:  :py:class:`TopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologySummary>`
    
    .. attribute:: topology_nodes
    
    	Node database in XTC
    	**type**\:  :py:class:`TopologyNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes>`
    
    .. attribute:: prefix_infos
    
    	Prefixes database in XTC
    	**type**\:  :py:class:`PrefixInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(PceTopology, self).__init__()
        self._top_entity = None

        self.yang_name = "pce-topology"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("topology-summary", ("topology_summary", PceTopology.TopologySummary)), ("topology-nodes", ("topology_nodes", PceTopology.TopologyNodes)), ("prefix-infos", ("prefix_infos", PceTopology.PrefixInfos))])
        self._leafs = OrderedDict()

        self.topology_summary = PceTopology.TopologySummary()
        self.topology_summary.parent = self
        self._children_name_map["topology_summary"] = "topology-summary"

        self.topology_nodes = PceTopology.TopologyNodes()
        self.topology_nodes.parent = self
        self._children_name_map["topology_nodes"] = "topology-nodes"

        self.prefix_infos = PceTopology.PrefixInfos()
        self.prefix_infos.parent = self
        self._children_name_map["prefix_infos"] = "prefix-infos"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PceTopology, [], name, value)


    class TopologySummary(Entity):
        """
        Node summary database in XTC
        
        .. attribute:: stats_topology_update
        
        	Statistics on topology update
        	**type**\:  :py:class:`StatsTopologyUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologySummary.StatsTopologyUpdate>`
        
        .. attribute:: nodes
        
        	Number of PCE nodes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lookup_nodes
        
        	Number of lookup nodes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefixes
        
        	Number of prefixes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefix_sids
        
        	Number of total prefix SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: regular_prefix_sids
        
        	Number of reguar prefix SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: strict_prefix_sids
        
        	Number of strict prefix SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: links
        
        	Number of links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: epe_links
        
        	Number of EPE links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: adjacency_sids
        
        	Number of total adjacency SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: epesids
        
        	Number of total EPE SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: protected_adjacency_sids
        
        	Number of protected adjacency SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: un_protected_adjacency_sids
        
        	Number of unprotected adjacency SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: topology_consistent
        
        	True if topology is consistent
        	**type**\: bool
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PceTopology.TopologySummary, self).__init__()

            self.yang_name = "topology-summary"
            self.yang_parent_name = "pce-topology"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("stats-topology-update", ("stats_topology_update", PceTopology.TopologySummary.StatsTopologyUpdate))])
            self._leafs = OrderedDict([
                ('nodes', (YLeaf(YType.uint32, 'nodes'), ['int'])),
                ('lookup_nodes', (YLeaf(YType.uint32, 'lookup-nodes'), ['int'])),
                ('prefixes', (YLeaf(YType.uint32, 'prefixes'), ['int'])),
                ('prefix_sids', (YLeaf(YType.uint32, 'prefix-sids'), ['int'])),
                ('regular_prefix_sids', (YLeaf(YType.uint32, 'regular-prefix-sids'), ['int'])),
                ('strict_prefix_sids', (YLeaf(YType.uint32, 'strict-prefix-sids'), ['int'])),
                ('links', (YLeaf(YType.uint32, 'links'), ['int'])),
                ('epe_links', (YLeaf(YType.uint32, 'epe-links'), ['int'])),
                ('adjacency_sids', (YLeaf(YType.uint32, 'adjacency-sids'), ['int'])),
                ('epesids', (YLeaf(YType.uint32, 'epesids'), ['int'])),
                ('protected_adjacency_sids', (YLeaf(YType.uint32, 'protected-adjacency-sids'), ['int'])),
                ('un_protected_adjacency_sids', (YLeaf(YType.uint32, 'un-protected-adjacency-sids'), ['int'])),
                ('topology_consistent', (YLeaf(YType.boolean, 'topology-consistent'), ['bool'])),
            ])
            self.nodes = None
            self.lookup_nodes = None
            self.prefixes = None
            self.prefix_sids = None
            self.regular_prefix_sids = None
            self.strict_prefix_sids = None
            self.links = None
            self.epe_links = None
            self.adjacency_sids = None
            self.epesids = None
            self.protected_adjacency_sids = None
            self.un_protected_adjacency_sids = None
            self.topology_consistent = None

            self.stats_topology_update = PceTopology.TopologySummary.StatsTopologyUpdate()
            self.stats_topology_update.parent = self
            self._children_name_map["stats_topology_update"] = "stats-topology-update"
            self._segment_path = lambda: "topology-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PceTopology.TopologySummary, [u'nodes', u'lookup_nodes', u'prefixes', u'prefix_sids', u'regular_prefix_sids', u'strict_prefix_sids', u'links', u'epe_links', u'adjacency_sids', u'epesids', u'protected_adjacency_sids', u'un_protected_adjacency_sids', u'topology_consistent'], name, value)


        class StatsTopologyUpdate(Entity):
            """
            Statistics on topology update
            
            .. attribute:: num_nodes_added
            
            	Number of nodes added
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_deleted
            
            	Number of nodes deleted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_links_added
            
            	Number of links added
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_links_deleted
            
            	Number of links deleted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_added
            
            	Number of prefixes added
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_deleted
            
            	Number of prefixes deleted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PceTopology.TopologySummary.StatsTopologyUpdate, self).__init__()

                self.yang_name = "stats-topology-update"
                self.yang_parent_name = "topology-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('num_nodes_added', (YLeaf(YType.uint32, 'num-nodes-added'), ['int'])),
                    ('num_nodes_deleted', (YLeaf(YType.uint32, 'num-nodes-deleted'), ['int'])),
                    ('num_links_added', (YLeaf(YType.uint32, 'num-links-added'), ['int'])),
                    ('num_links_deleted', (YLeaf(YType.uint32, 'num-links-deleted'), ['int'])),
                    ('num_prefixes_added', (YLeaf(YType.uint32, 'num-prefixes-added'), ['int'])),
                    ('num_prefixes_deleted', (YLeaf(YType.uint32, 'num-prefixes-deleted'), ['int'])),
                ])
                self.num_nodes_added = None
                self.num_nodes_deleted = None
                self.num_links_added = None
                self.num_links_deleted = None
                self.num_prefixes_added = None
                self.num_prefixes_deleted = None
                self._segment_path = lambda: "stats-topology-update"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/topology-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PceTopology.TopologySummary.StatsTopologyUpdate, [u'num_nodes_added', u'num_nodes_deleted', u'num_links_added', u'num_links_deleted', u'num_prefixes_added', u'num_prefixes_deleted'], name, value)


    class TopologyNodes(Entity):
        """
        Node database in XTC
        
        .. attribute:: topology_node
        
        	Node information
        	**type**\: list of  		 :py:class:`TopologyNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PceTopology.TopologyNodes, self).__init__()

            self.yang_name = "topology-nodes"
            self.yang_parent_name = "pce-topology"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("topology-node", ("topology_node", PceTopology.TopologyNodes.TopologyNode))])
            self._leafs = OrderedDict()

            self.topology_node = YList(self)
            self._segment_path = lambda: "topology-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PceTopology.TopologyNodes, [], name, value)


        class TopologyNode(Entity):
            """
            Node information
            
            .. attribute:: node_identifier  (key)
            
            	Node Identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:  :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: overload
            
            	Node Overload Bit
            	**type**\: bool
            
            .. attribute:: prefixe
            
            	Prefixes
            	**type**\: list of  		 :py:class:`Prefixe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Prefixe>`
            
            .. attribute:: ipv4_link
            
            	IPv4 Link information
            	**type**\: list of  		 :py:class:`Ipv4Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link>`
            
            .. attribute:: ipv6_link
            
            	IPv6 Link information
            	**type**\: list of  		 :py:class:`Ipv6Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PceTopology.TopologyNodes.TopologyNode, self).__init__()

                self.yang_name = "topology-node"
                self.yang_parent_name = "topology-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_identifier']
                self._child_classes = OrderedDict([("node-protocol-identifier", ("node_protocol_identifier", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier)), ("prefixe", ("prefixe", PceTopology.TopologyNodes.TopologyNode.Prefixe)), ("ipv4-link", ("ipv4_link", PceTopology.TopologyNodes.TopologyNode.Ipv4Link)), ("ipv6-link", ("ipv6_link", PceTopology.TopologyNodes.TopologyNode.Ipv6Link))])
                self._leafs = OrderedDict([
                    ('node_identifier', (YLeaf(YType.uint32, 'node-identifier'), ['int'])),
                    ('node_identifier_xr', (YLeaf(YType.uint32, 'node-identifier-xr'), ['int'])),
                    ('overload', (YLeaf(YType.boolean, 'overload'), ['bool'])),
                ])
                self.node_identifier = None
                self.node_identifier_xr = None
                self.overload = None

                self.node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"

                self.prefixe = YList(self)
                self.ipv4_link = YList(self)
                self.ipv6_link = YList(self)
                self._segment_path = lambda: "topology-node" + "[node-identifier='" + str(self.node_identifier) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/topology-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode, ['node_identifier', u'node_identifier_xr', u'overload'], name, value)


            class NodeProtocolIdentifier(Entity):
                """
                Node protocol identifier
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\: str
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\: bool
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\: bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of  		 :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("igp-information", ("igp_information", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation)), ("srgb-information", ("srgb_information", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ('ipv4_bgp_router_id_set', (YLeaf(YType.boolean, 'ipv4-bgp-router-id-set'), ['bool'])),
                        ('ipv4_bgp_router_id', (YLeaf(YType.str, 'ipv4-bgp-router-id'), ['str'])),
                        ('ipv4te_router_id_set', (YLeaf(YType.boolean, 'ipv4te-router-id-set'), ['bool'])),
                        ('ipv4te_router_id', (YLeaf(YType.str, 'ipv4te-router-id'), ['str'])),
                    ])
                    self.node_name = None
                    self.ipv4_bgp_router_id_set = None
                    self.ipv4_bgp_router_id = None
                    self.ipv4te_router_id_set = None
                    self.ipv4te_router_id = None

                    self.igp_information = YList(self)
                    self.srgb_information = YList(self)
                    self._segment_path = lambda: "node-protocol-identifier"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier, [u'node_name', u'ipv4_bgp_router_id_set', u'ipv4_bgp_router_id', u'ipv4te_router_id_set', u'ipv4te_router_id'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.node_id = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, [u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class SrgbInformation(Entity):
                    """
                    SRGB information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId>`
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation, self).__init__()

                        self.yang_name = "srgb-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.uint32, 'start'), ['int'])),
                            ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.start = None
                        self.size = None
                        self.domain_identifier = None

                        self.node_id = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "srgb-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation, [u'start', u'size', u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "srgb-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


            class Prefixe(Entity):
                """
                Prefixes
                
                .. attribute:: pfx_sid
                
                	Prefix SID
                	**type**\:  :py:class:`PfxSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid>`
                
                .. attribute:: node_id
                
                	Link\-state node identifier
                	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId>`
                
                .. attribute:: domain_identifier
                
                	Domain identifier
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceTopology.TopologyNodes.TopologyNode.Prefixe, self).__init__()

                    self.yang_name = "prefixe"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pfx-sid", ("pfx_sid", PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid)), ("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId))])
                    self._leafs = OrderedDict([
                        ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                    ])
                    self.domain_identifier = None

                    self.pfx_sid = PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid()
                    self.pfx_sid.parent = self
                    self._children_name_map["pfx_sid"] = "pfx-sid"

                    self.node_id = PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId()
                    self.node_id.parent = self
                    self._children_name_map["node_id"] = "node-id"
                    self._segment_path = lambda: "prefixe"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Prefixe, [u'domain_identifier'], name, value)


                class PfxSid(Entity):
                    """
                    Prefix SID
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\: bool
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\: bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\: bool
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\: bool
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\: bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid, self).__init__()

                        self.yang_name = "pfx-sid"
                        self.yang_parent_name = "prefixe"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Sid', '')])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ('rflag', (YLeaf(YType.boolean, 'rflag'), ['bool'])),
                            ('nflag', (YLeaf(YType.boolean, 'nflag'), ['bool'])),
                            ('pflag', (YLeaf(YType.boolean, 'pflag'), ['bool'])),
                            ('eflag', (YLeaf(YType.boolean, 'eflag'), ['bool'])),
                            ('vflag', (YLeaf(YType.boolean, 'vflag'), ['bool'])),
                            ('lflag', (YLeaf(YType.boolean, 'lflag'), ['bool'])),
                        ])
                        self.sid_type = None
                        self.mpls_label = None
                        self.rflag = None
                        self.nflag = None
                        self.pflag = None
                        self.eflag = None
                        self.vflag = None
                        self.lflag = None

                        self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._segment_path = lambda: "pfx-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid, [u'sid_type', u'mpls_label', u'rflag', u'nflag', u'pflag', u'eflag', u'vflag', u'lflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "pfx-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid-prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class NodeId(Entity):
                    """
                    Link\-state node identifier
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp>`
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ls_identifier
                    
                    	Link\-State identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId, self).__init__()

                        self.yang_name = "node-id"
                        self.yang_parent_name = "prefixe"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp))])
                        self._leafs = OrderedDict([
                            ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                            ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                        ])
                        self.autonomous_system_number = None
                        self.ls_identifier = None

                        self.igp = PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._segment_path = lambda: "node-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf>`
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "node-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp))])
                            self._leafs = OrderedDict([
                                ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                            ])
                            self.igp_id = None

                            self.isis = PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"

                            self.ospf = PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"

                            self.bgp = PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._segment_path = lambda: "igp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp, [u'igp_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\: str
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                    ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                ])
                                self.system_id = None
                                self.level = None
                                self._segment_path = lambda: "isis"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                    ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                ])
                                self.router_id = None
                                self.area = None
                                self._segment_path = lambda: "ospf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                    ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                ])
                                self.router_id = None
                                self.confed_asn = None
                                self._segment_path = lambda: "bgp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


            class Ipv4Link(Entity):
                """
                IPv4 Link information
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:  :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation>`
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:  :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: performance_metrics
                
                	Performance metrics
                	**type**\:  :py:class:`PerformanceMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics>`
                
                .. attribute:: local_ipv4_address
                
                	Local IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_ipv4_address
                
                	Remote IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: administrative_groups
                
                	Link admin\-groups
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: srlgs
                
                	SRLG Values
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of  		 :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link, self).__init__()

                    self.yang_name = "ipv4-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-igp-information", ("local_igp_information", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation)), ("remote-node-protocol-identifier", ("remote_node_protocol_identifier", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier)), ("performance-metrics", ("performance_metrics", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics)), ("adjacency-sid", ("adjacency_sid", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid))])
                    self._leafs = OrderedDict([
                        ('local_ipv4_address', (YLeaf(YType.str, 'local-ipv4-address'), ['str'])),
                        ('remote_ipv4_address', (YLeaf(YType.str, 'remote-ipv4-address'), ['str'])),
                        ('igp_metric', (YLeaf(YType.uint32, 'igp-metric'), ['int'])),
                        ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                        ('maximum_link_bandwidth', (YLeaf(YType.uint64, 'maximum-link-bandwidth'), ['int'])),
                        ('max_reservable_bandwidth', (YLeaf(YType.uint64, 'max-reservable-bandwidth'), ['int'])),
                        ('administrative_groups', (YLeaf(YType.uint32, 'administrative-groups'), ['int'])),
                        ('srlgs', (YLeafList(YType.uint32, 'srlgs'), ['int'])),
                    ])
                    self.local_ipv4_address = None
                    self.remote_ipv4_address = None
                    self.igp_metric = None
                    self.te_metric = None
                    self.maximum_link_bandwidth = None
                    self.max_reservable_bandwidth = None
                    self.administrative_groups = None
                    self.srlgs = []

                    self.local_igp_information = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"

                    self.remote_node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"

                    self.performance_metrics = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics()
                    self.performance_metrics.parent = self
                    self._children_name_map["performance_metrics"] = "performance-metrics"

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv4-link"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link, [u'local_ipv4_address', u'remote_ipv4_address', u'igp_metric', u'te_metric', u'maximum_link_bandwidth', u'max_reservable_bandwidth', u'administrative_groups', u'srlgs'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.node_id = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "local-igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, [u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class RemoteNodeProtocolIdentifier(Entity):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\: str
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\: bool
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\: bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of  		 :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp-information", ("igp_information", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation)), ("srgb-information", ("srgb_information", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('ipv4_bgp_router_id_set', (YLeaf(YType.boolean, 'ipv4-bgp-router-id-set'), ['bool'])),
                            ('ipv4_bgp_router_id', (YLeaf(YType.str, 'ipv4-bgp-router-id'), ['str'])),
                            ('ipv4te_router_id_set', (YLeaf(YType.boolean, 'ipv4te-router-id-set'), ['bool'])),
                            ('ipv4te_router_id', (YLeaf(YType.str, 'ipv4te-router-id'), ['str'])),
                        ])
                        self.node_name = None
                        self.ipv4_bgp_router_id_set = None
                        self.ipv4_bgp_router_id = None
                        self.ipv4te_router_id_set = None
                        self.ipv4te_router_id = None

                        self.igp_information = YList(self)
                        self.srgb_information = YList(self)
                        self._segment_path = lambda: "remote-node-protocol-identifier"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, [u'node_name', u'ipv4_bgp_router_id_set', u'ipv4_bgp_router_id', u'ipv4te_router_id_set', u'ipv4te_router_id'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: node_id
                        
                        	Link\-state node identifier
                        	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId>`
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId))])
                            self._leafs = OrderedDict([
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.domain_identifier = None

                            self.node_id = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId()
                            self.node_id.parent = self
                            self._children_name_map["node_id"] = "node-id"
                            self._segment_path = lambda: "igp-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, [u'domain_identifier'], name, value)


                        class NodeId(Entity):
                            """
                            Link\-state node identifier
                            
                            .. attribute:: igp
                            
                            	IGP\-specific information
                            	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp>`
                            
                            .. attribute:: autonomous_system_number
                            
                            	Autonomous System Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ls_identifier
                            
                            	Link\-State identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId, self).__init__()

                                self.yang_name = "node-id"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp))])
                                self._leafs = OrderedDict([
                                    ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                    ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                                ])
                                self.autonomous_system_number = None
                                self.ls_identifier = None

                                self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                                self._segment_path = lambda: "node-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                            class Igp(Entity):
                                """
                                IGP\-specific information
                                
                                .. attribute:: isis
                                
                                	ISIS information
                                	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis>`
                                
                                .. attribute:: ospf
                                
                                	OSPF information
                                	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf>`
                                
                                .. attribute:: bgp
                                
                                	BGP information
                                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp>`
                                
                                .. attribute:: igp_id
                                
                                	IGP ID
                                	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp, self).__init__()

                                    self.yang_name = "igp"
                                    self.yang_parent_name = "node-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp))])
                                    self._leafs = OrderedDict([
                                        ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                    ])
                                    self.igp_id = None

                                    self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis()
                                    self.isis.parent = self
                                    self._children_name_map["isis"] = "isis"

                                    self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf()
                                    self.ospf.parent = self
                                    self._children_name_map["ospf"] = "ospf"

                                    self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp()
                                    self.bgp.parent = self
                                    self._children_name_map["bgp"] = "bgp"
                                    self._segment_path = lambda: "igp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                                class Isis(Entity):
                                    """
                                    ISIS information
                                    
                                    .. attribute:: system_id
                                    
                                    	ISIS system ID
                                    	**type**\: str
                                    
                                    .. attribute:: level
                                    
                                    	ISIS level
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, self).__init__()

                                        self.yang_name = "isis"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.system_id = None
                                        self.level = None
                                        self._segment_path = lambda: "isis"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                                class Ospf(Entity):
                                    """
                                    OSPF information
                                    
                                    .. attribute:: router_id
                                    
                                    	OSPF router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: area
                                    
                                    	OSPF area
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, self).__init__()

                                        self.yang_name = "ospf"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.area = None
                                        self._segment_path = lambda: "ospf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                                class Bgp(Entity):
                                    """
                                    BGP information
                                    
                                    .. attribute:: router_id
                                    
                                    	BGP router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: confed_asn
                                    
                                    	Confederation ASN
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.confed_asn = None
                                        self._segment_path = lambda: "bgp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                    class SrgbInformation(Entity):
                        """
                        SRGB information
                        
                        .. attribute:: node_id
                        
                        	Link\-state node identifier
                        	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId>`
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation, self).__init__()

                            self.yang_name = "srgb-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId))])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.uint32, 'start'), ['int'])),
                                ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.start = None
                            self.size = None
                            self.domain_identifier = None

                            self.node_id = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId()
                            self.node_id.parent = self
                            self._children_name_map["node_id"] = "node-id"
                            self._segment_path = lambda: "srgb-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation, [u'start', u'size', u'domain_identifier'], name, value)


                        class NodeId(Entity):
                            """
                            Link\-state node identifier
                            
                            .. attribute:: igp
                            
                            	IGP\-specific information
                            	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp>`
                            
                            .. attribute:: autonomous_system_number
                            
                            	Autonomous System Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ls_identifier
                            
                            	Link\-State identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId, self).__init__()

                                self.yang_name = "node-id"
                                self.yang_parent_name = "srgb-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp))])
                                self._leafs = OrderedDict([
                                    ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                    ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                                ])
                                self.autonomous_system_number = None
                                self.ls_identifier = None

                                self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                                self._segment_path = lambda: "node-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                            class Igp(Entity):
                                """
                                IGP\-specific information
                                
                                .. attribute:: isis
                                
                                	ISIS information
                                	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis>`
                                
                                .. attribute:: ospf
                                
                                	OSPF information
                                	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf>`
                                
                                .. attribute:: bgp
                                
                                	BGP information
                                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp>`
                                
                                .. attribute:: igp_id
                                
                                	IGP ID
                                	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp, self).__init__()

                                    self.yang_name = "igp"
                                    self.yang_parent_name = "node-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp))])
                                    self._leafs = OrderedDict([
                                        ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                    ])
                                    self.igp_id = None

                                    self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis()
                                    self.isis.parent = self
                                    self._children_name_map["isis"] = "isis"

                                    self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf()
                                    self.ospf.parent = self
                                    self._children_name_map["ospf"] = "ospf"

                                    self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp()
                                    self.bgp.parent = self
                                    self._children_name_map["bgp"] = "bgp"
                                    self._segment_path = lambda: "igp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp, [u'igp_id'], name, value)


                                class Isis(Entity):
                                    """
                                    ISIS information
                                    
                                    .. attribute:: system_id
                                    
                                    	ISIS system ID
                                    	**type**\: str
                                    
                                    .. attribute:: level
                                    
                                    	ISIS level
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, self).__init__()

                                        self.yang_name = "isis"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.system_id = None
                                        self.level = None
                                        self._segment_path = lambda: "isis"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                                class Ospf(Entity):
                                    """
                                    OSPF information
                                    
                                    .. attribute:: router_id
                                    
                                    	OSPF router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: area
                                    
                                    	OSPF area
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, self).__init__()

                                        self.yang_name = "ospf"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.area = None
                                        self._segment_path = lambda: "ospf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                                class Bgp(Entity):
                                    """
                                    BGP information
                                    
                                    .. attribute:: router_id
                                    
                                    	BGP router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: confed_asn
                                    
                                    	Confederation ASN
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.confed_asn = None
                                        self._segment_path = lambda: "bgp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class PerformanceMetrics(Entity):
                    """
                    Performance metrics
                    
                    .. attribute:: unidirectional_min_delay
                    
                    	Min delay
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics, self).__init__()

                        self.yang_name = "performance-metrics"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('unidirectional_min_delay', (YLeaf(YType.uint32, 'unidirectional-min-delay'), ['int'])),
                        ])
                        self.unidirectional_min_delay = None
                        self._segment_path = lambda: "performance-metrics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics, [u'unidirectional_min_delay'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\: bool
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\: bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\: bool
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\: bool
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\: bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Sid', '')])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ('rflag', (YLeaf(YType.boolean, 'rflag'), ['bool'])),
                            ('nflag', (YLeaf(YType.boolean, 'nflag'), ['bool'])),
                            ('pflag', (YLeaf(YType.boolean, 'pflag'), ['bool'])),
                            ('eflag', (YLeaf(YType.boolean, 'eflag'), ['bool'])),
                            ('vflag', (YLeaf(YType.boolean, 'vflag'), ['bool'])),
                            ('lflag', (YLeaf(YType.boolean, 'lflag'), ['bool'])),
                        ])
                        self.sid_type = None
                        self.mpls_label = None
                        self.rflag = None
                        self.nflag = None
                        self.pflag = None
                        self.eflag = None
                        self.vflag = None
                        self.lflag = None

                        self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._segment_path = lambda: "adjacency-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, [u'sid_type', u'mpls_label', u'rflag', u'nflag', u'pflag', u'eflag', u'vflag', u'lflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid-prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class Ipv6Link(Entity):
                """
                IPv6 Link information
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:  :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation>`
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:  :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: local_ipv6_address
                
                	Local IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_ipv6_address
                
                	Remote IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of  		 :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link, self).__init__()

                    self.yang_name = "ipv6-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-igp-information", ("local_igp_information", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation)), ("remote-node-protocol-identifier", ("remote_node_protocol_identifier", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier)), ("adjacency-sid", ("adjacency_sid", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid))])
                    self._leafs = OrderedDict([
                        ('local_ipv6_address', (YLeaf(YType.str, 'local-ipv6-address'), ['str'])),
                        ('remote_ipv6_address', (YLeaf(YType.str, 'remote-ipv6-address'), ['str'])),
                        ('igp_metric', (YLeaf(YType.uint32, 'igp-metric'), ['int'])),
                        ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                        ('maximum_link_bandwidth', (YLeaf(YType.uint64, 'maximum-link-bandwidth'), ['int'])),
                        ('max_reservable_bandwidth', (YLeaf(YType.uint64, 'max-reservable-bandwidth'), ['int'])),
                    ])
                    self.local_ipv6_address = None
                    self.remote_ipv6_address = None
                    self.igp_metric = None
                    self.te_metric = None
                    self.maximum_link_bandwidth = None
                    self.max_reservable_bandwidth = None

                    self.local_igp_information = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"

                    self.remote_node_protocol_identifier = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv6-link"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link, [u'local_ipv6_address', u'remote_ipv6_address', u'igp_metric', u'te_metric', u'maximum_link_bandwidth', u'max_reservable_bandwidth'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.node_id = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "local-igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, [u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class RemoteNodeProtocolIdentifier(Entity):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\: str
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\: bool
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\: bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of  		 :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp-information", ("igp_information", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation)), ("srgb-information", ("srgb_information", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('ipv4_bgp_router_id_set', (YLeaf(YType.boolean, 'ipv4-bgp-router-id-set'), ['bool'])),
                            ('ipv4_bgp_router_id', (YLeaf(YType.str, 'ipv4-bgp-router-id'), ['str'])),
                            ('ipv4te_router_id_set', (YLeaf(YType.boolean, 'ipv4te-router-id-set'), ['bool'])),
                            ('ipv4te_router_id', (YLeaf(YType.str, 'ipv4te-router-id'), ['str'])),
                        ])
                        self.node_name = None
                        self.ipv4_bgp_router_id_set = None
                        self.ipv4_bgp_router_id = None
                        self.ipv4te_router_id_set = None
                        self.ipv4te_router_id = None

                        self.igp_information = YList(self)
                        self.srgb_information = YList(self)
                        self._segment_path = lambda: "remote-node-protocol-identifier"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, [u'node_name', u'ipv4_bgp_router_id_set', u'ipv4_bgp_router_id', u'ipv4te_router_id_set', u'ipv4te_router_id'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: node_id
                        
                        	Link\-state node identifier
                        	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId>`
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId))])
                            self._leafs = OrderedDict([
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.domain_identifier = None

                            self.node_id = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId()
                            self.node_id.parent = self
                            self._children_name_map["node_id"] = "node-id"
                            self._segment_path = lambda: "igp-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, [u'domain_identifier'], name, value)


                        class NodeId(Entity):
                            """
                            Link\-state node identifier
                            
                            .. attribute:: igp
                            
                            	IGP\-specific information
                            	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp>`
                            
                            .. attribute:: autonomous_system_number
                            
                            	Autonomous System Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ls_identifier
                            
                            	Link\-State identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId, self).__init__()

                                self.yang_name = "node-id"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp))])
                                self._leafs = OrderedDict([
                                    ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                    ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                                ])
                                self.autonomous_system_number = None
                                self.ls_identifier = None

                                self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                                self._segment_path = lambda: "node-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                            class Igp(Entity):
                                """
                                IGP\-specific information
                                
                                .. attribute:: isis
                                
                                	ISIS information
                                	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis>`
                                
                                .. attribute:: ospf
                                
                                	OSPF information
                                	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf>`
                                
                                .. attribute:: bgp
                                
                                	BGP information
                                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp>`
                                
                                .. attribute:: igp_id
                                
                                	IGP ID
                                	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp, self).__init__()

                                    self.yang_name = "igp"
                                    self.yang_parent_name = "node-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp))])
                                    self._leafs = OrderedDict([
                                        ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                    ])
                                    self.igp_id = None

                                    self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis()
                                    self.isis.parent = self
                                    self._children_name_map["isis"] = "isis"

                                    self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf()
                                    self.ospf.parent = self
                                    self._children_name_map["ospf"] = "ospf"

                                    self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp()
                                    self.bgp.parent = self
                                    self._children_name_map["bgp"] = "bgp"
                                    self._segment_path = lambda: "igp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                                class Isis(Entity):
                                    """
                                    ISIS information
                                    
                                    .. attribute:: system_id
                                    
                                    	ISIS system ID
                                    	**type**\: str
                                    
                                    .. attribute:: level
                                    
                                    	ISIS level
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, self).__init__()

                                        self.yang_name = "isis"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.system_id = None
                                        self.level = None
                                        self._segment_path = lambda: "isis"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                                class Ospf(Entity):
                                    """
                                    OSPF information
                                    
                                    .. attribute:: router_id
                                    
                                    	OSPF router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: area
                                    
                                    	OSPF area
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, self).__init__()

                                        self.yang_name = "ospf"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.area = None
                                        self._segment_path = lambda: "ospf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                                class Bgp(Entity):
                                    """
                                    BGP information
                                    
                                    .. attribute:: router_id
                                    
                                    	BGP router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: confed_asn
                                    
                                    	Confederation ASN
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.confed_asn = None
                                        self._segment_path = lambda: "bgp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                    class SrgbInformation(Entity):
                        """
                        SRGB information
                        
                        .. attribute:: node_id
                        
                        	Link\-state node identifier
                        	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId>`
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation, self).__init__()

                            self.yang_name = "srgb-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId))])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.uint32, 'start'), ['int'])),
                                ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.start = None
                            self.size = None
                            self.domain_identifier = None

                            self.node_id = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId()
                            self.node_id.parent = self
                            self._children_name_map["node_id"] = "node-id"
                            self._segment_path = lambda: "srgb-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation, [u'start', u'size', u'domain_identifier'], name, value)


                        class NodeId(Entity):
                            """
                            Link\-state node identifier
                            
                            .. attribute:: igp
                            
                            	IGP\-specific information
                            	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp>`
                            
                            .. attribute:: autonomous_system_number
                            
                            	Autonomous System Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ls_identifier
                            
                            	Link\-State identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId, self).__init__()

                                self.yang_name = "node-id"
                                self.yang_parent_name = "srgb-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("igp", ("igp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp))])
                                self._leafs = OrderedDict([
                                    ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                    ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                                ])
                                self.autonomous_system_number = None
                                self.ls_identifier = None

                                self.igp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                                self._segment_path = lambda: "node-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                            class Igp(Entity):
                                """
                                IGP\-specific information
                                
                                .. attribute:: isis
                                
                                	ISIS information
                                	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis>`
                                
                                .. attribute:: ospf
                                
                                	OSPF information
                                	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf>`
                                
                                .. attribute:: bgp
                                
                                	BGP information
                                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp>`
                                
                                .. attribute:: igp_id
                                
                                	IGP ID
                                	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp, self).__init__()

                                    self.yang_name = "igp"
                                    self.yang_parent_name = "node-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("isis", ("isis", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp))])
                                    self._leafs = OrderedDict([
                                        ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                    ])
                                    self.igp_id = None

                                    self.isis = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis()
                                    self.isis.parent = self
                                    self._children_name_map["isis"] = "isis"

                                    self.ospf = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf()
                                    self.ospf.parent = self
                                    self._children_name_map["ospf"] = "ospf"

                                    self.bgp = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp()
                                    self.bgp.parent = self
                                    self._children_name_map["bgp"] = "bgp"
                                    self._segment_path = lambda: "igp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp, [u'igp_id'], name, value)


                                class Isis(Entity):
                                    """
                                    ISIS information
                                    
                                    .. attribute:: system_id
                                    
                                    	ISIS system ID
                                    	**type**\: str
                                    
                                    .. attribute:: level
                                    
                                    	ISIS level
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, self).__init__()

                                        self.yang_name = "isis"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.system_id = None
                                        self.level = None
                                        self._segment_path = lambda: "isis"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                                class Ospf(Entity):
                                    """
                                    OSPF information
                                    
                                    .. attribute:: router_id
                                    
                                    	OSPF router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: area
                                    
                                    	OSPF area
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, self).__init__()

                                        self.yang_name = "ospf"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.area = None
                                        self._segment_path = lambda: "ospf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                                class Bgp(Entity):
                                    """
                                    BGP information
                                    
                                    .. attribute:: router_id
                                    
                                    	BGP router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: confed_asn
                                    
                                    	Confederation ASN
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.confed_asn = None
                                        self._segment_path = lambda: "bgp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\: bool
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\: bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\: bool
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\: bool
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\: bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Sid', '')])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ('rflag', (YLeaf(YType.boolean, 'rflag'), ['bool'])),
                            ('nflag', (YLeaf(YType.boolean, 'nflag'), ['bool'])),
                            ('pflag', (YLeaf(YType.boolean, 'pflag'), ['bool'])),
                            ('eflag', (YLeaf(YType.boolean, 'eflag'), ['bool'])),
                            ('vflag', (YLeaf(YType.boolean, 'vflag'), ['bool'])),
                            ('lflag', (YLeaf(YType.boolean, 'lflag'), ['bool'])),
                        ])
                        self.sid_type = None
                        self.mpls_label = None
                        self.rflag = None
                        self.nflag = None
                        self.pflag = None
                        self.eflag = None
                        self.vflag = None
                        self.lflag = None

                        self.sid_prefix = PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._segment_path = lambda: "adjacency-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, [u'sid_type', u'mpls_label', u'rflag', u'nflag', u'pflag', u'eflag', u'vflag', u'lflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid-prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, [u'af_name', u'ipv4', u'ipv6'], name, value)


    class PrefixInfos(Entity):
        """
        Prefixes database in XTC
        
        .. attribute:: prefix_info
        
        	PCE prefix information
        	**type**\: list of  		 :py:class:`PrefixInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PceTopology.PrefixInfos, self).__init__()

            self.yang_name = "prefix-infos"
            self.yang_parent_name = "pce-topology"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prefix-info", ("prefix_info", PceTopology.PrefixInfos.PrefixInfo))])
            self._leafs = OrderedDict()

            self.prefix_info = YList(self)
            self._segment_path = lambda: "prefix-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PceTopology.PrefixInfos, [], name, value)


        class PrefixInfo(Entity):
            """
            PCE prefix information
            
            .. attribute:: node_identifier  (key)
            
            	Node ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:  :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: address
            
            	Prefix address
            	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.Address>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PceTopology.PrefixInfos.PrefixInfo, self).__init__()

                self.yang_name = "prefix-info"
                self.yang_parent_name = "prefix-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_identifier']
                self._child_classes = OrderedDict([("node-protocol-identifier", ("node_protocol_identifier", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier)), ("address", ("address", PceTopology.PrefixInfos.PrefixInfo.Address))])
                self._leafs = OrderedDict([
                    ('node_identifier', (YLeaf(YType.uint32, 'node-identifier'), ['int'])),
                    ('node_identifier_xr', (YLeaf(YType.uint32, 'node-identifier-xr'), ['int'])),
                ])
                self.node_identifier = None
                self.node_identifier_xr = None

                self.node_protocol_identifier = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"

                self.address = YList(self)
                self._segment_path = lambda: "prefix-info" + "[node-identifier='" + str(self.node_identifier) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce-topology/prefix-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo, ['node_identifier', u'node_identifier_xr'], name, value)


            class NodeProtocolIdentifier(Entity):
                """
                Node protocol identifier
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\: str
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\: bool
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\: bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of  		 :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("igp-information", ("igp_information", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation)), ("srgb-information", ("srgb_information", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ('ipv4_bgp_router_id_set', (YLeaf(YType.boolean, 'ipv4-bgp-router-id-set'), ['bool'])),
                        ('ipv4_bgp_router_id', (YLeaf(YType.str, 'ipv4-bgp-router-id'), ['str'])),
                        ('ipv4te_router_id_set', (YLeaf(YType.boolean, 'ipv4te-router-id-set'), ['bool'])),
                        ('ipv4te_router_id', (YLeaf(YType.str, 'ipv4te-router-id'), ['str'])),
                    ])
                    self.node_name = None
                    self.ipv4_bgp_router_id_set = None
                    self.ipv4_bgp_router_id = None
                    self.ipv4te_router_id_set = None
                    self.ipv4te_router_id = None

                    self.igp_information = YList(self)
                    self.srgb_information = YList(self)
                    self._segment_path = lambda: "node-protocol-identifier"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, [u'node_name', u'ipv4_bgp_router_id_set', u'ipv4_bgp_router_id', u'ipv4te_router_id_set', u'ipv4te_router_id'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.node_id = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, [u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class SrgbInformation(Entity):
                    """
                    SRGB information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId>`
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation, self).__init__()

                        self.yang_name = "srgb-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.uint32, 'start'), ['int'])),
                            ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.start = None
                        self.size = None
                        self.domain_identifier = None

                        self.node_id = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "srgb-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation, [u'start', u'size', u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "srgb-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


            class Address(Entity):
                """
                Prefix address
                
                .. attribute:: ip
                
                	Prefix IP address
                	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceTopology.PrefixInfos.PrefixInfo.Address.Ip>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PceTopology.PrefixInfos.PrefixInfo.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ip", ("ip", PceTopology.PrefixInfos.PrefixInfo.Address.Ip))])
                    self._leafs = OrderedDict()

                    self.ip = PceTopology.PrefixInfos.PrefixInfo.Address.Ip()
                    self.ip.parent = self
                    self._children_name_map["ip"] = "ip"
                    self._segment_path = lambda: "address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.Address, [], name, value)


                class Ip(Entity):
                    """
                    Prefix IP address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PceTopology.PrefixInfos.PrefixInfo.Address.Ip, self).__init__()

                        self.yang_name = "ip"
                        self.yang_parent_name = "address"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "ip"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PceTopology.PrefixInfos.PrefixInfo.Address.Ip, [u'af_name', u'ipv4', u'ipv6'], name, value)

    def clone_ptr(self):
        self._top_entity = PceTopology()
        return self._top_entity

class Pce(Entity):
    """
    pce
    
    .. attribute:: verification_events
    
    	PCE Verification events in XTC
    	**type**\:  :py:class:`VerificationEvents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.VerificationEvents>`
    
    .. attribute:: association_infos
    
    	Associaition database in XTC
    	**type**\:  :py:class:`AssociationInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos>`
    
    .. attribute:: cspf
    
    	CSPF path info
    	**type**\:  :py:class:`Cspf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf>`
    
    .. attribute:: topology_summary
    
    	Node summary database in XTC
    	**type**\:  :py:class:`TopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologySummary>`
    
    .. attribute:: tunnel_infos
    
    	Tunnel database in XTC
    	**type**\:  :py:class:`TunnelInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos>`
    
    .. attribute:: peer_detail_infos
    
    	Detailed peers database in XTC
    	**type**\:  :py:class:`PeerDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos>`
    
    .. attribute:: topology_nodes
    
    	Node database in XTC
    	**type**\:  :py:class:`TopologyNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes>`
    
    .. attribute:: prefix_infos
    
    	Prefixes database in XTC
    	**type**\:  :py:class:`PrefixInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos>`
    
    .. attribute:: lsp_summary
    
    	LSP summary database in XTC
    	**type**\:  :py:class:`LspSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary>`
    
    .. attribute:: peer_infos
    
    	Peers database in XTC
    	**type**\:  :py:class:`PeerInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos>`
    
    .. attribute:: tunnel_detail_infos
    
    	Detailed tunnel database in XTC
    	**type**\:  :py:class:`TunnelDetailInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos>`
    
    

    """

    _prefix = 'infra-xtc-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(Pce, self).__init__()
        self._top_entity = None

        self.yang_name = "pce"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("verification-events", ("verification_events", Pce.VerificationEvents)), ("association-infos", ("association_infos", Pce.AssociationInfos)), ("cspf", ("cspf", Pce.Cspf)), ("topology-summary", ("topology_summary", Pce.TopologySummary)), ("tunnel-infos", ("tunnel_infos", Pce.TunnelInfos)), ("peer-detail-infos", ("peer_detail_infos", Pce.PeerDetailInfos)), ("topology-nodes", ("topology_nodes", Pce.TopologyNodes)), ("prefix-infos", ("prefix_infos", Pce.PrefixInfos)), ("lsp-summary", ("lsp_summary", Pce.LspSummary)), ("peer-infos", ("peer_infos", Pce.PeerInfos)), ("tunnel-detail-infos", ("tunnel_detail_infos", Pce.TunnelDetailInfos))])
        self._leafs = OrderedDict()

        self.verification_events = Pce.VerificationEvents()
        self.verification_events.parent = self
        self._children_name_map["verification_events"] = "verification-events"

        self.association_infos = Pce.AssociationInfos()
        self.association_infos.parent = self
        self._children_name_map["association_infos"] = "association-infos"

        self.cspf = Pce.Cspf()
        self.cspf.parent = self
        self._children_name_map["cspf"] = "cspf"

        self.topology_summary = Pce.TopologySummary()
        self.topology_summary.parent = self
        self._children_name_map["topology_summary"] = "topology-summary"

        self.tunnel_infos = Pce.TunnelInfos()
        self.tunnel_infos.parent = self
        self._children_name_map["tunnel_infos"] = "tunnel-infos"

        self.peer_detail_infos = Pce.PeerDetailInfos()
        self.peer_detail_infos.parent = self
        self._children_name_map["peer_detail_infos"] = "peer-detail-infos"

        self.topology_nodes = Pce.TopologyNodes()
        self.topology_nodes.parent = self
        self._children_name_map["topology_nodes"] = "topology-nodes"

        self.prefix_infos = Pce.PrefixInfos()
        self.prefix_infos.parent = self
        self._children_name_map["prefix_infos"] = "prefix-infos"

        self.lsp_summary = Pce.LspSummary()
        self.lsp_summary.parent = self
        self._children_name_map["lsp_summary"] = "lsp-summary"

        self.peer_infos = Pce.PeerInfos()
        self.peer_infos.parent = self
        self._children_name_map["peer_infos"] = "peer-infos"

        self.tunnel_detail_infos = Pce.TunnelDetailInfos()
        self.tunnel_detail_infos.parent = self
        self._children_name_map["tunnel_detail_infos"] = "tunnel-detail-infos"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Pce, [], name, value)


    class VerificationEvents(Entity):
        """
        PCE Verification events in XTC
        
        .. attribute:: verification_event
        
        	PCE single verification event
        	**type**\: list of  		 :py:class:`VerificationEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.VerificationEvents.VerificationEvent>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.VerificationEvents, self).__init__()

            self.yang_name = "verification-events"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("verification-event", ("verification_event", Pce.VerificationEvents.VerificationEvent))])
            self._leafs = OrderedDict()

            self.verification_event = YList(self)
            self._segment_path = lambda: "verification-events"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.VerificationEvents, [], name, value)


        class VerificationEvent(Entity):
            """
            PCE single verification event
            
            .. attribute:: event_idx  (key)
            
            	Index of an event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: event_id
            
            	Event ID in range 1 \- 0xFFFFFFFF. 0 is invalid
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: event_message
            
            	Event message
            	**type**\: str
            
            .. attribute:: time_stamp
            
            	Event time, relative to Jan 1, 1970
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.VerificationEvents.VerificationEvent, self).__init__()

                self.yang_name = "verification-event"
                self.yang_parent_name = "verification-events"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['event_idx']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('event_idx', (YLeaf(YType.uint32, 'event-idx'), ['int'])),
                    ('event_id', (YLeaf(YType.uint32, 'event-id'), ['int'])),
                    ('event_message', (YLeaf(YType.str, 'event-message'), ['str'])),
                    ('time_stamp', (YLeaf(YType.uint32, 'time-stamp'), ['int'])),
                ])
                self.event_idx = None
                self.event_id = None
                self.event_message = None
                self.time_stamp = None
                self._segment_path = lambda: "verification-event" + "[event-idx='" + str(self.event_idx) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/verification-events/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.VerificationEvents.VerificationEvent, ['event_idx', u'event_id', u'event_message', u'time_stamp'], name, value)


    class AssociationInfos(Entity):
        """
        Associaition database in XTC
        
        .. attribute:: association_info
        
        	PCE Association information
        	**type**\: list of  		 :py:class:`AssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos.AssociationInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.AssociationInfos, self).__init__()

            self.yang_name = "association-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("association-info", ("association_info", Pce.AssociationInfos.AssociationInfo))])
            self._leafs = OrderedDict()

            self.association_info = YList(self)
            self._segment_path = lambda: "association-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.AssociationInfos, [], name, value)


        class AssociationInfo(Entity):
            """
            PCE Association information
            
            .. attribute:: group_id  (key)
            
            	Group ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: type
            
            	Type
            	**type**\:  :py:class:`PceAsso <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAsso>`
            
            .. attribute:: sub_id
            
            	Sub ID
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: association_source
            
            	Association Source
            	**type**\:  :py:class:`AssociationSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos.AssociationInfo.AssociationSource>`
            
            .. attribute:: association_type
            
            	Association Type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: association_id
            
            	Association ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: strict
            
            	Association Strict Mode
            	**type**\: bool
            
            .. attribute:: status
            
            	Association Status
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: headends_swapped
            
            	Headends Swapped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: association_lsp
            
            	Association LSP Info
            	**type**\: list of  		 :py:class:`AssociationLsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos.AssociationInfo.AssociationLsp>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.AssociationInfos.AssociationInfo, self).__init__()

                self.yang_name = "association-info"
                self.yang_parent_name = "association-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group_id']
                self._child_classes = OrderedDict([("association-source", ("association_source", Pce.AssociationInfos.AssociationInfo.AssociationSource)), ("association-lsp", ("association_lsp", Pce.AssociationInfos.AssociationInfo.AssociationLsp))])
                self._leafs = OrderedDict([
                    ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAsso', '')])),
                    ('sub_id', (YLeaf(YType.str, 'sub-id'), ['str','str'])),
                    ('association_type', (YLeaf(YType.uint32, 'association-type'), ['int'])),
                    ('association_id', (YLeaf(YType.uint32, 'association-id'), ['int'])),
                    ('strict', (YLeaf(YType.boolean, 'strict'), ['bool'])),
                    ('status', (YLeaf(YType.uint32, 'status'), ['int'])),
                    ('headends_swapped', (YLeaf(YType.uint32, 'headends-swapped'), ['int'])),
                ])
                self.group_id = None
                self.type = None
                self.sub_id = None
                self.association_type = None
                self.association_id = None
                self.strict = None
                self.status = None
                self.headends_swapped = None

                self.association_source = Pce.AssociationInfos.AssociationInfo.AssociationSource()
                self.association_source.parent = self
                self._children_name_map["association_source"] = "association-source"

                self.association_lsp = YList(self)
                self._segment_path = lambda: "association-info" + "[group-id='" + str(self.group_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/association-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.AssociationInfos.AssociationInfo, ['group_id', 'type', 'sub_id', u'association_type', u'association_id', u'strict', u'status', u'headends_swapped'], name, value)


            class AssociationSource(Entity):
                """
                Association Source
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.AssociationInfos.AssociationInfo.AssociationSource, self).__init__()

                    self.yang_name = "association-source"
                    self.yang_parent_name = "association-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "association-source"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.AssociationInfos.AssociationInfo.AssociationSource, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class AssociationLsp(Entity):
                """
                Association LSP Info
                
                .. attribute:: pcc_address
                
                	PCC address
                	**type**\:  :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.AssociationInfos.AssociationInfo.AssociationLsp.PccAddress>`
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tunnel_name
                
                	Tunnel Name
                	**type**\: str
                
                .. attribute:: pce_based
                
                	PCE Based
                	**type**\: bool
                
                .. attribute:: plsp_id
                
                	PLSP ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.AssociationInfos.AssociationInfo.AssociationLsp, self).__init__()

                    self.yang_name = "association-lsp"
                    self.yang_parent_name = "association-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pcc-address", ("pcc_address", Pce.AssociationInfos.AssociationInfo.AssociationLsp.PccAddress))])
                    self._leafs = OrderedDict([
                        ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                        ('lspid', (YLeaf(YType.uint32, 'lspid'), ['int'])),
                        ('tunnel_name', (YLeaf(YType.str, 'tunnel-name'), ['str'])),
                        ('pce_based', (YLeaf(YType.boolean, 'pce-based'), ['bool'])),
                        ('plsp_id', (YLeaf(YType.uint32, 'plsp-id'), ['int'])),
                    ])
                    self.tunnel_id = None
                    self.lspid = None
                    self.tunnel_name = None
                    self.pce_based = None
                    self.plsp_id = None

                    self.pcc_address = Pce.AssociationInfos.AssociationInfo.AssociationLsp.PccAddress()
                    self.pcc_address.parent = self
                    self._children_name_map["pcc_address"] = "pcc-address"
                    self._segment_path = lambda: "association-lsp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.AssociationInfos.AssociationInfo.AssociationLsp, [u'tunnel_id', u'lspid', u'tunnel_name', u'pce_based', u'plsp_id'], name, value)


                class PccAddress(Entity):
                    """
                    PCC address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.AssociationInfos.AssociationInfo.AssociationLsp.PccAddress, self).__init__()

                        self.yang_name = "pcc-address"
                        self.yang_parent_name = "association-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "pcc-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.AssociationInfos.AssociationInfo.AssociationLsp.PccAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


    class Cspf(Entity):
        """
        CSPF path info
        
        .. attribute:: cspf_paths
        
        	This table models the path calculation capabilities in XTC.A GET operation for the complete table will return no entries
        	**type**\:  :py:class:`CspfPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.Cspf, self).__init__()

            self.yang_name = "cspf"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cspf-paths", ("cspf_paths", Pce.Cspf.CspfPaths))])
            self._leafs = OrderedDict()

            self.cspf_paths = Pce.Cspf.CspfPaths()
            self.cspf_paths.parent = self
            self._children_name_map["cspf_paths"] = "cspf-paths"
            self._segment_path = lambda: "cspf"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.Cspf, [], name, value)


        class CspfPaths(Entity):
            """
            This table models the path calculation
            capabilities in XTC.A GET operation for the
            complete table will return no entries.
            
            .. attribute:: cspf_path
            
            	A GET operation on this class returns the path 
            	**type**\: list of  		 :py:class:`CspfPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.Cspf.CspfPaths, self).__init__()

                self.yang_name = "cspf-paths"
                self.yang_parent_name = "cspf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("cspf-path", ("cspf_path", Pce.Cspf.CspfPaths.CspfPath))])
                self._leafs = OrderedDict()

                self.cspf_path = YList(self)
                self._segment_path = lambda: "cspf-paths"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/cspf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.Cspf.CspfPaths, [], name, value)


            class CspfPath(Entity):
                """
                A GET operation on this class returns the path
                .
                
                .. attribute:: af  (key)
                
                	Address Family
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: source1  (key)
                
                	Source of path 1
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination1  (key)
                
                	Destination of path 1
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: metric_type  (key)
                
                	Metric type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: source2  (key)
                
                	Source of path 2
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: destination2  (key)
                
                	Destination of path 2
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: disjoint_level  (key)
                
                	Disjointness level
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disjoint_strict  (key)
                
                	Strict disjointness required
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: shortest_path  (key)
                
                	Whether path 1 or 2 should be shortest
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: headends_swapped
                
                	Headends swapped
                	**type**\:  :py:class:`PceHeadendSwap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceHeadendSwap>`
                
                .. attribute:: cspf_result
                
                	CSPF Result
                	**type**\:  :py:class:`PceCspfRc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceCspfRc>`
                
                .. attribute:: iterations_done
                
                	Iterations of the Suurballe\-Tarjan algorithm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_path
                
                	Output PCE paths
                	**type**\: list of  		 :py:class:`OutputPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath.OutputPath>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.Cspf.CspfPaths.CspfPath, self).__init__()

                    self.yang_name = "cspf-path"
                    self.yang_parent_name = "cspf-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['af','source1','destination1','metric_type','source2','destination2','disjoint_level','disjoint_strict','shortest_path']
                    self._child_classes = OrderedDict([("output-path", ("output_path", Pce.Cspf.CspfPaths.CspfPath.OutputPath))])
                    self._leafs = OrderedDict([
                        ('af', (YLeaf(YType.uint32, 'af'), ['int'])),
                        ('source1', (YLeaf(YType.str, 'source1'), ['str','str'])),
                        ('destination1', (YLeaf(YType.str, 'destination1'), ['str','str'])),
                        ('metric_type', (YLeaf(YType.uint32, 'metric-type'), ['int'])),
                        ('source2', (YLeaf(YType.str, 'source2'), ['str','str'])),
                        ('destination2', (YLeaf(YType.str, 'destination2'), ['str','str'])),
                        ('disjoint_level', (YLeaf(YType.uint32, 'disjoint-level'), ['int'])),
                        ('disjoint_strict', (YLeaf(YType.uint32, 'disjoint-strict'), ['int'])),
                        ('shortest_path', (YLeaf(YType.uint32, 'shortest-path'), ['int'])),
                        ('headends_swapped', (YLeaf(YType.enumeration, 'headends-swapped'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceHeadendSwap', '')])),
                        ('cspf_result', (YLeaf(YType.enumeration, 'cspf-result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceCspfRc', '')])),
                        ('iterations_done', (YLeaf(YType.uint32, 'iterations-done'), ['int'])),
                    ])
                    self.af = None
                    self.source1 = None
                    self.destination1 = None
                    self.metric_type = None
                    self.source2 = None
                    self.destination2 = None
                    self.disjoint_level = None
                    self.disjoint_strict = None
                    self.shortest_path = None
                    self.headends_swapped = None
                    self.cspf_result = None
                    self.iterations_done = None

                    self.output_path = YList(self)
                    self._segment_path = lambda: "cspf-path" + "[af='" + str(self.af) + "']" + "[source1='" + str(self.source1) + "']" + "[destination1='" + str(self.destination1) + "']" + "[metric-type='" + str(self.metric_type) + "']" + "[source2='" + str(self.source2) + "']" + "[destination2='" + str(self.destination2) + "']" + "[disjoint-level='" + str(self.disjoint_level) + "']" + "[disjoint-strict='" + str(self.disjoint_strict) + "']" + "[shortest-path='" + str(self.shortest_path) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/cspf/cspf-paths/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath, ['af', 'source1', 'destination1', 'metric_type', 'source2', 'destination2', 'disjoint_level', 'disjoint_strict', 'shortest_path', u'headends_swapped', u'cspf_result', u'iterations_done'], name, value)


                class OutputPath(Entity):
                    """
                    Output PCE paths
                    
                    .. attribute:: source
                    
                    	Source of path
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source>`
                    
                    .. attribute:: destination
                    
                    	Destination of path
                    	**type**\:  :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination>`
                    
                    .. attribute:: cost
                    
                    	Cost
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: hops
                    
                    	Hop addresses
                    	**type**\: list of  		 :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.Cspf.CspfPaths.CspfPath.OutputPath.Hops>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.Cspf.CspfPaths.CspfPath.OutputPath, self).__init__()

                        self.yang_name = "output-path"
                        self.yang_parent_name = "cspf-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("source", ("source", Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source)), ("destination", ("destination", Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination)), ("hops", ("hops", Pce.Cspf.CspfPaths.CspfPath.OutputPath.Hops))])
                        self._leafs = OrderedDict([
                            ('cost', (YLeaf(YType.uint64, 'cost'), ['int'])),
                        ])
                        self.cost = None

                        self.source = Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source()
                        self.source.parent = self
                        self._children_name_map["source"] = "source"

                        self.destination = Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination()
                        self.destination.parent = self
                        self._children_name_map["destination"] = "destination"

                        self.hops = YList(self)
                        self._segment_path = lambda: "output-path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath.OutputPath, [u'cost'], name, value)


                    class Source(Entity):
                        """
                        Source of path
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "output-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Source, [u'af_name', u'ipv4', u'ipv6'], name, value)


                    class Destination(Entity):
                        """
                        Destination of path
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination, self).__init__()

                            self.yang_name = "destination"
                            self.yang_parent_name = "output-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "destination"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Destination, [u'af_name', u'ipv4', u'ipv6'], name, value)


                    class Hops(Entity):
                        """
                        Hop addresses
                        
                        .. attribute:: address_family
                        
                        	Address Family
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 prefix
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 prefix
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Hops, self).__init__()

                            self.yang_name = "hops"
                            self.yang_parent_name = "output-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address_family', (YLeaf(YType.uint8, 'address-family'), ['int'])),
                                ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                            ])
                            self.address_family = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None
                            self._segment_path = lambda: "hops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.Cspf.CspfPaths.CspfPath.OutputPath.Hops, [u'address_family', u'ipv4_prefix', u'ipv6_prefix'], name, value)


    class TopologySummary(Entity):
        """
        Node summary database in XTC
        
        .. attribute:: stats_topology_update
        
        	Statistics on topology update
        	**type**\:  :py:class:`StatsTopologyUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologySummary.StatsTopologyUpdate>`
        
        .. attribute:: nodes
        
        	Number of PCE nodes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lookup_nodes
        
        	Number of lookup nodes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefixes
        
        	Number of prefixes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefix_sids
        
        	Number of total prefix SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: regular_prefix_sids
        
        	Number of reguar prefix SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: strict_prefix_sids
        
        	Number of strict prefix SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: links
        
        	Number of links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: epe_links
        
        	Number of EPE links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: adjacency_sids
        
        	Number of total adjacency SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: epesids
        
        	Number of total EPE SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: protected_adjacency_sids
        
        	Number of protected adjacency SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: un_protected_adjacency_sids
        
        	Number of unprotected adjacency SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: topology_consistent
        
        	True if topology is consistent
        	**type**\: bool
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.TopologySummary, self).__init__()

            self.yang_name = "topology-summary"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("stats-topology-update", ("stats_topology_update", Pce.TopologySummary.StatsTopologyUpdate))])
            self._leafs = OrderedDict([
                ('nodes', (YLeaf(YType.uint32, 'nodes'), ['int'])),
                ('lookup_nodes', (YLeaf(YType.uint32, 'lookup-nodes'), ['int'])),
                ('prefixes', (YLeaf(YType.uint32, 'prefixes'), ['int'])),
                ('prefix_sids', (YLeaf(YType.uint32, 'prefix-sids'), ['int'])),
                ('regular_prefix_sids', (YLeaf(YType.uint32, 'regular-prefix-sids'), ['int'])),
                ('strict_prefix_sids', (YLeaf(YType.uint32, 'strict-prefix-sids'), ['int'])),
                ('links', (YLeaf(YType.uint32, 'links'), ['int'])),
                ('epe_links', (YLeaf(YType.uint32, 'epe-links'), ['int'])),
                ('adjacency_sids', (YLeaf(YType.uint32, 'adjacency-sids'), ['int'])),
                ('epesids', (YLeaf(YType.uint32, 'epesids'), ['int'])),
                ('protected_adjacency_sids', (YLeaf(YType.uint32, 'protected-adjacency-sids'), ['int'])),
                ('un_protected_adjacency_sids', (YLeaf(YType.uint32, 'un-protected-adjacency-sids'), ['int'])),
                ('topology_consistent', (YLeaf(YType.boolean, 'topology-consistent'), ['bool'])),
            ])
            self.nodes = None
            self.lookup_nodes = None
            self.prefixes = None
            self.prefix_sids = None
            self.regular_prefix_sids = None
            self.strict_prefix_sids = None
            self.links = None
            self.epe_links = None
            self.adjacency_sids = None
            self.epesids = None
            self.protected_adjacency_sids = None
            self.un_protected_adjacency_sids = None
            self.topology_consistent = None

            self.stats_topology_update = Pce.TopologySummary.StatsTopologyUpdate()
            self.stats_topology_update.parent = self
            self._children_name_map["stats_topology_update"] = "stats-topology-update"
            self._segment_path = lambda: "topology-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.TopologySummary, [u'nodes', u'lookup_nodes', u'prefixes', u'prefix_sids', u'regular_prefix_sids', u'strict_prefix_sids', u'links', u'epe_links', u'adjacency_sids', u'epesids', u'protected_adjacency_sids', u'un_protected_adjacency_sids', u'topology_consistent'], name, value)


        class StatsTopologyUpdate(Entity):
            """
            Statistics on topology update
            
            .. attribute:: num_nodes_added
            
            	Number of nodes added
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_nodes_deleted
            
            	Number of nodes deleted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_links_added
            
            	Number of links added
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_links_deleted
            
            	Number of links deleted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_added
            
            	Number of prefixes added
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: num_prefixes_deleted
            
            	Number of prefixes deleted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.TopologySummary.StatsTopologyUpdate, self).__init__()

                self.yang_name = "stats-topology-update"
                self.yang_parent_name = "topology-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('num_nodes_added', (YLeaf(YType.uint32, 'num-nodes-added'), ['int'])),
                    ('num_nodes_deleted', (YLeaf(YType.uint32, 'num-nodes-deleted'), ['int'])),
                    ('num_links_added', (YLeaf(YType.uint32, 'num-links-added'), ['int'])),
                    ('num_links_deleted', (YLeaf(YType.uint32, 'num-links-deleted'), ['int'])),
                    ('num_prefixes_added', (YLeaf(YType.uint32, 'num-prefixes-added'), ['int'])),
                    ('num_prefixes_deleted', (YLeaf(YType.uint32, 'num-prefixes-deleted'), ['int'])),
                ])
                self.num_nodes_added = None
                self.num_nodes_deleted = None
                self.num_links_added = None
                self.num_links_deleted = None
                self.num_prefixes_added = None
                self.num_prefixes_deleted = None
                self._segment_path = lambda: "stats-topology-update"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/topology-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.TopologySummary.StatsTopologyUpdate, [u'num_nodes_added', u'num_nodes_deleted', u'num_links_added', u'num_links_deleted', u'num_prefixes_added', u'num_prefixes_deleted'], name, value)


    class TunnelInfos(Entity):
        """
        Tunnel database in XTC
        
        .. attribute:: tunnel_info
        
        	Tunnel information
        	**type**\: list of  		 :py:class:`TunnelInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.TunnelInfos, self).__init__()

            self.yang_name = "tunnel-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel-info", ("tunnel_info", Pce.TunnelInfos.TunnelInfo))])
            self._leafs = OrderedDict()

            self.tunnel_info = YList(self)
            self._segment_path = lambda: "tunnel-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.TunnelInfos, [], name, value)


        class TunnelInfo(Entity):
            """
            Tunnel information
            
            .. attribute:: peer_address  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: plsp_id  (key)
            
            	PCEP LSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tunnel_name  (key)
            
            	Tunnel name
            	**type**\: str
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo.PccAddress>`
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\: str
            
            .. attribute:: brief_lsp_information
            
            	Brief LSP information
            	**type**\: list of  		 :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo.BriefLspInformation>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.TunnelInfos.TunnelInfo, self).__init__()

                self.yang_name = "tunnel-info"
                self.yang_parent_name = "tunnel-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_address','plsp_id','tunnel_name']
                self._child_classes = OrderedDict([("pcc-address", ("pcc_address", Pce.TunnelInfos.TunnelInfo.PccAddress)), ("brief-lsp-information", ("brief_lsp_information", Pce.TunnelInfos.TunnelInfo.BriefLspInformation))])
                self._leafs = OrderedDict([
                    ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str','str'])),
                    ('plsp_id', (YLeaf(YType.uint32, 'plsp-id'), ['int'])),
                    ('tunnel_name', (YLeaf(YType.str, 'tunnel-name'), ['str'])),
                    ('tunnel_name_xr', (YLeaf(YType.str, 'tunnel-name-xr'), ['str'])),
                ])
                self.peer_address = None
                self.plsp_id = None
                self.tunnel_name = None
                self.tunnel_name_xr = None

                self.pcc_address = Pce.TunnelInfos.TunnelInfo.PccAddress()
                self.pcc_address.parent = self
                self._children_name_map["pcc_address"] = "pcc-address"

                self.brief_lsp_information = YList(self)
                self._segment_path = lambda: "tunnel-info" + "[peer-address='" + str(self.peer_address) + "']" + "[plsp-id='" + str(self.plsp_id) + "']" + "[tunnel-name='" + str(self.tunnel_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/tunnel-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.TunnelInfos.TunnelInfo, ['peer_address', 'plsp_id', 'tunnel_name', u'tunnel_name_xr'], name, value)


            class PccAddress(Entity):
                """
                PCC address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TunnelInfos.TunnelInfo.PccAddress, self).__init__()

                    self.yang_name = "pcc-address"
                    self.yang_parent_name = "tunnel-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "pcc-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TunnelInfos.TunnelInfo.PccAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class BriefLspInformation(Entity):
                """
                Brief LSP information
                
                .. attribute:: source_address
                
                	Source address
                	**type**\:  :py:class:`SourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress>`
                
                .. attribute:: destination_address
                
                	Destination address
                	**type**\:  :py:class:`DestinationAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress>`
                
                .. attribute:: tunnel_id
                
                	Tunnel ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lspid
                
                	LSP ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: binding_sid
                
                	Binding SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsp_setup_type
                
                	LSP Setup Type
                	**type**\:  :py:class:`LspSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetup>`
                
                .. attribute:: operational_state
                
                	Operational state
                	**type**\:  :py:class:`PcepLspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspState>`
                
                .. attribute:: administrative_state
                
                	Admin state
                	**type**\:  :py:class:`LspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspState>`
                
                .. attribute:: msd
                
                	Maximum SID Depth
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TunnelInfos.TunnelInfo.BriefLspInformation, self).__init__()

                    self.yang_name = "brief-lsp-information"
                    self.yang_parent_name = "tunnel-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("source-address", ("source_address", Pce.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress)), ("destination-address", ("destination_address", Pce.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress))])
                    self._leafs = OrderedDict([
                        ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                        ('lspid', (YLeaf(YType.uint32, 'lspid'), ['int'])),
                        ('binding_sid', (YLeaf(YType.uint32, 'binding-sid'), ['int'])),
                        ('lsp_setup_type', (YLeaf(YType.enumeration, 'lsp-setup-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspSetup', '')])),
                        ('operational_state', (YLeaf(YType.enumeration, 'operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepLspState', '')])),
                        ('administrative_state', (YLeaf(YType.enumeration, 'administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspState', '')])),
                        ('msd', (YLeaf(YType.uint32, 'msd'), ['int'])),
                    ])
                    self.tunnel_id = None
                    self.lspid = None
                    self.binding_sid = None
                    self.lsp_setup_type = None
                    self.operational_state = None
                    self.administrative_state = None
                    self.msd = None

                    self.source_address = Pce.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress()
                    self.source_address.parent = self
                    self._children_name_map["source_address"] = "source-address"

                    self.destination_address = Pce.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress()
                    self.destination_address.parent = self
                    self._children_name_map["destination_address"] = "destination-address"
                    self._segment_path = lambda: "brief-lsp-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TunnelInfos.TunnelInfo.BriefLspInformation, [u'tunnel_id', u'lspid', u'binding_sid', u'lsp_setup_type', u'operational_state', u'administrative_state', u'msd'], name, value)


                class SourceAddress(Entity):
                    """
                    Source address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress, self).__init__()

                        self.yang_name = "source-address"
                        self.yang_parent_name = "brief-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "source-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelInfos.TunnelInfo.BriefLspInformation.SourceAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class DestinationAddress(Entity):
                    """
                    Destination address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress, self).__init__()

                        self.yang_name = "destination-address"
                        self.yang_parent_name = "brief-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "destination-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelInfos.TunnelInfo.BriefLspInformation.DestinationAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


    class PeerDetailInfos(Entity):
        """
        Detailed peers database in XTC
        
        .. attribute:: peer_detail_info
        
        	Detailed PCE peer information
        	**type**\: list of  		 :py:class:`PeerDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.PeerDetailInfos, self).__init__()

            self.yang_name = "peer-detail-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("peer-detail-info", ("peer_detail_info", Pce.PeerDetailInfos.PeerDetailInfo))])
            self._leafs = OrderedDict()

            self.peer_detail_info = YList(self)
            self._segment_path = lambda: "peer-detail-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.PeerDetailInfos, [], name, value)


        class PeerDetailInfo(Entity):
            """
            Detailed PCE peer information
            
            .. attribute:: peer_address  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  :py:class:`PeerAddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.PeerAddressXr>`
            
            .. attribute:: detail_pcep_information
            
            	Detailed PCE protocol information
            	**type**\:  :py:class:`DetailPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation>`
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:  :py:class:`PceProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProto>`
            
            .. attribute:: max_sid_depth
            
            	Maximum SID Depth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.PeerDetailInfos.PeerDetailInfo, self).__init__()

                self.yang_name = "peer-detail-info"
                self.yang_parent_name = "peer-detail-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_address']
                self._child_classes = OrderedDict([("peer-address-xr", ("peer_address_xr", Pce.PeerDetailInfos.PeerDetailInfo.PeerAddressXr)), ("detail-pcep-information", ("detail_pcep_information", Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation))])
                self._leafs = OrderedDict([
                    ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str','str'])),
                    ('peer_protocol', (YLeaf(YType.enumeration, 'peer-protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceProto', '')])),
                    ('max_sid_depth', (YLeaf(YType.uint32, 'max-sid-depth'), ['int'])),
                ])
                self.peer_address = None
                self.peer_protocol = None
                self.max_sid_depth = None

                self.peer_address_xr = Pce.PeerDetailInfos.PeerDetailInfo.PeerAddressXr()
                self.peer_address_xr.parent = self
                self._children_name_map["peer_address_xr"] = "peer-address-xr"

                self.detail_pcep_information = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation()
                self.detail_pcep_information.parent = self
                self._children_name_map["detail_pcep_information"] = "detail-pcep-information"
                self._segment_path = lambda: "peer-detail-info" + "[peer-address='" + str(self.peer_address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/peer-detail-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo, ['peer_address', u'peer_protocol', u'max_sid_depth'], name, value)


            class PeerAddressXr(Entity):
                """
                Peer address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.PeerDetailInfos.PeerDetailInfo.PeerAddressXr, self).__init__()

                    self.yang_name = "peer-address-xr"
                    self.yang_parent_name = "peer-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "peer-address-xr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.PeerAddressXr, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class DetailPcepInformation(Entity):
                """
                Detailed PCE protocol information
                
                .. attribute:: brief_pcep_information
                
                	Brief PCE protocol information
                	**type**\:  :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation>`
                
                .. attribute:: last_error_rx
                
                	Last PCError received
                	**type**\:  :py:class:`LastErrorRx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx>`
                
                .. attribute:: last_error_tx
                
                	Last PCError sent
                	**type**\:  :py:class:`LastErrorTx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx>`
                
                .. attribute:: error
                
                	Error (for display only)
                	**type**\: str
                
                .. attribute:: speaker_id
                
                	Speaker Entity ID
                	**type**\: str
                
                .. attribute:: pcep_up_time
                
                	PCEP Up Time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: keepalives
                
                	Keepalive count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: md5_enabled
                
                	MD5 Authentication Enabled
                	**type**\: bool
                
                .. attribute:: keychain_enabled
                
                	Keychain based Authentication Enabled
                	**type**\: bool
                
                .. attribute:: negotiated_local_keepalive
                
                	Negotiated KA
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_remote_keepalive
                
                	Negotiated KA
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: negotiated_dead_time
                
                	Negotiated DT
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_rx
                
                	PCEReq Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_request_tx
                
                	PCEReq Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_rx
                
                	PCERep Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_reply_tx
                
                	PCERep Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_rx
                
                	PCEErr Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_error_tx
                
                	PCEErr Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_open_tx
                
                	PCEOpen Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_open_rx
                
                	PCEOpen Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_rx
                
                	PCERpt Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_report_tx
                
                	PCERpt Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_rx
                
                	PCEUpd Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_update_tx
                
                	PCEUpd Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_rx
                
                	PCEInit Rx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_initiate_tx
                
                	PCEInit Tx
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pce_keepalive_tx
                
                	PCE Keepalive Tx
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_keepalive_rx
                
                	PCE Keepalive Rx
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: local_session_id
                
                	Local PCEP session ID
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: remote_session_id
                
                	Remote PCEP session ID
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: minimum_keepalive_interval
                
                	Minimum keepalive interval for the peer
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: maximum_dead_interval
                
                	Maximum dead interval for the peer
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: max_sid_depth
                
                	Maximum number of labels the peer can impose
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation, self).__init__()

                    self.yang_name = "detail-pcep-information"
                    self.yang_parent_name = "peer-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("brief-pcep-information", ("brief_pcep_information", Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation)), ("last-error-rx", ("last_error_rx", Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx)), ("last-error-tx", ("last_error_tx", Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx))])
                    self._leafs = OrderedDict([
                        ('error', (YLeaf(YType.str, 'error'), ['str'])),
                        ('speaker_id', (YLeaf(YType.str, 'speaker-id'), ['str'])),
                        ('pcep_up_time', (YLeaf(YType.uint32, 'pcep-up-time'), ['int'])),
                        ('keepalives', (YLeaf(YType.uint32, 'keepalives'), ['int'])),
                        ('md5_enabled', (YLeaf(YType.boolean, 'md5-enabled'), ['bool'])),
                        ('keychain_enabled', (YLeaf(YType.boolean, 'keychain-enabled'), ['bool'])),
                        ('negotiated_local_keepalive', (YLeaf(YType.uint32, 'negotiated-local-keepalive'), ['int'])),
                        ('negotiated_remote_keepalive', (YLeaf(YType.uint32, 'negotiated-remote-keepalive'), ['int'])),
                        ('negotiated_dead_time', (YLeaf(YType.uint32, 'negotiated-dead-time'), ['int'])),
                        ('pce_request_rx', (YLeaf(YType.uint32, 'pce-request-rx'), ['int'])),
                        ('pce_request_tx', (YLeaf(YType.uint32, 'pce-request-tx'), ['int'])),
                        ('pce_reply_rx', (YLeaf(YType.uint32, 'pce-reply-rx'), ['int'])),
                        ('pce_reply_tx', (YLeaf(YType.uint32, 'pce-reply-tx'), ['int'])),
                        ('pce_error_rx', (YLeaf(YType.uint32, 'pce-error-rx'), ['int'])),
                        ('pce_error_tx', (YLeaf(YType.uint32, 'pce-error-tx'), ['int'])),
                        ('pce_open_tx', (YLeaf(YType.uint32, 'pce-open-tx'), ['int'])),
                        ('pce_open_rx', (YLeaf(YType.uint32, 'pce-open-rx'), ['int'])),
                        ('pce_report_rx', (YLeaf(YType.uint32, 'pce-report-rx'), ['int'])),
                        ('pce_report_tx', (YLeaf(YType.uint32, 'pce-report-tx'), ['int'])),
                        ('pce_update_rx', (YLeaf(YType.uint32, 'pce-update-rx'), ['int'])),
                        ('pce_update_tx', (YLeaf(YType.uint32, 'pce-update-tx'), ['int'])),
                        ('pce_initiate_rx', (YLeaf(YType.uint32, 'pce-initiate-rx'), ['int'])),
                        ('pce_initiate_tx', (YLeaf(YType.uint32, 'pce-initiate-tx'), ['int'])),
                        ('pce_keepalive_tx', (YLeaf(YType.uint64, 'pce-keepalive-tx'), ['int'])),
                        ('pce_keepalive_rx', (YLeaf(YType.uint64, 'pce-keepalive-rx'), ['int'])),
                        ('local_session_id', (YLeaf(YType.uint8, 'local-session-id'), ['int'])),
                        ('remote_session_id', (YLeaf(YType.uint8, 'remote-session-id'), ['int'])),
                        ('minimum_keepalive_interval', (YLeaf(YType.uint8, 'minimum-keepalive-interval'), ['int'])),
                        ('maximum_dead_interval', (YLeaf(YType.uint8, 'maximum-dead-interval'), ['int'])),
                        ('max_sid_depth', (YLeaf(YType.uint8, 'max-sid-depth'), ['int'])),
                    ])
                    self.error = None
                    self.speaker_id = None
                    self.pcep_up_time = None
                    self.keepalives = None
                    self.md5_enabled = None
                    self.keychain_enabled = None
                    self.negotiated_local_keepalive = None
                    self.negotiated_remote_keepalive = None
                    self.negotiated_dead_time = None
                    self.pce_request_rx = None
                    self.pce_request_tx = None
                    self.pce_reply_rx = None
                    self.pce_reply_tx = None
                    self.pce_error_rx = None
                    self.pce_error_tx = None
                    self.pce_open_tx = None
                    self.pce_open_rx = None
                    self.pce_report_rx = None
                    self.pce_report_tx = None
                    self.pce_update_rx = None
                    self.pce_update_tx = None
                    self.pce_initiate_rx = None
                    self.pce_initiate_tx = None
                    self.pce_keepalive_tx = None
                    self.pce_keepalive_rx = None
                    self.local_session_id = None
                    self.remote_session_id = None
                    self.minimum_keepalive_interval = None
                    self.maximum_dead_interval = None
                    self.max_sid_depth = None

                    self.brief_pcep_information = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation()
                    self.brief_pcep_information.parent = self
                    self._children_name_map["brief_pcep_information"] = "brief-pcep-information"

                    self.last_error_rx = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx()
                    self.last_error_rx.parent = self
                    self._children_name_map["last_error_rx"] = "last-error-rx"

                    self.last_error_tx = Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx()
                    self.last_error_tx.parent = self
                    self._children_name_map["last_error_tx"] = "last-error-tx"
                    self._segment_path = lambda: "detail-pcep-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation, [u'error', u'speaker_id', u'pcep_up_time', u'keepalives', u'md5_enabled', u'keychain_enabled', u'negotiated_local_keepalive', u'negotiated_remote_keepalive', u'negotiated_dead_time', u'pce_request_rx', u'pce_request_tx', u'pce_reply_rx', u'pce_reply_tx', u'pce_error_rx', u'pce_error_tx', u'pce_open_tx', u'pce_open_rx', u'pce_report_rx', u'pce_report_tx', u'pce_update_rx', u'pce_update_tx', u'pce_initiate_rx', u'pce_initiate_tx', u'pce_keepalive_tx', u'pce_keepalive_rx', u'local_session_id', u'remote_session_id', u'minimum_keepalive_interval', u'maximum_dead_interval', u'max_sid_depth'], name, value)


                class BriefPcepInformation(Entity):
                    """
                    Brief PCE protocol information
                    
                    .. attribute:: pcep_state
                    
                    	PCEP State
                    	**type**\:  :py:class:`PcepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepState>`
                    
                    .. attribute:: stateful
                    
                    	Stateful
                    	**type**\: bool
                    
                    .. attribute:: capability_update
                    
                    	Update capability
                    	**type**\: bool
                    
                    .. attribute:: capability_instantiate
                    
                    	Instantiation capability
                    	**type**\: bool
                    
                    .. attribute:: capability_segment_routing
                    
                    	Segment Routing capability
                    	**type**\: bool
                    
                    .. attribute:: capability_triggered_sync
                    
                    	Triggered Synchronization capability
                    	**type**\: bool
                    
                    .. attribute:: capability_db_version
                    
                    	DB version capability
                    	**type**\: bool
                    
                    .. attribute:: capability_delta_sync
                    
                    	Delta Synchronization capability
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation, self).__init__()

                        self.yang_name = "brief-pcep-information"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pcep_state', (YLeaf(YType.enumeration, 'pcep-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepState', '')])),
                            ('stateful', (YLeaf(YType.boolean, 'stateful'), ['bool'])),
                            ('capability_update', (YLeaf(YType.boolean, 'capability-update'), ['bool'])),
                            ('capability_instantiate', (YLeaf(YType.boolean, 'capability-instantiate'), ['bool'])),
                            ('capability_segment_routing', (YLeaf(YType.boolean, 'capability-segment-routing'), ['bool'])),
                            ('capability_triggered_sync', (YLeaf(YType.boolean, 'capability-triggered-sync'), ['bool'])),
                            ('capability_db_version', (YLeaf(YType.boolean, 'capability-db-version'), ['bool'])),
                            ('capability_delta_sync', (YLeaf(YType.boolean, 'capability-delta-sync'), ['bool'])),
                        ])
                        self.pcep_state = None
                        self.stateful = None
                        self.capability_update = None
                        self.capability_instantiate = None
                        self.capability_segment_routing = None
                        self.capability_triggered_sync = None
                        self.capability_db_version = None
                        self.capability_delta_sync = None
                        self._segment_path = lambda: "brief-pcep-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.BriefPcepInformation, [u'pcep_state', u'stateful', u'capability_update', u'capability_instantiate', u'capability_segment_routing', u'capability_triggered_sync', u'capability_db_version', u'capability_delta_sync'], name, value)


                class LastErrorRx(Entity):
                    """
                    Last PCError received
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx, self).__init__()

                        self.yang_name = "last-error-rx"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pc_error_type', (YLeaf(YType.uint8, 'pc-error-type'), ['int'])),
                            ('pc_error_value', (YLeaf(YType.uint8, 'pc-error-value'), ['int'])),
                        ])
                        self.pc_error_type = None
                        self.pc_error_value = None
                        self._segment_path = lambda: "last-error-rx"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorRx, [u'pc_error_type', u'pc_error_value'], name, value)


                class LastErrorTx(Entity):
                    """
                    Last PCError sent
                    
                    .. attribute:: pc_error_type
                    
                    	PCEP Error type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pc_error_value
                    
                    	PCEP Error Value
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx, self).__init__()

                        self.yang_name = "last-error-tx"
                        self.yang_parent_name = "detail-pcep-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pc_error_type', (YLeaf(YType.uint8, 'pc-error-type'), ['int'])),
                            ('pc_error_value', (YLeaf(YType.uint8, 'pc-error-value'), ['int'])),
                        ])
                        self.pc_error_type = None
                        self.pc_error_value = None
                        self._segment_path = lambda: "last-error-tx"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PeerDetailInfos.PeerDetailInfo.DetailPcepInformation.LastErrorTx, [u'pc_error_type', u'pc_error_value'], name, value)


    class TopologyNodes(Entity):
        """
        Node database in XTC
        
        .. attribute:: topology_node
        
        	Node information
        	**type**\: list of  		 :py:class:`TopologyNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.TopologyNodes, self).__init__()

            self.yang_name = "topology-nodes"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("topology-node", ("topology_node", Pce.TopologyNodes.TopologyNode))])
            self._leafs = OrderedDict()

            self.topology_node = YList(self)
            self._segment_path = lambda: "topology-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.TopologyNodes, [], name, value)


        class TopologyNode(Entity):
            """
            Node information
            
            .. attribute:: node_identifier  (key)
            
            	Node Identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:  :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: overload
            
            	Node Overload Bit
            	**type**\: bool
            
            .. attribute:: prefixe
            
            	Prefixes
            	**type**\: list of  		 :py:class:`Prefixe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Prefixe>`
            
            .. attribute:: ipv4_link
            
            	IPv4 Link information
            	**type**\: list of  		 :py:class:`Ipv4Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link>`
            
            .. attribute:: ipv6_link
            
            	IPv6 Link information
            	**type**\: list of  		 :py:class:`Ipv6Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.TopologyNodes.TopologyNode, self).__init__()

                self.yang_name = "topology-node"
                self.yang_parent_name = "topology-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_identifier']
                self._child_classes = OrderedDict([("node-protocol-identifier", ("node_protocol_identifier", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier)), ("prefixe", ("prefixe", Pce.TopologyNodes.TopologyNode.Prefixe)), ("ipv4-link", ("ipv4_link", Pce.TopologyNodes.TopologyNode.Ipv4Link)), ("ipv6-link", ("ipv6_link", Pce.TopologyNodes.TopologyNode.Ipv6Link))])
                self._leafs = OrderedDict([
                    ('node_identifier', (YLeaf(YType.uint32, 'node-identifier'), ['int'])),
                    ('node_identifier_xr', (YLeaf(YType.uint32, 'node-identifier-xr'), ['int'])),
                    ('overload', (YLeaf(YType.boolean, 'overload'), ['bool'])),
                ])
                self.node_identifier = None
                self.node_identifier_xr = None
                self.overload = None

                self.node_protocol_identifier = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"

                self.prefixe = YList(self)
                self.ipv4_link = YList(self)
                self.ipv6_link = YList(self)
                self._segment_path = lambda: "topology-node" + "[node-identifier='" + str(self.node_identifier) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/topology-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.TopologyNodes.TopologyNode, ['node_identifier', u'node_identifier_xr', u'overload'], name, value)


            class NodeProtocolIdentifier(Entity):
                """
                Node protocol identifier
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\: str
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\: bool
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\: bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of  		 :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("igp-information", ("igp_information", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation)), ("srgb-information", ("srgb_information", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ('ipv4_bgp_router_id_set', (YLeaf(YType.boolean, 'ipv4-bgp-router-id-set'), ['bool'])),
                        ('ipv4_bgp_router_id', (YLeaf(YType.str, 'ipv4-bgp-router-id'), ['str'])),
                        ('ipv4te_router_id_set', (YLeaf(YType.boolean, 'ipv4te-router-id-set'), ['bool'])),
                        ('ipv4te_router_id', (YLeaf(YType.str, 'ipv4te-router-id'), ['str'])),
                    ])
                    self.node_name = None
                    self.ipv4_bgp_router_id_set = None
                    self.ipv4_bgp_router_id = None
                    self.ipv4te_router_id_set = None
                    self.ipv4te_router_id = None

                    self.igp_information = YList(self)
                    self.srgb_information = YList(self)
                    self._segment_path = lambda: "node-protocol-identifier"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier, [u'node_name', u'ipv4_bgp_router_id_set', u'ipv4_bgp_router_id', u'ipv4te_router_id_set', u'ipv4te_router_id'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.node_id = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, [u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class SrgbInformation(Entity):
                    """
                    SRGB information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId>`
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation, self).__init__()

                        self.yang_name = "srgb-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.uint32, 'start'), ['int'])),
                            ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.start = None
                        self.size = None
                        self.domain_identifier = None

                        self.node_id = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "srgb-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation, [u'start', u'size', u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "srgb-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


            class Prefixe(Entity):
                """
                Prefixes
                
                .. attribute:: pfx_sid
                
                	Prefix SID
                	**type**\:  :py:class:`PfxSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid>`
                
                .. attribute:: node_id
                
                	Link\-state node identifier
                	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Prefixe.NodeId>`
                
                .. attribute:: domain_identifier
                
                	Domain identifier
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TopologyNodes.TopologyNode.Prefixe, self).__init__()

                    self.yang_name = "prefixe"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pfx-sid", ("pfx_sid", Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid)), ("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.Prefixe.NodeId))])
                    self._leafs = OrderedDict([
                        ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                    ])
                    self.domain_identifier = None

                    self.pfx_sid = Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid()
                    self.pfx_sid.parent = self
                    self._children_name_map["pfx_sid"] = "pfx-sid"

                    self.node_id = Pce.TopologyNodes.TopologyNode.Prefixe.NodeId()
                    self.node_id.parent = self
                    self._children_name_map["node_id"] = "node-id"
                    self._segment_path = lambda: "prefixe"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Prefixe, [u'domain_identifier'], name, value)


                class PfxSid(Entity):
                    """
                    Prefix SID
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\: bool
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\: bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\: bool
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\: bool
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\: bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid, self).__init__()

                        self.yang_name = "pfx-sid"
                        self.yang_parent_name = "prefixe"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Sid', '')])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ('rflag', (YLeaf(YType.boolean, 'rflag'), ['bool'])),
                            ('nflag', (YLeaf(YType.boolean, 'nflag'), ['bool'])),
                            ('pflag', (YLeaf(YType.boolean, 'pflag'), ['bool'])),
                            ('eflag', (YLeaf(YType.boolean, 'eflag'), ['bool'])),
                            ('vflag', (YLeaf(YType.boolean, 'vflag'), ['bool'])),
                            ('lflag', (YLeaf(YType.boolean, 'lflag'), ['bool'])),
                        ])
                        self.sid_type = None
                        self.mpls_label = None
                        self.rflag = None
                        self.nflag = None
                        self.pflag = None
                        self.eflag = None
                        self.vflag = None
                        self.lflag = None

                        self.sid_prefix = Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._segment_path = lambda: "pfx-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid, [u'sid_type', u'mpls_label', u'rflag', u'nflag', u'pflag', u'eflag', u'vflag', u'lflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "pfx-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid-prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Prefixe.PfxSid.SidPrefix, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class NodeId(Entity):
                    """
                    Link\-state node identifier
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp>`
                    
                    .. attribute:: autonomous_system_number
                    
                    	Autonomous System Number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ls_identifier
                    
                    	Link\-State identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId, self).__init__()

                        self.yang_name = "node-id"
                        self.yang_parent_name = "prefixe"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp))])
                        self._leafs = OrderedDict([
                            ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                            ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                        ])
                        self.autonomous_system_number = None
                        self.ls_identifier = None

                        self.igp = Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._segment_path = lambda: "node-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf>`
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "node-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp))])
                            self._leafs = OrderedDict([
                                ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                            ])
                            self.igp_id = None

                            self.isis = Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"

                            self.ospf = Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"

                            self.bgp = Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._segment_path = lambda: "igp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp, [u'igp_id'], name, value)


                        class Isis(Entity):
                            """
                            ISIS information
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\: str
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis, self).__init__()

                                self.yang_name = "isis"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                    ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                ])
                                self.system_id = None
                                self.level = None
                                self._segment_path = lambda: "isis"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                        class Ospf(Entity):
                            """
                            OSPF information
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf, self).__init__()

                                self.yang_name = "ospf"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                    ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                ])
                                self.router_id = None
                                self.area = None
                                self._segment_path = lambda: "ospf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: confed_asn
                            
                            	Confederation ASN
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                    ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                ])
                                self.router_id = None
                                self.confed_asn = None
                                self._segment_path = lambda: "bgp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Prefixe.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


            class Ipv4Link(Entity):
                """
                IPv4 Link information
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:  :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation>`
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:  :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: performance_metrics
                
                	Performance metrics
                	**type**\:  :py:class:`PerformanceMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics>`
                
                .. attribute:: local_ipv4_address
                
                	Local IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_ipv4_address
                
                	Remote IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: administrative_groups
                
                	Link admin\-groups
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: srlgs
                
                	SRLG Values
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of  		 :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link, self).__init__()

                    self.yang_name = "ipv4-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-igp-information", ("local_igp_information", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation)), ("remote-node-protocol-identifier", ("remote_node_protocol_identifier", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier)), ("performance-metrics", ("performance_metrics", Pce.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics)), ("adjacency-sid", ("adjacency_sid", Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid))])
                    self._leafs = OrderedDict([
                        ('local_ipv4_address', (YLeaf(YType.str, 'local-ipv4-address'), ['str'])),
                        ('remote_ipv4_address', (YLeaf(YType.str, 'remote-ipv4-address'), ['str'])),
                        ('igp_metric', (YLeaf(YType.uint32, 'igp-metric'), ['int'])),
                        ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                        ('maximum_link_bandwidth', (YLeaf(YType.uint64, 'maximum-link-bandwidth'), ['int'])),
                        ('max_reservable_bandwidth', (YLeaf(YType.uint64, 'max-reservable-bandwidth'), ['int'])),
                        ('administrative_groups', (YLeaf(YType.uint32, 'administrative-groups'), ['int'])),
                        ('srlgs', (YLeafList(YType.uint32, 'srlgs'), ['int'])),
                    ])
                    self.local_ipv4_address = None
                    self.remote_ipv4_address = None
                    self.igp_metric = None
                    self.te_metric = None
                    self.maximum_link_bandwidth = None
                    self.max_reservable_bandwidth = None
                    self.administrative_groups = None
                    self.srlgs = []

                    self.local_igp_information = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"

                    self.remote_node_protocol_identifier = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"

                    self.performance_metrics = Pce.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics()
                    self.performance_metrics.parent = self
                    self._children_name_map["performance_metrics"] = "performance-metrics"

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv4-link"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link, [u'local_ipv4_address', u'remote_ipv4_address', u'igp_metric', u'te_metric', u'maximum_link_bandwidth', u'max_reservable_bandwidth', u'administrative_groups', u'srlgs'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.node_id = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "local-igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, [u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class RemoteNodeProtocolIdentifier(Entity):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\: str
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\: bool
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\: bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of  		 :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp-information", ("igp_information", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation)), ("srgb-information", ("srgb_information", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('ipv4_bgp_router_id_set', (YLeaf(YType.boolean, 'ipv4-bgp-router-id-set'), ['bool'])),
                            ('ipv4_bgp_router_id', (YLeaf(YType.str, 'ipv4-bgp-router-id'), ['str'])),
                            ('ipv4te_router_id_set', (YLeaf(YType.boolean, 'ipv4te-router-id-set'), ['bool'])),
                            ('ipv4te_router_id', (YLeaf(YType.str, 'ipv4te-router-id'), ['str'])),
                        ])
                        self.node_name = None
                        self.ipv4_bgp_router_id_set = None
                        self.ipv4_bgp_router_id = None
                        self.ipv4te_router_id_set = None
                        self.ipv4te_router_id = None

                        self.igp_information = YList(self)
                        self.srgb_information = YList(self)
                        self._segment_path = lambda: "remote-node-protocol-identifier"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, [u'node_name', u'ipv4_bgp_router_id_set', u'ipv4_bgp_router_id', u'ipv4te_router_id_set', u'ipv4te_router_id'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: node_id
                        
                        	Link\-state node identifier
                        	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId>`
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId))])
                            self._leafs = OrderedDict([
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.domain_identifier = None

                            self.node_id = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId()
                            self.node_id.parent = self
                            self._children_name_map["node_id"] = "node-id"
                            self._segment_path = lambda: "igp-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, [u'domain_identifier'], name, value)


                        class NodeId(Entity):
                            """
                            Link\-state node identifier
                            
                            .. attribute:: igp
                            
                            	IGP\-specific information
                            	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp>`
                            
                            .. attribute:: autonomous_system_number
                            
                            	Autonomous System Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ls_identifier
                            
                            	Link\-State identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId, self).__init__()

                                self.yang_name = "node-id"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp))])
                                self._leafs = OrderedDict([
                                    ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                    ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                                ])
                                self.autonomous_system_number = None
                                self.ls_identifier = None

                                self.igp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                                self._segment_path = lambda: "node-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                            class Igp(Entity):
                                """
                                IGP\-specific information
                                
                                .. attribute:: isis
                                
                                	ISIS information
                                	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis>`
                                
                                .. attribute:: ospf
                                
                                	OSPF information
                                	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf>`
                                
                                .. attribute:: bgp
                                
                                	BGP information
                                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp>`
                                
                                .. attribute:: igp_id
                                
                                	IGP ID
                                	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp, self).__init__()

                                    self.yang_name = "igp"
                                    self.yang_parent_name = "node-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp))])
                                    self._leafs = OrderedDict([
                                        ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                    ])
                                    self.igp_id = None

                                    self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis()
                                    self.isis.parent = self
                                    self._children_name_map["isis"] = "isis"

                                    self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf()
                                    self.ospf.parent = self
                                    self._children_name_map["ospf"] = "ospf"

                                    self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp()
                                    self.bgp.parent = self
                                    self._children_name_map["bgp"] = "bgp"
                                    self._segment_path = lambda: "igp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                                class Isis(Entity):
                                    """
                                    ISIS information
                                    
                                    .. attribute:: system_id
                                    
                                    	ISIS system ID
                                    	**type**\: str
                                    
                                    .. attribute:: level
                                    
                                    	ISIS level
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, self).__init__()

                                        self.yang_name = "isis"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.system_id = None
                                        self.level = None
                                        self._segment_path = lambda: "isis"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                                class Ospf(Entity):
                                    """
                                    OSPF information
                                    
                                    .. attribute:: router_id
                                    
                                    	OSPF router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: area
                                    
                                    	OSPF area
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, self).__init__()

                                        self.yang_name = "ospf"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.area = None
                                        self._segment_path = lambda: "ospf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                                class Bgp(Entity):
                                    """
                                    BGP information
                                    
                                    .. attribute:: router_id
                                    
                                    	BGP router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: confed_asn
                                    
                                    	Confederation ASN
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.confed_asn = None
                                        self._segment_path = lambda: "bgp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                    class SrgbInformation(Entity):
                        """
                        SRGB information
                        
                        .. attribute:: node_id
                        
                        	Link\-state node identifier
                        	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId>`
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation, self).__init__()

                            self.yang_name = "srgb-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId))])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.uint32, 'start'), ['int'])),
                                ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.start = None
                            self.size = None
                            self.domain_identifier = None

                            self.node_id = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId()
                            self.node_id.parent = self
                            self._children_name_map["node_id"] = "node-id"
                            self._segment_path = lambda: "srgb-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation, [u'start', u'size', u'domain_identifier'], name, value)


                        class NodeId(Entity):
                            """
                            Link\-state node identifier
                            
                            .. attribute:: igp
                            
                            	IGP\-specific information
                            	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp>`
                            
                            .. attribute:: autonomous_system_number
                            
                            	Autonomous System Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ls_identifier
                            
                            	Link\-State identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId, self).__init__()

                                self.yang_name = "node-id"
                                self.yang_parent_name = "srgb-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp))])
                                self._leafs = OrderedDict([
                                    ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                    ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                                ])
                                self.autonomous_system_number = None
                                self.ls_identifier = None

                                self.igp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                                self._segment_path = lambda: "node-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                            class Igp(Entity):
                                """
                                IGP\-specific information
                                
                                .. attribute:: isis
                                
                                	ISIS information
                                	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis>`
                                
                                .. attribute:: ospf
                                
                                	OSPF information
                                	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf>`
                                
                                .. attribute:: bgp
                                
                                	BGP information
                                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp>`
                                
                                .. attribute:: igp_id
                                
                                	IGP ID
                                	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp, self).__init__()

                                    self.yang_name = "igp"
                                    self.yang_parent_name = "node-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp))])
                                    self._leafs = OrderedDict([
                                        ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                    ])
                                    self.igp_id = None

                                    self.isis = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis()
                                    self.isis.parent = self
                                    self._children_name_map["isis"] = "isis"

                                    self.ospf = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf()
                                    self.ospf.parent = self
                                    self._children_name_map["ospf"] = "ospf"

                                    self.bgp = Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp()
                                    self.bgp.parent = self
                                    self._children_name_map["bgp"] = "bgp"
                                    self._segment_path = lambda: "igp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp, [u'igp_id'], name, value)


                                class Isis(Entity):
                                    """
                                    ISIS information
                                    
                                    .. attribute:: system_id
                                    
                                    	ISIS system ID
                                    	**type**\: str
                                    
                                    .. attribute:: level
                                    
                                    	ISIS level
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, self).__init__()

                                        self.yang_name = "isis"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.system_id = None
                                        self.level = None
                                        self._segment_path = lambda: "isis"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                                class Ospf(Entity):
                                    """
                                    OSPF information
                                    
                                    .. attribute:: router_id
                                    
                                    	OSPF router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: area
                                    
                                    	OSPF area
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, self).__init__()

                                        self.yang_name = "ospf"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.area = None
                                        self._segment_path = lambda: "ospf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                                class Bgp(Entity):
                                    """
                                    BGP information
                                    
                                    .. attribute:: router_id
                                    
                                    	BGP router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: confed_asn
                                    
                                    	Confederation ASN
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.confed_asn = None
                                        self._segment_path = lambda: "bgp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class PerformanceMetrics(Entity):
                    """
                    Performance metrics
                    
                    .. attribute:: unidirectional_min_delay
                    
                    	Min delay
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics, self).__init__()

                        self.yang_name = "performance-metrics"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('unidirectional_min_delay', (YLeaf(YType.uint32, 'unidirectional-min-delay'), ['int'])),
                        ])
                        self.unidirectional_min_delay = None
                        self._segment_path = lambda: "performance-metrics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics, [u'unidirectional_min_delay'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\: bool
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\: bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\: bool
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\: bool
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\: bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Sid', '')])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ('rflag', (YLeaf(YType.boolean, 'rflag'), ['bool'])),
                            ('nflag', (YLeaf(YType.boolean, 'nflag'), ['bool'])),
                            ('pflag', (YLeaf(YType.boolean, 'pflag'), ['bool'])),
                            ('eflag', (YLeaf(YType.boolean, 'eflag'), ['bool'])),
                            ('vflag', (YLeaf(YType.boolean, 'vflag'), ['bool'])),
                            ('lflag', (YLeaf(YType.boolean, 'lflag'), ['bool'])),
                        ])
                        self.sid_type = None
                        self.mpls_label = None
                        self.rflag = None
                        self.nflag = None
                        self.pflag = None
                        self.eflag = None
                        self.vflag = None
                        self.lflag = None

                        self.sid_prefix = Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._segment_path = lambda: "adjacency-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, [u'sid_type', u'mpls_label', u'rflag', u'nflag', u'pflag', u'eflag', u'vflag', u'lflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid-prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class Ipv6Link(Entity):
                """
                IPv6 Link information
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:  :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation>`
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:  :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier>`
                
                .. attribute:: local_ipv6_address
                
                	Local IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_ipv6_address
                
                	Remote IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of  		 :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link, self).__init__()

                    self.yang_name = "ipv6-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-igp-information", ("local_igp_information", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation)), ("remote-node-protocol-identifier", ("remote_node_protocol_identifier", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier)), ("adjacency-sid", ("adjacency_sid", Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid))])
                    self._leafs = OrderedDict([
                        ('local_ipv6_address', (YLeaf(YType.str, 'local-ipv6-address'), ['str'])),
                        ('remote_ipv6_address', (YLeaf(YType.str, 'remote-ipv6-address'), ['str'])),
                        ('igp_metric', (YLeaf(YType.uint32, 'igp-metric'), ['int'])),
                        ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                        ('maximum_link_bandwidth', (YLeaf(YType.uint64, 'maximum-link-bandwidth'), ['int'])),
                        ('max_reservable_bandwidth', (YLeaf(YType.uint64, 'max-reservable-bandwidth'), ['int'])),
                    ])
                    self.local_ipv6_address = None
                    self.remote_ipv6_address = None
                    self.igp_metric = None
                    self.te_metric = None
                    self.maximum_link_bandwidth = None
                    self.max_reservable_bandwidth = None

                    self.local_igp_information = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"

                    self.remote_node_protocol_identifier = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv6-link"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link, [u'local_ipv6_address', u'remote_ipv6_address', u'igp_metric', u'te_metric', u'maximum_link_bandwidth', u'max_reservable_bandwidth'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.node_id = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "local-igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, [u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class RemoteNodeProtocolIdentifier(Entity):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\: str
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\: bool
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\: bool
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    .. attribute:: srgb_information
                    
                    	SRGB information
                    	**type**\: list of  		 :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp-information", ("igp_information", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation)), ("srgb-information", ("srgb_information", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation))])
                        self._leafs = OrderedDict([
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('ipv4_bgp_router_id_set', (YLeaf(YType.boolean, 'ipv4-bgp-router-id-set'), ['bool'])),
                            ('ipv4_bgp_router_id', (YLeaf(YType.str, 'ipv4-bgp-router-id'), ['str'])),
                            ('ipv4te_router_id_set', (YLeaf(YType.boolean, 'ipv4te-router-id-set'), ['bool'])),
                            ('ipv4te_router_id', (YLeaf(YType.str, 'ipv4te-router-id'), ['str'])),
                        ])
                        self.node_name = None
                        self.ipv4_bgp_router_id_set = None
                        self.ipv4_bgp_router_id = None
                        self.ipv4te_router_id_set = None
                        self.ipv4te_router_id = None

                        self.igp_information = YList(self)
                        self.srgb_information = YList(self)
                        self._segment_path = lambda: "remote-node-protocol-identifier"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, [u'node_name', u'ipv4_bgp_router_id_set', u'ipv4_bgp_router_id', u'ipv4te_router_id_set', u'ipv4te_router_id'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: node_id
                        
                        	Link\-state node identifier
                        	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId>`
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId))])
                            self._leafs = OrderedDict([
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.domain_identifier = None

                            self.node_id = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId()
                            self.node_id.parent = self
                            self._children_name_map["node_id"] = "node-id"
                            self._segment_path = lambda: "igp-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, [u'domain_identifier'], name, value)


                        class NodeId(Entity):
                            """
                            Link\-state node identifier
                            
                            .. attribute:: igp
                            
                            	IGP\-specific information
                            	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp>`
                            
                            .. attribute:: autonomous_system_number
                            
                            	Autonomous System Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ls_identifier
                            
                            	Link\-State identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId, self).__init__()

                                self.yang_name = "node-id"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp))])
                                self._leafs = OrderedDict([
                                    ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                    ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                                ])
                                self.autonomous_system_number = None
                                self.ls_identifier = None

                                self.igp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                                self._segment_path = lambda: "node-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                            class Igp(Entity):
                                """
                                IGP\-specific information
                                
                                .. attribute:: isis
                                
                                	ISIS information
                                	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis>`
                                
                                .. attribute:: ospf
                                
                                	OSPF information
                                	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf>`
                                
                                .. attribute:: bgp
                                
                                	BGP information
                                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp>`
                                
                                .. attribute:: igp_id
                                
                                	IGP ID
                                	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp, self).__init__()

                                    self.yang_name = "igp"
                                    self.yang_parent_name = "node-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp))])
                                    self._leafs = OrderedDict([
                                        ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                    ])
                                    self.igp_id = None

                                    self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis()
                                    self.isis.parent = self
                                    self._children_name_map["isis"] = "isis"

                                    self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf()
                                    self.ospf.parent = self
                                    self._children_name_map["ospf"] = "ospf"

                                    self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp()
                                    self.bgp.parent = self
                                    self._children_name_map["bgp"] = "bgp"
                                    self._segment_path = lambda: "igp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                                class Isis(Entity):
                                    """
                                    ISIS information
                                    
                                    .. attribute:: system_id
                                    
                                    	ISIS system ID
                                    	**type**\: str
                                    
                                    .. attribute:: level
                                    
                                    	ISIS level
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, self).__init__()

                                        self.yang_name = "isis"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.system_id = None
                                        self.level = None
                                        self._segment_path = lambda: "isis"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                                class Ospf(Entity):
                                    """
                                    OSPF information
                                    
                                    .. attribute:: router_id
                                    
                                    	OSPF router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: area
                                    
                                    	OSPF area
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, self).__init__()

                                        self.yang_name = "ospf"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.area = None
                                        self._segment_path = lambda: "ospf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                                class Bgp(Entity):
                                    """
                                    BGP information
                                    
                                    .. attribute:: router_id
                                    
                                    	BGP router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: confed_asn
                                    
                                    	Confederation ASN
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.confed_asn = None
                                        self._segment_path = lambda: "bgp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                    class SrgbInformation(Entity):
                        """
                        SRGB information
                        
                        .. attribute:: node_id
                        
                        	Link\-state node identifier
                        	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId>`
                        
                        .. attribute:: start
                        
                        	SRGB start
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: size
                        
                        	SRGB size
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation, self).__init__()

                            self.yang_name = "srgb-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-id", ("node_id", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId))])
                            self._leafs = OrderedDict([
                                ('start', (YLeaf(YType.uint32, 'start'), ['int'])),
                                ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.start = None
                            self.size = None
                            self.domain_identifier = None

                            self.node_id = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId()
                            self.node_id.parent = self
                            self._children_name_map["node_id"] = "node-id"
                            self._segment_path = lambda: "srgb-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation, [u'start', u'size', u'domain_identifier'], name, value)


                        class NodeId(Entity):
                            """
                            Link\-state node identifier
                            
                            .. attribute:: igp
                            
                            	IGP\-specific information
                            	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp>`
                            
                            .. attribute:: autonomous_system_number
                            
                            	Autonomous System Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ls_identifier
                            
                            	Link\-State identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId, self).__init__()

                                self.yang_name = "node-id"
                                self.yang_parent_name = "srgb-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("igp", ("igp", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp))])
                                self._leafs = OrderedDict([
                                    ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                    ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                                ])
                                self.autonomous_system_number = None
                                self.ls_identifier = None

                                self.igp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                                self._segment_path = lambda: "node-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                            class Igp(Entity):
                                """
                                IGP\-specific information
                                
                                .. attribute:: isis
                                
                                	ISIS information
                                	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis>`
                                
                                .. attribute:: ospf
                                
                                	OSPF information
                                	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf>`
                                
                                .. attribute:: bgp
                                
                                	BGP information
                                	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp>`
                                
                                .. attribute:: igp_id
                                
                                	IGP ID
                                	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp, self).__init__()

                                    self.yang_name = "igp"
                                    self.yang_parent_name = "node-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("isis", ("isis", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp))])
                                    self._leafs = OrderedDict([
                                        ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                    ])
                                    self.igp_id = None

                                    self.isis = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis()
                                    self.isis.parent = self
                                    self._children_name_map["isis"] = "isis"

                                    self.ospf = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf()
                                    self.ospf.parent = self
                                    self._children_name_map["ospf"] = "ospf"

                                    self.bgp = Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp()
                                    self.bgp.parent = self
                                    self._children_name_map["bgp"] = "bgp"
                                    self._segment_path = lambda: "igp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp, [u'igp_id'], name, value)


                                class Isis(Entity):
                                    """
                                    ISIS information
                                    
                                    .. attribute:: system_id
                                    
                                    	ISIS system ID
                                    	**type**\: str
                                    
                                    .. attribute:: level
                                    
                                    	ISIS level
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, self).__init__()

                                        self.yang_name = "isis"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.system_id = None
                                        self.level = None
                                        self._segment_path = lambda: "isis"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                                class Ospf(Entity):
                                    """
                                    OSPF information
                                    
                                    .. attribute:: router_id
                                    
                                    	OSPF router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: area
                                    
                                    	OSPF area
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, self).__init__()

                                        self.yang_name = "ospf"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.area = None
                                        self._segment_path = lambda: "ospf"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                                class Bgp(Entity):
                                    """
                                    BGP information
                                    
                                    .. attribute:: router_id
                                    
                                    	BGP router ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: confed_asn
                                    
                                    	Confederation ASN
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'infra-xtc-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "igp"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                            ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                        ])
                                        self.router_id = None
                                        self.confed_asn = None
                                        self._segment_path = lambda: "bgp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Sid>`
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rflag
                    
                    	R Flag
                    	**type**\: bool
                    
                    .. attribute:: nflag
                    
                    	N Flag
                    	**type**\: bool
                    
                    .. attribute:: pflag
                    
                    	P Flag
                    	**type**\: bool
                    
                    .. attribute:: eflag
                    
                    	E Flag
                    	**type**\: bool
                    
                    .. attribute:: vflag
                    
                    	V Flag
                    	**type**\: bool
                    
                    .. attribute:: lflag
                    
                    	L Flag
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'Sid', '')])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ('rflag', (YLeaf(YType.boolean, 'rflag'), ['bool'])),
                            ('nflag', (YLeaf(YType.boolean, 'nflag'), ['bool'])),
                            ('pflag', (YLeaf(YType.boolean, 'pflag'), ['bool'])),
                            ('eflag', (YLeaf(YType.boolean, 'eflag'), ['bool'])),
                            ('vflag', (YLeaf(YType.boolean, 'vflag'), ['bool'])),
                            ('lflag', (YLeaf(YType.boolean, 'lflag'), ['bool'])),
                        ])
                        self.sid_type = None
                        self.mpls_label = None
                        self.rflag = None
                        self.nflag = None
                        self.pflag = None
                        self.eflag = None
                        self.vflag = None
                        self.lflag = None

                        self.sid_prefix = Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._segment_path = lambda: "adjacency-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, [u'sid_type', u'mpls_label', u'rflag', u'nflag', u'pflag', u'eflag', u'vflag', u'lflag'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid-prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, [u'af_name', u'ipv4', u'ipv6'], name, value)


    class PrefixInfos(Entity):
        """
        Prefixes database in XTC
        
        .. attribute:: prefix_info
        
        	PCE prefix information
        	**type**\: list of  		 :py:class:`PrefixInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.PrefixInfos, self).__init__()

            self.yang_name = "prefix-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prefix-info", ("prefix_info", Pce.PrefixInfos.PrefixInfo))])
            self._leafs = OrderedDict()

            self.prefix_info = YList(self)
            self._segment_path = lambda: "prefix-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.PrefixInfos, [], name, value)


        class PrefixInfo(Entity):
            """
            PCE prefix information
            
            .. attribute:: node_identifier  (key)
            
            	Node ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:  :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: address
            
            	Prefix address
            	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.Address>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.PrefixInfos.PrefixInfo, self).__init__()

                self.yang_name = "prefix-info"
                self.yang_parent_name = "prefix-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_identifier']
                self._child_classes = OrderedDict([("node-protocol-identifier", ("node_protocol_identifier", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier)), ("address", ("address", Pce.PrefixInfos.PrefixInfo.Address))])
                self._leafs = OrderedDict([
                    ('node_identifier', (YLeaf(YType.uint32, 'node-identifier'), ['int'])),
                    ('node_identifier_xr', (YLeaf(YType.uint32, 'node-identifier-xr'), ['int'])),
                ])
                self.node_identifier = None
                self.node_identifier_xr = None

                self.node_protocol_identifier = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"

                self.address = YList(self)
                self._segment_path = lambda: "prefix-info" + "[node-identifier='" + str(self.node_identifier) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/prefix-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.PrefixInfos.PrefixInfo, ['node_identifier', u'node_identifier_xr'], name, value)


            class NodeProtocolIdentifier(Entity):
                """
                Node protocol identifier
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\: str
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\: bool
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\: bool
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation>`
                
                .. attribute:: srgb_information
                
                	SRGB information
                	**type**\: list of  		 :py:class:`SrgbInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("igp-information", ("igp_information", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation)), ("srgb-information", ("srgb_information", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                        ('ipv4_bgp_router_id_set', (YLeaf(YType.boolean, 'ipv4-bgp-router-id-set'), ['bool'])),
                        ('ipv4_bgp_router_id', (YLeaf(YType.str, 'ipv4-bgp-router-id'), ['str'])),
                        ('ipv4te_router_id_set', (YLeaf(YType.boolean, 'ipv4te-router-id-set'), ['bool'])),
                        ('ipv4te_router_id', (YLeaf(YType.str, 'ipv4te-router-id'), ['str'])),
                    ])
                    self.node_name = None
                    self.ipv4_bgp_router_id_set = None
                    self.ipv4_bgp_router_id = None
                    self.ipv4te_router_id_set = None
                    self.ipv4te_router_id = None

                    self.igp_information = YList(self)
                    self.srgb_information = YList(self)
                    self._segment_path = lambda: "node-protocol-identifier"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, [u'node_name', u'ipv4_bgp_router_id_set', u'ipv4_bgp_router_id', u'ipv4te_router_id_set', u'ipv4te_router_id'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.node_id = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, [u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


                class SrgbInformation(Entity):
                    """
                    SRGB information
                    
                    .. attribute:: node_id
                    
                    	Link\-state node identifier
                    	**type**\:  :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId>`
                    
                    .. attribute:: start
                    
                    	SRGB start
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: size
                    
                    	SRGB size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation, self).__init__()

                        self.yang_name = "srgb-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId))])
                        self._leafs = OrderedDict([
                            ('start', (YLeaf(YType.uint32, 'start'), ['int'])),
                            ('size', (YLeaf(YType.uint32, 'size'), ['int'])),
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.start = None
                        self.size = None
                        self.domain_identifier = None

                        self.node_id = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId()
                        self.node_id.parent = self
                        self._children_name_map["node_id"] = "node-id"
                        self._segment_path = lambda: "srgb-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation, [u'start', u'size', u'domain_identifier'], name, value)


                    class NodeId(Entity):
                        """
                        Link\-state node identifier
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp>`
                        
                        .. attribute:: autonomous_system_number
                        
                        	Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ls_identifier
                        
                        	Link\-State identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "srgb-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                                ('ls_identifier', (YLeaf(YType.uint32, 'ls-identifier'), ['int'])),
                            ])
                            self.autonomous_system_number = None
                            self.ls_identifier = None

                            self.igp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "node-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId, [u'autonomous_system_number', u'ls_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`PceIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "node-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis)), ("ospf", ("ospf", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf)), ("bgp", ("bgp", Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp, [u'igp_id'], name, value)


                            class Isis(Entity):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, self).__init__()

                                    self.yang_name = "isis"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('system_id', (YLeaf(YType.str, 'system-id'), ['str'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.system_id = None
                                    self.level = None
                                    self._segment_path = lambda: "isis"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Isis, [u'system_id', u'level'], name, value)


                            class Ospf(Entity):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, self).__init__()

                                    self.yang_name = "ospf"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('area', (YLeaf(YType.uint32, 'area'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.area = None
                                    self._segment_path = lambda: "ospf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Ospf, [u'router_id', u'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: confed_asn
                                
                                	Confederation ASN
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-xtc-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('confed_asn', (YLeaf(YType.uint32, 'confed-asn'), ['int'])),
                                    ])
                                    self.router_id = None
                                    self.confed_asn = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.SrgbInformation.NodeId.Igp.Bgp, [u'router_id', u'confed_asn'], name, value)


            class Address(Entity):
                """
                Prefix address
                
                .. attribute:: ip
                
                	Prefix IP address
                	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PrefixInfos.PrefixInfo.Address.Ip>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.PrefixInfos.PrefixInfo.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ip", ("ip", Pce.PrefixInfos.PrefixInfo.Address.Ip))])
                    self._leafs = OrderedDict()

                    self.ip = Pce.PrefixInfos.PrefixInfo.Address.Ip()
                    self.ip.parent = self
                    self._children_name_map["ip"] = "ip"
                    self._segment_path = lambda: "address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PrefixInfos.PrefixInfo.Address, [], name, value)


                class Ip(Entity):
                    """
                    Prefix IP address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.PrefixInfos.PrefixInfo.Address.Ip, self).__init__()

                        self.yang_name = "ip"
                        self.yang_parent_name = "address"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "ip"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.PrefixInfos.PrefixInfo.Address.Ip, [u'af_name', u'ipv4', u'ipv6'], name, value)


    class LspSummary(Entity):
        """
        LSP summary database in XTC
        
        .. attribute:: all_ls_ps
        
        	Summary for all peers
        	**type**\:  :py:class:`AllLsPs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.AllLsPs>`
        
        .. attribute:: peer_ls_ps_info
        
        	Number of LSPs for specific peer
        	**type**\: list of  		 :py:class:`PeerLsPsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.PeerLsPsInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.LspSummary, self).__init__()

            self.yang_name = "lsp-summary"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("all-ls-ps", ("all_ls_ps", Pce.LspSummary.AllLsPs)), ("peer-ls-ps-info", ("peer_ls_ps_info", Pce.LspSummary.PeerLsPsInfo))])
            self._leafs = OrderedDict()

            self.all_ls_ps = Pce.LspSummary.AllLsPs()
            self.all_ls_ps.parent = self
            self._children_name_map["all_ls_ps"] = "all-ls-ps"

            self.peer_ls_ps_info = YList(self)
            self._segment_path = lambda: "lsp-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.LspSummary, [], name, value)


        class AllLsPs(Entity):
            """
            Summary for all peers
            
            .. attribute:: all_ls_ps
            
            	Number of all LSPs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_ls_ps
            
            	Number of operational LSPs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: admin_up_ls_ps
            
            	Number of administratively up LSPs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sr_ls_ps
            
            	Number of LSPs with Segment routing setup type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvp_ls_ps
            
            	Number of LSPs with RSVP setup type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.LspSummary.AllLsPs, self).__init__()

                self.yang_name = "all-ls-ps"
                self.yang_parent_name = "lsp-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('all_ls_ps', (YLeaf(YType.uint32, 'all-ls-ps'), ['int'])),
                    ('up_ls_ps', (YLeaf(YType.uint32, 'up-ls-ps'), ['int'])),
                    ('admin_up_ls_ps', (YLeaf(YType.uint32, 'admin-up-ls-ps'), ['int'])),
                    ('sr_ls_ps', (YLeaf(YType.uint32, 'sr-ls-ps'), ['int'])),
                    ('rsvp_ls_ps', (YLeaf(YType.uint32, 'rsvp-ls-ps'), ['int'])),
                ])
                self.all_ls_ps = None
                self.up_ls_ps = None
                self.admin_up_ls_ps = None
                self.sr_ls_ps = None
                self.rsvp_ls_ps = None
                self._segment_path = lambda: "all-ls-ps"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/lsp-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.LspSummary.AllLsPs, [u'all_ls_ps', u'up_ls_ps', u'admin_up_ls_ps', u'sr_ls_ps', u'rsvp_ls_ps'], name, value)


        class PeerLsPsInfo(Entity):
            """
            Number of LSPs for specific peer
            
            .. attribute:: lsp_summary
            
            	Number of LSPs for specific peer
            	**type**\:  :py:class:`LspSummary_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.PeerLsPsInfo.LspSummary_>`
            
            .. attribute:: peer_address
            
            	Peer address
            	**type**\:  :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.LspSummary.PeerLsPsInfo.PeerAddress>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.LspSummary.PeerLsPsInfo, self).__init__()

                self.yang_name = "peer-ls-ps-info"
                self.yang_parent_name = "lsp-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("lsp-summary", ("lsp_summary", Pce.LspSummary.PeerLsPsInfo.LspSummary_)), ("peer-address", ("peer_address", Pce.LspSummary.PeerLsPsInfo.PeerAddress))])
                self._leafs = OrderedDict()

                self.lsp_summary = Pce.LspSummary.PeerLsPsInfo.LspSummary_()
                self.lsp_summary.parent = self
                self._children_name_map["lsp_summary"] = "lsp-summary"

                self.peer_address = Pce.LspSummary.PeerLsPsInfo.PeerAddress()
                self.peer_address.parent = self
                self._children_name_map["peer_address"] = "peer-address"
                self._segment_path = lambda: "peer-ls-ps-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/lsp-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.LspSummary.PeerLsPsInfo, [], name, value)


            class LspSummary_(Entity):
                """
                Number of LSPs for specific peer
                
                .. attribute:: all_ls_ps
                
                	Number of all LSPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up_ls_ps
                
                	Number of operational LSPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: admin_up_ls_ps
                
                	Number of administratively up LSPs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sr_ls_ps
                
                	Number of LSPs with Segment routing setup type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: rsvp_ls_ps
                
                	Number of LSPs with RSVP setup type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.LspSummary.PeerLsPsInfo.LspSummary_, self).__init__()

                    self.yang_name = "lsp-summary"
                    self.yang_parent_name = "peer-ls-ps-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('all_ls_ps', (YLeaf(YType.uint32, 'all-ls-ps'), ['int'])),
                        ('up_ls_ps', (YLeaf(YType.uint32, 'up-ls-ps'), ['int'])),
                        ('admin_up_ls_ps', (YLeaf(YType.uint32, 'admin-up-ls-ps'), ['int'])),
                        ('sr_ls_ps', (YLeaf(YType.uint32, 'sr-ls-ps'), ['int'])),
                        ('rsvp_ls_ps', (YLeaf(YType.uint32, 'rsvp-ls-ps'), ['int'])),
                    ])
                    self.all_ls_ps = None
                    self.up_ls_ps = None
                    self.admin_up_ls_ps = None
                    self.sr_ls_ps = None
                    self.rsvp_ls_ps = None
                    self._segment_path = lambda: "lsp-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/lsp-summary/peer-ls-ps-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.LspSummary.PeerLsPsInfo.LspSummary_, [u'all_ls_ps', u'up_ls_ps', u'admin_up_ls_ps', u'sr_ls_ps', u'rsvp_ls_ps'], name, value)


            class PeerAddress(Entity):
                """
                Peer address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.LspSummary.PeerLsPsInfo.PeerAddress, self).__init__()

                    self.yang_name = "peer-address"
                    self.yang_parent_name = "peer-ls-ps-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "peer-address"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/lsp-summary/peer-ls-ps-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.LspSummary.PeerLsPsInfo.PeerAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


    class PeerInfos(Entity):
        """
        Peers database in XTC
        
        .. attribute:: peer_info
        
        	PCE peer information
        	**type**\: list of  		 :py:class:`PeerInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos.PeerInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.PeerInfos, self).__init__()

            self.yang_name = "peer-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("peer-info", ("peer_info", Pce.PeerInfos.PeerInfo))])
            self._leafs = OrderedDict()

            self.peer_info = YList(self)
            self._segment_path = lambda: "peer-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.PeerInfos, [], name, value)


        class PeerInfo(Entity):
            """
            PCE peer information
            
            .. attribute:: peer_address  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_address_xr
            
            	Peer address
            	**type**\:  :py:class:`PeerAddressXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos.PeerInfo.PeerAddressXr>`
            
            .. attribute:: brief_pcep_information
            
            	PCE protocol information
            	**type**\:  :py:class:`BriefPcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.PeerInfos.PeerInfo.BriefPcepInformation>`
            
            .. attribute:: peer_protocol
            
            	Protocol between PCE and peer
            	**type**\:  :py:class:`PceProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceProto>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.PeerInfos.PeerInfo, self).__init__()

                self.yang_name = "peer-info"
                self.yang_parent_name = "peer-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_address']
                self._child_classes = OrderedDict([("peer-address-xr", ("peer_address_xr", Pce.PeerInfos.PeerInfo.PeerAddressXr)), ("brief-pcep-information", ("brief_pcep_information", Pce.PeerInfos.PeerInfo.BriefPcepInformation))])
                self._leafs = OrderedDict([
                    ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str','str'])),
                    ('peer_protocol', (YLeaf(YType.enumeration, 'peer-protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceProto', '')])),
                ])
                self.peer_address = None
                self.peer_protocol = None

                self.peer_address_xr = Pce.PeerInfos.PeerInfo.PeerAddressXr()
                self.peer_address_xr.parent = self
                self._children_name_map["peer_address_xr"] = "peer-address-xr"

                self.brief_pcep_information = Pce.PeerInfos.PeerInfo.BriefPcepInformation()
                self.brief_pcep_information.parent = self
                self._children_name_map["brief_pcep_information"] = "brief-pcep-information"
                self._segment_path = lambda: "peer-info" + "[peer-address='" + str(self.peer_address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/peer-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.PeerInfos.PeerInfo, ['peer_address', u'peer_protocol'], name, value)


            class PeerAddressXr(Entity):
                """
                Peer address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.PeerInfos.PeerInfo.PeerAddressXr, self).__init__()

                    self.yang_name = "peer-address-xr"
                    self.yang_parent_name = "peer-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "peer-address-xr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PeerInfos.PeerInfo.PeerAddressXr, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class BriefPcepInformation(Entity):
                """
                PCE protocol information
                
                .. attribute:: pcep_state
                
                	PCEP State
                	**type**\:  :py:class:`PcepState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepState>`
                
                .. attribute:: stateful
                
                	Stateful
                	**type**\: bool
                
                .. attribute:: capability_update
                
                	Update capability
                	**type**\: bool
                
                .. attribute:: capability_instantiate
                
                	Instantiation capability
                	**type**\: bool
                
                .. attribute:: capability_segment_routing
                
                	Segment Routing capability
                	**type**\: bool
                
                .. attribute:: capability_triggered_sync
                
                	Triggered Synchronization capability
                	**type**\: bool
                
                .. attribute:: capability_db_version
                
                	DB version capability
                	**type**\: bool
                
                .. attribute:: capability_delta_sync
                
                	Delta Synchronization capability
                	**type**\: bool
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.PeerInfos.PeerInfo.BriefPcepInformation, self).__init__()

                    self.yang_name = "brief-pcep-information"
                    self.yang_parent_name = "peer-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('pcep_state', (YLeaf(YType.enumeration, 'pcep-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepState', '')])),
                        ('stateful', (YLeaf(YType.boolean, 'stateful'), ['bool'])),
                        ('capability_update', (YLeaf(YType.boolean, 'capability-update'), ['bool'])),
                        ('capability_instantiate', (YLeaf(YType.boolean, 'capability-instantiate'), ['bool'])),
                        ('capability_segment_routing', (YLeaf(YType.boolean, 'capability-segment-routing'), ['bool'])),
                        ('capability_triggered_sync', (YLeaf(YType.boolean, 'capability-triggered-sync'), ['bool'])),
                        ('capability_db_version', (YLeaf(YType.boolean, 'capability-db-version'), ['bool'])),
                        ('capability_delta_sync', (YLeaf(YType.boolean, 'capability-delta-sync'), ['bool'])),
                    ])
                    self.pcep_state = None
                    self.stateful = None
                    self.capability_update = None
                    self.capability_instantiate = None
                    self.capability_segment_routing = None
                    self.capability_triggered_sync = None
                    self.capability_db_version = None
                    self.capability_delta_sync = None
                    self._segment_path = lambda: "brief-pcep-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.PeerInfos.PeerInfo.BriefPcepInformation, [u'pcep_state', u'stateful', u'capability_update', u'capability_instantiate', u'capability_segment_routing', u'capability_triggered_sync', u'capability_db_version', u'capability_delta_sync'], name, value)


    class TunnelDetailInfos(Entity):
        """
        Detailed tunnel database in XTC
        
        .. attribute:: tunnel_detail_info
        
        	Detailed tunnel information
        	**type**\: list of  		 :py:class:`TunnelDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo>`
        
        

        """

        _prefix = 'infra-xtc-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Pce.TunnelDetailInfos, self).__init__()

            self.yang_name = "tunnel-detail-infos"
            self.yang_parent_name = "pce"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel-detail-info", ("tunnel_detail_info", Pce.TunnelDetailInfos.TunnelDetailInfo))])
            self._leafs = OrderedDict()

            self.tunnel_detail_info = YList(self)
            self._segment_path = lambda: "tunnel-detail-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pce.TunnelDetailInfos, [], name, value)


        class TunnelDetailInfo(Entity):
            """
            Detailed tunnel information
            
            .. attribute:: peer_address  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: plsp_id  (key)
            
            	PCEP LSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tunnel_name  (key)
            
            	Tunnel name
            	**type**\: str
            
            .. attribute:: pcc_address
            
            	PCC address
            	**type**\:  :py:class:`PccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.PccAddress>`
            
            .. attribute:: private_lsp_information
            
            	Private LSP information
            	**type**\:  :py:class:`PrivateLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation>`
            
            .. attribute:: tunnel_name_xr
            
            	Tunnel Name
            	**type**\: str
            
            .. attribute:: xtc_controlled
            
            	Allow XTC reoptimizations
            	**type**\: bool
            
            .. attribute:: color
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: detail_lsp_information
            
            	Detail LSP information
            	**type**\: list of  		 :py:class:`DetailLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation>`
            
            

            """

            _prefix = 'infra-xtc-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Pce.TunnelDetailInfos.TunnelDetailInfo, self).__init__()

                self.yang_name = "tunnel-detail-info"
                self.yang_parent_name = "tunnel-detail-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_address','plsp_id','tunnel_name']
                self._child_classes = OrderedDict([("pcc-address", ("pcc_address", Pce.TunnelDetailInfos.TunnelDetailInfo.PccAddress)), ("private-lsp-information", ("private_lsp_information", Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation)), ("detail-lsp-information", ("detail_lsp_information", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation))])
                self._leafs = OrderedDict([
                    ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str','str'])),
                    ('plsp_id', (YLeaf(YType.uint32, 'plsp-id'), ['int'])),
                    ('tunnel_name', (YLeaf(YType.str, 'tunnel-name'), ['str'])),
                    ('tunnel_name_xr', (YLeaf(YType.str, 'tunnel-name-xr'), ['str'])),
                    ('xtc_controlled', (YLeaf(YType.boolean, 'xtc-controlled'), ['bool'])),
                    ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                ])
                self.peer_address = None
                self.plsp_id = None
                self.tunnel_name = None
                self.tunnel_name_xr = None
                self.xtc_controlled = None
                self.color = None

                self.pcc_address = Pce.TunnelDetailInfos.TunnelDetailInfo.PccAddress()
                self.pcc_address.parent = self
                self._children_name_map["pcc_address"] = "pcc-address"

                self.private_lsp_information = Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation()
                self.private_lsp_information.parent = self
                self._children_name_map["private_lsp_information"] = "private-lsp-information"

                self.detail_lsp_information = YList(self)
                self._segment_path = lambda: "tunnel-detail-info" + "[peer-address='" + str(self.peer_address) + "']" + "[plsp-id='" + str(self.plsp_id) + "']" + "[tunnel-name='" + str(self.tunnel_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-oper:pce/tunnel-detail-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo, ['peer_address', 'plsp_id', 'tunnel_name', u'tunnel_name_xr', u'xtc_controlled', u'color'], name, value)


            class PccAddress(Entity):
                """
                PCC address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TunnelDetailInfos.TunnelDetailInfo.PccAddress, self).__init__()

                    self.yang_name = "pcc-address"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "pcc-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.PccAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


            class PrivateLspInformation(Entity):
                """
                Private LSP information
                
                .. attribute:: event_buffer
                
                	LSP Event buffer
                	**type**\: list of  		 :py:class:`EventBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation, self).__init__()

                    self.yang_name = "private-lsp-information"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("event-buffer", ("event_buffer", Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer))])
                    self._leafs = OrderedDict()

                    self.event_buffer = YList(self)
                    self._segment_path = lambda: "private-lsp-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation, [], name, value)


                class EventBuffer(Entity):
                    """
                    LSP Event buffer
                    
                    .. attribute:: event_id
                    
                    	Event ID in range 1 \- 0xFFFFFFFF. 0 is invalid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: event_message
                    
                    	Event message
                    	**type**\: str
                    
                    .. attribute:: time_stamp
                    
                    	Event time, relative to Jan 1, 1970
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer, self).__init__()

                        self.yang_name = "event-buffer"
                        self.yang_parent_name = "private-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('event_id', (YLeaf(YType.uint32, 'event-id'), ['int'])),
                            ('event_message', (YLeaf(YType.str, 'event-message'), ['str'])),
                            ('time_stamp', (YLeaf(YType.uint32, 'time-stamp'), ['int'])),
                        ])
                        self.event_id = None
                        self.event_message = None
                        self.time_stamp = None
                        self._segment_path = lambda: "event-buffer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.PrivateLspInformation.EventBuffer, [u'event_id', u'event_message', u'time_stamp'], name, value)


            class DetailLspInformation(Entity):
                """
                Detail LSP information
                
                .. attribute:: brief_lsp_information
                
                	Brief LSP information
                	**type**\:  :py:class:`BriefLspInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation>`
                
                .. attribute:: er_os
                
                	Paths
                	**type**\:  :py:class:`ErOs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs>`
                
                .. attribute:: lsppcep_information
                
                	PCEP related LSP information
                	**type**\:  :py:class:`LsppcepInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation>`
                
                .. attribute:: lsp_association_info
                
                	LSP association information
                	**type**\:  :py:class:`LspAssociationInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo>`
                
                .. attribute:: lsp_attributes
                
                	LSP attributes
                	**type**\:  :py:class:`LspAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes>`
                
                .. attribute:: sub_delegated_pce
                
                	Sub delegated PCE
                	**type**\:  :py:class:`SubDelegatedPce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce>`
                
                .. attribute:: state_sync_pce
                
                	State\-sync PCE
                	**type**\:  :py:class:`StateSyncPce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce>`
                
                .. attribute:: reporting_pcc_address
                
                	Reporting PCC address
                	**type**\:  :py:class:`ReportingPccAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress>`
                
                .. attribute:: signaled_bandwidth_specified
                
                	True if router notifies signal bandwidth
                	**type**\: bool
                
                .. attribute:: signaled_bandwidth
                
                	Signaled Bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: actual_bandwidth_specified
                
                	True if router notifies actual bandwidth
                	**type**\: bool
                
                .. attribute:: actual_bandwidth
                
                	Actual bandwidth utilized in the data\-plane
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: lsp_role
                
                	LSP Role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: computing_pce
                
                	Computing PCE
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: srlg_info
                
                	List of SLRGs used by LSP
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: rro
                
                	RRO
                	**type**\: list of  		 :py:class:`Rro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro>`
                
                

                """

                _prefix = 'infra-xtc-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation, self).__init__()

                    self.yang_name = "detail-lsp-information"
                    self.yang_parent_name = "tunnel-detail-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("brief-lsp-information", ("brief_lsp_information", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation)), ("er-os", ("er_os", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs)), ("lsppcep-information", ("lsppcep_information", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation)), ("lsp-association-info", ("lsp_association_info", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo)), ("lsp-attributes", ("lsp_attributes", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes)), ("sub-delegated-pce", ("sub_delegated_pce", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce)), ("state-sync-pce", ("state_sync_pce", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce)), ("reporting-pcc-address", ("reporting_pcc_address", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress)), ("rro", ("rro", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro))])
                    self._leafs = OrderedDict([
                        ('signaled_bandwidth_specified', (YLeaf(YType.boolean, 'signaled-bandwidth-specified'), ['bool'])),
                        ('signaled_bandwidth', (YLeaf(YType.uint64, 'signaled-bandwidth'), ['int'])),
                        ('actual_bandwidth_specified', (YLeaf(YType.boolean, 'actual-bandwidth-specified'), ['bool'])),
                        ('actual_bandwidth', (YLeaf(YType.uint64, 'actual-bandwidth'), ['int'])),
                        ('lsp_role', (YLeaf(YType.uint32, 'lsp-role'), ['int'])),
                        ('computing_pce', (YLeaf(YType.uint32, 'computing-pce'), ['int'])),
                        ('srlg_info', (YLeafList(YType.uint32, 'srlg-info'), ['int'])),
                    ])
                    self.signaled_bandwidth_specified = None
                    self.signaled_bandwidth = None
                    self.actual_bandwidth_specified = None
                    self.actual_bandwidth = None
                    self.lsp_role = None
                    self.computing_pce = None
                    self.srlg_info = []

                    self.brief_lsp_information = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation()
                    self.brief_lsp_information.parent = self
                    self._children_name_map["brief_lsp_information"] = "brief-lsp-information"

                    self.er_os = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs()
                    self.er_os.parent = self
                    self._children_name_map["er_os"] = "er-os"

                    self.lsppcep_information = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation()
                    self.lsppcep_information.parent = self
                    self._children_name_map["lsppcep_information"] = "lsppcep-information"

                    self.lsp_association_info = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo()
                    self.lsp_association_info.parent = self
                    self._children_name_map["lsp_association_info"] = "lsp-association-info"

                    self.lsp_attributes = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes()
                    self.lsp_attributes.parent = self
                    self._children_name_map["lsp_attributes"] = "lsp-attributes"

                    self.sub_delegated_pce = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce()
                    self.sub_delegated_pce.parent = self
                    self._children_name_map["sub_delegated_pce"] = "sub-delegated-pce"

                    self.state_sync_pce = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce()
                    self.state_sync_pce.parent = self
                    self._children_name_map["state_sync_pce"] = "state-sync-pce"

                    self.reporting_pcc_address = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress()
                    self.reporting_pcc_address.parent = self
                    self._children_name_map["reporting_pcc_address"] = "reporting-pcc-address"

                    self.rro = YList(self)
                    self._segment_path = lambda: "detail-lsp-information"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation, [u'signaled_bandwidth_specified', u'signaled_bandwidth', u'actual_bandwidth_specified', u'actual_bandwidth', u'lsp_role', u'computing_pce', u'srlg_info'], name, value)


                class BriefLspInformation(Entity):
                    """
                    Brief LSP information
                    
                    .. attribute:: source_address
                    
                    	Source address
                    	**type**\:  :py:class:`SourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress>`
                    
                    .. attribute:: destination_address
                    
                    	Destination address
                    	**type**\:  :py:class:`DestinationAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress>`
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lspid
                    
                    	LSP ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_sid
                    
                    	Binding SID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lsp_setup_type
                    
                    	LSP Setup Type
                    	**type**\:  :py:class:`LspSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspSetup>`
                    
                    .. attribute:: operational_state
                    
                    	Operational state
                    	**type**\:  :py:class:`PcepLspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PcepLspState>`
                    
                    .. attribute:: administrative_state
                    
                    	Admin state
                    	**type**\:  :py:class:`LspState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.LspState>`
                    
                    .. attribute:: msd
                    
                    	Maximum SID Depth
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation, self).__init__()

                        self.yang_name = "brief-lsp-information"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("source-address", ("source_address", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress)), ("destination-address", ("destination_address", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress))])
                        self._leafs = OrderedDict([
                            ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                            ('lspid', (YLeaf(YType.uint32, 'lspid'), ['int'])),
                            ('binding_sid', (YLeaf(YType.uint32, 'binding-sid'), ['int'])),
                            ('lsp_setup_type', (YLeaf(YType.enumeration, 'lsp-setup-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspSetup', '')])),
                            ('operational_state', (YLeaf(YType.enumeration, 'operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PcepLspState', '')])),
                            ('administrative_state', (YLeaf(YType.enumeration, 'administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'LspState', '')])),
                            ('msd', (YLeaf(YType.uint32, 'msd'), ['int'])),
                        ])
                        self.tunnel_id = None
                        self.lspid = None
                        self.binding_sid = None
                        self.lsp_setup_type = None
                        self.operational_state = None
                        self.administrative_state = None
                        self.msd = None

                        self.source_address = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress()
                        self.source_address.parent = self
                        self._children_name_map["source_address"] = "source-address"

                        self.destination_address = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress()
                        self.destination_address.parent = self
                        self._children_name_map["destination_address"] = "destination-address"
                        self._segment_path = lambda: "brief-lsp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation, [u'tunnel_id', u'lspid', u'binding_sid', u'lsp_setup_type', u'operational_state', u'administrative_state', u'msd'], name, value)


                    class SourceAddress(Entity):
                        """
                        Source address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress, self).__init__()

                            self.yang_name = "source-address"
                            self.yang_parent_name = "brief-lsp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "source-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.SourceAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


                    class DestinationAddress(Entity):
                        """
                        Destination address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress, self).__init__()

                            self.yang_name = "destination-address"
                            self.yang_parent_name = "brief-lsp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "destination-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.BriefLspInformation.DestinationAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class ErOs(Entity):
                    """
                    Paths
                    
                    .. attribute:: reported_metric_type
                    
                    	Reported Metric Type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_metric_value
                    
                    	Reported Metric Value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_type
                    
                    	Computed Metric Type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_metric_value
                    
                    	Computed Metric Value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: computed_hop_list_time
                    
                    	Computed Hop List Time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reported_rsvp_path
                    
                    	Reported RSVP path
                    	**type**\: list of  		 :py:class:`ReportedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath>`
                    
                    .. attribute:: reported_sr_path
                    
                    	Reported SR path
                    	**type**\: list of  		 :py:class:`ReportedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath>`
                    
                    .. attribute:: computed_rsvp_path
                    
                    	Computed RSVP path
                    	**type**\: list of  		 :py:class:`ComputedRsvpPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath>`
                    
                    .. attribute:: computed_sr_path
                    
                    	Computed SR path
                    	**type**\: list of  		 :py:class:`ComputedSrPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath>`
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs, self).__init__()

                        self.yang_name = "er-os"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("reported-rsvp-path", ("reported_rsvp_path", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath)), ("reported-sr-path", ("reported_sr_path", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath)), ("computed-rsvp-path", ("computed_rsvp_path", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath)), ("computed-sr-path", ("computed_sr_path", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath))])
                        self._leafs = OrderedDict([
                            ('reported_metric_type', (YLeaf(YType.uint32, 'reported-metric-type'), ['int'])),
                            ('reported_metric_value', (YLeaf(YType.uint32, 'reported-metric-value'), ['int'])),
                            ('computed_metric_type', (YLeaf(YType.uint32, 'computed-metric-type'), ['int'])),
                            ('computed_metric_value', (YLeaf(YType.uint32, 'computed-metric-value'), ['int'])),
                            ('computed_hop_list_time', (YLeaf(YType.uint32, 'computed-hop-list-time'), ['int'])),
                        ])
                        self.reported_metric_type = None
                        self.reported_metric_value = None
                        self.computed_metric_type = None
                        self.computed_metric_value = None
                        self.computed_hop_list_time = None

                        self.reported_rsvp_path = YList(self)
                        self.reported_sr_path = YList(self)
                        self.computed_rsvp_path = YList(self)
                        self.computed_sr_path = YList(self)
                        self._segment_path = lambda: "er-os"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs, [u'reported_metric_type', u'reported_metric_value', u'computed_metric_type', u'computed_metric_value', u'computed_hop_list_time'], name, value)


                    class ReportedRsvpPath(Entity):
                        """
                        Reported RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath, self).__init__()

                            self.yang_name = "reported-rsvp-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                            ])
                            self.hop_address = None
                            self._segment_path = lambda: "reported-rsvp-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedRsvpPath, [u'hop_address'], name, value)


                    class ReportedSrPath(Entity):
                        """
                        Reported SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  :py:class:`LocalAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr>`
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  :py:class:`RemoteAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr>`
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath, self).__init__()

                            self.yang_name = "reported-sr-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-addr", ("local_addr", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr)), ("remote-addr", ("remote_addr", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSid', '')])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.sid_type = None
                            self.mpls_label = None

                            self.local_addr = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr()
                            self.local_addr.parent = self
                            self._children_name_map["local_addr"] = "local-addr"

                            self.remote_addr = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr()
                            self.remote_addr.parent = self
                            self._children_name_map["remote_addr"] = "remote-addr"
                            self._segment_path = lambda: "reported-sr-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath, [u'sid_type', u'mpls_label'], name, value)


                        class LocalAddr(Entity):
                            """
                            Local Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr, self).__init__()

                                self.yang_name = "local-addr"
                                self.yang_parent_name = "reported-sr-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "local-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.LocalAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                        class RemoteAddr(Entity):
                            """
                            Remote Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr, self).__init__()

                                self.yang_name = "remote-addr"
                                self.yang_parent_name = "reported-sr-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "remote-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ReportedSrPath.RemoteAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                    class ComputedRsvpPath(Entity):
                        """
                        Computed RSVP path
                        
                        .. attribute:: hop_address
                        
                        	RSVP hop address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath, self).__init__()

                            self.yang_name = "computed-rsvp-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('hop_address', (YLeaf(YType.str, 'hop-address'), ['str'])),
                            ])
                            self.hop_address = None
                            self._segment_path = lambda: "computed-rsvp-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedRsvpPath, [u'hop_address'], name, value)


                    class ComputedSrPath(Entity):
                        """
                        Computed SR path
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  :py:class:`LocalAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr>`
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  :py:class:`RemoteAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr>`
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath, self).__init__()

                            self.yang_name = "computed-sr-path"
                            self.yang_parent_name = "er-os"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-addr", ("local_addr", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr)), ("remote-addr", ("remote_addr", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSid', '')])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.sid_type = None
                            self.mpls_label = None

                            self.local_addr = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr()
                            self.local_addr.parent = self
                            self._children_name_map["local_addr"] = "local-addr"

                            self.remote_addr = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr()
                            self.remote_addr.parent = self
                            self._children_name_map["remote_addr"] = "remote-addr"
                            self._segment_path = lambda: "computed-sr-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath, [u'sid_type', u'mpls_label'], name, value)


                        class LocalAddr(Entity):
                            """
                            Local Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr, self).__init__()

                                self.yang_name = "local-addr"
                                self.yang_parent_name = "computed-sr-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "local-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.LocalAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                        class RemoteAddr(Entity):
                            """
                            Remote Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr, self).__init__()

                                self.yang_name = "remote-addr"
                                self.yang_parent_name = "computed-sr-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "remote-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ErOs.ComputedSrPath.RemoteAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class LsppcepInformation(Entity):
                    """
                    PCEP related LSP information
                    
                    .. attribute:: rsvp_error
                    
                    	RSVP error info
                    	**type**\:  :py:class:`RsvpError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError>`
                    
                    .. attribute:: pcepid
                    
                    	PCE protocol identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pcep_flag_d
                    
                    	PCEP LSP delegation flag
                    	**type**\: bool
                    
                    .. attribute:: pcep_flag_s
                    
                    	PCEP LSP state\-sync flag
                    	**type**\: bool
                    
                    .. attribute:: pcep_flag_r
                    
                    	PCEP LSP remove flag
                    	**type**\: bool
                    
                    .. attribute:: pcep_flag_a
                    
                    	PCEP LSP admin flag
                    	**type**\: bool
                    
                    .. attribute:: pcep_flag_o
                    
                    	PCEP LSP operation flag
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pcep_flag_c
                    
                    	PCEP LSP initiated flag
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation, self).__init__()

                        self.yang_name = "lsppcep-information"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rsvp-error", ("rsvp_error", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError))])
                        self._leafs = OrderedDict([
                            ('pcepid', (YLeaf(YType.uint32, 'pcepid'), ['int'])),
                            ('pcep_flag_d', (YLeaf(YType.boolean, 'pcep-flag-d'), ['bool'])),
                            ('pcep_flag_s', (YLeaf(YType.boolean, 'pcep-flag-s'), ['bool'])),
                            ('pcep_flag_r', (YLeaf(YType.boolean, 'pcep-flag-r'), ['bool'])),
                            ('pcep_flag_a', (YLeaf(YType.boolean, 'pcep-flag-a'), ['bool'])),
                            ('pcep_flag_o', (YLeaf(YType.uint8, 'pcep-flag-o'), ['int'])),
                            ('pcep_flag_c', (YLeaf(YType.uint8, 'pcep-flag-c'), ['int'])),
                        ])
                        self.pcepid = None
                        self.pcep_flag_d = None
                        self.pcep_flag_s = None
                        self.pcep_flag_r = None
                        self.pcep_flag_a = None
                        self.pcep_flag_o = None
                        self.pcep_flag_c = None

                        self.rsvp_error = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError()
                        self.rsvp_error.parent = self
                        self._children_name_map["rsvp_error"] = "rsvp-error"
                        self._segment_path = lambda: "lsppcep-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation, [u'pcepid', u'pcep_flag_d', u'pcep_flag_s', u'pcep_flag_r', u'pcep_flag_a', u'pcep_flag_o', u'pcep_flag_c'], name, value)


                    class RsvpError(Entity):
                        """
                        RSVP error info
                        
                        .. attribute:: node_address
                        
                        	RSVP error node address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: error_flags
                        
                        	RSVP error flags
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_code
                        
                        	RSVP error code
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: error_value
                        
                        	RSVP error value
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError, self).__init__()

                            self.yang_name = "rsvp-error"
                            self.yang_parent_name = "lsppcep-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_address', (YLeaf(YType.str, 'node-address'), ['str'])),
                                ('error_flags', (YLeaf(YType.uint8, 'error-flags'), ['int'])),
                                ('error_code', (YLeaf(YType.uint8, 'error-code'), ['int'])),
                                ('error_value', (YLeaf(YType.uint16, 'error-value'), ['int'])),
                            ])
                            self.node_address = None
                            self.error_flags = None
                            self.error_code = None
                            self.error_value = None
                            self._segment_path = lambda: "rsvp-error"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LsppcepInformation.RsvpError, [u'node_address', u'error_flags', u'error_code', u'error_value'], name, value)


                class LspAssociationInfo(Entity):
                    """
                    LSP association information
                    
                    .. attribute:: association_source
                    
                    	Association Source
                    	**type**\:  :py:class:`AssociationSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource>`
                    
                    .. attribute:: association_type
                    
                    	Association Type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: association_id
                    
                    	Association ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo, self).__init__()

                        self.yang_name = "lsp-association-info"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("association-source", ("association_source", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource))])
                        self._leafs = OrderedDict([
                            ('association_type', (YLeaf(YType.uint32, 'association-type'), ['int'])),
                            ('association_id', (YLeaf(YType.uint32, 'association-id'), ['int'])),
                        ])
                        self.association_type = None
                        self.association_id = None

                        self.association_source = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource()
                        self.association_source.parent = self
                        self._children_name_map["association_source"] = "association-source"
                        self._segment_path = lambda: "lsp-association-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo, [u'association_type', u'association_id'], name, value)


                    class AssociationSource(Entity):
                        """
                        Association Source
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource, self).__init__()

                            self.yang_name = "association-source"
                            self.yang_parent_name = "lsp-association-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "association-source"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAssociationInfo.AssociationSource, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class LspAttributes(Entity):
                    """
                    LSP attributes
                    
                    .. attribute:: affinity_exclude_any
                    
                    	Affinity exclude any
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_any
                    
                    	Affinity include any
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: affinity_include_all
                    
                    	Affinity include all
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: setup_priority
                    
                    	Setup Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: hold_priority
                    
                    	Hold Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: local_protection
                    
                    	True, if local protection is desired
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes, self).__init__()

                        self.yang_name = "lsp-attributes"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('affinity_exclude_any', (YLeaf(YType.uint32, 'affinity-exclude-any'), ['int'])),
                            ('affinity_include_any', (YLeaf(YType.uint32, 'affinity-include-any'), ['int'])),
                            ('affinity_include_all', (YLeaf(YType.uint32, 'affinity-include-all'), ['int'])),
                            ('setup_priority', (YLeaf(YType.uint8, 'setup-priority'), ['int'])),
                            ('hold_priority', (YLeaf(YType.uint8, 'hold-priority'), ['int'])),
                            ('local_protection', (YLeaf(YType.boolean, 'local-protection'), ['bool'])),
                        ])
                        self.affinity_exclude_any = None
                        self.affinity_include_any = None
                        self.affinity_include_all = None
                        self.setup_priority = None
                        self.hold_priority = None
                        self.local_protection = None
                        self._segment_path = lambda: "lsp-attributes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.LspAttributes, [u'affinity_exclude_any', u'affinity_include_any', u'affinity_include_all', u'setup_priority', u'hold_priority', u'local_protection'], name, value)


                class SubDelegatedPce(Entity):
                    """
                    Sub delegated PCE
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce, self).__init__()

                        self.yang_name = "sub-delegated-pce"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "sub-delegated-pce"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.SubDelegatedPce, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class StateSyncPce(Entity):
                    """
                    State\-sync PCE
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce, self).__init__()

                        self.yang_name = "state-sync-pce"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "state-sync-pce"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.StateSyncPce, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class ReportingPccAddress(Entity):
                    """
                    Reporting PCC address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress, self).__init__()

                        self.yang_name = "reporting-pcc-address"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "reporting-pcc-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.ReportingPccAddress, [u'af_name', u'ipv4', u'ipv6'], name, value)


                class Rro(Entity):
                    """
                    RRO
                    
                    .. attribute:: sr_rro
                    
                    	Segment Routing RRO info
                    	**type**\:  :py:class:`SrRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro>`
                    
                    .. attribute:: rro_type
                    
                    	RRO Type
                    	**type**\:  :py:class:`PceRro <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceRro>`
                    
                    .. attribute:: ipv4_address
                    
                    	IPv4 address of RRO
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: mpls_label
                    
                    	MPLS label of RRO
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: flags
                    
                    	RRO Flags
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro, self).__init__()

                        self.yang_name = "rro"
                        self.yang_parent_name = "detail-lsp-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sr-rro", ("sr_rro", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro))])
                        self._leafs = OrderedDict([
                            ('rro_type', (YLeaf(YType.enumeration, 'rro-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceRro', '')])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ('flags', (YLeaf(YType.uint8, 'flags'), ['int'])),
                        ])
                        self.rro_type = None
                        self.ipv4_address = None
                        self.mpls_label = None
                        self.flags = None

                        self.sr_rro = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro()
                        self.sr_rro.parent = self
                        self._children_name_map["sr_rro"] = "sr-rro"
                        self._segment_path = lambda: "rro"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro, [u'rro_type', u'ipv4_address', u'mpls_label', u'flags'], name, value)


                    class SrRro(Entity):
                        """
                        Segment Routing RRO info
                        
                        .. attribute:: local_addr
                        
                        	Local Address
                        	**type**\:  :py:class:`LocalAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr>`
                        
                        .. attribute:: remote_addr
                        
                        	Remote Address
                        	**type**\:  :py:class:`RemoteAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr>`
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`PceSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceSrSid>`
                        
                        .. attribute:: mpls_label
                        
                        	Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro, self).__init__()

                            self.yang_name = "sr-rro"
                            self.yang_parent_name = "rro"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-addr", ("local_addr", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr)), ("remote-addr", ("remote_addr", Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceSrSid', '')])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.sid_type = None
                            self.mpls_label = None

                            self.local_addr = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr()
                            self.local_addr.parent = self
                            self._children_name_map["local_addr"] = "local-addr"

                            self.remote_addr = Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr()
                            self.remote_addr.parent = self
                            self._children_name_map["remote_addr"] = "remote-addr"
                            self._segment_path = lambda: "sr-rro"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro, [u'sid_type', u'mpls_label'], name, value)


                        class LocalAddr(Entity):
                            """
                            Local Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr, self).__init__()

                                self.yang_name = "local-addr"
                                self.yang_parent_name = "sr-rro"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "local-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.LocalAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)


                        class RemoteAddr(Entity):
                            """
                            Remote Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`PceAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper.PceAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr, self).__init__()

                                self.yang_name = "remote-addr"
                                self.yang_parent_name = "sr-rro"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_oper', 'PceAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "remote-addr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pce.TunnelDetailInfos.TunnelDetailInfo.DetailLspInformation.Rro.SrRro.RemoteAddr, [u'af_name', u'ipv4', u'ipv6'], name, value)

    def clone_ptr(self):
        self._top_entity = Pce()
        return self._top_entity

