""" Cisco_IOS_XR_infra_xtc_agent_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc\-agent package operational data.

This module contains definitions
for the following management objects\:
  pcc\: Path\-computation client in XTC
  xtc\: xtc

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class XtcAddressFamily(Enum):
    """
    XtcAddressFamily (Enum Class)

    Xtc address family

    .. data:: ipv4 = 1

    	IPv4 address family

    .. data:: ipv6 = 2

    	IPv6 address family

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class XtcAfId(Enum):
    """
    XtcAfId (Enum Class)

    Xtc af id

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


class XtcBsidError(Enum):
    """
    XtcBsidError (Enum Class)

    Xtc bsid error

    .. data:: none = 0

    	No error

    .. data:: allocating = 1

    	Error allocating via LSD

    .. data:: exists = 2

    	Explicitly configured BSID already exists

    .. data:: internal = 3

    	Internal error

    .. data:: color_endpoint_exists = 4

    	Configured BSID used by another color/end-point

    .. data:: forwarding_rewrite_error = 5

    	BSID Forwarding rewrite (label xconnect) failed

    .. data:: srlb_invalid_label = 6

    	BSID not valid within SRLB range

    .. data:: internal_error = 7

    	Internal error

    """

    none = Enum.YLeaf(0, "none")

    allocating = Enum.YLeaf(1, "allocating")

    exists = Enum.YLeaf(2, "exists")

    internal = Enum.YLeaf(3, "internal")

    color_endpoint_exists = Enum.YLeaf(4, "color-endpoint-exists")

    forwarding_rewrite_error = Enum.YLeaf(5, "forwarding-rewrite-error")

    srlb_invalid_label = Enum.YLeaf(6, "srlb-invalid-label")

    internal_error = Enum.YLeaf(7, "internal-error")


class XtcBsidMode(Enum):
    """
    XtcBsidMode (Enum Class)

    XTC BSID MODE type

    .. data:: explicit = 0

    	Explicit binding SID

    .. data:: dynamic = 1

    	Dynamic binding SID

    """

    explicit = Enum.YLeaf(0, "explicit")

    dynamic = Enum.YLeaf(1, "dynamic")


class XtcDisjointness(Enum):
    """
    XtcDisjointness (Enum Class)

    XTC policy path type

    .. data:: no_disjointness = 0

    	No Disjointness

    .. data:: link_disjointness = 1

    	Link disjointness

    .. data:: node_disjointness = 2

    	Node disjointness

    .. data:: srlg_disjointness = 3

    	SRLG disjointness

    .. data:: srlg_node_disjointness = 4

    	SRLG-Node disjointness

    """

    no_disjointness = Enum.YLeaf(0, "no-disjointness")

    link_disjointness = Enum.YLeaf(1, "link-disjointness")

    node_disjointness = Enum.YLeaf(2, "node-disjointness")

    srlg_disjointness = Enum.YLeaf(3, "srlg-disjointness")

    srlg_node_disjointness = Enum.YLeaf(4, "srlg-node-disjointness")


class XtcIgpInfoId(Enum):
    """
    XtcIgpInfoId (Enum Class)

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


class XtcPolicyPath(Enum):
    """
    XtcPolicyPath (Enum Class)

    XTC policy path type

    .. data:: explicit = 0

    	Explicit path

    .. data:: dynamic = 1

    	Dynamic path

    .. data:: dynamic_pce = 2

    	Dynamic PCE-based path

    """

    explicit = Enum.YLeaf(0, "explicit")

    dynamic = Enum.YLeaf(1, "dynamic")

    dynamic_pce = Enum.YLeaf(2, "dynamic-pce")


class XtcSid(Enum):
    """
    XtcSid (Enum Class)

    Xtc sid

    .. data:: none = 0

    	None

    .. data:: mpls = 1

    	MPLS

    .. data:: ipv6 = 2

    	IPv6

    """

    none = Enum.YLeaf(0, "none")

    mpls = Enum.YLeaf(1, "mpls")

    ipv6 = Enum.YLeaf(2, "ipv6")


class XtcSid1(Enum):
    """
    XtcSid1 (Enum Class)

    XTC SID Types

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


class XtcSrSid(Enum):
    """
    XtcSrSid (Enum Class)

    XTC SR SID type

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



class Pcc(Entity):
    """
    Path\-computation client in XTC
    
    .. attribute:: plsps
    
    	PCC PLSP database in XTC
    	**type**\:  :py:class:`Plsps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps>`
    
    .. attribute:: peers
    
    	PCC peer database in XTC
    	**type**\:  :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Peers>`
    
    

    """

    _prefix = 'infra-xtc-agent-oper'
    _revision = '2017-09-11'

    def __init__(self):
        super(Pcc, self).__init__()
        self._top_entity = None

        self.yang_name = "pcc"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-agent-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("plsps", ("plsps", Pcc.Plsps)), ("peers", ("peers", Pcc.Peers))])
        self._leafs = OrderedDict()

        self.plsps = Pcc.Plsps()
        self.plsps.parent = self
        self._children_name_map["plsps"] = "plsps"

        self.peers = Pcc.Peers()
        self.peers.parent = self
        self._children_name_map["peers"] = "peers"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:pcc"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Pcc, [], name, value)


    class Plsps(Entity):
        """
        PCC PLSP database in XTC
        
        .. attribute:: plsp
        
        	PCC PLSP information
        	**type**\: list of  		 :py:class:`Plsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp>`
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Pcc.Plsps, self).__init__()

            self.yang_name = "plsps"
            self.yang_parent_name = "pcc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("plsp", ("plsp", Pcc.Plsps.Plsp))])
            self._leafs = OrderedDict()

            self.plsp = YList(self)
            self._segment_path = lambda: "plsps"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:pcc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pcc.Plsps, [], name, value)


        class Plsp(Entity):
            """
            PCC PLSP information
            
            .. attribute:: plsp_id  (key)
            
            	PLSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stats
            
            	Stats
            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Stats>`
            
            .. attribute:: plsp_id_xr
            
            	PLSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sym_path_name
            
            	Symbolic Path Name
            	**type**\: str
            
            .. attribute:: refcnt
            
            	Refcnt
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            .. attribute:: conn_delegated_to
            
            	CONN delegated to
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: event_history
            
            	event history
            	**type**\: list of  		 :py:class:`EventHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.EventHistory>`
            
            .. attribute:: path
            
            	path
            	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path>`
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Pcc.Plsps.Plsp, self).__init__()

                self.yang_name = "plsp"
                self.yang_parent_name = "plsps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['plsp_id']
                self._child_classes = OrderedDict([("stats", ("stats", Pcc.Plsps.Plsp.Stats)), ("event-history", ("event_history", Pcc.Plsps.Plsp.EventHistory)), ("path", ("path", Pcc.Plsps.Plsp.Path))])
                self._leafs = OrderedDict([
                    ('plsp_id', (YLeaf(YType.uint32, 'plsp-id'), ['int'])),
                    ('plsp_id_xr', (YLeaf(YType.uint32, 'plsp-id-xr'), ['int'])),
                    ('sym_path_name', (YLeaf(YType.str, 'sym-path-name'), ['str'])),
                    ('refcnt', (YLeaf(YType.int64, 'refcnt'), ['int'])),
                    ('conn_delegated_to', (YLeaf(YType.uint32, 'conn-delegated-to'), ['int'])),
                ])
                self.plsp_id = None
                self.plsp_id_xr = None
                self.sym_path_name = None
                self.refcnt = None
                self.conn_delegated_to = None

                self.stats = Pcc.Plsps.Plsp.Stats()
                self.stats.parent = self
                self._children_name_map["stats"] = "stats"

                self.event_history = YList(self)
                self.path = YList(self)
                self._segment_path = lambda: "plsp" + "[plsp-id='" + str(self.plsp_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:pcc/plsps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pcc.Plsps.Plsp, ['plsp_id', 'plsp_id_xr', 'sym_path_name', 'refcnt', 'conn_delegated_to'], name, value)


            class Stats(Entity):
                """
                Stats
                
                .. attribute:: paths_created
                
                	Paths Created
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: paths_destroyed
                
                	Paths Destroyed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: path_create_errors
                
                	Path create errors
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: path_destroy_errors
                
                	Path destroy errors
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: requests_created
                
                	Requests created
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: requests_destroyed
                
                	Requests destroyed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: requests_failed
                
                	Requests failed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Pcc.Plsps.Plsp.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "plsp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('paths_created', (YLeaf(YType.uint64, 'paths-created'), ['int'])),
                        ('paths_destroyed', (YLeaf(YType.uint64, 'paths-destroyed'), ['int'])),
                        ('path_create_errors', (YLeaf(YType.uint64, 'path-create-errors'), ['int'])),
                        ('path_destroy_errors', (YLeaf(YType.uint64, 'path-destroy-errors'), ['int'])),
                        ('requests_created', (YLeaf(YType.uint64, 'requests-created'), ['int'])),
                        ('requests_destroyed', (YLeaf(YType.uint64, 'requests-destroyed'), ['int'])),
                        ('requests_failed', (YLeaf(YType.uint64, 'requests-failed'), ['int'])),
                    ])
                    self.paths_created = None
                    self.paths_destroyed = None
                    self.path_create_errors = None
                    self.path_destroy_errors = None
                    self.requests_created = None
                    self.requests_destroyed = None
                    self.requests_failed = None
                    self._segment_path = lambda: "stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pcc.Plsps.Plsp.Stats, ['paths_created', 'paths_destroyed', 'path_create_errors', 'path_destroy_errors', 'requests_created', 'requests_destroyed', 'requests_failed'], name, value)


            class EventHistory(Entity):
                """
                event history
                
                .. attribute:: ts
                
                	Timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: desc
                
                	Description
                	**type**\: str
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Pcc.Plsps.Plsp.EventHistory, self).__init__()

                    self.yang_name = "event-history"
                    self.yang_parent_name = "plsp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ts', (YLeaf(YType.uint64, 'ts'), ['int'])),
                        ('desc', (YLeaf(YType.str, 'desc'), ['str'])),
                    ])
                    self.ts = None
                    self.desc = None
                    self._segment_path = lambda: "event-history"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pcc.Plsps.Plsp.EventHistory, ['ts', 'desc'], name, value)


            class Path(Entity):
                """
                path
                
                .. attribute:: stats
                
                	stats
                	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.Stats>`
                
                .. attribute:: used_bw
                
                	used bw
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: requested_bw
                
                	requested bw
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: metric_value
                
                	metric value
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: refcnt
                
                	refcnt
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: lsp_plsp_id
                
                	LSP PLSP ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: binding_sid_value
                
                	Binding SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsp_id_tlv_ext_tunnel_id
                
                	Ext Tun ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsp_id_tlv_tunnel_endpoint_address
                
                	Tun endpoint address
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsp_id_tlv_tunnel_sender_address
                
                	Tun sender address
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: srp_id
                
                	SRP ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsp_id_tlv_lsp_id
                
                	LSP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: lsp_id_tlv_tunnel_id
                
                	Tunnel ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: lsp_id
                
                	Application LSP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: binding_sid_type
                
                	Binding SID type
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: lsp_oper
                
                	LSP oper flags
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: path_setup_type
                
                	Path setup type
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: metric_type
                
                	Metric type
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: is_reported
                
                	is reported
                	**type**\: bool
                
                .. attribute:: lsp_a_flag
                
                	LSP A Flag
                	**type**\: bool
                
                .. attribute:: lsp_r_flag
                
                	LSP R Flag
                	**type**\: bool
                
                .. attribute:: lsp_s_flag
                
                	LSP S Flag
                	**type**\: bool
                
                .. attribute:: lsp_d_flag
                
                	LSP D Flag
                	**type**\: bool
                
                .. attribute:: lsp_c_flag
                
                	LSP C Flag
                	**type**\: bool
                
                .. attribute:: ero_hop
                
                	ero hop
                	**type**\: list of  		 :py:class:`EroHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.EroHop>`
                
                .. attribute:: rro_hop
                
                	rro hop
                	**type**\: list of  		 :py:class:`RroHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.RroHop>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Pcc.Plsps.Plsp.Path, self).__init__()

                    self.yang_name = "path"
                    self.yang_parent_name = "plsp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("stats", ("stats", Pcc.Plsps.Plsp.Path.Stats)), ("ero-hop", ("ero_hop", Pcc.Plsps.Plsp.Path.EroHop)), ("rro-hop", ("rro_hop", Pcc.Plsps.Plsp.Path.RroHop))])
                    self._leafs = OrderedDict([
                        ('used_bw', (YLeaf(YType.int64, 'used-bw'), ['int'])),
                        ('requested_bw', (YLeaf(YType.int64, 'requested-bw'), ['int'])),
                        ('metric_value', (YLeaf(YType.int64, 'metric-value'), ['int'])),
                        ('refcnt', (YLeaf(YType.int64, 'refcnt'), ['int'])),
                        ('lsp_plsp_id', (YLeaf(YType.uint32, 'lsp-plsp-id'), ['int'])),
                        ('binding_sid_value', (YLeaf(YType.uint32, 'binding-sid-value'), ['int'])),
                        ('lsp_id_tlv_ext_tunnel_id', (YLeaf(YType.uint32, 'lsp-id-tlv-ext-tunnel-id'), ['int'])),
                        ('lsp_id_tlv_tunnel_endpoint_address', (YLeaf(YType.uint32, 'lsp-id-tlv-tunnel-endpoint-address'), ['int'])),
                        ('lsp_id_tlv_tunnel_sender_address', (YLeaf(YType.uint32, 'lsp-id-tlv-tunnel-sender-address'), ['int'])),
                        ('srp_id', (YLeaf(YType.uint32, 'srp-id'), ['int'])),
                        ('lsp_id_tlv_lsp_id', (YLeaf(YType.uint16, 'lsp-id-tlv-lsp-id'), ['int'])),
                        ('lsp_id_tlv_tunnel_id', (YLeaf(YType.uint16, 'lsp-id-tlv-tunnel-id'), ['int'])),
                        ('lsp_id', (YLeaf(YType.uint16, 'lsp-id'), ['int'])),
                        ('binding_sid_type', (YLeaf(YType.uint16, 'binding-sid-type'), ['int'])),
                        ('lsp_oper', (YLeaf(YType.uint8, 'lsp-oper'), ['int'])),
                        ('path_setup_type', (YLeaf(YType.uint8, 'path-setup-type'), ['int'])),
                        ('metric_type', (YLeaf(YType.uint8, 'metric-type'), ['int'])),
                        ('is_reported', (YLeaf(YType.boolean, 'is-reported'), ['bool'])),
                        ('lsp_a_flag', (YLeaf(YType.boolean, 'lsp-a-flag'), ['bool'])),
                        ('lsp_r_flag', (YLeaf(YType.boolean, 'lsp-r-flag'), ['bool'])),
                        ('lsp_s_flag', (YLeaf(YType.boolean, 'lsp-s-flag'), ['bool'])),
                        ('lsp_d_flag', (YLeaf(YType.boolean, 'lsp-d-flag'), ['bool'])),
                        ('lsp_c_flag', (YLeaf(YType.boolean, 'lsp-c-flag'), ['bool'])),
                    ])
                    self.used_bw = None
                    self.requested_bw = None
                    self.metric_value = None
                    self.refcnt = None
                    self.lsp_plsp_id = None
                    self.binding_sid_value = None
                    self.lsp_id_tlv_ext_tunnel_id = None
                    self.lsp_id_tlv_tunnel_endpoint_address = None
                    self.lsp_id_tlv_tunnel_sender_address = None
                    self.srp_id = None
                    self.lsp_id_tlv_lsp_id = None
                    self.lsp_id_tlv_tunnel_id = None
                    self.lsp_id = None
                    self.binding_sid_type = None
                    self.lsp_oper = None
                    self.path_setup_type = None
                    self.metric_type = None
                    self.is_reported = None
                    self.lsp_a_flag = None
                    self.lsp_r_flag = None
                    self.lsp_s_flag = None
                    self.lsp_d_flag = None
                    self.lsp_c_flag = None

                    self.stats = Pcc.Plsps.Plsp.Path.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"

                    self.ero_hop = YList(self)
                    self.rro_hop = YList(self)
                    self._segment_path = lambda: "path"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pcc.Plsps.Plsp.Path, ['used_bw', 'requested_bw', 'metric_value', 'refcnt', 'lsp_plsp_id', 'binding_sid_value', 'lsp_id_tlv_ext_tunnel_id', 'lsp_id_tlv_tunnel_endpoint_address', 'lsp_id_tlv_tunnel_sender_address', 'srp_id', 'lsp_id_tlv_lsp_id', 'lsp_id_tlv_tunnel_id', 'lsp_id', 'binding_sid_type', 'lsp_oper', 'path_setup_type', 'metric_type', 'is_reported', 'lsp_a_flag', 'lsp_r_flag', 'lsp_s_flag', 'lsp_d_flag', 'lsp_c_flag'], name, value)


                class Stats(Entity):
                    """
                    stats
                    
                    .. attribute:: reports_requested
                    
                    	Reports requested
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reports_sent
                    
                    	Reports sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reports_failed_to_send
                    
                    	Reports failed
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Pcc.Plsps.Plsp.Path.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('reports_requested', (YLeaf(YType.uint64, 'reports-requested'), ['int'])),
                            ('reports_sent', (YLeaf(YType.uint64, 'reports-sent'), ['int'])),
                            ('reports_failed_to_send', (YLeaf(YType.uint64, 'reports-failed-to-send'), ['int'])),
                        ])
                        self.reports_requested = None
                        self.reports_sent = None
                        self.reports_failed_to_send = None
                        self._segment_path = lambda: "stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pcc.Plsps.Plsp.Path.Stats, ['reports_requested', 'reports_sent', 'reports_failed_to_send'], name, value)


                class EroHop(Entity):
                    """
                    ero hop
                    
                    .. attribute:: data
                    
                    	data
                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.EroHop.Data>`
                    
                    .. attribute:: loose
                    
                    	is loose hop
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Pcc.Plsps.Plsp.Path.EroHop, self).__init__()

                        self.yang_name = "ero-hop"
                        self.yang_parent_name = "path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("data", ("data", Pcc.Plsps.Plsp.Path.EroHop.Data))])
                        self._leafs = OrderedDict([
                            ('loose', (YLeaf(YType.boolean, 'loose'), ['bool'])),
                        ])
                        self.loose = None

                        self.data = Pcc.Plsps.Plsp.Path.EroHop.Data()
                        self.data.parent = self
                        self._children_name_map["data"] = "data"
                        self._segment_path = lambda: "ero-hop"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pcc.Plsps.Plsp.Path.EroHop, ['loose'], name, value)


                    class Data(Entity):
                        """
                        data
                        
                        .. attribute:: ipv4
                        
                        	IPv4 hop info
                        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.EroHop.Data.Ipv4>`
                        
                        .. attribute:: sr_v4
                        
                        	SR IPv4 hop info
                        	**type**\:  :py:class:`SrV4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.EroHop.Data.SrV4>`
                        
                        .. attribute:: hop_type
                        
                        	HopType
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Pcc.Plsps.Plsp.Path.EroHop.Data, self).__init__()

                            self.yang_name = "data"
                            self.yang_parent_name = "ero-hop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv4", ("ipv4", Pcc.Plsps.Plsp.Path.EroHop.Data.Ipv4)), ("sr-v4", ("sr_v4", Pcc.Plsps.Plsp.Path.EroHop.Data.SrV4))])
                            self._leafs = OrderedDict([
                                ('hop_type', (YLeaf(YType.uint8, 'hop-type'), ['int'])),
                            ])
                            self.hop_type = None

                            self.ipv4 = Pcc.Plsps.Plsp.Path.EroHop.Data.Ipv4()
                            self.ipv4.parent = self
                            self._children_name_map["ipv4"] = "ipv4"

                            self.sr_v4 = Pcc.Plsps.Plsp.Path.EroHop.Data.SrV4()
                            self.sr_v4.parent = self
                            self._children_name_map["sr_v4"] = "sr-v4"
                            self._segment_path = lambda: "data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pcc.Plsps.Plsp.Path.EroHop.Data, ['hop_type'], name, value)


                        class Ipv4(Entity):
                            """
                            IPv4 hop info
                            
                            .. attribute:: v4_addr
                            
                            	IPv4 prefix
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_len
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Pcc.Plsps.Plsp.Path.EroHop.Data.Ipv4, self).__init__()

                                self.yang_name = "ipv4"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('v4_addr', (YLeaf(YType.uint32, 'v4-addr'), ['int'])),
                                    ('prefix_len', (YLeaf(YType.uint8, 'prefix-len'), ['int'])),
                                ])
                                self.v4_addr = None
                                self.prefix_len = None
                                self._segment_path = lambda: "ipv4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pcc.Plsps.Plsp.Path.EroHop.Data.Ipv4, ['v4_addr', 'prefix_len'], name, value)


                        class SrV4(Entity):
                            """
                            SR IPv4 hop info
                            
                            .. attribute:: type
                            
                            	SID type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cflag
                            
                            	C flag
                            	**type**\: bool
                            
                            .. attribute:: sid
                            
                            	SID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remote_addr
                            
                            	Remote address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_addr
                            
                            	Local address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Pcc.Plsps.Plsp.Path.EroHop.Data.SrV4, self).__init__()

                                self.yang_name = "sr-v4"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                    ('cflag', (YLeaf(YType.boolean, 'cflag'), ['bool'])),
                                    ('sid', (YLeaf(YType.uint32, 'sid'), ['int'])),
                                    ('remote_addr', (YLeaf(YType.uint32, 'remote-addr'), ['int'])),
                                    ('local_addr', (YLeaf(YType.uint32, 'local-addr'), ['int'])),
                                ])
                                self.type = None
                                self.cflag = None
                                self.sid = None
                                self.remote_addr = None
                                self.local_addr = None
                                self._segment_path = lambda: "sr-v4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pcc.Plsps.Plsp.Path.EroHop.Data.SrV4, ['type', 'cflag', 'sid', 'remote_addr', 'local_addr'], name, value)


                class RroHop(Entity):
                    """
                    rro hop
                    
                    .. attribute:: data
                    
                    	data
                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.RroHop.Data>`
                    
                    .. attribute:: loose
                    
                    	is loose hop
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Pcc.Plsps.Plsp.Path.RroHop, self).__init__()

                        self.yang_name = "rro-hop"
                        self.yang_parent_name = "path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("data", ("data", Pcc.Plsps.Plsp.Path.RroHop.Data))])
                        self._leafs = OrderedDict([
                            ('loose', (YLeaf(YType.boolean, 'loose'), ['bool'])),
                        ])
                        self.loose = None

                        self.data = Pcc.Plsps.Plsp.Path.RroHop.Data()
                        self.data.parent = self
                        self._children_name_map["data"] = "data"
                        self._segment_path = lambda: "rro-hop"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pcc.Plsps.Plsp.Path.RroHop, ['loose'], name, value)


                    class Data(Entity):
                        """
                        data
                        
                        .. attribute:: ipv4
                        
                        	IPv4 hop info
                        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.RroHop.Data.Ipv4>`
                        
                        .. attribute:: sr_v4
                        
                        	SR IPv4 hop info
                        	**type**\:  :py:class:`SrV4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.RroHop.Data.SrV4>`
                        
                        .. attribute:: hop_type
                        
                        	HopType
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Pcc.Plsps.Plsp.Path.RroHop.Data, self).__init__()

                            self.yang_name = "data"
                            self.yang_parent_name = "rro-hop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv4", ("ipv4", Pcc.Plsps.Plsp.Path.RroHop.Data.Ipv4)), ("sr-v4", ("sr_v4", Pcc.Plsps.Plsp.Path.RroHop.Data.SrV4))])
                            self._leafs = OrderedDict([
                                ('hop_type', (YLeaf(YType.uint8, 'hop-type'), ['int'])),
                            ])
                            self.hop_type = None

                            self.ipv4 = Pcc.Plsps.Plsp.Path.RroHop.Data.Ipv4()
                            self.ipv4.parent = self
                            self._children_name_map["ipv4"] = "ipv4"

                            self.sr_v4 = Pcc.Plsps.Plsp.Path.RroHop.Data.SrV4()
                            self.sr_v4.parent = self
                            self._children_name_map["sr_v4"] = "sr-v4"
                            self._segment_path = lambda: "data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pcc.Plsps.Plsp.Path.RroHop.Data, ['hop_type'], name, value)


                        class Ipv4(Entity):
                            """
                            IPv4 hop info
                            
                            .. attribute:: v4_addr
                            
                            	IPv4 prefix
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: prefix_len
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Pcc.Plsps.Plsp.Path.RroHop.Data.Ipv4, self).__init__()

                                self.yang_name = "ipv4"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('v4_addr', (YLeaf(YType.uint32, 'v4-addr'), ['int'])),
                                    ('prefix_len', (YLeaf(YType.uint8, 'prefix-len'), ['int'])),
                                ])
                                self.v4_addr = None
                                self.prefix_len = None
                                self._segment_path = lambda: "ipv4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pcc.Plsps.Plsp.Path.RroHop.Data.Ipv4, ['v4_addr', 'prefix_len'], name, value)


                        class SrV4(Entity):
                            """
                            SR IPv4 hop info
                            
                            .. attribute:: type
                            
                            	SID type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: cflag
                            
                            	C flag
                            	**type**\: bool
                            
                            .. attribute:: sid
                            
                            	SID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remote_addr
                            
                            	Remote address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_addr
                            
                            	Local address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Pcc.Plsps.Plsp.Path.RroHop.Data.SrV4, self).__init__()

                                self.yang_name = "sr-v4"
                                self.yang_parent_name = "data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                    ('cflag', (YLeaf(YType.boolean, 'cflag'), ['bool'])),
                                    ('sid', (YLeaf(YType.uint32, 'sid'), ['int'])),
                                    ('remote_addr', (YLeaf(YType.uint32, 'remote-addr'), ['int'])),
                                    ('local_addr', (YLeaf(YType.uint32, 'local-addr'), ['int'])),
                                ])
                                self.type = None
                                self.cflag = None
                                self.sid = None
                                self.remote_addr = None
                                self.local_addr = None
                                self._segment_path = lambda: "sr-v4"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pcc.Plsps.Plsp.Path.RroHop.Data.SrV4, ['type', 'cflag', 'sid', 'remote_addr', 'local_addr'], name, value)


    class Peers(Entity):
        """
        PCC peer database in XTC
        
        .. attribute:: peer
        
        	PCC peer information
        	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Peers.Peer>`
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Pcc.Peers, self).__init__()

            self.yang_name = "peers"
            self.yang_parent_name = "pcc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("peer", ("peer", Pcc.Peers.Peer))])
            self._leafs = OrderedDict()

            self.peer = YList(self)
            self._segment_path = lambda: "peers"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:pcc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pcc.Peers, [], name, value)


        class Peer(Entity):
            """
            PCC peer information
            
            .. attribute:: peer_addr  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: socket_info
            
            	socket info
            	**type**\:  :py:class:`SocketInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Peers.Peer.SocketInfo>`
            
            .. attribute:: stats
            
            	stats
            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Peers.Peer.Stats>`
            
            .. attribute:: handle
            
            	internal handle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: state_str
            
            	connection state
            	**type**\: str
            
            .. attribute:: local_ok
            
            	local accepted
            	**type**\: bool
            
            .. attribute:: remote_ok
            
            	remote accepted
            	**type**\: bool
            
            .. attribute:: open_retry
            
            	open retry count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ref_cnt
            
            	ref count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rx_state_str
            
            	socket state
            	**type**\: str
            
            .. attribute:: holddown_counter
            
            	holddown counter
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: pcep_up_ts
            
            	PCEP up timestamp
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: precedence
            
            	Precedence
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: ka_interval_local
            
            	KA interval local
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ka_interval_remote
            
            	KA interval remote
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dead_interval_local
            
            	Dead interval local
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dead_interval_remote
            
            	Dead interval remote
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pcep_session_id_local
            
            	PCEP session ID local
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pcep_session_id_remote
            
            	PCEP session ID remote
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pcep_server_ipv4_addr
            
            	PCEP server Ipv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pcep_client_ipv4_addr
            
            	PCEP client Ipv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: is_stateful_local
            
            	is stateful local
            	**type**\: bool
            
            .. attribute:: is_stateful_remote
            
            	is stateful remote
            	**type**\: bool
            
            .. attribute:: is_stateful_u_flag_local
            
            	is stateful with U flag local
            	**type**\: bool
            
            .. attribute:: is_stateful_u_flag_remote
            
            	is stateful with U flag remote
            	**type**\: bool
            
            .. attribute:: is_segment_routing_local
            
            	is segment routing local
            	**type**\: bool
            
            .. attribute:: is_segment_routing_remote
            
            	is segment routing remote
            	**type**\: bool
            
            .. attribute:: is_initiate_local
            
            	local initiate capability
            	**type**\: bool
            
            .. attribute:: is_initiate_remote
            
            	remote initiate capability
            	**type**\: bool
            
            .. attribute:: is_best_pce
            
            	is this the best PCE to delegate to
            	**type**\: bool
            
            .. attribute:: sr_msd_local
            
            	SR MSD local
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: sr_msd_remote
            
            	SR MSD remote
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Pcc.Peers.Peer, self).__init__()

                self.yang_name = "peer"
                self.yang_parent_name = "peers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['peer_addr']
                self._child_classes = OrderedDict([("socket-info", ("socket_info", Pcc.Peers.Peer.SocketInfo)), ("stats", ("stats", Pcc.Peers.Peer.Stats))])
                self._leafs = OrderedDict([
                    ('peer_addr', (YLeaf(YType.str, 'peer-addr'), ['str','str'])),
                    ('handle', (YLeaf(YType.uint32, 'handle'), ['int'])),
                    ('state_str', (YLeaf(YType.str, 'state-str'), ['str'])),
                    ('local_ok', (YLeaf(YType.boolean, 'local-ok'), ['bool'])),
                    ('remote_ok', (YLeaf(YType.boolean, 'remote-ok'), ['bool'])),
                    ('open_retry', (YLeaf(YType.uint32, 'open-retry'), ['int'])),
                    ('ref_cnt', (YLeaf(YType.uint32, 'ref-cnt'), ['int'])),
                    ('rx_state_str', (YLeaf(YType.str, 'rx-state-str'), ['str'])),
                    ('holddown_counter', (YLeaf(YType.uint16, 'holddown-counter'), ['int'])),
                    ('pcep_up_ts', (YLeaf(YType.uint64, 'pcep-up-ts'), ['int'])),
                    ('precedence', (YLeaf(YType.uint8, 'precedence'), ['int'])),
                    ('ka_interval_local', (YLeaf(YType.uint32, 'ka-interval-local'), ['int'])),
                    ('ka_interval_remote', (YLeaf(YType.uint32, 'ka-interval-remote'), ['int'])),
                    ('dead_interval_local', (YLeaf(YType.uint32, 'dead-interval-local'), ['int'])),
                    ('dead_interval_remote', (YLeaf(YType.uint32, 'dead-interval-remote'), ['int'])),
                    ('pcep_session_id_local', (YLeaf(YType.uint32, 'pcep-session-id-local'), ['int'])),
                    ('pcep_session_id_remote', (YLeaf(YType.uint32, 'pcep-session-id-remote'), ['int'])),
                    ('pcep_server_ipv4_addr', (YLeaf(YType.str, 'pcep-server-ipv4-addr'), ['str'])),
                    ('pcep_client_ipv4_addr', (YLeaf(YType.str, 'pcep-client-ipv4-addr'), ['str'])),
                    ('is_stateful_local', (YLeaf(YType.boolean, 'is-stateful-local'), ['bool'])),
                    ('is_stateful_remote', (YLeaf(YType.boolean, 'is-stateful-remote'), ['bool'])),
                    ('is_stateful_u_flag_local', (YLeaf(YType.boolean, 'is-stateful-u-flag-local'), ['bool'])),
                    ('is_stateful_u_flag_remote', (YLeaf(YType.boolean, 'is-stateful-u-flag-remote'), ['bool'])),
                    ('is_segment_routing_local', (YLeaf(YType.boolean, 'is-segment-routing-local'), ['bool'])),
                    ('is_segment_routing_remote', (YLeaf(YType.boolean, 'is-segment-routing-remote'), ['bool'])),
                    ('is_initiate_local', (YLeaf(YType.boolean, 'is-initiate-local'), ['bool'])),
                    ('is_initiate_remote', (YLeaf(YType.boolean, 'is-initiate-remote'), ['bool'])),
                    ('is_best_pce', (YLeaf(YType.boolean, 'is-best-pce'), ['bool'])),
                    ('sr_msd_local', (YLeaf(YType.uint8, 'sr-msd-local'), ['int'])),
                    ('sr_msd_remote', (YLeaf(YType.uint8, 'sr-msd-remote'), ['int'])),
                ])
                self.peer_addr = None
                self.handle = None
                self.state_str = None
                self.local_ok = None
                self.remote_ok = None
                self.open_retry = None
                self.ref_cnt = None
                self.rx_state_str = None
                self.holddown_counter = None
                self.pcep_up_ts = None
                self.precedence = None
                self.ka_interval_local = None
                self.ka_interval_remote = None
                self.dead_interval_local = None
                self.dead_interval_remote = None
                self.pcep_session_id_local = None
                self.pcep_session_id_remote = None
                self.pcep_server_ipv4_addr = None
                self.pcep_client_ipv4_addr = None
                self.is_stateful_local = None
                self.is_stateful_remote = None
                self.is_stateful_u_flag_local = None
                self.is_stateful_u_flag_remote = None
                self.is_segment_routing_local = None
                self.is_segment_routing_remote = None
                self.is_initiate_local = None
                self.is_initiate_remote = None
                self.is_best_pce = None
                self.sr_msd_local = None
                self.sr_msd_remote = None

                self.socket_info = Pcc.Peers.Peer.SocketInfo()
                self.socket_info.parent = self
                self._children_name_map["socket_info"] = "socket-info"

                self.stats = Pcc.Peers.Peer.Stats()
                self.stats.parent = self
                self._children_name_map["stats"] = "stats"
                self._segment_path = lambda: "peer" + "[peer-addr='" + str(self.peer_addr) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:pcc/peers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pcc.Peers.Peer, ['peer_addr', 'handle', 'state_str', 'local_ok', 'remote_ok', 'open_retry', 'ref_cnt', 'rx_state_str', 'holddown_counter', 'pcep_up_ts', 'precedence', 'ka_interval_local', 'ka_interval_remote', 'dead_interval_local', 'dead_interval_remote', 'pcep_session_id_local', 'pcep_session_id_remote', 'pcep_server_ipv4_addr', 'pcep_client_ipv4_addr', 'is_stateful_local', 'is_stateful_remote', 'is_stateful_u_flag_local', 'is_stateful_u_flag_remote', 'is_segment_routing_local', 'is_segment_routing_remote', 'is_initiate_local', 'is_initiate_remote', 'is_best_pce', 'sr_msd_local', 'sr_msd_remote'], name, value)


            class SocketInfo(Entity):
                """
                socket info
                
                .. attribute:: fd
                
                	file descriptor
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: wnotify
                
                	write notify
                	**type**\: bool
                
                .. attribute:: rnotify
                
                	read notify
                	**type**\: bool
                
                .. attribute:: refcnt
                
                	ref count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: selected
                
                	selected
                	**type**\: bool
                
                .. attribute:: owner
                
                	owner
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: csockaddr_str
                
                	client address
                	**type**\: str
                
                .. attribute:: ssockaddr_str
                
                	server address
                	**type**\: str
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Pcc.Peers.Peer.SocketInfo, self).__init__()

                    self.yang_name = "socket-info"
                    self.yang_parent_name = "peer"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('fd', (YLeaf(YType.int64, 'fd'), ['int'])),
                        ('wnotify', (YLeaf(YType.boolean, 'wnotify'), ['bool'])),
                        ('rnotify', (YLeaf(YType.boolean, 'rnotify'), ['bool'])),
                        ('refcnt', (YLeaf(YType.uint32, 'refcnt'), ['int'])),
                        ('selected', (YLeaf(YType.boolean, 'selected'), ['bool'])),
                        ('owner', (YLeaf(YType.uint32, 'owner'), ['int'])),
                        ('csockaddr_str', (YLeaf(YType.str, 'csockaddr-str'), ['str'])),
                        ('ssockaddr_str', (YLeaf(YType.str, 'ssockaddr-str'), ['str'])),
                    ])
                    self.fd = None
                    self.wnotify = None
                    self.rnotify = None
                    self.refcnt = None
                    self.selected = None
                    self.owner = None
                    self.csockaddr_str = None
                    self.ssockaddr_str = None
                    self._segment_path = lambda: "socket-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pcc.Peers.Peer.SocketInfo, ['fd', 'wnotify', 'rnotify', 'refcnt', 'selected', 'owner', 'csockaddr_str', 'ssockaddr_str'], name, value)


            class Stats(Entity):
                """
                stats
                
                .. attribute:: ka_msg_rx
                
                	KA messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ka_msg_fail_rx
                
                	KA messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ka_msg_tx
                
                	KA messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ka_msg_fail_tx
                
                	KA messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcreq_msg_rx
                
                	PCREQ messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcreq_msg_fail_rx
                
                	PCREQ messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcreq_msg_tx
                
                	PCREQ messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcreq_msg_fail_tx
                
                	PCREQ messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcrep_msg_rx
                
                	PCREP messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcrep_msg_fail_rx
                
                	PCREP messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcrep_msg_tx
                
                	PCREP messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcrep_msg_fail_tx
                
                	PCREP messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcrpt_msg_rx
                
                	PCRPT messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcrpt_msg_fail_rx
                
                	PCRPT messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcrpt_msg_tx
                
                	PCRPT messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcrpt_msg_fail_tx
                
                	PCRPT messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcupd_msg_rx
                
                	PCUPD messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcupd_msg_fail_rx
                
                	PCUPD messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcupd_msg_tx
                
                	PCUPD messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcupd_msg_fail_tx
                
                	PCUPD messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: open_msg_rx
                
                	OPEN messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: open_msg_fail_rx
                
                	OPEN messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: open_msg_tx
                
                	OPEN messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: open_msg_fail_tx
                
                	OPEN messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcerr_msg_rx
                
                	PCERR messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcerr_msg_fail_rx
                
                	PCERR messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcerr_msg_tx
                
                	PCERR messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcerr_msg_fail_tx
                
                	PCERR messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcntf_msg_rx
                
                	PCNTF messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcntf_msg_fail_rx
                
                	PCNTF messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcntf_msg_tx
                
                	PCNTF messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcntf_msg_fail_tx
                
                	PCNTF messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_eos_msg_tx
                
                	PCE EOS messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pce_eos_msg_fail_tx
                
                	PCE EOS messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: close_msg_rx
                
                	CLOSE messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: close_msg_fail_rx
                
                	CLOSE messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: close_msg_tx
                
                	CLOSE messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: close_msg_fail_tx
                
                	CLOSE messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: unexpected_msg_rx
                
                	Unexpected messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: corrupted_msg_rx
                
                	Corrupted messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reply_time_index
                
                	index into recorded reply time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: minimum_reply_time
                
                	min reply time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: maximum_reply_time
                
                	max reply time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: requests_timed_out
                
                	requests timed out
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: last_pcerr_type_rx
                
                	last PCERR type received
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: last_pcerr_val_rx
                
                	last PCERR value received
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: last_pcerr_rx_ts
                
                	last time when PCERR was received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: last_pcerr_type_tx
                
                	last PCERR type transmitted
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: last_pcerr_val_tx
                
                	last PCERR value transmitted
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: last_pcerr_tx_ts
                
                	last time when PCERR was transmitted
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcinitiate_msg_rx
                
                	PCINITIATE messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: pcinitiate_msg_fail_rx
                
                	PCINITIATE messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: recorded_reply_time
                
                	Recorded reply time
                	**type**\: list of int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Pcc.Peers.Peer.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "peer"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ka_msg_rx', (YLeaf(YType.uint64, 'ka-msg-rx'), ['int'])),
                        ('ka_msg_fail_rx', (YLeaf(YType.uint64, 'ka-msg-fail-rx'), ['int'])),
                        ('ka_msg_tx', (YLeaf(YType.uint64, 'ka-msg-tx'), ['int'])),
                        ('ka_msg_fail_tx', (YLeaf(YType.uint64, 'ka-msg-fail-tx'), ['int'])),
                        ('pcreq_msg_rx', (YLeaf(YType.uint64, 'pcreq-msg-rx'), ['int'])),
                        ('pcreq_msg_fail_rx', (YLeaf(YType.uint64, 'pcreq-msg-fail-rx'), ['int'])),
                        ('pcreq_msg_tx', (YLeaf(YType.uint64, 'pcreq-msg-tx'), ['int'])),
                        ('pcreq_msg_fail_tx', (YLeaf(YType.uint64, 'pcreq-msg-fail-tx'), ['int'])),
                        ('pcrep_msg_rx', (YLeaf(YType.uint64, 'pcrep-msg-rx'), ['int'])),
                        ('pcrep_msg_fail_rx', (YLeaf(YType.uint64, 'pcrep-msg-fail-rx'), ['int'])),
                        ('pcrep_msg_tx', (YLeaf(YType.uint64, 'pcrep-msg-tx'), ['int'])),
                        ('pcrep_msg_fail_tx', (YLeaf(YType.uint64, 'pcrep-msg-fail-tx'), ['int'])),
                        ('pcrpt_msg_rx', (YLeaf(YType.uint64, 'pcrpt-msg-rx'), ['int'])),
                        ('pcrpt_msg_fail_rx', (YLeaf(YType.uint64, 'pcrpt-msg-fail-rx'), ['int'])),
                        ('pcrpt_msg_tx', (YLeaf(YType.uint64, 'pcrpt-msg-tx'), ['int'])),
                        ('pcrpt_msg_fail_tx', (YLeaf(YType.uint64, 'pcrpt-msg-fail-tx'), ['int'])),
                        ('pcupd_msg_rx', (YLeaf(YType.uint64, 'pcupd-msg-rx'), ['int'])),
                        ('pcupd_msg_fail_rx', (YLeaf(YType.uint64, 'pcupd-msg-fail-rx'), ['int'])),
                        ('pcupd_msg_tx', (YLeaf(YType.uint64, 'pcupd-msg-tx'), ['int'])),
                        ('pcupd_msg_fail_tx', (YLeaf(YType.uint64, 'pcupd-msg-fail-tx'), ['int'])),
                        ('open_msg_rx', (YLeaf(YType.uint64, 'open-msg-rx'), ['int'])),
                        ('open_msg_fail_rx', (YLeaf(YType.uint64, 'open-msg-fail-rx'), ['int'])),
                        ('open_msg_tx', (YLeaf(YType.uint64, 'open-msg-tx'), ['int'])),
                        ('open_msg_fail_tx', (YLeaf(YType.uint64, 'open-msg-fail-tx'), ['int'])),
                        ('pcerr_msg_rx', (YLeaf(YType.uint64, 'pcerr-msg-rx'), ['int'])),
                        ('pcerr_msg_fail_rx', (YLeaf(YType.uint64, 'pcerr-msg-fail-rx'), ['int'])),
                        ('pcerr_msg_tx', (YLeaf(YType.uint64, 'pcerr-msg-tx'), ['int'])),
                        ('pcerr_msg_fail_tx', (YLeaf(YType.uint64, 'pcerr-msg-fail-tx'), ['int'])),
                        ('pcntf_msg_rx', (YLeaf(YType.uint64, 'pcntf-msg-rx'), ['int'])),
                        ('pcntf_msg_fail_rx', (YLeaf(YType.uint64, 'pcntf-msg-fail-rx'), ['int'])),
                        ('pcntf_msg_tx', (YLeaf(YType.uint64, 'pcntf-msg-tx'), ['int'])),
                        ('pcntf_msg_fail_tx', (YLeaf(YType.uint64, 'pcntf-msg-fail-tx'), ['int'])),
                        ('pce_eos_msg_tx', (YLeaf(YType.uint64, 'pce-eos-msg-tx'), ['int'])),
                        ('pce_eos_msg_fail_tx', (YLeaf(YType.uint64, 'pce-eos-msg-fail-tx'), ['int'])),
                        ('close_msg_rx', (YLeaf(YType.uint64, 'close-msg-rx'), ['int'])),
                        ('close_msg_fail_rx', (YLeaf(YType.uint64, 'close-msg-fail-rx'), ['int'])),
                        ('close_msg_tx', (YLeaf(YType.uint64, 'close-msg-tx'), ['int'])),
                        ('close_msg_fail_tx', (YLeaf(YType.uint64, 'close-msg-fail-tx'), ['int'])),
                        ('unexpected_msg_rx', (YLeaf(YType.uint64, 'unexpected-msg-rx'), ['int'])),
                        ('corrupted_msg_rx', (YLeaf(YType.uint64, 'corrupted-msg-rx'), ['int'])),
                        ('reply_time_index', (YLeaf(YType.uint32, 'reply-time-index'), ['int'])),
                        ('minimum_reply_time', (YLeaf(YType.uint64, 'minimum-reply-time'), ['int'])),
                        ('maximum_reply_time', (YLeaf(YType.uint64, 'maximum-reply-time'), ['int'])),
                        ('requests_timed_out', (YLeaf(YType.uint64, 'requests-timed-out'), ['int'])),
                        ('last_pcerr_type_rx', (YLeaf(YType.uint8, 'last-pcerr-type-rx'), ['int'])),
                        ('last_pcerr_val_rx', (YLeaf(YType.uint8, 'last-pcerr-val-rx'), ['int'])),
                        ('last_pcerr_rx_ts', (YLeaf(YType.uint64, 'last-pcerr-rx-ts'), ['int'])),
                        ('last_pcerr_type_tx', (YLeaf(YType.uint8, 'last-pcerr-type-tx'), ['int'])),
                        ('last_pcerr_val_tx', (YLeaf(YType.uint8, 'last-pcerr-val-tx'), ['int'])),
                        ('last_pcerr_tx_ts', (YLeaf(YType.uint64, 'last-pcerr-tx-ts'), ['int'])),
                        ('pcinitiate_msg_rx', (YLeaf(YType.uint64, 'pcinitiate-msg-rx'), ['int'])),
                        ('pcinitiate_msg_fail_rx', (YLeaf(YType.uint64, 'pcinitiate-msg-fail-rx'), ['int'])),
                        ('recorded_reply_time', (YLeafList(YType.uint64, 'recorded-reply-time'), ['int'])),
                    ])
                    self.ka_msg_rx = None
                    self.ka_msg_fail_rx = None
                    self.ka_msg_tx = None
                    self.ka_msg_fail_tx = None
                    self.pcreq_msg_rx = None
                    self.pcreq_msg_fail_rx = None
                    self.pcreq_msg_tx = None
                    self.pcreq_msg_fail_tx = None
                    self.pcrep_msg_rx = None
                    self.pcrep_msg_fail_rx = None
                    self.pcrep_msg_tx = None
                    self.pcrep_msg_fail_tx = None
                    self.pcrpt_msg_rx = None
                    self.pcrpt_msg_fail_rx = None
                    self.pcrpt_msg_tx = None
                    self.pcrpt_msg_fail_tx = None
                    self.pcupd_msg_rx = None
                    self.pcupd_msg_fail_rx = None
                    self.pcupd_msg_tx = None
                    self.pcupd_msg_fail_tx = None
                    self.open_msg_rx = None
                    self.open_msg_fail_rx = None
                    self.open_msg_tx = None
                    self.open_msg_fail_tx = None
                    self.pcerr_msg_rx = None
                    self.pcerr_msg_fail_rx = None
                    self.pcerr_msg_tx = None
                    self.pcerr_msg_fail_tx = None
                    self.pcntf_msg_rx = None
                    self.pcntf_msg_fail_rx = None
                    self.pcntf_msg_tx = None
                    self.pcntf_msg_fail_tx = None
                    self.pce_eos_msg_tx = None
                    self.pce_eos_msg_fail_tx = None
                    self.close_msg_rx = None
                    self.close_msg_fail_rx = None
                    self.close_msg_tx = None
                    self.close_msg_fail_tx = None
                    self.unexpected_msg_rx = None
                    self.corrupted_msg_rx = None
                    self.reply_time_index = None
                    self.minimum_reply_time = None
                    self.maximum_reply_time = None
                    self.requests_timed_out = None
                    self.last_pcerr_type_rx = None
                    self.last_pcerr_val_rx = None
                    self.last_pcerr_rx_ts = None
                    self.last_pcerr_type_tx = None
                    self.last_pcerr_val_tx = None
                    self.last_pcerr_tx_ts = None
                    self.pcinitiate_msg_rx = None
                    self.pcinitiate_msg_fail_rx = None
                    self.recorded_reply_time = []
                    self._segment_path = lambda: "stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pcc.Peers.Peer.Stats, ['ka_msg_rx', 'ka_msg_fail_rx', 'ka_msg_tx', 'ka_msg_fail_tx', 'pcreq_msg_rx', 'pcreq_msg_fail_rx', 'pcreq_msg_tx', 'pcreq_msg_fail_tx', 'pcrep_msg_rx', 'pcrep_msg_fail_rx', 'pcrep_msg_tx', 'pcrep_msg_fail_tx', 'pcrpt_msg_rx', 'pcrpt_msg_fail_rx', 'pcrpt_msg_tx', 'pcrpt_msg_fail_tx', 'pcupd_msg_rx', 'pcupd_msg_fail_rx', 'pcupd_msg_tx', 'pcupd_msg_fail_tx', 'open_msg_rx', 'open_msg_fail_rx', 'open_msg_tx', 'open_msg_fail_tx', 'pcerr_msg_rx', 'pcerr_msg_fail_rx', 'pcerr_msg_tx', 'pcerr_msg_fail_tx', 'pcntf_msg_rx', 'pcntf_msg_fail_rx', 'pcntf_msg_tx', 'pcntf_msg_fail_tx', 'pce_eos_msg_tx', 'pce_eos_msg_fail_tx', 'close_msg_rx', 'close_msg_fail_rx', 'close_msg_tx', 'close_msg_fail_tx', 'unexpected_msg_rx', 'corrupted_msg_rx', 'reply_time_index', 'minimum_reply_time', 'maximum_reply_time', 'requests_timed_out', 'last_pcerr_type_rx', 'last_pcerr_val_rx', 'last_pcerr_rx_ts', 'last_pcerr_type_tx', 'last_pcerr_val_tx', 'last_pcerr_tx_ts', 'pcinitiate_msg_rx', 'pcinitiate_msg_fail_rx', 'recorded_reply_time'], name, value)

    def clone_ptr(self):
        self._top_entity = Pcc()
        return self._top_entity

class Xtc(Entity):
    """
    xtc
    
    .. attribute:: policies
    
    	Policy database in XTC Agent
    	**type**\:  :py:class:`Policies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies>`
    
    .. attribute:: policy_summary
    
    	Summary of all policies
    	**type**\:  :py:class:`PolicySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicySummary>`
    
    .. attribute:: on_demand_colors
    
    	On\-Demand Color database in XTC Agent
    	**type**\:  :py:class:`OnDemandColors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.OnDemandColors>`
    
    .. attribute:: forwarding
    
    	Forwarding information
    	**type**\:  :py:class:`Forwarding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Forwarding>`
    
    .. attribute:: controller
    
    	Controller information
    	**type**\:  :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller>`
    
    .. attribute:: topology_summary
    
    	Node summary database
    	**type**\:  :py:class:`TopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologySummary>`
    
    .. attribute:: topology_nodes
    
    	Node database in XTC Agent
    	**type**\:  :py:class:`TopologyNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes>`
    
    .. attribute:: prefix_infos
    
    	Prefixes database in XTC Agent
    	**type**\:  :py:class:`PrefixInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos>`
    
    

    """

    _prefix = 'infra-xtc-agent-oper'
    _revision = '2017-09-11'

    def __init__(self):
        super(Xtc, self).__init__()
        self._top_entity = None

        self.yang_name = "xtc"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-agent-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("policies", ("policies", Xtc.Policies)), ("policy-summary", ("policy_summary", Xtc.PolicySummary)), ("on-demand-colors", ("on_demand_colors", Xtc.OnDemandColors)), ("forwarding", ("forwarding", Xtc.Forwarding)), ("controller", ("controller", Xtc.Controller)), ("topology-summary", ("topology_summary", Xtc.TopologySummary)), ("topology-nodes", ("topology_nodes", Xtc.TopologyNodes)), ("prefix-infos", ("prefix_infos", Xtc.PrefixInfos))])
        self._leafs = OrderedDict()

        self.policies = Xtc.Policies()
        self.policies.parent = self
        self._children_name_map["policies"] = "policies"

        self.policy_summary = Xtc.PolicySummary()
        self.policy_summary.parent = self
        self._children_name_map["policy_summary"] = "policy-summary"

        self.on_demand_colors = Xtc.OnDemandColors()
        self.on_demand_colors.parent = self
        self._children_name_map["on_demand_colors"] = "on-demand-colors"

        self.forwarding = Xtc.Forwarding()
        self.forwarding.parent = self
        self._children_name_map["forwarding"] = "forwarding"

        self.controller = Xtc.Controller()
        self.controller.parent = self
        self._children_name_map["controller"] = "controller"

        self.topology_summary = Xtc.TopologySummary()
        self.topology_summary.parent = self
        self._children_name_map["topology_summary"] = "topology-summary"

        self.topology_nodes = Xtc.TopologyNodes()
        self.topology_nodes.parent = self
        self._children_name_map["topology_nodes"] = "topology-nodes"

        self.prefix_infos = Xtc.PrefixInfos()
        self.prefix_infos.parent = self
        self._children_name_map["prefix_infos"] = "prefix-infos"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Xtc, [], name, value)


    class Policies(Entity):
        """
        Policy database in XTC Agent
        
        .. attribute:: policy
        
        	Policy information
        	**type**\: list of  		 :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy>`
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Xtc.Policies, self).__init__()

            self.yang_name = "policies"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy", ("policy", Xtc.Policies.Policy))])
            self._leafs = OrderedDict()

            self.policy = YList(self)
            self._segment_path = lambda: "policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.Policies, [], name, value)


        class Policy(Entity):
            """
            Policy information
            
            .. attribute:: id  (key)
            
            	Policy ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: destination_address
            
            	Destination address
            	**type**\:  :py:class:`DestinationAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.DestinationAddress>`
            
            .. attribute:: binding_sid
            
            	Binding SID information
            	**type**\:  :py:class:`BindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.BindingSid>`
            
            .. attribute:: auto_policy_info
            
            	Autopolicy information
            	**type**\:  :py:class:`AutoPolicyInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.AutoPolicyInfo>`
            
            .. attribute:: policy_name
            
            	Policy name
            	**type**\: str
            
            .. attribute:: administrative_up
            
            	Admin up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: operational_up
            
            	Operational up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: color
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_auto_policy
            
            	Whether policy was automatically created or configured
            	**type**\: bool
            
            .. attribute:: transition_count
            
            	Indicates number of up/down transitions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: forward_class
            
            	Forward class of the policy
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: up_time
            
            	Policy up time in nano seconds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: nanosecond
            
            .. attribute:: up_age
            
            	Policy up age (since) in nano seconds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: nanosecond
            
            .. attribute:: down_time
            
            	Policy down time in nano seconds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: nanosecond
            
            .. attribute:: down_age
            
            	Policy down age (since) in nano seconds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: nanosecond
            
            .. attribute:: lsp_id
            
            	LSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: steering_bgp_disabled
            
            	Whether steering to BGP client is disabled
            	**type**\: bool
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: policy_group_identifier
            
            	Policy group identifier
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: local_label_identifier
            
            	Local label identifier
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: local_label
            
            	Local label
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: profile_id
            
            	Profile ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ipv6_caps_enabled
            
            	IPv6 caps enabled
            	**type**\: bool
            
            .. attribute:: paths
            
            	Path options
            	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths>`
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Xtc.Policies.Policy, self).__init__()

                self.yang_name = "policy"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_classes = OrderedDict([("destination-address", ("destination_address", Xtc.Policies.Policy.DestinationAddress)), ("binding-sid", ("binding_sid", Xtc.Policies.Policy.BindingSid)), ("auto-policy-info", ("auto_policy_info", Xtc.Policies.Policy.AutoPolicyInfo)), ("paths", ("paths", Xtc.Policies.Policy.Paths))])
                self._leafs = OrderedDict([
                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                    ('administrative_up', (YLeaf(YType.uint32, 'administrative-up'), ['int'])),
                    ('operational_up', (YLeaf(YType.uint32, 'operational-up'), ['int'])),
                    ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                    ('is_auto_policy', (YLeaf(YType.boolean, 'is-auto-policy'), ['bool'])),
                    ('transition_count', (YLeaf(YType.uint32, 'transition-count'), ['int'])),
                    ('forward_class', (YLeaf(YType.uint32, 'forward-class'), ['int'])),
                    ('up_time', (YLeaf(YType.uint64, 'up-time'), ['int'])),
                    ('up_age', (YLeaf(YType.uint64, 'up-age'), ['int'])),
                    ('down_time', (YLeaf(YType.uint64, 'down-time'), ['int'])),
                    ('down_age', (YLeaf(YType.uint64, 'down-age'), ['int'])),
                    ('lsp_id', (YLeaf(YType.uint32, 'lsp-id'), ['int'])),
                    ('steering_bgp_disabled', (YLeaf(YType.boolean, 'steering-bgp-disabled'), ['bool'])),
                    ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                    ('policy_group_identifier', (YLeaf(YType.uint16, 'policy-group-identifier'), ['int'])),
                    ('local_label_identifier', (YLeaf(YType.uint16, 'local-label-identifier'), ['int'])),
                    ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                    ('profile_id', (YLeaf(YType.uint16, 'profile-id'), ['int'])),
                    ('ipv6_caps_enabled', (YLeaf(YType.boolean, 'ipv6-caps-enabled'), ['bool'])),
                ])
                self.id = None
                self.policy_name = None
                self.administrative_up = None
                self.operational_up = None
                self.color = None
                self.is_auto_policy = None
                self.transition_count = None
                self.forward_class = None
                self.up_time = None
                self.up_age = None
                self.down_time = None
                self.down_age = None
                self.lsp_id = None
                self.steering_bgp_disabled = None
                self.interface_handle = None
                self.policy_group_identifier = None
                self.local_label_identifier = None
                self.local_label = None
                self.profile_id = None
                self.ipv6_caps_enabled = None

                self.destination_address = Xtc.Policies.Policy.DestinationAddress()
                self.destination_address.parent = self
                self._children_name_map["destination_address"] = "destination-address"

                self.binding_sid = Xtc.Policies.Policy.BindingSid()
                self.binding_sid.parent = self
                self._children_name_map["binding_sid"] = "binding-sid"

                self.auto_policy_info = Xtc.Policies.Policy.AutoPolicyInfo()
                self.auto_policy_info.parent = self
                self._children_name_map["auto_policy_info"] = "auto-policy-info"

                self.paths = YList(self)
                self._segment_path = lambda: "policy" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policies/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.Policies.Policy, ['id', 'policy_name', 'administrative_up', 'operational_up', 'color', 'is_auto_policy', 'transition_count', 'forward_class', 'up_time', 'up_age', 'down_time', 'down_age', 'lsp_id', 'steering_bgp_disabled', 'interface_handle', 'policy_group_identifier', 'local_label_identifier', 'local_label', 'profile_id', 'ipv6_caps_enabled'], name, value)


            class DestinationAddress(Entity):
                """
                Destination address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.Policies.Policy.DestinationAddress, self).__init__()

                    self.yang_name = "destination-address"
                    self.yang_parent_name = "policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                        ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                        ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4 = None
                    self.ipv6 = None
                    self._segment_path = lambda: "destination-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Policies.Policy.DestinationAddress, ['af_name', 'ipv4', 'ipv6'], name, value)


            class BindingSid(Entity):
                """
                Binding SID information
                
                .. attribute:: value
                
                	Binding SID value
                	**type**\:  :py:class:`Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.BindingSid.Value>`
                
                .. attribute:: bsid_mode
                
                	Binding SID Mode
                	**type**\:  :py:class:`XtcBsidMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcBsidMode>`
                
                .. attribute:: error
                
                	Binding SID error, if any
                	**type**\:  :py:class:`XtcBsidError <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcBsidError>`
                
                .. attribute:: state
                
                	State of the binding SID
                	**type**\: str
                
                .. attribute:: explicit_based
                
                	Whether the binding SID is explicit\-based
                	**type**\: bool
                
                .. attribute:: policy_selected
                
                	Whether the policy is selected for forwarding on this BSID
                	**type**\: bool
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.Policies.Policy.BindingSid, self).__init__()

                    self.yang_name = "binding-sid"
                    self.yang_parent_name = "policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("value", ("value", Xtc.Policies.Policy.BindingSid.Value))])
                    self._leafs = OrderedDict([
                        ('bsid_mode', (YLeaf(YType.enumeration, 'bsid-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcBsidMode', '')])),
                        ('error', (YLeaf(YType.enumeration, 'error'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcBsidError', '')])),
                        ('state', (YLeaf(YType.str, 'state'), ['str'])),
                        ('explicit_based', (YLeaf(YType.boolean, 'explicit-based'), ['bool'])),
                        ('policy_selected', (YLeaf(YType.boolean, 'policy-selected'), ['bool'])),
                    ])
                    self.bsid_mode = None
                    self.error = None
                    self.state = None
                    self.explicit_based = None
                    self.policy_selected = None

                    self.value = Xtc.Policies.Policy.BindingSid.Value()
                    self.value.parent = self
                    self._children_name_map["value"] = "value"
                    self._segment_path = lambda: "binding-sid"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Policies.Policy.BindingSid, ['bsid_mode', 'error', 'state', 'explicit_based', 'policy_selected'], name, value)


                class Value(Entity):
                    """
                    Binding SID value
                    
                    .. attribute:: sid_type
                    
                    	SIDType
                    	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                    
                    .. attribute:: label
                    
                    	MPLS label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.Policies.Policy.BindingSid.Value, self).__init__()

                        self.yang_name = "value"
                        self.yang_parent_name = "binding-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSid', '')])),
                            ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.sid_type = None
                        self.label = None
                        self.ipv6 = None
                        self._segment_path = lambda: "value"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.BindingSid.Value, ['sid_type', 'label', 'ipv6'], name, value)


            class AutoPolicyInfo(Entity):
                """
                Autopolicy information
                
                .. attribute:: creator_name
                
                	Name of client who created policy
                	**type**\: str
                
                .. attribute:: distinguisher
                
                	Distinguisher
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: preference
                
                	Preference of the policy
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.Policies.Policy.AutoPolicyInfo, self).__init__()

                    self.yang_name = "auto-policy-info"
                    self.yang_parent_name = "policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('creator_name', (YLeaf(YType.str, 'creator-name'), ['str'])),
                        ('distinguisher', (YLeaf(YType.uint32, 'distinguisher'), ['int'])),
                        ('preference', (YLeaf(YType.uint32, 'preference'), ['int'])),
                    ])
                    self.creator_name = None
                    self.distinguisher = None
                    self.preference = None
                    self._segment_path = lambda: "auto-policy-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Policies.Policy.AutoPolicyInfo, ['creator_name', 'distinguisher', 'preference'], name, value)


            class Paths(Entity):
                """
                Path options
                
                .. attribute:: sr_path_constraints
                
                	SR path constraints
                	**type**\:  :py:class:`SrPathConstraints <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.SrPathConstraints>`
                
                .. attribute:: index
                
                	Index number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Path option type
                	**type**\:  :py:class:`XtcPolicyPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcPolicyPath>`
                
                .. attribute:: name
                
                	Explicit path option name
                	**type**\: str
                
                .. attribute:: active
                
                	Whether the path is active (used)
                	**type**\: bool
                
                .. attribute:: weight
                
                	Configured weight of the path\-option
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: metric_type
                
                	Configured path metric type
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: metric_value
                
                	Path metric value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_valid
                
                	True if path is valid
                	**type**\: bool
                
                .. attribute:: pce_based_path
                
                	True if the path is to be computed by PCE
                	**type**\: bool
                
                .. attribute:: pce_address
                
                	Address of the PCE computed the path
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: error
                
                	Error (for display only)
                	**type**\: str
                
                .. attribute:: hops
                
                	SR hop list
                	**type**\: list of  		 :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.Hops>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.Policies.Policy.Paths, self).__init__()

                    self.yang_name = "paths"
                    self.yang_parent_name = "policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sr-path-constraints", ("sr_path_constraints", Xtc.Policies.Policy.Paths.SrPathConstraints)), ("hops", ("hops", Xtc.Policies.Policy.Paths.Hops))])
                    self._leafs = OrderedDict([
                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcPolicyPath', '')])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                        ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                        ('metric_type', (YLeaf(YType.uint8, 'metric-type'), ['int'])),
                        ('metric_value', (YLeaf(YType.uint32, 'metric-value'), ['int'])),
                        ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                        ('pce_based_path', (YLeaf(YType.boolean, 'pce-based-path'), ['bool'])),
                        ('pce_address', (YLeaf(YType.str, 'pce-address'), ['str'])),
                        ('error', (YLeaf(YType.str, 'error'), ['str'])),
                    ])
                    self.index = None
                    self.type = None
                    self.name = None
                    self.active = None
                    self.weight = None
                    self.metric_type = None
                    self.metric_value = None
                    self.is_valid = None
                    self.pce_based_path = None
                    self.pce_address = None
                    self.error = None

                    self.sr_path_constraints = Xtc.Policies.Policy.Paths.SrPathConstraints()
                    self.sr_path_constraints.parent = self
                    self._children_name_map["sr_path_constraints"] = "sr-path-constraints"

                    self.hops = YList(self)
                    self._segment_path = lambda: "paths"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Policies.Policy.Paths, ['index', 'type', 'name', 'active', 'weight', 'metric_type', 'metric_value', 'is_valid', 'pce_based_path', 'pce_address', 'error'], name, value)


                class SrPathConstraints(Entity):
                    """
                    SR path constraints
                    
                    .. attribute:: path_metrics
                    
                    	Path metrics
                    	**type**\:  :py:class:`PathMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.SrPathConstraints.PathMetrics>`
                    
                    .. attribute:: segments
                    
                    	Segments constraints
                    	**type**\:  :py:class:`Segments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.SrPathConstraints.Segments>`
                    
                    .. attribute:: affinity_constraint
                    
                    	Affinity constraints list
                    	**type**\: list of  		 :py:class:`AffinityConstraint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.SrPathConstraints.AffinityConstraint>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.Policies.Policy.Paths.SrPathConstraints, self).__init__()

                        self.yang_name = "sr-path-constraints"
                        self.yang_parent_name = "paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("path-metrics", ("path_metrics", Xtc.Policies.Policy.Paths.SrPathConstraints.PathMetrics)), ("segments", ("segments", Xtc.Policies.Policy.Paths.SrPathConstraints.Segments)), ("affinity-constraint", ("affinity_constraint", Xtc.Policies.Policy.Paths.SrPathConstraints.AffinityConstraint))])
                        self._leafs = OrderedDict()

                        self.path_metrics = Xtc.Policies.Policy.Paths.SrPathConstraints.PathMetrics()
                        self.path_metrics.parent = self
                        self._children_name_map["path_metrics"] = "path-metrics"

                        self.segments = Xtc.Policies.Policy.Paths.SrPathConstraints.Segments()
                        self.segments.parent = self
                        self._children_name_map["segments"] = "segments"

                        self.affinity_constraint = YList(self)
                        self._segment_path = lambda: "sr-path-constraints"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.Paths.SrPathConstraints, [], name, value)


                    class PathMetrics(Entity):
                        """
                        Path metrics
                        
                        .. attribute:: margin_relative
                        
                        	Margin Relative
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: margin_absolute
                        
                        	Margin Absolute
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: maximum_segments
                        
                        	Maximum number of segments
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: accumulative_te_metric
                        
                        	Accumulative TE metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: accumulative_igp_metric
                        
                        	Accumulative IGP metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: accumulative_delay
                        
                        	Accumulative delay
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.Policies.Policy.Paths.SrPathConstraints.PathMetrics, self).__init__()

                            self.yang_name = "path-metrics"
                            self.yang_parent_name = "sr-path-constraints"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('margin_relative', (YLeaf(YType.uint8, 'margin-relative'), ['int'])),
                                ('margin_absolute', (YLeaf(YType.uint8, 'margin-absolute'), ['int'])),
                                ('maximum_segments', (YLeaf(YType.uint16, 'maximum-segments'), ['int'])),
                                ('accumulative_te_metric', (YLeaf(YType.uint32, 'accumulative-te-metric'), ['int'])),
                                ('accumulative_igp_metric', (YLeaf(YType.uint32, 'accumulative-igp-metric'), ['int'])),
                                ('accumulative_delay', (YLeaf(YType.uint32, 'accumulative-delay'), ['int'])),
                            ])
                            self.margin_relative = None
                            self.margin_absolute = None
                            self.maximum_segments = None
                            self.accumulative_te_metric = None
                            self.accumulative_igp_metric = None
                            self.accumulative_delay = None
                            self._segment_path = lambda: "path-metrics"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.Paths.SrPathConstraints.PathMetrics, ['margin_relative', 'margin_absolute', 'maximum_segments', 'accumulative_te_metric', 'accumulative_igp_metric', 'accumulative_delay'], name, value)


                    class Segments(Entity):
                        """
                        Segments constraints
                        
                        .. attribute:: segment_algorithm
                        
                        	Segment Algorithm
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.Policies.Policy.Paths.SrPathConstraints.Segments, self).__init__()

                            self.yang_name = "segments"
                            self.yang_parent_name = "sr-path-constraints"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('segment_algorithm', (YLeaf(YType.uint8, 'segment-algorithm'), ['int'])),
                            ])
                            self.segment_algorithm = None
                            self._segment_path = lambda: "segments"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.Paths.SrPathConstraints.Segments, ['segment_algorithm'], name, value)


                    class AffinityConstraint(Entity):
                        """
                        Affinity constraints list
                        
                        .. attribute:: type
                        
                        	Affinity type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: value
                        
                        	Affinity value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: color
                        
                        	Colors
                        	**type**\: list of  		 :py:class:`Color <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.SrPathConstraints.AffinityConstraint.Color>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.Policies.Policy.Paths.SrPathConstraints.AffinityConstraint, self).__init__()

                            self.yang_name = "affinity-constraint"
                            self.yang_parent_name = "sr-path-constraints"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("color", ("color", Xtc.Policies.Policy.Paths.SrPathConstraints.AffinityConstraint.Color))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                            ])
                            self.type = None
                            self.value = None

                            self.color = YList(self)
                            self._segment_path = lambda: "affinity-constraint"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.Paths.SrPathConstraints.AffinityConstraint, ['type', 'value'], name, value)


                        class Color(Entity):
                            """
                            Colors
                            
                            .. attribute:: color
                            
                            	An affinity color
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.Policies.Policy.Paths.SrPathConstraints.AffinityConstraint.Color, self).__init__()

                                self.yang_name = "color"
                                self.yang_parent_name = "affinity-constraint"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('color', (YLeaf(YType.str, 'color'), ['str'])),
                                ])
                                self.color = None
                                self._segment_path = lambda: "color"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.Policies.Policy.Paths.SrPathConstraints.AffinityConstraint.Color, ['color'], name, value)


                class Hops(Entity):
                    """
                    SR hop list
                    
                    .. attribute:: sid
                    
                    	SID value
                    	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.Hops.Sid>`
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.Hops.LocalAddress>`
                    
                    .. attribute:: remote_address
                    
                    	Remote address
                    	**type**\:  :py:class:`RemoteAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.Paths.Hops.RemoteAddress>`
                    
                    .. attribute:: sid_type
                    
                    	SID type
                    	**type**\:  :py:class:`XtcSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSrSid>`
                    
                    .. attribute:: algorithm
                    
                    	Algorithim
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.Policies.Policy.Paths.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid", ("sid", Xtc.Policies.Policy.Paths.Hops.Sid)), ("local-address", ("local_address", Xtc.Policies.Policy.Paths.Hops.LocalAddress)), ("remote-address", ("remote_address", Xtc.Policies.Policy.Paths.Hops.RemoteAddress))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSrSid', '')])),
                            ('algorithm', (YLeaf(YType.uint8, 'algorithm'), ['int'])),
                        ])
                        self.sid_type = None
                        self.algorithm = None

                        self.sid = Xtc.Policies.Policy.Paths.Hops.Sid()
                        self.sid.parent = self
                        self._children_name_map["sid"] = "sid"

                        self.local_address = Xtc.Policies.Policy.Paths.Hops.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"

                        self.remote_address = Xtc.Policies.Policy.Paths.Hops.RemoteAddress()
                        self.remote_address.parent = self
                        self._children_name_map["remote_address"] = "remote-address"
                        self._segment_path = lambda: "hops"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.Paths.Hops, ['sid_type', 'algorithm'], name, value)


                    class Sid(Entity):
                        """
                        SID value
                        
                        .. attribute:: sid_type
                        
                        	SIDType
                        	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                        
                        .. attribute:: label
                        
                        	MPLS label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.Policies.Policy.Paths.Hops.Sid, self).__init__()

                            self.yang_name = "sid"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSid', '')])),
                                ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.sid_type = None
                            self.label = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.Paths.Hops.Sid, ['sid_type', 'label', 'ipv6'], name, value)


                    class LocalAddress(Entity):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.Policies.Policy.Paths.Hops.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "local-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.Paths.Hops.LocalAddress, ['af_name', 'ipv4', 'ipv6'], name, value)


                    class RemoteAddress(Entity):
                        """
                        Remote address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.Policies.Policy.Paths.Hops.RemoteAddress, self).__init__()

                            self.yang_name = "remote-address"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "remote-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.Paths.Hops.RemoteAddress, ['af_name', 'ipv4', 'ipv6'], name, value)


    class PolicySummary(Entity):
        """
        Summary of all policies
        
        .. attribute:: ipv4_source_address
        
        	IPv4 address used for IPv4 policies
        	**type**\:  :py:class:`Ipv4SourceAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicySummary.Ipv4SourceAddress>`
        
        .. attribute:: configured_total_policy_count
        
        	Total number of configured policies
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: configured_up_policy_count
        
        	Total number of configured policies that are operationally up
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: configured_down_policy_count
        
        	Total number of configured policies that are operationally down
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Xtc.PolicySummary, self).__init__()

            self.yang_name = "policy-summary"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv4-source-address", ("ipv4_source_address", Xtc.PolicySummary.Ipv4SourceAddress))])
            self._leafs = OrderedDict([
                ('configured_total_policy_count', (YLeaf(YType.uint32, 'configured-total-policy-count'), ['int'])),
                ('configured_up_policy_count', (YLeaf(YType.uint32, 'configured-up-policy-count'), ['int'])),
                ('configured_down_policy_count', (YLeaf(YType.uint32, 'configured-down-policy-count'), ['int'])),
            ])
            self.configured_total_policy_count = None
            self.configured_up_policy_count = None
            self.configured_down_policy_count = None

            self.ipv4_source_address = Xtc.PolicySummary.Ipv4SourceAddress()
            self.ipv4_source_address.parent = self
            self._children_name_map["ipv4_source_address"] = "ipv4-source-address"
            self._segment_path = lambda: "policy-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.PolicySummary, ['configured_total_policy_count', 'configured_up_policy_count', 'configured_down_policy_count'], name, value)


        class Ipv4SourceAddress(Entity):
            """
            IPv4 address used for IPv4 policies
            
            .. attribute:: af_name
            
            	AFName
            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
            
            .. attribute:: ipv4
            
            	IPv4 address type
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipv6
            
            	IPv6 address type
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Xtc.PolicySummary.Ipv4SourceAddress, self).__init__()

                self.yang_name = "ipv4-source-address"
                self.yang_parent_name = "policy-summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                ])
                self.af_name = None
                self.ipv4 = None
                self.ipv6 = None
                self._segment_path = lambda: "ipv4-source-address"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policy-summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.PolicySummary.Ipv4SourceAddress, ['af_name', 'ipv4', 'ipv6'], name, value)


    class OnDemandColors(Entity):
        """
        On\-Demand Color database in XTC Agent
        
        .. attribute:: on_demand_color
        
        	On Demand Color information
        	**type**\: list of  		 :py:class:`OnDemandColor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.OnDemandColors.OnDemandColor>`
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Xtc.OnDemandColors, self).__init__()

            self.yang_name = "on-demand-colors"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("on-demand-color", ("on_demand_color", Xtc.OnDemandColors.OnDemandColor))])
            self._leafs = OrderedDict()

            self.on_demand_color = YList(self)
            self._segment_path = lambda: "on-demand-colors"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.OnDemandColors, [], name, value)


        class OnDemandColor(Entity):
            """
            On Demand Color information
            
            .. attribute:: color  (key)
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: disjoint_path_info
            
            	Disjoint path information
            	**type**\:  :py:class:`DisjointPathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.OnDemandColors.OnDemandColor.DisjointPathInfo>`
            
            .. attribute:: color_xr
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: maximum_sid_depth
            
            	Maximum SID Depth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Xtc.OnDemandColors.OnDemandColor, self).__init__()

                self.yang_name = "on-demand-color"
                self.yang_parent_name = "on-demand-colors"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['color']
                self._child_classes = OrderedDict([("disjoint-path-info", ("disjoint_path_info", Xtc.OnDemandColors.OnDemandColor.DisjointPathInfo))])
                self._leafs = OrderedDict([
                    ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                    ('color_xr', (YLeaf(YType.uint32, 'color-xr'), ['int'])),
                    ('maximum_sid_depth', (YLeaf(YType.uint32, 'maximum-sid-depth'), ['int'])),
                ])
                self.color = None
                self.color_xr = None
                self.maximum_sid_depth = None

                self.disjoint_path_info = Xtc.OnDemandColors.OnDemandColor.DisjointPathInfo()
                self.disjoint_path_info.parent = self
                self._children_name_map["disjoint_path_info"] = "disjoint-path-info"
                self._segment_path = lambda: "on-demand-color" + "[color='" + str(self.color) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/on-demand-colors/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.OnDemandColors.OnDemandColor, ['color', 'color_xr', 'maximum_sid_depth'], name, value)


            class DisjointPathInfo(Entity):
                """
                Disjoint path information
                
                .. attribute:: disjointness_type
                
                	Disjointness type
                	**type**\:  :py:class:`XtcDisjointness <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcDisjointness>`
                
                .. attribute:: group_id
                
                	Group ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sub_id
                
                	Sub ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.OnDemandColors.OnDemandColor.DisjointPathInfo, self).__init__()

                    self.yang_name = "disjoint-path-info"
                    self.yang_parent_name = "on-demand-color"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('disjointness_type', (YLeaf(YType.enumeration, 'disjointness-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcDisjointness', '')])),
                        ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                        ('sub_id', (YLeaf(YType.uint32, 'sub-id'), ['int'])),
                    ])
                    self.disjointness_type = None
                    self.group_id = None
                    self.sub_id = None
                    self._segment_path = lambda: "disjoint-path-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.OnDemandColors.OnDemandColor.DisjointPathInfo, ['disjointness_type', 'group_id', 'sub_id'], name, value)


    class Forwarding(Entity):
        """
        Forwarding information
        
        .. attribute:: policy_forwardings
        
        	Forwarding information for policies
        	**type**\:  :py:class:`PolicyForwardings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Forwarding.PolicyForwardings>`
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Xtc.Forwarding, self).__init__()

            self.yang_name = "forwarding"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-forwardings", ("policy_forwardings", Xtc.Forwarding.PolicyForwardings))])
            self._leafs = OrderedDict()

            self.policy_forwardings = Xtc.Forwarding.PolicyForwardings()
            self.policy_forwardings.parent = self
            self._children_name_map["policy_forwardings"] = "policy-forwardings"
            self._segment_path = lambda: "forwarding"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.Forwarding, [], name, value)


        class PolicyForwardings(Entity):
            """
            Forwarding information for policies
            
            .. attribute:: policy_forwarding
            
            	Forwarding information for the policy
            	**type**\: list of  		 :py:class:`PolicyForwarding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Forwarding.PolicyForwardings.PolicyForwarding>`
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Xtc.Forwarding.PolicyForwardings, self).__init__()

                self.yang_name = "policy-forwardings"
                self.yang_parent_name = "forwarding"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policy-forwarding", ("policy_forwarding", Xtc.Forwarding.PolicyForwardings.PolicyForwarding))])
                self._leafs = OrderedDict()

                self.policy_forwarding = YList(self)
                self._segment_path = lambda: "policy-forwardings"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/forwarding/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.Forwarding.PolicyForwardings, [], name, value)


            class PolicyForwarding(Entity):
                """
                Forwarding information for the policy
                
                .. attribute:: name  (key)
                
                	Policy Name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: policy_name
                
                	Policy name
                	**type**\: str
                
                .. attribute:: is_local_label_valid
                
                	Is local label valid and allocated?
                	**type**\: bool
                
                .. attribute:: local_label
                
                	Local label for SR MPLS policy
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: are_stats_valid
                
                	Are policy stats valid?
                	**type**\: bool
                
                .. attribute:: forwarding_stats_pkts
                
                	Number of packets forwarded
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: forwarding_stats_bytes
                
                	Number of bytes forwarded
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: paths
                
                	Forwarding paths
                	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Forwarding.PolicyForwardings.PolicyForwarding.Paths>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.Forwarding.PolicyForwardings.PolicyForwarding, self).__init__()

                    self.yang_name = "policy-forwarding"
                    self.yang_parent_name = "policy-forwardings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("paths", ("paths", Xtc.Forwarding.PolicyForwardings.PolicyForwarding.Paths))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                        ('is_local_label_valid', (YLeaf(YType.boolean, 'is-local-label-valid'), ['bool'])),
                        ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                        ('are_stats_valid', (YLeaf(YType.boolean, 'are-stats-valid'), ['bool'])),
                        ('forwarding_stats_pkts', (YLeaf(YType.uint64, 'forwarding-stats-pkts'), ['int'])),
                        ('forwarding_stats_bytes', (YLeaf(YType.uint64, 'forwarding-stats-bytes'), ['int'])),
                    ])
                    self.name = None
                    self.policy_name = None
                    self.is_local_label_valid = None
                    self.local_label = None
                    self.are_stats_valid = None
                    self.forwarding_stats_pkts = None
                    self.forwarding_stats_bytes = None

                    self.paths = YList(self)
                    self._segment_path = lambda: "policy-forwarding" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/forwarding/policy-forwardings/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Forwarding.PolicyForwardings.PolicyForwarding, ['name', 'policy_name', 'is_local_label_valid', 'local_label', 'are_stats_valid', 'forwarding_stats_pkts', 'forwarding_stats_bytes'], name, value)


                class Paths(Entity):
                    """
                    Forwarding paths
                    
                    .. attribute:: outgoing_interface
                    
                    	Outgoing interface handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: next_hop_ipv4
                    
                    	IPv4 Next Hop
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: next_hop_table_id
                    
                    	Table ID for nexthop address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_protected
                    
                    	Is this path protected ?
                    	**type**\: bool
                    
                    .. attribute:: is_pure_bkup
                    
                    	Is this path a pure backup ?
                    	**type**\: bool
                    
                    .. attribute:: load_metric
                    
                    	Path's load metric for load balancing
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: path_id
                    
                    	path Id
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: bkup_path_id
                    
                    	Backup path Id
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: segment_list_name
                    
                    	Associated segment\-list
                    	**type**\: str
                    
                    .. attribute:: are_stats_valid
                    
                    	Are per path stats valid?
                    	**type**\: bool
                    
                    .. attribute:: forwarding_stats_pkts
                    
                    	Number of packets forwarded on this path
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: forwarding_stats_bytes
                    
                    	Number of bytes forwarded on this path
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: label_stack
                    
                    	Path outgoing labels
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.Forwarding.PolicyForwardings.PolicyForwarding.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "policy-forwarding"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                            ('next_hop_ipv4', (YLeaf(YType.str, 'next-hop-ipv4'), ['str'])),
                            ('next_hop_table_id', (YLeaf(YType.uint32, 'next-hop-table-id'), ['int'])),
                            ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                            ('is_pure_bkup', (YLeaf(YType.boolean, 'is-pure-bkup'), ['bool'])),
                            ('load_metric', (YLeaf(YType.uint32, 'load-metric'), ['int'])),
                            ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                            ('bkup_path_id', (YLeaf(YType.uint8, 'bkup-path-id'), ['int'])),
                            ('segment_list_name', (YLeaf(YType.str, 'segment-list-name'), ['str'])),
                            ('are_stats_valid', (YLeaf(YType.boolean, 'are-stats-valid'), ['bool'])),
                            ('forwarding_stats_pkts', (YLeaf(YType.uint64, 'forwarding-stats-pkts'), ['int'])),
                            ('forwarding_stats_bytes', (YLeaf(YType.uint64, 'forwarding-stats-bytes'), ['int'])),
                            ('label_stack', (YLeafList(YType.uint32, 'label-stack'), ['int'])),
                        ])
                        self.outgoing_interface = None
                        self.next_hop_ipv4 = None
                        self.next_hop_table_id = None
                        self.is_protected = None
                        self.is_pure_bkup = None
                        self.load_metric = None
                        self.path_id = None
                        self.bkup_path_id = None
                        self.segment_list_name = None
                        self.are_stats_valid = None
                        self.forwarding_stats_pkts = None
                        self.forwarding_stats_bytes = None
                        self.label_stack = []
                        self._segment_path = lambda: "paths"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Forwarding.PolicyForwardings.PolicyForwarding.Paths, ['outgoing_interface', 'next_hop_ipv4', 'next_hop_table_id', 'is_protected', 'is_pure_bkup', 'load_metric', 'path_id', 'bkup_path_id', 'segment_list_name', 'are_stats_valid', 'forwarding_stats_pkts', 'forwarding_stats_bytes', 'label_stack'], name, value)


    class Controller(Entity):
        """
        Controller information
        
        .. attribute:: policy_requests
        
        	Table containing policy requests
        	**type**\:  :py:class:`PolicyRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests>`
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Xtc.Controller, self).__init__()

            self.yang_name = "controller"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-requests", ("policy_requests", Xtc.Controller.PolicyRequests))])
            self._leafs = OrderedDict()

            self.policy_requests = Xtc.Controller.PolicyRequests()
            self.policy_requests.parent = self
            self._children_name_map["policy_requests"] = "policy-requests"
            self._segment_path = lambda: "controller"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.Controller, [], name, value)


        class PolicyRequests(Entity):
            """
            Table containing policy requests
            
            .. attribute:: policy_request
            
            	Policy request information
            	**type**\: list of  		 :py:class:`PolicyRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest>`
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Xtc.Controller.PolicyRequests, self).__init__()

                self.yang_name = "policy-requests"
                self.yang_parent_name = "controller"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policy-request", ("policy_request", Xtc.Controller.PolicyRequests.PolicyRequest))])
                self._leafs = OrderedDict()

                self.policy_request = YList(self)
                self._segment_path = lambda: "policy-requests"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/controller/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.Controller.PolicyRequests, [], name, value)


            class PolicyRequest(Entity):
                """
                Policy request information
                
                .. attribute:: source_address  (key)
                
                	Source Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: end_point_type  (key)
                
                	Endpoint Address Type
                	**type**\:  :py:class:`XtcAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAddressFamily>`
                
                .. attribute:: end_point_address  (key)
                
                	Endpoint Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: color  (key)
                
                	Color
                	**type**\: int
                
                	**range:** 1..4294967295
                
                .. attribute:: route_distinguisher  (key)
                
                	Route Distinguisher
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: end_point
                
                	End point
                	**type**\:  :py:class:`EndPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.EndPoint>`
                
                .. attribute:: source_address_xr
                
                	Source address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: binding_sid
                
                	Binding SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: preference
                
                	Preference
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: color_xr
                
                	Color
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_distinguisher_xr
                
                	Route distinguisher
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: creation_time
                
                	Creation time of the request in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: last_updated_time
                
                	Last updated time of the request in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: paths
                
                	Path options
                	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.Controller.PolicyRequests.PolicyRequest, self).__init__()

                    self.yang_name = "policy-request"
                    self.yang_parent_name = "policy-requests"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['source_address','end_point_type','end_point_address','color','route_distinguisher']
                    self._child_classes = OrderedDict([("end-point", ("end_point", Xtc.Controller.PolicyRequests.PolicyRequest.EndPoint)), ("paths", ("paths", Xtc.Controller.PolicyRequests.PolicyRequest.Paths))])
                    self._leafs = OrderedDict([
                        ('source_address', (YLeaf(YType.str, 'source-address'), ['str','str'])),
                        ('end_point_type', (YLeaf(YType.enumeration, 'end-point-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAddressFamily', '')])),
                        ('end_point_address', (YLeaf(YType.str, 'end-point-address'), ['str','str'])),
                        ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                        ('route_distinguisher', (YLeaf(YType.uint32, 'route-distinguisher'), ['int'])),
                        ('source_address_xr', (YLeaf(YType.str, 'source-address-xr'), ['str'])),
                        ('binding_sid', (YLeaf(YType.uint32, 'binding-sid'), ['int'])),
                        ('preference', (YLeaf(YType.uint32, 'preference'), ['int'])),
                        ('color_xr', (YLeaf(YType.uint32, 'color-xr'), ['int'])),
                        ('route_distinguisher_xr', (YLeaf(YType.uint32, 'route-distinguisher-xr'), ['int'])),
                        ('creation_time', (YLeaf(YType.uint32, 'creation-time'), ['int'])),
                        ('last_updated_time', (YLeaf(YType.uint32, 'last-updated-time'), ['int'])),
                    ])
                    self.source_address = None
                    self.end_point_type = None
                    self.end_point_address = None
                    self.color = None
                    self.route_distinguisher = None
                    self.source_address_xr = None
                    self.binding_sid = None
                    self.preference = None
                    self.color_xr = None
                    self.route_distinguisher_xr = None
                    self.creation_time = None
                    self.last_updated_time = None

                    self.end_point = Xtc.Controller.PolicyRequests.PolicyRequest.EndPoint()
                    self.end_point.parent = self
                    self._children_name_map["end_point"] = "end-point"

                    self.paths = YList(self)
                    self._segment_path = lambda: "policy-request" + "[source-address='" + str(self.source_address) + "']" + "[end-point-type='" + str(self.end_point_type) + "']" + "[end-point-address='" + str(self.end_point_address) + "']" + "[color='" + str(self.color) + "']" + "[route-distinguisher='" + str(self.route_distinguisher) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/controller/policy-requests/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest, ['source_address', 'end_point_type', 'end_point_address', 'color', 'route_distinguisher', 'source_address_xr', 'binding_sid', 'preference', 'color_xr', 'route_distinguisher_xr', 'creation_time', 'last_updated_time'], name, value)


                class EndPoint(Entity):
                    """
                    End point
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.Controller.PolicyRequests.PolicyRequest.EndPoint, self).__init__()

                        self.yang_name = "end-point"
                        self.yang_parent_name = "policy-request"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "end-point"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.EndPoint, ['af_name', 'ipv4', 'ipv6'], name, value)


                class Paths(Entity):
                    """
                    Path options
                    
                    .. attribute:: sr_path_constraints
                    
                    	SR path constraints
                    	**type**\:  :py:class:`SrPathConstraints <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints>`
                    
                    .. attribute:: index
                    
                    	Index number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	Path option type
                    	**type**\:  :py:class:`XtcPolicyPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcPolicyPath>`
                    
                    .. attribute:: name
                    
                    	Explicit path option name
                    	**type**\: str
                    
                    .. attribute:: active
                    
                    	Whether the path is active (used)
                    	**type**\: bool
                    
                    .. attribute:: weight
                    
                    	Configured weight of the path\-option
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: metric_type
                    
                    	Configured path metric type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: metric_value
                    
                    	Path metric value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_valid
                    
                    	True if path is valid
                    	**type**\: bool
                    
                    .. attribute:: pce_based_path
                    
                    	True if the path is to be computed by PCE
                    	**type**\: bool
                    
                    .. attribute:: pce_address
                    
                    	Address of the PCE computed the path
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: error
                    
                    	Error (for display only)
                    	**type**\: str
                    
                    .. attribute:: hops
                    
                    	SR hop list
                    	**type**\: list of  		 :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "policy-request"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sr-path-constraints", ("sr_path_constraints", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints)), ("hops", ("hops", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops))])
                        self._leafs = OrderedDict([
                            ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcPolicyPath', '')])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                            ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                            ('metric_type', (YLeaf(YType.uint8, 'metric-type'), ['int'])),
                            ('metric_value', (YLeaf(YType.uint32, 'metric-value'), ['int'])),
                            ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                            ('pce_based_path', (YLeaf(YType.boolean, 'pce-based-path'), ['bool'])),
                            ('pce_address', (YLeaf(YType.str, 'pce-address'), ['str'])),
                            ('error', (YLeaf(YType.str, 'error'), ['str'])),
                        ])
                        self.index = None
                        self.type = None
                        self.name = None
                        self.active = None
                        self.weight = None
                        self.metric_type = None
                        self.metric_value = None
                        self.is_valid = None
                        self.pce_based_path = None
                        self.pce_address = None
                        self.error = None

                        self.sr_path_constraints = Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints()
                        self.sr_path_constraints.parent = self
                        self._children_name_map["sr_path_constraints"] = "sr-path-constraints"

                        self.hops = YList(self)
                        self._segment_path = lambda: "paths"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths, ['index', 'type', 'name', 'active', 'weight', 'metric_type', 'metric_value', 'is_valid', 'pce_based_path', 'pce_address', 'error'], name, value)


                    class SrPathConstraints(Entity):
                        """
                        SR path constraints
                        
                        .. attribute:: path_metrics
                        
                        	Path metrics
                        	**type**\:  :py:class:`PathMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.PathMetrics>`
                        
                        .. attribute:: segments
                        
                        	Segments constraints
                        	**type**\:  :py:class:`Segments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.Segments>`
                        
                        .. attribute:: affinity_constraint
                        
                        	Affinity constraints list
                        	**type**\: list of  		 :py:class:`AffinityConstraint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.AffinityConstraint>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints, self).__init__()

                            self.yang_name = "sr-path-constraints"
                            self.yang_parent_name = "paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("path-metrics", ("path_metrics", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.PathMetrics)), ("segments", ("segments", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.Segments)), ("affinity-constraint", ("affinity_constraint", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.AffinityConstraint))])
                            self._leafs = OrderedDict()

                            self.path_metrics = Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.PathMetrics()
                            self.path_metrics.parent = self
                            self._children_name_map["path_metrics"] = "path-metrics"

                            self.segments = Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.Segments()
                            self.segments.parent = self
                            self._children_name_map["segments"] = "segments"

                            self.affinity_constraint = YList(self)
                            self._segment_path = lambda: "sr-path-constraints"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints, [], name, value)


                        class PathMetrics(Entity):
                            """
                            Path metrics
                            
                            .. attribute:: margin_relative
                            
                            	Margin Relative
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: margin_absolute
                            
                            	Margin Absolute
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: maximum_segments
                            
                            	Maximum number of segments
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: accumulative_te_metric
                            
                            	Accumulative TE metric
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accumulative_igp_metric
                            
                            	Accumulative IGP metric
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accumulative_delay
                            
                            	Accumulative delay
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.PathMetrics, self).__init__()

                                self.yang_name = "path-metrics"
                                self.yang_parent_name = "sr-path-constraints"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('margin_relative', (YLeaf(YType.uint8, 'margin-relative'), ['int'])),
                                    ('margin_absolute', (YLeaf(YType.uint8, 'margin-absolute'), ['int'])),
                                    ('maximum_segments', (YLeaf(YType.uint16, 'maximum-segments'), ['int'])),
                                    ('accumulative_te_metric', (YLeaf(YType.uint32, 'accumulative-te-metric'), ['int'])),
                                    ('accumulative_igp_metric', (YLeaf(YType.uint32, 'accumulative-igp-metric'), ['int'])),
                                    ('accumulative_delay', (YLeaf(YType.uint32, 'accumulative-delay'), ['int'])),
                                ])
                                self.margin_relative = None
                                self.margin_absolute = None
                                self.maximum_segments = None
                                self.accumulative_te_metric = None
                                self.accumulative_igp_metric = None
                                self.accumulative_delay = None
                                self._segment_path = lambda: "path-metrics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.PathMetrics, ['margin_relative', 'margin_absolute', 'maximum_segments', 'accumulative_te_metric', 'accumulative_igp_metric', 'accumulative_delay'], name, value)


                        class Segments(Entity):
                            """
                            Segments constraints
                            
                            .. attribute:: segment_algorithm
                            
                            	Segment Algorithm
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.Segments, self).__init__()

                                self.yang_name = "segments"
                                self.yang_parent_name = "sr-path-constraints"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('segment_algorithm', (YLeaf(YType.uint8, 'segment-algorithm'), ['int'])),
                                ])
                                self.segment_algorithm = None
                                self._segment_path = lambda: "segments"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.Segments, ['segment_algorithm'], name, value)


                        class AffinityConstraint(Entity):
                            """
                            Affinity constraints list
                            
                            .. attribute:: type
                            
                            	Affinity type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: value
                            
                            	Affinity value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: color
                            
                            	Colors
                            	**type**\: list of  		 :py:class:`Color <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.AffinityConstraint.Color>`
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.AffinityConstraint, self).__init__()

                                self.yang_name = "affinity-constraint"
                                self.yang_parent_name = "sr-path-constraints"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("color", ("color", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.AffinityConstraint.Color))])
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ])
                                self.type = None
                                self.value = None

                                self.color = YList(self)
                                self._segment_path = lambda: "affinity-constraint"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.AffinityConstraint, ['type', 'value'], name, value)


                            class Color(Entity):
                                """
                                Colors
                                
                                .. attribute:: color
                                
                                	An affinity color
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.AffinityConstraint.Color, self).__init__()

                                    self.yang_name = "color"
                                    self.yang_parent_name = "affinity-constraint"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('color', (YLeaf(YType.str, 'color'), ['str'])),
                                    ])
                                    self.color = None
                                    self._segment_path = lambda: "color"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.SrPathConstraints.AffinityConstraint.Color, ['color'], name, value)


                    class Hops(Entity):
                        """
                        SR hop list
                        
                        .. attribute:: sid
                        
                        	SID value
                        	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.Sid>`
                        
                        .. attribute:: local_address
                        
                        	Local address
                        	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.LocalAddress>`
                        
                        .. attribute:: remote_address
                        
                        	Remote address
                        	**type**\:  :py:class:`RemoteAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.RemoteAddress>`
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`XtcSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSrSid>`
                        
                        .. attribute:: algorithm
                        
                        	Algorithim
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops, self).__init__()

                            self.yang_name = "hops"
                            self.yang_parent_name = "paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sid", ("sid", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.Sid)), ("local-address", ("local_address", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.LocalAddress)), ("remote-address", ("remote_address", Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.RemoteAddress))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSrSid', '')])),
                                ('algorithm', (YLeaf(YType.uint8, 'algorithm'), ['int'])),
                            ])
                            self.sid_type = None
                            self.algorithm = None

                            self.sid = Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.Sid()
                            self.sid.parent = self
                            self._children_name_map["sid"] = "sid"

                            self.local_address = Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.LocalAddress()
                            self.local_address.parent = self
                            self._children_name_map["local_address"] = "local-address"

                            self.remote_address = Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.RemoteAddress()
                            self.remote_address.parent = self
                            self._children_name_map["remote_address"] = "remote-address"
                            self._segment_path = lambda: "hops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops, ['sid_type', 'algorithm'], name, value)


                        class Sid(Entity):
                            """
                            SID value
                            
                            .. attribute:: sid_type
                            
                            	SIDType
                            	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                            
                            .. attribute:: label
                            
                            	MPLS label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.Sid, self).__init__()

                                self.yang_name = "sid"
                                self.yang_parent_name = "hops"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSid', '')])),
                                    ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.sid_type = None
                                self.label = None
                                self.ipv6 = None
                                self._segment_path = lambda: "sid"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.Sid, ['sid_type', 'label', 'ipv6'], name, value)


                        class LocalAddress(Entity):
                            """
                            Local address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.LocalAddress, self).__init__()

                                self.yang_name = "local-address"
                                self.yang_parent_name = "hops"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "local-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.LocalAddress, ['af_name', 'ipv4', 'ipv6'], name, value)


                        class RemoteAddress(Entity):
                            """
                            Remote address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.RemoteAddress, self).__init__()

                                self.yang_name = "remote-address"
                                self.yang_parent_name = "hops"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                                    ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                    ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4 = None
                                self.ipv6 = None
                                self._segment_path = lambda: "remote-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.Paths.Hops.RemoteAddress, ['af_name', 'ipv4', 'ipv6'], name, value)


    class TopologySummary(Entity):
        """
        Node summary database
        
        .. attribute:: nodes
        
        	Number of nodes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefixes
        
        	Number of prefixes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: prefix_sids
        
        	Number of prefix SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: links
        
        	Number of links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: adjacency_sids
        
        	Number of adjacency SIDs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Xtc.TopologySummary, self).__init__()

            self.yang_name = "topology-summary"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('nodes', (YLeaf(YType.uint32, 'nodes'), ['int'])),
                ('prefixes', (YLeaf(YType.uint32, 'prefixes'), ['int'])),
                ('prefix_sids', (YLeaf(YType.uint32, 'prefix-sids'), ['int'])),
                ('links', (YLeaf(YType.uint32, 'links'), ['int'])),
                ('adjacency_sids', (YLeaf(YType.uint32, 'adjacency-sids'), ['int'])),
            ])
            self.nodes = None
            self.prefixes = None
            self.prefix_sids = None
            self.links = None
            self.adjacency_sids = None
            self._segment_path = lambda: "topology-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.TopologySummary, ['nodes', 'prefixes', 'prefix_sids', 'links', 'adjacency_sids'], name, value)


    class TopologyNodes(Entity):
        """
        Node database in XTC Agent
        
        .. attribute:: topology_node
        
        	Node information
        	**type**\: list of  		 :py:class:`TopologyNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode>`
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Xtc.TopologyNodes, self).__init__()

            self.yang_name = "topology-nodes"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("topology-node", ("topology_node", Xtc.TopologyNodes.TopologyNode))])
            self._leafs = OrderedDict()

            self.topology_node = YList(self)
            self._segment_path = lambda: "topology-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.TopologyNodes, [], name, value)


        class TopologyNode(Entity):
            """
            Node information
            
            .. attribute:: node_identifier  (key)
            
            	Node Identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:  :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: overload
            
            	Node Overload Bit
            	**type**\: bool
            
            .. attribute:: prefix_sid
            
            	Prefix SIDs
            	**type**\: list of  		 :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.PrefixSid>`
            
            .. attribute:: ipv4_link
            
            	IPv4 Link information
            	**type**\: list of  		 :py:class:`Ipv4Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link>`
            
            .. attribute:: ipv6_link
            
            	IPv6 Link information
            	**type**\: list of  		 :py:class:`Ipv6Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link>`
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Xtc.TopologyNodes.TopologyNode, self).__init__()

                self.yang_name = "topology-node"
                self.yang_parent_name = "topology-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_identifier']
                self._child_classes = OrderedDict([("node-protocol-identifier", ("node_protocol_identifier", Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier)), ("prefix-sid", ("prefix_sid", Xtc.TopologyNodes.TopologyNode.PrefixSid)), ("ipv4-link", ("ipv4_link", Xtc.TopologyNodes.TopologyNode.Ipv4Link)), ("ipv6-link", ("ipv6_link", Xtc.TopologyNodes.TopologyNode.Ipv6Link))])
                self._leafs = OrderedDict([
                    ('node_identifier', (YLeaf(YType.uint32, 'node-identifier'), ['int'])),
                    ('node_identifier_xr', (YLeaf(YType.uint32, 'node-identifier-xr'), ['int'])),
                    ('overload', (YLeaf(YType.boolean, 'overload'), ['bool'])),
                ])
                self.node_identifier = None
                self.node_identifier_xr = None
                self.overload = None

                self.node_protocol_identifier = Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"

                self.prefix_sid = YList(self)
                self.ipv4_link = YList(self)
                self.ipv6_link = YList(self)
                self._segment_path = lambda: "topology-node" + "[node-identifier='" + str(self.node_identifier) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/topology-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.TopologyNodes.TopologyNode, ['node_identifier', 'node_identifier_xr', 'overload'], name, value)


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
                	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("igp-information", ("igp_information", Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation))])
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
                    self._segment_path = lambda: "node-protocol-identifier"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier, ['node_name', 'ipv4_bgp_router_id_set', 'ipv4_bgp_router_id', 'ipv4te_router_id_set', 'ipv4te_router_id'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp", ("igp", Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.igp = Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._segment_path = lambda: "igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation, ['domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("isis", ("isis", Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis)), ("ospf", ("ospf", Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf)), ("bgp", ("bgp", Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp))])
                            self._leafs = OrderedDict([
                                ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcIgpInfoId', '')])),
                            ])
                            self.igp_id = None

                            self.isis = Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"

                            self.ospf = Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"

                            self.bgp = Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._segment_path = lambda: "igp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


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

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

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
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis, ['system_id', 'level'], name, value)


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

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

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
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['router_id', 'area'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                ])
                                self.router_id = None
                                self._segment_path = lambda: "bgp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['router_id'], name, value)


            class PrefixSid(Entity):
                """
                Prefix SIDs
                
                .. attribute:: sid_prefix
                
                	Prefix
                	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.PrefixSid.SidPrefix>`
                
                .. attribute:: sid_type
                
                	SID Type
                	**type**\:  :py:class:`XtcSid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid1>`
                
                .. attribute:: algorithm
                
                	Prefix\-SID algorithm number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mpls_label
                
                	MPLS Label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.TopologyNodes.TopologyNode.PrefixSid, self).__init__()

                    self.yang_name = "prefix-sid"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", Xtc.TopologyNodes.TopologyNode.PrefixSid.SidPrefix))])
                    self._leafs = OrderedDict([
                        ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSid1', '')])),
                        ('algorithm', (YLeaf(YType.uint32, 'algorithm'), ['int'])),
                        ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                    ])
                    self.sid_type = None
                    self.algorithm = None
                    self.mpls_label = None

                    self.sid_prefix = Xtc.TopologyNodes.TopologyNode.PrefixSid.SidPrefix()
                    self.sid_prefix.parent = self
                    self._children_name_map["sid_prefix"] = "sid-prefix"
                    self._segment_path = lambda: "prefix-sid"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.PrefixSid, ['sid_type', 'algorithm', 'mpls_label'], name, value)


                class SidPrefix(Entity):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.TopologyNodes.TopologyNode.PrefixSid.SidPrefix, self).__init__()

                        self.yang_name = "sid-prefix"
                        self.yang_parent_name = "prefix-sid"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "sid-prefix"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.PrefixSid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


            class Ipv4Link(Entity):
                """
                IPv4 Link information
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:  :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation>`
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:  :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier>`
                
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
                	**type**\: list of  		 :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.TopologyNodes.TopologyNode.Ipv4Link, self).__init__()

                    self.yang_name = "ipv4-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-igp-information", ("local_igp_information", Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation)), ("remote-node-protocol-identifier", ("remote_node_protocol_identifier", Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier)), ("adjacency-sid", ("adjacency_sid", Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid))])
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

                    self.local_igp_information = Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"

                    self.remote_node_protocol_identifier = Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv4-link"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link, ['local_ipv4_address', 'remote_ipv4_address', 'igp_metric', 'te_metric', 'maximum_link_bandwidth', 'max_reservable_bandwidth', 'administrative_groups', 'srlgs'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp", ("igp", Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.igp = Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._segment_path = lambda: "local-igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation, ['domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf>`
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("isis", ("isis", Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis)), ("ospf", ("ospf", Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf)), ("bgp", ("bgp", Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp))])
                            self._leafs = OrderedDict([
                                ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcIgpInfoId', '')])),
                            ])
                            self.igp_id = None

                            self.isis = Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"

                            self.ospf = Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"

                            self.bgp = Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._segment_path = lambda: "igp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp, ['igp_id'], name, value)


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

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis, self).__init__()

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
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis, ['system_id', 'level'], name, value)


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

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf, self).__init__()

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
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf, ['router_id', 'area'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                ])
                                self.router_id = None
                                self._segment_path = lambda: "bgp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp, ['router_id'], name, value)


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
                    	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp-information", ("igp_information", Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation))])
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
                        self._segment_path = lambda: "remote-node-protocol-identifier"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier, ['node_name', 'ipv4_bgp_router_id_set', 'ipv4_bgp_router_id', 'ipv4te_router_id_set', 'ipv4te_router_id'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp))])
                            self._leafs = OrderedDict([
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.domain_identifier = None

                            self.igp = Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "igp-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation, ['domain_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis)), ("ospf", ("ospf", Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf)), ("bgp", ("bgp", Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


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

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

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
                                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, ['system_id', 'level'], name, value)


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

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

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
                                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['router_id', 'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                    ])
                                    self.router_id = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['router_id'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`XtcSid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid1>`
                    
                    .. attribute:: algorithm
                    
                    	Prefix\-SID algorithm number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSid1', '')])),
                            ('algorithm', (YLeaf(YType.uint32, 'algorithm'), ['int'])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                        ])
                        self.sid_type = None
                        self.algorithm = None
                        self.mpls_label = None

                        self.sid_prefix = Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._segment_path = lambda: "adjacency-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid, ['sid_type', 'algorithm', 'mpls_label'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid-prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


            class Ipv6Link(Entity):
                """
                IPv6 Link information
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:  :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation>`
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:  :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier>`
                
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
                	**type**\: list of  		 :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.TopologyNodes.TopologyNode.Ipv6Link, self).__init__()

                    self.yang_name = "ipv6-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-igp-information", ("local_igp_information", Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation)), ("remote-node-protocol-identifier", ("remote_node_protocol_identifier", Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier)), ("adjacency-sid", ("adjacency_sid", Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid))])
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

                    self.local_igp_information = Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"

                    self.remote_node_protocol_identifier = Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv6-link"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link, ['local_ipv6_address', 'remote_ipv6_address', 'igp_metric', 'te_metric', 'maximum_link_bandwidth', 'max_reservable_bandwidth'], name, value)


                class LocalIgpInformation(Entity):
                    """
                    Local node IGP information
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, self).__init__()

                        self.yang_name = "local-igp-information"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp", ("igp", Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.igp = Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._segment_path = lambda: "local-igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation, ['domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf>`
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "local-igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("isis", ("isis", Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis)), ("ospf", ("ospf", Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf)), ("bgp", ("bgp", Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp))])
                            self._leafs = OrderedDict([
                                ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcIgpInfoId', '')])),
                            ])
                            self.igp_id = None

                            self.isis = Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"

                            self.ospf = Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"

                            self.bgp = Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._segment_path = lambda: "igp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp, ['igp_id'], name, value)


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

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis, self).__init__()

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
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis, ['system_id', 'level'], name, value)


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

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf, self).__init__()

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
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf, ['router_id', 'area'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                ])
                                self.router_id = None
                                self._segment_path = lambda: "bgp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp, ['router_id'], name, value)


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
                    	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, self).__init__()

                        self.yang_name = "remote-node-protocol-identifier"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp-information", ("igp_information", Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation))])
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
                        self._segment_path = lambda: "remote-node-protocol-identifier"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier, ['node_name', 'ipv4_bgp_router_id_set', 'ipv4_bgp_router_id', 'ipv4te_router_id_set', 'ipv4te_router_id'], name, value)


                    class IgpInformation(Entity):
                        """
                        IGP information
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, self).__init__()

                            self.yang_name = "igp-information"
                            self.yang_parent_name = "remote-node-protocol-identifier"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("igp", ("igp", Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp))])
                            self._leafs = OrderedDict([
                                ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                            ])
                            self.domain_identifier = None

                            self.igp = Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._segment_path = lambda: "igp-information"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation, ['domain_identifier'], name, value)


                        class Igp(Entity):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "igp-information"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("isis", ("isis", Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis)), ("ospf", ("ospf", Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf)), ("bgp", ("bgp", Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp))])
                                self._leafs = OrderedDict([
                                    ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcIgpInfoId', '')])),
                                ])
                                self.igp_id = None

                                self.isis = Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis()
                                self.isis.parent = self
                                self._children_name_map["isis"] = "isis"

                                self.ospf = Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                                self.ospf.parent = self
                                self._children_name_map["ospf"] = "ospf"

                                self.bgp = Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                                self._segment_path = lambda: "igp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


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

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

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
                                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis, ['system_id', 'level'], name, value)


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

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

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
                                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['router_id', 'area'], name, value)


                            class Bgp(Entity):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2017-09-11'

                                def __init__(self):
                                    super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                    self.yang_name = "bgp"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                    ])
                                    self.router_id = None
                                    self._segment_path = lambda: "bgp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['router_id'], name, value)


                class AdjacencySid(Entity):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix>`
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`XtcSid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid1>`
                    
                    .. attribute:: algorithm
                    
                    	Prefix\-SID algorithm number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, self).__init__()

                        self.yang_name = "adjacency-sid"
                        self.yang_parent_name = "ipv6-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sid-prefix", ("sid_prefix", Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix))])
                        self._leafs = OrderedDict([
                            ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSid1', '')])),
                            ('algorithm', (YLeaf(YType.uint32, 'algorithm'), ['int'])),
                            ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                        ])
                        self.sid_type = None
                        self.algorithm = None
                        self.mpls_label = None

                        self.sid_prefix = Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix()
                        self.sid_prefix.parent = self
                        self._children_name_map["sid_prefix"] = "sid-prefix"
                        self._segment_path = lambda: "adjacency-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid, ['sid_type', 'algorithm', 'mpls_label'], name, value)


                    class SidPrefix(Entity):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, self).__init__()

                            self.yang_name = "sid-prefix"
                            self.yang_parent_name = "adjacency-sid"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                                ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                                ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4 = None
                            self.ipv6 = None
                            self._segment_path = lambda: "sid-prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix, ['af_name', 'ipv4', 'ipv6'], name, value)


    class PrefixInfos(Entity):
        """
        Prefixes database in XTC Agent
        
        .. attribute:: prefix_info
        
        	Prefix information
        	**type**\: list of  		 :py:class:`PrefixInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo>`
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2017-09-11'

        def __init__(self):
            super(Xtc.PrefixInfos, self).__init__()

            self.yang_name = "prefix-infos"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prefix-info", ("prefix_info", Xtc.PrefixInfos.PrefixInfo))])
            self._leafs = OrderedDict()

            self.prefix_info = YList(self)
            self._segment_path = lambda: "prefix-infos"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.PrefixInfos, [], name, value)


        class PrefixInfo(Entity):
            """
            Prefix information
            
            .. attribute:: node_identifier  (key)
            
            	Node ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:  :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier>`
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: address
            
            	Prefix address
            	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.Address>`
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2017-09-11'

            def __init__(self):
                super(Xtc.PrefixInfos.PrefixInfo, self).__init__()

                self.yang_name = "prefix-info"
                self.yang_parent_name = "prefix-infos"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_identifier']
                self._child_classes = OrderedDict([("node-protocol-identifier", ("node_protocol_identifier", Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier)), ("address", ("address", Xtc.PrefixInfos.PrefixInfo.Address))])
                self._leafs = OrderedDict([
                    ('node_identifier', (YLeaf(YType.uint32, 'node-identifier'), ['int'])),
                    ('node_identifier_xr', (YLeaf(YType.uint32, 'node-identifier-xr'), ['int'])),
                ])
                self.node_identifier = None
                self.node_identifier_xr = None

                self.node_protocol_identifier = Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier()
                self.node_protocol_identifier.parent = self
                self._children_name_map["node_protocol_identifier"] = "node-protocol-identifier"

                self.address = YList(self)
                self._segment_path = lambda: "prefix-info" + "[node-identifier='" + str(self.node_identifier) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/prefix-infos/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.PrefixInfos.PrefixInfo, ['node_identifier', 'node_identifier_xr'], name, value)


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
                	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, self).__init__()

                    self.yang_name = "node-protocol-identifier"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("igp-information", ("igp_information", Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation))])
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
                    self._segment_path = lambda: "node-protocol-identifier"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier, ['node_name', 'ipv4_bgp_router_id_set', 'ipv4_bgp_router_id', 'ipv4te_router_id_set', 'ipv4te_router_id'], name, value)


                class IgpInformation(Entity):
                    """
                    IGP information
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, self).__init__()

                        self.yang_name = "igp-information"
                        self.yang_parent_name = "node-protocol-identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("igp", ("igp", Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp))])
                        self._leafs = OrderedDict([
                            ('domain_identifier', (YLeaf(YType.uint64, 'domain-identifier'), ['int'])),
                        ])
                        self.domain_identifier = None

                        self.igp = Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._segment_path = lambda: "igp-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation, ['domain_identifier'], name, value)


                    class Igp(Entity):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2017-09-11'

                        def __init__(self):
                            super(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "igp-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("isis", ("isis", Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis)), ("ospf", ("ospf", Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf)), ("bgp", ("bgp", Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp))])
                            self._leafs = OrderedDict([
                                ('igp_id', (YLeaf(YType.enumeration, 'igp-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcIgpInfoId', '')])),
                            ])
                            self.igp_id = None

                            self.isis = Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis()
                            self.isis.parent = self
                            self._children_name_map["isis"] = "isis"

                            self.ospf = Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf()
                            self.ospf.parent = self
                            self._children_name_map["ospf"] = "ospf"

                            self.bgp = Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp()
                            self.bgp.parent = self
                            self._children_name_map["bgp"] = "bgp"
                            self._segment_path = lambda: "igp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp, ['igp_id'], name, value)


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

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis, self).__init__()

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
                                self._perform_setattr(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis, ['system_id', 'level'], name, value)


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

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, self).__init__()

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
                                self._perform_setattr(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf, ['router_id', 'area'], name, value)


                        class Bgp(Entity):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2017-09-11'

                            def __init__(self):
                                super(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, self).__init__()

                                self.yang_name = "bgp"
                                self.yang_parent_name = "igp"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                ])
                                self.router_id = None
                                self._segment_path = lambda: "bgp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp, ['router_id'], name, value)


            class Address(Entity):
                """
                Prefix address
                
                .. attribute:: ip_address
                
                	Prefix IP address
                	**type**\:  :py:class:`IpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.Address.IpAddress>`
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2017-09-11'

                def __init__(self):
                    super(Xtc.PrefixInfos.PrefixInfo.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "prefix-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ip-address", ("ip_address", Xtc.PrefixInfos.PrefixInfo.Address.IpAddress))])
                    self._leafs = OrderedDict()

                    self.ip_address = Xtc.PrefixInfos.PrefixInfo.Address.IpAddress()
                    self.ip_address.parent = self
                    self._children_name_map["ip_address"] = "ip-address"
                    self._segment_path = lambda: "address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.PrefixInfos.PrefixInfo.Address, [], name, value)


                class IpAddress(Entity):
                    """
                    Prefix IP address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2017-09-11'

                    def __init__(self):
                        super(Xtc.PrefixInfos.PrefixInfo.Address.IpAddress, self).__init__()

                        self.yang_name = "ip-address"
                        self.yang_parent_name = "address"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAfId', '')])),
                            ('ipv4', (YLeaf(YType.str, 'ipv4'), ['str'])),
                            ('ipv6', (YLeaf(YType.str, 'ipv6'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4 = None
                        self.ipv6 = None
                        self._segment_path = lambda: "ip-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.PrefixInfos.PrefixInfo.Address.IpAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

    def clone_ptr(self):
        self._top_entity = Xtc()
        return self._top_entity

