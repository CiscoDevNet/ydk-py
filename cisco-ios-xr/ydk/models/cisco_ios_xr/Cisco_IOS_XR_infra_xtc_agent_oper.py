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
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CmnHaCase(Enum):
    """
    CmnHaCase (Enum Class)

    Various HA cases

    .. data:: ha_case_migration = 0

    	HA Case Migration

    .. data:: ha_case_restart = 1

    	HA Case Restart

    .. data:: ha_case_switchover = 2

    	HA Case Switchover

    .. data:: ha_case_startup = 3

    	HA Case Startup

    .. data:: ha_case_invalid = 4

    	HA Case Invalid

    """

    ha_case_migration = Enum.YLeaf(0, "ha-case-migration")

    ha_case_restart = Enum.YLeaf(1, "ha-case-restart")

    ha_case_switchover = Enum.YLeaf(2, "ha-case-switchover")

    ha_case_startup = Enum.YLeaf(3, "ha-case-startup")

    ha_case_invalid = Enum.YLeaf(4, "ha-case-invalid")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['CmnHaCase']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcAddressFamily']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcAfId']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcDisjointness']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcIgpInfoId']


class XtcPolicyCpathProtoOrigin(Enum):
    """
    XtcPolicyCpathProtoOrigin (Enum Class)

    Policy candidate path protocol origin

    .. data:: unknown = 0

    	unknown

    .. data:: pcep = 10

    	pcep

    .. data:: bgp = 20

    	bgp

    .. data:: configuration = 30

    	configuration

    """

    unknown = Enum.YLeaf(0, "unknown")

    pcep = Enum.YLeaf(10, "pcep")

    bgp = Enum.YLeaf(20, "bgp")

    configuration = Enum.YLeaf(30, "configuration")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcPolicyCpathProtoOrigin']


class XtcPolicyLspSmState(Enum):
    """
    XtcPolicyLspSmState (Enum Class)

    XTC policy LSP FSM states

    .. data:: unknown = 0

    	Unknown

    .. data:: initialized = 1

    	Initialized

    .. data:: deleted = 2

    	Deleted

    .. data:: programmed = 3

    	Programmed; all forwarding rewrites created

    .. data:: egress_paths_pending = 4

    	Waiting for egress paths

    .. data:: out_of_resources_pending = 5

    	Waiting for resources to become available

    .. data:: label_allocation_pending = 6

    	Waiting for label allocation result

    .. data:: label_allocation_cleanup_pending = 7

    	Waiting for label free result

    .. data:: label_rewrite_pending = 8

    	Waiting for label rewrite create result

    .. data:: label_rewrite_cleanup_pending = 9

    	Waiting for label rewrite delete result

    .. data:: bsid_allocation_pending = 10

    	Waiting for BSID label allocation result

    .. data:: bsid_allocation_cleanup_pending = 11

    	Waiting for BSID label free result

    .. data:: bsid_rewrite_pending = 12

    	Waiting for BSID rewrite create result

    .. data:: bsid_rewrite_cleanup_pending = 13

    	Waiting for BSID rewrite delete result

    .. data:: tunnel_rewrite_pending = 14

    	Waiting for tunnel rewrite create result

    .. data:: tunnel_rewrite_cleanup_pending = 15

    	Waiting for tunnel rewrite delete result

    .. data:: install_timer_pending = 16

    	Waiting for install timer to expire

    .. data:: cleanup_timer_pending = 17

    	Waiting for cleanup timer to expire

    """

    unknown = Enum.YLeaf(0, "unknown")

    initialized = Enum.YLeaf(1, "initialized")

    deleted = Enum.YLeaf(2, "deleted")

    programmed = Enum.YLeaf(3, "programmed")

    egress_paths_pending = Enum.YLeaf(4, "egress-paths-pending")

    out_of_resources_pending = Enum.YLeaf(5, "out-of-resources-pending")

    label_allocation_pending = Enum.YLeaf(6, "label-allocation-pending")

    label_allocation_cleanup_pending = Enum.YLeaf(7, "label-allocation-cleanup-pending")

    label_rewrite_pending = Enum.YLeaf(8, "label-rewrite-pending")

    label_rewrite_cleanup_pending = Enum.YLeaf(9, "label-rewrite-cleanup-pending")

    bsid_allocation_pending = Enum.YLeaf(10, "bsid-allocation-pending")

    bsid_allocation_cleanup_pending = Enum.YLeaf(11, "bsid-allocation-cleanup-pending")

    bsid_rewrite_pending = Enum.YLeaf(12, "bsid-rewrite-pending")

    bsid_rewrite_cleanup_pending = Enum.YLeaf(13, "bsid-rewrite-cleanup-pending")

    tunnel_rewrite_pending = Enum.YLeaf(14, "tunnel-rewrite-pending")

    tunnel_rewrite_cleanup_pending = Enum.YLeaf(15, "tunnel-rewrite-cleanup-pending")

    install_timer_pending = Enum.YLeaf(16, "install-timer-pending")

    cleanup_timer_pending = Enum.YLeaf(17, "cleanup-timer-pending")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcPolicyLspSmState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcPolicyPath']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcSid']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcSid1']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcSrSid']


class XtcigpProtocol(Enum):
    """
    XtcigpProtocol (Enum Class)

    Xtcigp protocol

    .. data:: unknown = 0

    	Unknown protocol

    .. data:: isis = 1

    	ISIS protocol

    .. data:: ospf = 2

    	OSPF protocol

    .. data:: bgp = 4

    	BGP protocol

    .. data:: te = 8

    	TE protocol

    """

    unknown = Enum.YLeaf(0, "unknown")

    isis = Enum.YLeaf(1, "isis")

    ospf = Enum.YLeaf(2, "ospf")

    bgp = Enum.YLeaf(4, "bgp")

    te = Enum.YLeaf(8, "te")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['XtcigpProtocol']



class Pcc(_Entity_):
    """
    Path\-computation client in XTC
    
    .. attribute:: plsps
    
    	PCC PLSP database in XTC
    	**type**\:  :py:class:`Plsps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps>`
    
    	**config**\: False
    
    .. attribute:: peers
    
    	PCC peer database in XTC
    	**type**\:  :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Peers>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-xtc-agent-oper'
    _revision = '2019-09-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class Plsps(_Entity_):
        """
        PCC PLSP database in XTC
        
        .. attribute:: plsp
        
        	PCC PLSP information
        	**type**\: list of  		 :py:class:`Plsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Plsp(_Entity_):
            """
            PCC PLSP information
            
            .. attribute:: plsp_id  (key)
            
            	PLSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: stats
            
            	Stats
            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Stats>`
            
            	**config**\: False
            
            .. attribute:: plsp_id_xr
            
            	PLSP ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: sym_path_name
            
            	Symbolic Path Name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: refcnt
            
            	Refcnt
            	**type**\: int
            
            	**range:** \-9223372036854775808..9223372036854775807
            
            	**config**\: False
            
            .. attribute:: conn_delegated_to
            
            	CONN delegated to
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: event_history
            
            	event history
            	**type**\: list of  		 :py:class:`EventHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.EventHistory>`
            
            	**config**\: False
            
            .. attribute:: path
            
            	path
            	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class Stats(_Entity_):
                """
                Stats
                
                .. attribute:: paths_created
                
                	Paths Created
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: paths_destroyed
                
                	Paths Destroyed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: path_create_errors
                
                	Path create errors
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: path_destroy_errors
                
                	Path destroy errors
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: requests_created
                
                	Requests created
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: requests_destroyed
                
                	Requests destroyed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: requests_failed
                
                	Requests failed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Pcc.Plsps.Plsp.Stats']['meta_info']


            class EventHistory(_Entity_):
                """
                event history
                
                .. attribute:: ts
                
                	Timestamp
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: desc
                
                	Description
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Pcc.Plsps.Plsp.EventHistory']['meta_info']


            class Path(_Entity_):
                """
                path
                
                .. attribute:: stats
                
                	stats
                	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.Stats>`
                
                	**config**\: False
                
                .. attribute:: used_bw
                
                	used bw
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                	**config**\: False
                
                .. attribute:: requested_bw
                
                	requested bw
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                	**config**\: False
                
                .. attribute:: metric_value
                
                	metric value
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                	**config**\: False
                
                .. attribute:: refcnt
                
                	refcnt
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                	**config**\: False
                
                .. attribute:: lsp_plsp_id
                
                	LSP PLSP ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: binding_sid_value
                
                	Binding SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: lsp_id_tlv_ext_tunnel_id
                
                	Ext Tun ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: lsp_id_tlv_tunnel_endpoint_address
                
                	Tun endpoint address
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: lsp_id_tlv_tunnel_sender_address
                
                	Tun sender address
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: srp_id
                
                	SRP ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: lsp_id_tlv_lsp_id
                
                	LSP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: lsp_id_tlv_tunnel_id
                
                	Tunnel ID
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: lsp_id
                
                	Application LSP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: binding_sid_type
                
                	Binding SID type
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: lsp_oper
                
                	LSP oper flags
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: path_setup_type
                
                	Path setup type
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: metric_type
                
                	Metric type
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: is_reported
                
                	is reported
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: lsp_a_flag
                
                	LSP A Flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: lsp_r_flag
                
                	LSP R Flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: lsp_s_flag
                
                	LSP S Flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: lsp_d_flag
                
                	LSP D Flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: lsp_c_flag
                
                	LSP C Flag
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ero_hop
                
                	ero hop
                	**type**\: list of  		 :py:class:`EroHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.EroHop>`
                
                	**config**\: False
                
                .. attribute:: rro_hop
                
                	rro hop
                	**type**\: list of  		 :py:class:`RroHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.RroHop>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class Stats(_Entity_):
                    """
                    stats
                    
                    .. attribute:: reports_requested
                    
                    	Reports requested
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: reports_sent
                    
                    	Reports sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: reports_failed_to_send
                    
                    	Reports failed
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Pcc.Plsps.Plsp.Path.Stats']['meta_info']


                class EroHop(_Entity_):
                    """
                    ero hop
                    
                    .. attribute:: data
                    
                    	data
                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.EroHop.Data>`
                    
                    	**config**\: False
                    
                    .. attribute:: loose
                    
                    	is loose hop
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Data(_Entity_):
                        """
                        data
                        
                        .. attribute:: ipv4
                        
                        	IPv4 hop info
                        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.EroHop.Data.Ipv4>`
                        
                        	**config**\: False
                        
                        .. attribute:: sr_v4
                        
                        	SR IPv4 hop info
                        	**type**\:  :py:class:`SrV4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.EroHop.Data.SrV4>`
                        
                        	**config**\: False
                        
                        .. attribute:: hop_type
                        
                        	HopType
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Ipv4(_Entity_):
                            """
                            IPv4 hop info
                            
                            .. attribute:: v4_addr
                            
                            	IPv4 prefix
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: prefix_len
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Pcc.Plsps.Plsp.Path.EroHop.Data.Ipv4']['meta_info']


                        class SrV4(_Entity_):
                            """
                            SR IPv4 hop info
                            
                            .. attribute:: type
                            
                            	SID type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: cflag
                            
                            	C flag
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: sid
                            
                            	SID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: remote_addr
                            
                            	Remote address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: local_addr
                            
                            	Local address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Pcc.Plsps.Plsp.Path.EroHop.Data.SrV4']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Pcc.Plsps.Plsp.Path.EroHop.Data']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Pcc.Plsps.Plsp.Path.EroHop']['meta_info']


                class RroHop(_Entity_):
                    """
                    rro hop
                    
                    .. attribute:: data
                    
                    	data
                    	**type**\:  :py:class:`Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.RroHop.Data>`
                    
                    	**config**\: False
                    
                    .. attribute:: loose
                    
                    	is loose hop
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Data(_Entity_):
                        """
                        data
                        
                        .. attribute:: ipv4
                        
                        	IPv4 hop info
                        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.RroHop.Data.Ipv4>`
                        
                        	**config**\: False
                        
                        .. attribute:: sr_v4
                        
                        	SR IPv4 hop info
                        	**type**\:  :py:class:`SrV4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Plsps.Plsp.Path.RroHop.Data.SrV4>`
                        
                        	**config**\: False
                        
                        .. attribute:: hop_type
                        
                        	HopType
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Ipv4(_Entity_):
                            """
                            IPv4 hop info
                            
                            .. attribute:: v4_addr
                            
                            	IPv4 prefix
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: prefix_len
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Pcc.Plsps.Plsp.Path.RroHop.Data.Ipv4']['meta_info']


                        class SrV4(_Entity_):
                            """
                            SR IPv4 hop info
                            
                            .. attribute:: type
                            
                            	SID type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: cflag
                            
                            	C flag
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: sid
                            
                            	SID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: remote_addr
                            
                            	Remote address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: local_addr
                            
                            	Local address
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Pcc.Plsps.Plsp.Path.RroHop.Data.SrV4']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Pcc.Plsps.Plsp.Path.RroHop.Data']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Pcc.Plsps.Plsp.Path.RroHop']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Pcc.Plsps.Plsp.Path']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Pcc.Plsps.Plsp']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Pcc.Plsps']['meta_info']


    class Peers(_Entity_):
        """
        PCC peer database in XTC
        
        .. attribute:: peer
        
        	PCC peer information
        	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Peers.Peer>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Peer(_Entity_):
            """
            PCC peer information
            
            .. attribute:: peer_addr  (key)
            
            	Peer Address
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: socket_info
            
            	socket info
            	**type**\:  :py:class:`SocketInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Peers.Peer.SocketInfo>`
            
            	**config**\: False
            
            .. attribute:: stats
            
            	stats
            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Pcc.Peers.Peer.Stats>`
            
            	**config**\: False
            
            .. attribute:: handle
            
            	internal handle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: state_str
            
            	connection state
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: local_ok
            
            	local accepted
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: remote_ok
            
            	remote accepted
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: open_retry
            
            	open retry count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ref_cnt
            
            	ref count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rx_state_str
            
            	socket state
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: holddown_counter
            
            	holddown counter
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: pcep_up_ts
            
            	PCEP up timestamp
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: precedence
            
            	Precedence
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: ka_interval_local
            
            	KA interval local
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ka_interval_remote
            
            	KA interval remote
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dead_interval_local
            
            	Dead interval local
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: dead_interval_remote
            
            	Dead interval remote
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: pcep_session_id_local
            
            	PCEP session ID local
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: pcep_session_id_remote
            
            	PCEP session ID remote
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: pcep_server_ipv4_addr
            
            	PCEP server Ipv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: pcep_client_ipv4_addr
            
            	PCEP client Ipv4 address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            .. attribute:: is_stateful_local
            
            	is stateful local
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_stateful_remote
            
            	is stateful remote
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_stateful_u_flag_local
            
            	is stateful with U flag local
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_stateful_u_flag_remote
            
            	is stateful with U flag remote
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_segment_routing_local
            
            	is segment routing local
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_segment_routing_remote
            
            	is segment routing remote
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_initiate_local
            
            	local initiate capability
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_initiate_remote
            
            	remote initiate capability
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: is_best_pce
            
            	is this the best PCE to delegate to
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: sr_msd_local
            
            	SR MSD local
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: sr_msd_remote
            
            	SR MSD remote
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class SocketInfo(_Entity_):
                """
                socket info
                
                .. attribute:: fd
                
                	file descriptor
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                	**config**\: False
                
                .. attribute:: wnotify
                
                	write notify
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: rnotify
                
                	read notify
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: refcnt
                
                	ref count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: selected
                
                	selected
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: owner
                
                	owner
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: csockaddr_str
                
                	client address
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ssockaddr_str
                
                	server address
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Pcc.Peers.Peer.SocketInfo']['meta_info']


            class Stats(_Entity_):
                """
                stats
                
                .. attribute:: ka_msg_rx
                
                	KA messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: ka_msg_fail_rx
                
                	KA messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: ka_msg_tx
                
                	KA messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: ka_msg_fail_tx
                
                	KA messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcreq_msg_rx
                
                	PCREQ messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcreq_msg_fail_rx
                
                	PCREQ messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcreq_msg_tx
                
                	PCREQ messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcreq_msg_fail_tx
                
                	PCREQ messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcrep_msg_rx
                
                	PCREP messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcrep_msg_fail_rx
                
                	PCREP messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcrep_msg_tx
                
                	PCREP messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcrep_msg_fail_tx
                
                	PCREP messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcrpt_msg_rx
                
                	PCRPT messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcrpt_msg_fail_rx
                
                	PCRPT messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcrpt_msg_tx
                
                	PCRPT messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcrpt_msg_fail_tx
                
                	PCRPT messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcupd_msg_rx
                
                	PCUPD messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcupd_msg_fail_rx
                
                	PCUPD messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcupd_msg_tx
                
                	PCUPD messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcupd_msg_fail_tx
                
                	PCUPD messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: open_msg_rx
                
                	OPEN messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: open_msg_fail_rx
                
                	OPEN messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: open_msg_tx
                
                	OPEN messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: open_msg_fail_tx
                
                	OPEN messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcerr_msg_rx
                
                	PCERR messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcerr_msg_fail_rx
                
                	PCERR messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcerr_msg_tx
                
                	PCERR messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcerr_msg_fail_tx
                
                	PCERR messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcntf_msg_rx
                
                	PCNTF messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcntf_msg_fail_rx
                
                	PCNTF messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcntf_msg_tx
                
                	PCNTF messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcntf_msg_fail_tx
                
                	PCNTF messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pce_eos_msg_tx
                
                	PCE EOS messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pce_eos_msg_fail_tx
                
                	PCE EOS messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: close_msg_rx
                
                	CLOSE messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: close_msg_fail_rx
                
                	CLOSE messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: close_msg_tx
                
                	CLOSE messages txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: close_msg_fail_tx
                
                	CLOSE messages fail txed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: unexpected_msg_rx
                
                	Unexpected messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: corrupted_msg_rx
                
                	Corrupted messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: reply_time_index
                
                	index into recorded reply time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: minimum_reply_time
                
                	min reply time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: maximum_reply_time
                
                	max reply time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: requests_timed_out
                
                	requests timed out
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: last_pcerr_type_rx
                
                	last PCERR type received
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: last_pcerr_val_rx
                
                	last PCERR value received
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: last_pcerr_rx_ts
                
                	last time when PCERR was received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: last_pcerr_type_tx
                
                	last PCERR type transmitted
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: last_pcerr_val_tx
                
                	last PCERR value transmitted
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: last_pcerr_tx_ts
                
                	last time when PCERR was transmitted
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcinitiate_msg_rx
                
                	PCINITIATE messages rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: pcinitiate_msg_fail_rx
                
                	PCINITIATE messages fail rxed
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: recorded_reply_time
                
                	Recorded reply time
                	**type**\: list of int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Pcc.Peers.Peer.Stats']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Pcc.Peers.Peer']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Pcc.Peers']['meta_info']

    def clone_ptr(self):
        self._top_entity = Pcc()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['Pcc']['meta_info']


class Xtc(_Entity_):
    """
    xtc
    
    .. attribute:: policies
    
    	Policy database in XTC Agent
    	**type**\:  :py:class:`Policies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies>`
    
    	**config**\: False
    
    .. attribute:: interfaces
    
    	Interface database in XTC Agent
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Interfaces>`
    
    	**config**\: False
    
    .. attribute:: policy_forwardings
    
    	Forwarding information for policies
    	**type**\:  :py:class:`PolicyForwardings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings>`
    
    	**config**\: False
    
    .. attribute:: policy_summary
    
    	Summary of all policies
    	**type**\:  :py:class:`PolicySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicySummary>`
    
    	**config**\: False
    
    .. attribute:: on_demand_colors
    
    	On\-Demand Color database in XTC Agent
    	**type**\:  :py:class:`OnDemandColors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.OnDemandColors>`
    
    	**config**\: False
    
    .. attribute:: controller
    
    	Controller information
    	**type**\:  :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller>`
    
    	**config**\: False
    
    .. attribute:: topology_nodes
    
    	Node database in XTC Agent
    	**type**\:  :py:class:`TopologyNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes>`
    
    	**config**\: False
    
    .. attribute:: topology_summaries
    
    	Node summary table
    	**type**\:  :py:class:`TopologySummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologySummaries>`
    
    	**config**\: False
    
    .. attribute:: prefix_infos
    
    	Prefixes database in XTC Agent
    	**type**\:  :py:class:`PrefixInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos>`
    
    	**config**\: False
    
    .. attribute:: interface_summary
    
    	Summary of all interfaces
    	**type**\:  :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.InterfaceSummary>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-xtc-agent-oper'
    _revision = '2019-09-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Xtc, self).__init__()
        self._top_entity = None

        self.yang_name = "xtc"
        self.yang_parent_name = "Cisco-IOS-XR-infra-xtc-agent-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("policies", ("policies", Xtc.Policies)), ("interfaces", ("interfaces", Xtc.Interfaces)), ("policy-forwardings", ("policy_forwardings", Xtc.PolicyForwardings)), ("policy-summary", ("policy_summary", Xtc.PolicySummary)), ("on-demand-colors", ("on_demand_colors", Xtc.OnDemandColors)), ("controller", ("controller", Xtc.Controller)), ("topology-nodes", ("topology_nodes", Xtc.TopologyNodes)), ("topology-summaries", ("topology_summaries", Xtc.TopologySummaries)), ("prefix-infos", ("prefix_infos", Xtc.PrefixInfos)), ("interface-summary", ("interface_summary", Xtc.InterfaceSummary))])
        self._leafs = OrderedDict()

        self.policies = Xtc.Policies()
        self.policies.parent = self
        self._children_name_map["policies"] = "policies"

        self.interfaces = Xtc.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.policy_forwardings = Xtc.PolicyForwardings()
        self.policy_forwardings.parent = self
        self._children_name_map["policy_forwardings"] = "policy-forwardings"

        self.policy_summary = Xtc.PolicySummary()
        self.policy_summary.parent = self
        self._children_name_map["policy_summary"] = "policy-summary"

        self.on_demand_colors = Xtc.OnDemandColors()
        self.on_demand_colors.parent = self
        self._children_name_map["on_demand_colors"] = "on-demand-colors"

        self.controller = Xtc.Controller()
        self.controller.parent = self
        self._children_name_map["controller"] = "controller"

        self.topology_nodes = Xtc.TopologyNodes()
        self.topology_nodes.parent = self
        self._children_name_map["topology_nodes"] = "topology-nodes"

        self.topology_summaries = Xtc.TopologySummaries()
        self.topology_summaries.parent = self
        self._children_name_map["topology_summaries"] = "topology-summaries"

        self.prefix_infos = Xtc.PrefixInfos()
        self.prefix_infos.parent = self
        self._children_name_map["prefix_infos"] = "prefix-infos"

        self.interface_summary = Xtc.InterfaceSummary()
        self.interface_summary.parent = self
        self._children_name_map["interface_summary"] = "interface-summary"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Xtc, [], name, value)


    class Policies(_Entity_):
        """
        Policy database in XTC Agent
        
        .. attribute:: policy
        
        	Policy information
        	**type**\: list of  		 :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class Policy(_Entity_):
            """
            Policy information
            
            .. attribute:: id  (key)
            
            	Policy ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: destination_address
            
            	Destination address
            	**type**\:  :py:class:`DestinationAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.DestinationAddress>`
            
            	**config**\: False
            
            .. attribute:: binding_sid
            
            	Binding SID information
            	**type**\:  :py:class:`BindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.BindingSid>`
            
            	**config**\: False
            
            .. attribute:: policy_name
            
            	Policy name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: administrative_up
            
            	Admin up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: operational_up
            
            	Operational up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: color
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: transition_count
            
            	Indicates number of up/down transitions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: forward_class
            
            	Forward class of the policy
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: up_time
            
            	Policy up time in nano seconds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: nanosecond
            
            .. attribute:: up_age
            
            	Policy up age (since) in nano seconds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: nanosecond
            
            .. attribute:: down_time
            
            	Policy down time in nano seconds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: nanosecond
            
            .. attribute:: down_age
            
            	Policy down age (since) in nano seconds
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: nanosecond
            
            .. attribute:: steering_bgp_disabled
            
            	Whether steering to BGP client is disabled
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: profile_id
            
            	deprecated \- replaced by key list in xtc\_pcc\_info\_bag
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: ipv6_caps_enabled
            
            	IPv6 caps enabled
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: candidate_path
            
            	Candidate paths
            	**type**\: list of  		 :py:class:`CandidatePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath>`
            
            	**config**\: False
            
            .. attribute:: ls_ps
            
            	LSPs
            	**type**\: list of  		 :py:class:`LsPs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.LsPs>`
            
            	**config**\: False
            
            .. attribute:: event_buffer
            
            	Policy Event buffer
            	**type**\: list of  		 :py:class:`EventBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.EventBuffer>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Xtc.Policies.Policy, self).__init__()

                self.yang_name = "policy"
                self.yang_parent_name = "policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_classes = OrderedDict([("destination-address", ("destination_address", Xtc.Policies.Policy.DestinationAddress)), ("binding-sid", ("binding_sid", Xtc.Policies.Policy.BindingSid)), ("candidate-path", ("candidate_path", Xtc.Policies.Policy.CandidatePath)), ("ls-ps", ("ls_ps", Xtc.Policies.Policy.LsPs)), ("event-buffer", ("event_buffer", Xtc.Policies.Policy.EventBuffer))])
                self._leafs = OrderedDict([
                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                    ('administrative_up', (YLeaf(YType.uint32, 'administrative-up'), ['int'])),
                    ('operational_up', (YLeaf(YType.uint32, 'operational-up'), ['int'])),
                    ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                    ('transition_count', (YLeaf(YType.uint32, 'transition-count'), ['int'])),
                    ('forward_class', (YLeaf(YType.uint32, 'forward-class'), ['int'])),
                    ('up_time', (YLeaf(YType.uint64, 'up-time'), ['int'])),
                    ('up_age', (YLeaf(YType.uint64, 'up-age'), ['int'])),
                    ('down_time', (YLeaf(YType.uint64, 'down-time'), ['int'])),
                    ('down_age', (YLeaf(YType.uint64, 'down-age'), ['int'])),
                    ('steering_bgp_disabled', (YLeaf(YType.boolean, 'steering-bgp-disabled'), ['bool'])),
                    ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                    ('profile_id', (YLeaf(YType.uint16, 'profile-id'), ['int'])),
                    ('ipv6_caps_enabled', (YLeaf(YType.boolean, 'ipv6-caps-enabled'), ['bool'])),
                ])
                self.id = None
                self.policy_name = None
                self.administrative_up = None
                self.operational_up = None
                self.color = None
                self.transition_count = None
                self.forward_class = None
                self.up_time = None
                self.up_age = None
                self.down_time = None
                self.down_age = None
                self.steering_bgp_disabled = None
                self.interface_handle = None
                self.profile_id = None
                self.ipv6_caps_enabled = None

                self.destination_address = Xtc.Policies.Policy.DestinationAddress()
                self.destination_address.parent = self
                self._children_name_map["destination_address"] = "destination-address"

                self.binding_sid = Xtc.Policies.Policy.BindingSid()
                self.binding_sid.parent = self
                self._children_name_map["binding_sid"] = "binding-sid"

                self.candidate_path = YList(self)
                self.ls_ps = YList(self)
                self.event_buffer = YList(self)
                self._segment_path = lambda: "policy" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policies/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.Policies.Policy, ['id', 'policy_name', 'administrative_up', 'operational_up', 'color', 'transition_count', 'forward_class', 'up_time', 'up_age', 'down_time', 'down_age', 'steering_bgp_disabled', 'interface_handle', 'profile_id', 'ipv6_caps_enabled'], name, value)


            class DestinationAddress(_Entity_):
                """
                Destination address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                
                	**config**\: False
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.Policies.Policy.DestinationAddress']['meta_info']


            class BindingSid(_Entity_):
                """
                Binding SID information
                
                .. attribute:: value
                
                	Binding SID value
                	**type**\:  :py:class:`Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.BindingSid.Value>`
                
                	**config**\: False
                
                .. attribute:: is_fallback_dynamic
                
                	Whether the BSID is in fallback dynamic mode
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_within_srlb_range
                
                	Whether the BSID is within SRLB range
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.Policies.Policy.BindingSid, self).__init__()

                    self.yang_name = "binding-sid"
                    self.yang_parent_name = "policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("value", ("value", Xtc.Policies.Policy.BindingSid.Value))])
                    self._leafs = OrderedDict([
                        ('is_fallback_dynamic', (YLeaf(YType.boolean, 'is-fallback-dynamic'), ['bool'])),
                        ('is_within_srlb_range', (YLeaf(YType.boolean, 'is-within-srlb-range'), ['bool'])),
                    ])
                    self.is_fallback_dynamic = None
                    self.is_within_srlb_range = None

                    self.value = Xtc.Policies.Policy.BindingSid.Value()
                    self.value.parent = self
                    self._children_name_map["value"] = "value"
                    self._segment_path = lambda: "binding-sid"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Policies.Policy.BindingSid, ['is_fallback_dynamic', 'is_within_srlb_range'], name, value)


                class Value(_Entity_):
                    """
                    Binding SID value
                    
                    .. attribute:: sid_type
                    
                    	SIDType
                    	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                    
                    	**config**\: False
                    
                    .. attribute:: label
                    
                    	MPLS label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.BindingSid.Value']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.Policies.Policy.BindingSid']['meta_info']


            class CandidatePath(_Entity_):
                """
                Candidate paths
                
                .. attribute:: originator
                
                	Candidate path originator
                	**type**\:  :py:class:`Originator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.Originator>`
                
                	**config**\: False
                
                .. attribute:: sr_path_constraints
                
                	SR candidate path constraints
                	**type**\:  :py:class:`SrPathConstraints <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SrPathConstraints>`
                
                	**config**\: False
                
                .. attribute:: requested_bsid
                
                	Requested binding SID
                	**type**\:  :py:class:`RequestedBsid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.RequestedBsid>`
                
                	**config**\: False
                
                .. attribute:: cleanup_timer
                
                	Cleanup timer if the candidate path is in the process of being cleaned up
                	**type**\:  :py:class:`CleanupTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.CleanupTimer>`
                
                	**config**\: False
                
                .. attribute:: pcc_information
                
                	PCC PCEP\-related information
                	**type**\:  :py:class:`PccInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.PccInformation>`
                
                	**config**\: False
                
                .. attribute:: name
                
                	Candidate path name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: preference
                
                	Candidate path preference
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: protocol_originator
                
                	Candidate path protocol origin
                	**type**\:  :py:class:`XtcPolicyCpathProtoOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcPolicyCpathProtoOrigin>`
                
                	**config**\: False
                
                .. attribute:: discriminator
                
                	Candidate path discriminator
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: is_active
                
                	Whether this is the currently active candidate path
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_reoptimizing
                
                	Whether this is the candidate path that the policy is reoptimizing to
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: shutdown
                
                	If set, the candidate path is administratively shutdown
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: error
                
                	Candidate path error (for display only)
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: segment_list
                
                	Segment lists of the candidate path
                	**type**\: list of  		 :py:class:`SegmentList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SegmentList>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.Policies.Policy.CandidatePath, self).__init__()

                    self.yang_name = "candidate-path"
                    self.yang_parent_name = "policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("originator", ("originator", Xtc.Policies.Policy.CandidatePath.Originator)), ("sr-path-constraints", ("sr_path_constraints", Xtc.Policies.Policy.CandidatePath.SrPathConstraints)), ("requested-bsid", ("requested_bsid", Xtc.Policies.Policy.CandidatePath.RequestedBsid)), ("cleanup-timer", ("cleanup_timer", Xtc.Policies.Policy.CandidatePath.CleanupTimer)), ("pcc-information", ("pcc_information", Xtc.Policies.Policy.CandidatePath.PccInformation)), ("segment-list", ("segment_list", Xtc.Policies.Policy.CandidatePath.SegmentList))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('preference', (YLeaf(YType.uint32, 'preference'), ['int'])),
                        ('protocol_originator', (YLeaf(YType.enumeration, 'protocol-originator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcPolicyCpathProtoOrigin', '')])),
                        ('discriminator', (YLeaf(YType.uint32, 'discriminator'), ['int'])),
                        ('is_active', (YLeaf(YType.boolean, 'is-active'), ['bool'])),
                        ('is_reoptimizing', (YLeaf(YType.boolean, 'is-reoptimizing'), ['bool'])),
                        ('shutdown', (YLeaf(YType.boolean, 'shutdown'), ['bool'])),
                        ('error', (YLeaf(YType.str, 'error'), ['str'])),
                    ])
                    self.name = None
                    self.preference = None
                    self.protocol_originator = None
                    self.discriminator = None
                    self.is_active = None
                    self.is_reoptimizing = None
                    self.shutdown = None
                    self.error = None

                    self.originator = Xtc.Policies.Policy.CandidatePath.Originator()
                    self.originator.parent = self
                    self._children_name_map["originator"] = "originator"

                    self.sr_path_constraints = Xtc.Policies.Policy.CandidatePath.SrPathConstraints()
                    self.sr_path_constraints.parent = self
                    self._children_name_map["sr_path_constraints"] = "sr-path-constraints"

                    self.requested_bsid = Xtc.Policies.Policy.CandidatePath.RequestedBsid()
                    self.requested_bsid.parent = self
                    self._children_name_map["requested_bsid"] = "requested-bsid"

                    self.cleanup_timer = Xtc.Policies.Policy.CandidatePath.CleanupTimer()
                    self.cleanup_timer.parent = self
                    self._children_name_map["cleanup_timer"] = "cleanup-timer"

                    self.pcc_information = Xtc.Policies.Policy.CandidatePath.PccInformation()
                    self.pcc_information.parent = self
                    self._children_name_map["pcc_information"] = "pcc-information"

                    self.segment_list = YList(self)
                    self._segment_path = lambda: "candidate-path"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Policies.Policy.CandidatePath, ['name', 'preference', 'protocol_originator', 'discriminator', 'is_active', 'is_reoptimizing', 'shutdown', 'error'], name, value)


                class Originator(_Entity_):
                    """
                    Candidate path originator
                    
                    .. attribute:: node_address
                    
                    	Originator node address
                    	**type**\:  :py:class:`NodeAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.Originator.NodeAddress>`
                    
                    	**config**\: False
                    
                    .. attribute:: autonomous_system_number
                    
                    	Originator Autonomous System Number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.CandidatePath.Originator, self).__init__()

                        self.yang_name = "originator"
                        self.yang_parent_name = "candidate-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-address", ("node_address", Xtc.Policies.Policy.CandidatePath.Originator.NodeAddress))])
                        self._leafs = OrderedDict([
                            ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                        ])
                        self.autonomous_system_number = None

                        self.node_address = Xtc.Policies.Policy.CandidatePath.Originator.NodeAddress()
                        self.node_address.parent = self
                        self._children_name_map["node_address"] = "node-address"
                        self._segment_path = lambda: "originator"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.CandidatePath.Originator, ['autonomous_system_number'], name, value)


                    class NodeAddress(_Entity_):
                        """
                        Originator node address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.CandidatePath.Originator.NodeAddress, self).__init__()

                            self.yang_name = "node-address"
                            self.yang_parent_name = "originator"
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
                            self._segment_path = lambda: "node-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.CandidatePath.Originator.NodeAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.CandidatePath.Originator.NodeAddress']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.CandidatePath.Originator']['meta_info']


                class SrPathConstraints(_Entity_):
                    """
                    SR candidate path constraints
                    
                    .. attribute:: path_metrics
                    
                    	Path metrics
                    	**type**\:  :py:class:`PathMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SrPathConstraints.PathMetrics>`
                    
                    	**config**\: False
                    
                    .. attribute:: segments
                    
                    	Segments constraints
                    	**type**\:  :py:class:`Segments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SrPathConstraints.Segments>`
                    
                    	**config**\: False
                    
                    .. attribute:: affinity_constraint
                    
                    	Affinity constraints list
                    	**type**\: list of  		 :py:class:`AffinityConstraint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.CandidatePath.SrPathConstraints, self).__init__()

                        self.yang_name = "sr-path-constraints"
                        self.yang_parent_name = "candidate-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("path-metrics", ("path_metrics", Xtc.Policies.Policy.CandidatePath.SrPathConstraints.PathMetrics)), ("segments", ("segments", Xtc.Policies.Policy.CandidatePath.SrPathConstraints.Segments)), ("affinity-constraint", ("affinity_constraint", Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint))])
                        self._leafs = OrderedDict()

                        self.path_metrics = Xtc.Policies.Policy.CandidatePath.SrPathConstraints.PathMetrics()
                        self.path_metrics.parent = self
                        self._children_name_map["path_metrics"] = "path-metrics"

                        self.segments = Xtc.Policies.Policy.CandidatePath.SrPathConstraints.Segments()
                        self.segments.parent = self
                        self._children_name_map["segments"] = "segments"

                        self.affinity_constraint = YList(self)
                        self._segment_path = lambda: "sr-path-constraints"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SrPathConstraints, [], name, value)


                    class PathMetrics(_Entity_):
                        """
                        Path metrics
                        
                        .. attribute:: margin_relative
                        
                        	Margin Relative
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: margin_absolute
                        
                        	Margin Absolute
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: maximum_segments
                        
                        	Maximum number of segments
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: accumulative_te_metric
                        
                        	Accumulative TE metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: accumulative_igp_metric
                        
                        	Accumulative IGP metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: accumulative_delay
                        
                        	Accumulative delay
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.CandidatePath.SrPathConstraints.PathMetrics, self).__init__()

                            self.yang_name = "path-metrics"
                            self.yang_parent_name = "sr-path-constraints"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('margin_relative', (YLeaf(YType.uint32, 'margin-relative'), ['int'])),
                                ('margin_absolute', (YLeaf(YType.uint32, 'margin-absolute'), ['int'])),
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
                            self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SrPathConstraints.PathMetrics, ['margin_relative', 'margin_absolute', 'maximum_segments', 'accumulative_te_metric', 'accumulative_igp_metric', 'accumulative_delay'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SrPathConstraints.PathMetrics']['meta_info']


                    class Segments(_Entity_):
                        """
                        Segments constraints
                        
                        .. attribute:: segment_algorithm
                        
                        	Segment Algorithm
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.CandidatePath.SrPathConstraints.Segments, self).__init__()

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
                            self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SrPathConstraints.Segments, ['segment_algorithm'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SrPathConstraints.Segments']['meta_info']


                    class AffinityConstraint(_Entity_):
                        """
                        Affinity constraints list
                        
                        .. attribute:: type
                        
                        	Affinity type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: value
                        
                        	Affinity value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: extended_value
                        
                        	Extended Affinity values
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: color
                        
                        	Colors
                        	**type**\: list of  		 :py:class:`Color <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint.Color>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint, self).__init__()

                            self.yang_name = "affinity-constraint"
                            self.yang_parent_name = "sr-path-constraints"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("color", ("color", Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint.Color))])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('extended_value', (YLeafList(YType.uint32, 'extended-value'), ['int'])),
                            ])
                            self.type = None
                            self.value = None
                            self.extended_value = []

                            self.color = YList(self)
                            self._segment_path = lambda: "affinity-constraint"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint, ['type', 'value', 'extended_value'], name, value)


                        class Color(_Entity_):
                            """
                            Colors
                            
                            .. attribute:: color
                            
                            	An affinity color
                            	**type**\: str
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint.Color, self).__init__()

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
                                self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint.Color, ['color'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint.Color']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SrPathConstraints.AffinityConstraint']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SrPathConstraints']['meta_info']


                class RequestedBsid(_Entity_):
                    """
                    Requested binding SID
                    
                    .. attribute:: sid_type
                    
                    	SIDType
                    	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                    
                    	**config**\: False
                    
                    .. attribute:: label
                    
                    	MPLS label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.CandidatePath.RequestedBsid, self).__init__()

                        self.yang_name = "requested-bsid"
                        self.yang_parent_name = "candidate-path"
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
                        self._segment_path = lambda: "requested-bsid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.CandidatePath.RequestedBsid, ['sid_type', 'label', 'ipv6'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.CandidatePath.RequestedBsid']['meta_info']


                class CleanupTimer(_Entity_):
                    """
                    Cleanup timer if the candidate path is in the
                    process of being cleaned up
                    
                    .. attribute:: running
                    
                    	Whether the timer is running
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: remaining_seconds
                    
                    	Number of remaining seconds
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: remaining_nano_seconds
                    
                    	Number of remaining nanoseconds
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.CandidatePath.CleanupTimer, self).__init__()

                        self.yang_name = "cleanup-timer"
                        self.yang_parent_name = "candidate-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('running', (YLeaf(YType.boolean, 'running'), ['bool'])),
                            ('remaining_seconds', (YLeaf(YType.int64, 'remaining-seconds'), ['int'])),
                            ('remaining_nano_seconds', (YLeaf(YType.int64, 'remaining-nano-seconds'), ['int'])),
                        ])
                        self.running = None
                        self.remaining_seconds = None
                        self.remaining_nano_seconds = None
                        self._segment_path = lambda: "cleanup-timer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.CandidatePath.CleanupTimer, ['running', 'remaining_seconds', 'remaining_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.CandidatePath.CleanupTimer']['meta_info']


                class PccInformation(_Entity_):
                    """
                    PCC PCEP\-related information
                    
                    .. attribute:: orphan_timer
                    
                    	Orphan timer for PCE\-initiated candidate paths in orphan state
                    	**type**\:  :py:class:`OrphanTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.PccInformation.OrphanTimer>`
                    
                    	**config**\: False
                    
                    .. attribute:: fallback_timer
                    
                    	Timer for delaying delegation revoke back to LSP originator
                    	**type**\:  :py:class:`FallbackTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.PccInformation.FallbackTimer>`
                    
                    	**config**\: False
                    
                    .. attribute:: symbolic_name
                    
                    	Symbolic name of the PLSP
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: plsp_id
                    
                    	PLSP\-ID associated with the PCC info
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: is_orphan
                    
                    	Whether the candidate path is in orphan state
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: profile_key
                    
                    	List of profile keys
                    	**type**\: list of  		 :py:class:`ProfileKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.PccInformation.ProfileKey>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.CandidatePath.PccInformation, self).__init__()

                        self.yang_name = "pcc-information"
                        self.yang_parent_name = "candidate-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("orphan-timer", ("orphan_timer", Xtc.Policies.Policy.CandidatePath.PccInformation.OrphanTimer)), ("fallback-timer", ("fallback_timer", Xtc.Policies.Policy.CandidatePath.PccInformation.FallbackTimer)), ("profile-key", ("profile_key", Xtc.Policies.Policy.CandidatePath.PccInformation.ProfileKey))])
                        self._leafs = OrderedDict([
                            ('symbolic_name', (YLeaf(YType.str, 'symbolic-name'), ['str'])),
                            ('plsp_id', (YLeaf(YType.uint32, 'plsp-id'), ['int'])),
                            ('is_orphan', (YLeaf(YType.boolean, 'is-orphan'), ['bool'])),
                        ])
                        self.symbolic_name = None
                        self.plsp_id = None
                        self.is_orphan = None

                        self.orphan_timer = Xtc.Policies.Policy.CandidatePath.PccInformation.OrphanTimer()
                        self.orphan_timer.parent = self
                        self._children_name_map["orphan_timer"] = "orphan-timer"

                        self.fallback_timer = Xtc.Policies.Policy.CandidatePath.PccInformation.FallbackTimer()
                        self.fallback_timer.parent = self
                        self._children_name_map["fallback_timer"] = "fallback-timer"

                        self.profile_key = YList(self)
                        self._segment_path = lambda: "pcc-information"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.CandidatePath.PccInformation, ['symbolic_name', 'plsp_id', 'is_orphan'], name, value)


                    class OrphanTimer(_Entity_):
                        """
                        Orphan timer for PCE\-initiated candidate paths
                        in orphan state
                        
                        .. attribute:: running
                        
                        	Whether the timer is running
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: remaining_seconds
                        
                        	Number of remaining seconds
                        	**type**\: int
                        
                        	**range:** \-9223372036854775808..9223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: remaining_nano_seconds
                        
                        	Number of remaining nanoseconds
                        	**type**\: int
                        
                        	**range:** \-9223372036854775808..9223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.CandidatePath.PccInformation.OrphanTimer, self).__init__()

                            self.yang_name = "orphan-timer"
                            self.yang_parent_name = "pcc-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('running', (YLeaf(YType.boolean, 'running'), ['bool'])),
                                ('remaining_seconds', (YLeaf(YType.int64, 'remaining-seconds'), ['int'])),
                                ('remaining_nano_seconds', (YLeaf(YType.int64, 'remaining-nano-seconds'), ['int'])),
                            ])
                            self.running = None
                            self.remaining_seconds = None
                            self.remaining_nano_seconds = None
                            self._segment_path = lambda: "orphan-timer"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.CandidatePath.PccInformation.OrphanTimer, ['running', 'remaining_seconds', 'remaining_nano_seconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.CandidatePath.PccInformation.OrphanTimer']['meta_info']


                    class FallbackTimer(_Entity_):
                        """
                        Timer for delaying delegation revoke back to LSP
                        originator
                        
                        .. attribute:: running
                        
                        	Whether the timer is running
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: remaining_seconds
                        
                        	Number of remaining seconds
                        	**type**\: int
                        
                        	**range:** \-9223372036854775808..9223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: remaining_nano_seconds
                        
                        	Number of remaining nanoseconds
                        	**type**\: int
                        
                        	**range:** \-9223372036854775808..9223372036854775807
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.CandidatePath.PccInformation.FallbackTimer, self).__init__()

                            self.yang_name = "fallback-timer"
                            self.yang_parent_name = "pcc-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('running', (YLeaf(YType.boolean, 'running'), ['bool'])),
                                ('remaining_seconds', (YLeaf(YType.int64, 'remaining-seconds'), ['int'])),
                                ('remaining_nano_seconds', (YLeaf(YType.int64, 'remaining-nano-seconds'), ['int'])),
                            ])
                            self.running = None
                            self.remaining_seconds = None
                            self.remaining_nano_seconds = None
                            self._segment_path = lambda: "fallback-timer"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.CandidatePath.PccInformation.FallbackTimer, ['running', 'remaining_seconds', 'remaining_nano_seconds'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.CandidatePath.PccInformation.FallbackTimer']['meta_info']


                    class ProfileKey(_Entity_):
                        """
                        List of profile keys
                        
                        .. attribute:: id
                        
                        	Numeric part of profile key
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: source_address
                        
                        	Source IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.CandidatePath.PccInformation.ProfileKey, self).__init__()

                            self.yang_name = "profile-key"
                            self.yang_parent_name = "pcc-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', (YLeaf(YType.uint16, 'id'), ['int'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                            ])
                            self.id = None
                            self.source_address = None
                            self._segment_path = lambda: "profile-key"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.CandidatePath.PccInformation.ProfileKey, ['id', 'source_address'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.CandidatePath.PccInformation.ProfileKey']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.CandidatePath.PccInformation']['meta_info']


                class SegmentList(_Entity_):
                    """
                    Segment lists of the candidate path
                    
                    .. attribute:: name
                    
                    	Explicit segment list name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	Segment list type
                    	**type**\:  :py:class:`XtcPolicyPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcPolicyPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: active
                    
                    	Whether the segment list is active (used)
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: weight
                    
                    	Weight of the segment list
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: metric_type
                    
                    	Metric type of the segment list
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: metric_value
                    
                    	Accumulated metric of the segment list
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: is_valid
                    
                    	True if path is valid
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: pce_based_path
                    
                    	True if the path is to be computed by PCE
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: pce_address
                    
                    	Address of the PCE computed the path
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: error
                    
                    	Error (for display only)
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: hops
                    
                    	SR hop list
                    	**type**\: list of  		 :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SegmentList.Hops>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.CandidatePath.SegmentList, self).__init__()

                        self.yang_name = "segment-list"
                        self.yang_parent_name = "candidate-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hops", ("hops", Xtc.Policies.Policy.CandidatePath.SegmentList.Hops))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcPolicyPath', '')])),
                            ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                            ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                            ('metric_type', (YLeaf(YType.uint8, 'metric-type'), ['int'])),
                            ('metric_value', (YLeaf(YType.uint64, 'metric-value'), ['int'])),
                            ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                            ('pce_based_path', (YLeaf(YType.boolean, 'pce-based-path'), ['bool'])),
                            ('pce_address', (YLeaf(YType.str, 'pce-address'), ['str'])),
                            ('error', (YLeaf(YType.str, 'error'), ['str'])),
                        ])
                        self.name = None
                        self.type = None
                        self.active = None
                        self.weight = None
                        self.metric_type = None
                        self.metric_value = None
                        self.is_valid = None
                        self.pce_based_path = None
                        self.pce_address = None
                        self.error = None

                        self.hops = YList(self)
                        self._segment_path = lambda: "segment-list"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SegmentList, ['name', 'type', 'active', 'weight', 'metric_type', 'metric_value', 'is_valid', 'pce_based_path', 'pce_address', 'error'], name, value)


                    class Hops(_Entity_):
                        """
                        SR hop list
                        
                        .. attribute:: sid
                        
                        	SID value
                        	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.Sid>`
                        
                        	**config**\: False
                        
                        .. attribute:: local_address
                        
                        	Local address
                        	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.LocalAddress>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_address
                        
                        	Remote address
                        	**type**\:  :py:class:`RemoteAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.RemoteAddress>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`XtcSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSrSid>`
                        
                        	**config**\: False
                        
                        .. attribute:: algorithm
                        
                        	Algorithim
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.CandidatePath.SegmentList.Hops, self).__init__()

                            self.yang_name = "hops"
                            self.yang_parent_name = "segment-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sid", ("sid", Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.Sid)), ("local-address", ("local_address", Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.LocalAddress)), ("remote-address", ("remote_address", Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.RemoteAddress))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSrSid', '')])),
                                ('algorithm', (YLeaf(YType.uint8, 'algorithm'), ['int'])),
                            ])
                            self.sid_type = None
                            self.algorithm = None

                            self.sid = Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.Sid()
                            self.sid.parent = self
                            self._children_name_map["sid"] = "sid"

                            self.local_address = Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.LocalAddress()
                            self.local_address.parent = self
                            self._children_name_map["local_address"] = "local-address"

                            self.remote_address = Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.RemoteAddress()
                            self.remote_address.parent = self
                            self._children_name_map["remote_address"] = "remote-address"
                            self._segment_path = lambda: "hops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SegmentList.Hops, ['sid_type', 'algorithm'], name, value)


                        class Sid(_Entity_):
                            """
                            SID value
                            
                            .. attribute:: sid_type
                            
                            	SIDType
                            	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                            
                            	**config**\: False
                            
                            .. attribute:: label
                            
                            	MPLS label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.Sid, self).__init__()

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
                                self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.Sid, ['sid_type', 'label', 'ipv6'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.Sid']['meta_info']


                        class LocalAddress(_Entity_):
                            """
                            Local address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.LocalAddress, self).__init__()

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
                                self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.LocalAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.LocalAddress']['meta_info']


                        class RemoteAddress(_Entity_):
                            """
                            Remote address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.RemoteAddress, self).__init__()

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
                                self._perform_setattr(Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.RemoteAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SegmentList.Hops.RemoteAddress']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SegmentList.Hops']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.CandidatePath.SegmentList']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.Policies.Policy.CandidatePath']['meta_info']


            class LsPs(_Entity_):
                """
                LSPs
                
                .. attribute:: binding_sid
                
                	Binding SID information
                	**type**\:  :py:class:`BindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.LsPs.BindingSid>`
                
                	**config**\: False
                
                .. attribute:: install_timer
                
                	Install timer information
                	**type**\:  :py:class:`InstallTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.LsPs.InstallTimer>`
                
                	**config**\: False
                
                .. attribute:: cleanup_timer
                
                	Cleanup timer information
                	**type**\:  :py:class:`CleanupTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.LsPs.CleanupTimer>`
                
                	**config**\: False
                
                .. attribute:: lsp_id
                
                	LSP ID
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: policy_id
                
                	Policy ID
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                .. attribute:: local_label
                
                	Local label of the LSP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: state
                
                	Current LSP state
                	**type**\:  :py:class:`XtcPolicyLspSmState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcPolicyLspSmState>`
                
                	**config**\: False
                
                .. attribute:: is_active_lsp
                
                	Whether this is the active LSP
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: is_reoptimized_lsp
                
                	Whether this is the reoptimized LSP
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.Policies.Policy.LsPs, self).__init__()

                    self.yang_name = "ls-ps"
                    self.yang_parent_name = "policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("binding-sid", ("binding_sid", Xtc.Policies.Policy.LsPs.BindingSid)), ("install-timer", ("install_timer", Xtc.Policies.Policy.LsPs.InstallTimer)), ("cleanup-timer", ("cleanup_timer", Xtc.Policies.Policy.LsPs.CleanupTimer))])
                    self._leafs = OrderedDict([
                        ('lsp_id', (YLeaf(YType.uint16, 'lsp-id'), ['int'])),
                        ('policy_id', (YLeaf(YType.uint16, 'policy-id'), ['int'])),
                        ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcPolicyLspSmState', '')])),
                        ('is_active_lsp', (YLeaf(YType.boolean, 'is-active-lsp'), ['bool'])),
                        ('is_reoptimized_lsp', (YLeaf(YType.boolean, 'is-reoptimized-lsp'), ['bool'])),
                    ])
                    self.lsp_id = None
                    self.policy_id = None
                    self.local_label = None
                    self.state = None
                    self.is_active_lsp = None
                    self.is_reoptimized_lsp = None

                    self.binding_sid = Xtc.Policies.Policy.LsPs.BindingSid()
                    self.binding_sid.parent = self
                    self._children_name_map["binding_sid"] = "binding-sid"

                    self.install_timer = Xtc.Policies.Policy.LsPs.InstallTimer()
                    self.install_timer.parent = self
                    self._children_name_map["install_timer"] = "install-timer"

                    self.cleanup_timer = Xtc.Policies.Policy.LsPs.CleanupTimer()
                    self.cleanup_timer.parent = self
                    self._children_name_map["cleanup_timer"] = "cleanup-timer"
                    self._segment_path = lambda: "ls-ps"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Policies.Policy.LsPs, ['lsp_id', 'policy_id', 'local_label', 'state', 'is_active_lsp', 'is_reoptimized_lsp'], name, value)


                class BindingSid(_Entity_):
                    """
                    Binding SID information
                    
                    .. attribute:: value
                    
                    	Binding SID value
                    	**type**\:  :py:class:`Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Policies.Policy.LsPs.BindingSid.Value>`
                    
                    	**config**\: False
                    
                    .. attribute:: is_fallback_dynamic
                    
                    	Whether the BSID is in fallback dynamic mode
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_within_srlb_range
                    
                    	Whether the BSID is within SRLB range
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.LsPs.BindingSid, self).__init__()

                        self.yang_name = "binding-sid"
                        self.yang_parent_name = "ls-ps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("value", ("value", Xtc.Policies.Policy.LsPs.BindingSid.Value))])
                        self._leafs = OrderedDict([
                            ('is_fallback_dynamic', (YLeaf(YType.boolean, 'is-fallback-dynamic'), ['bool'])),
                            ('is_within_srlb_range', (YLeaf(YType.boolean, 'is-within-srlb-range'), ['bool'])),
                        ])
                        self.is_fallback_dynamic = None
                        self.is_within_srlb_range = None

                        self.value = Xtc.Policies.Policy.LsPs.BindingSid.Value()
                        self.value.parent = self
                        self._children_name_map["value"] = "value"
                        self._segment_path = lambda: "binding-sid"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.LsPs.BindingSid, ['is_fallback_dynamic', 'is_within_srlb_range'], name, value)


                    class Value(_Entity_):
                        """
                        Binding SID value
                        
                        .. attribute:: sid_type
                        
                        	SIDType
                        	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                        
                        	**config**\: False
                        
                        .. attribute:: label
                        
                        	MPLS label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Policies.Policy.LsPs.BindingSid.Value, self).__init__()

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
                            self._perform_setattr(Xtc.Policies.Policy.LsPs.BindingSid.Value, ['sid_type', 'label', 'ipv6'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Policies.Policy.LsPs.BindingSid.Value']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.LsPs.BindingSid']['meta_info']


                class InstallTimer(_Entity_):
                    """
                    Install timer information
                    
                    .. attribute:: running
                    
                    	Whether the timer is running
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: remaining_seconds
                    
                    	Number of remaining seconds
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: remaining_nano_seconds
                    
                    	Number of remaining nanoseconds
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.LsPs.InstallTimer, self).__init__()

                        self.yang_name = "install-timer"
                        self.yang_parent_name = "ls-ps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('running', (YLeaf(YType.boolean, 'running'), ['bool'])),
                            ('remaining_seconds', (YLeaf(YType.int64, 'remaining-seconds'), ['int'])),
                            ('remaining_nano_seconds', (YLeaf(YType.int64, 'remaining-nano-seconds'), ['int'])),
                        ])
                        self.running = None
                        self.remaining_seconds = None
                        self.remaining_nano_seconds = None
                        self._segment_path = lambda: "install-timer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.LsPs.InstallTimer, ['running', 'remaining_seconds', 'remaining_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.LsPs.InstallTimer']['meta_info']


                class CleanupTimer(_Entity_):
                    """
                    Cleanup timer information
                    
                    .. attribute:: running
                    
                    	Whether the timer is running
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: remaining_seconds
                    
                    	Number of remaining seconds
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: remaining_nano_seconds
                    
                    	Number of remaining nanoseconds
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Policies.Policy.LsPs.CleanupTimer, self).__init__()

                        self.yang_name = "cleanup-timer"
                        self.yang_parent_name = "ls-ps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('running', (YLeaf(YType.boolean, 'running'), ['bool'])),
                            ('remaining_seconds', (YLeaf(YType.int64, 'remaining-seconds'), ['int'])),
                            ('remaining_nano_seconds', (YLeaf(YType.int64, 'remaining-nano-seconds'), ['int'])),
                        ])
                        self.running = None
                        self.remaining_seconds = None
                        self.remaining_nano_seconds = None
                        self._segment_path = lambda: "cleanup-timer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Policies.Policy.LsPs.CleanupTimer, ['running', 'remaining_seconds', 'remaining_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Policies.Policy.LsPs.CleanupTimer']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.Policies.Policy.LsPs']['meta_info']


            class EventBuffer(_Entity_):
                """
                Policy Event buffer
                
                .. attribute:: event_message
                
                	Event message
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: time_stamp
                
                	Event time, relative to Jan 1, 1970
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.Policies.Policy.EventBuffer, self).__init__()

                    self.yang_name = "event-buffer"
                    self.yang_parent_name = "policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('event_message', (YLeaf(YType.str, 'event-message'), ['str'])),
                        ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                    ])
                    self.event_message = None
                    self.time_stamp = None
                    self._segment_path = lambda: "event-buffer"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Policies.Policy.EventBuffer, ['event_message', 'time_stamp'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.Policies.Policy.EventBuffer']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Xtc.Policies.Policy']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.Policies']['meta_info']


    class Interfaces(_Entity_):
        """
        Interface database in XTC Agent
        
        .. attribute:: interface
        
        	Interface information
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Interfaces.Interface>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Xtc.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Xtc.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.Interfaces, [], name, value)


        class Interface(_Entity_):
            """
            Interface information
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: name
            
            	Name of the interface
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: operational_up
            
            	Operational up
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Xtc.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('interface_handle', (YLeaf(YType.str, 'interface-handle'), ['str'])),
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('operational_up', (YLeaf(YType.boolean, 'operational-up'), ['bool'])),
                ])
                self.interface_name = None
                self.interface_handle = None
                self.name = None
                self.operational_up = None
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.Interfaces.Interface, ['interface_name', 'interface_handle', 'name', 'operational_up'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Xtc.Interfaces.Interface']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.Interfaces']['meta_info']


    class PolicyForwardings(_Entity_):
        """
        Forwarding information for policies
        
        .. attribute:: policy_forwarding
        
        	Forwarding information for the policy
        	**type**\: list of  		 :py:class:`PolicyForwarding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Xtc.PolicyForwardings, self).__init__()

            self.yang_name = "policy-forwardings"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-forwarding", ("policy_forwarding", Xtc.PolicyForwardings.PolicyForwarding))])
            self._leafs = OrderedDict()

            self.policy_forwarding = YList(self)
            self._segment_path = lambda: "policy-forwardings"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.PolicyForwardings, [], name, value)


        class PolicyForwarding(_Entity_):
            """
            Forwarding information for the policy
            
            .. attribute:: name  (key)
            
            	Policy Name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: endpoint_address
            
            	Endpoint address
            	**type**\:  :py:class:`EndpointAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.EndpointAddress>`
            
            	**config**\: False
            
            .. attribute:: binding_sid
            
            	Programmed Binding SID
            	**type**\:  :py:class:`BindingSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.BindingSid>`
            
            	**config**\: False
            
            .. attribute:: stats
            
            	Overall forwarding stats of the policy
            	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.Stats>`
            
            	**config**\: False
            
            .. attribute:: active_lsp
            
            	Active LSP information
            	**type**\:  :py:class:`ActiveLsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp>`
            
            	**config**\: False
            
            .. attribute:: reoptimized_lsp
            
            	Reoptimized LSP information
            	**type**\:  :py:class:`ReoptimizedLsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp>`
            
            	**config**\: False
            
            .. attribute:: policy_name
            
            	Policy name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: color
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Xtc.PolicyForwardings.PolicyForwarding, self).__init__()

                self.yang_name = "policy-forwarding"
                self.yang_parent_name = "policy-forwardings"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("endpoint-address", ("endpoint_address", Xtc.PolicyForwardings.PolicyForwarding.EndpointAddress)), ("binding-sid", ("binding_sid", Xtc.PolicyForwardings.PolicyForwarding.BindingSid)), ("stats", ("stats", Xtc.PolicyForwardings.PolicyForwarding.Stats)), ("active-lsp", ("active_lsp", Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp)), ("reoptimized-lsp", ("reoptimized_lsp", Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                    ('color', (YLeaf(YType.uint32, 'color'), ['int'])),
                ])
                self.name = None
                self.policy_name = None
                self.color = None

                self.endpoint_address = Xtc.PolicyForwardings.PolicyForwarding.EndpointAddress()
                self.endpoint_address.parent = self
                self._children_name_map["endpoint_address"] = "endpoint-address"

                self.binding_sid = Xtc.PolicyForwardings.PolicyForwarding.BindingSid()
                self.binding_sid.parent = self
                self._children_name_map["binding_sid"] = "binding-sid"

                self.stats = Xtc.PolicyForwardings.PolicyForwarding.Stats()
                self.stats.parent = self
                self._children_name_map["stats"] = "stats"

                self.active_lsp = Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp()
                self.active_lsp.parent = self
                self._children_name_map["active_lsp"] = "active-lsp"

                self.reoptimized_lsp = Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp()
                self.reoptimized_lsp.parent = self
                self._children_name_map["reoptimized_lsp"] = "reoptimized-lsp"
                self._segment_path = lambda: "policy-forwarding" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policy-forwardings/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding, ['name', 'policy_name', 'color'], name, value)


            class EndpointAddress(_Entity_):
                """
                Endpoint address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                
                	**config**\: False
                
                .. attribute:: ipv4
                
                	IPv4 address type
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: ipv6
                
                	IPv6 address type
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.PolicyForwardings.PolicyForwarding.EndpointAddress, self).__init__()

                    self.yang_name = "endpoint-address"
                    self.yang_parent_name = "policy-forwarding"
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
                    self._segment_path = lambda: "endpoint-address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.EndpointAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.EndpointAddress']['meta_info']


            class BindingSid(_Entity_):
                """
                Programmed Binding SID
                
                .. attribute:: sid_type
                
                	SIDType
                	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                
                	**config**\: False
                
                .. attribute:: label
                
                	MPLS label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ipv6
                
                	IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.PolicyForwardings.PolicyForwarding.BindingSid, self).__init__()

                    self.yang_name = "binding-sid"
                    self.yang_parent_name = "policy-forwarding"
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
                    self._segment_path = lambda: "binding-sid"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.BindingSid, ['sid_type', 'label', 'ipv6'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.BindingSid']['meta_info']


            class Stats(_Entity_):
                """
                Overall forwarding stats of the policy
                
                .. attribute:: packets
                
                	Number of packets forwarded
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bytes
                
                	Number of bytes forwarded
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                	**units**\: byte
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.PolicyForwardings.PolicyForwarding.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "policy-forwarding"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                        ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                    ])
                    self.packets = None
                    self.bytes = None
                    self._segment_path = lambda: "stats"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.Stats, ['packets', 'bytes'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.Stats']['meta_info']


            class ActiveLsp(_Entity_):
                """
                Active LSP information
                
                .. attribute:: candidate_path
                
                	Candidate path associated with this LSP
                	**type**\:  :py:class:`CandidatePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath>`
                
                	**config**\: False
                
                .. attribute:: local_label
                
                	Local label of the LSP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: segment_list
                
                	Segment lists
                	**type**\: list of  		 :py:class:`SegmentList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp, self).__init__()

                    self.yang_name = "active-lsp"
                    self.yang_parent_name = "policy-forwarding"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("candidate-path", ("candidate_path", Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath)), ("segment-list", ("segment_list", Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList))])
                    self._leafs = OrderedDict([
                        ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                    ])
                    self.local_label = None

                    self.candidate_path = Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath()
                    self.candidate_path.parent = self
                    self._children_name_map["candidate_path"] = "candidate-path"

                    self.segment_list = YList(self)
                    self._segment_path = lambda: "active-lsp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp, ['local_label'], name, value)


                class CandidatePath(_Entity_):
                    """
                    Candidate path associated with this LSP
                    
                    .. attribute:: originator
                    
                    	Candidate path originator
                    	**type**\:  :py:class:`Originator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator>`
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Name of the candidate path, if any
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: preference
                    
                    	Candidate path preference
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: protocol_originator
                    
                    	Candidate path protocol origin
                    	**type**\:  :py:class:`XtcPolicyCpathProtoOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcPolicyCpathProtoOrigin>`
                    
                    	**config**\: False
                    
                    .. attribute:: discriminator
                    
                    	Candidate path discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath, self).__init__()

                        self.yang_name = "candidate-path"
                        self.yang_parent_name = "active-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("originator", ("originator", Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('preference', (YLeaf(YType.uint32, 'preference'), ['int'])),
                            ('protocol_originator', (YLeaf(YType.enumeration, 'protocol-originator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcPolicyCpathProtoOrigin', '')])),
                            ('discriminator', (YLeaf(YType.uint32, 'discriminator'), ['int'])),
                        ])
                        self.name = None
                        self.preference = None
                        self.protocol_originator = None
                        self.discriminator = None

                        self.originator = Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator()
                        self.originator.parent = self
                        self._children_name_map["originator"] = "originator"
                        self._segment_path = lambda: "candidate-path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath, ['name', 'preference', 'protocol_originator', 'discriminator'], name, value)


                    class Originator(_Entity_):
                        """
                        Candidate path originator
                        
                        .. attribute:: node_address
                        
                        	Originator node address
                        	**type**\:  :py:class:`NodeAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator.NodeAddress>`
                        
                        	**config**\: False
                        
                        .. attribute:: autonomous_system_number
                        
                        	Originator Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator, self).__init__()

                            self.yang_name = "originator"
                            self.yang_parent_name = "candidate-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-address", ("node_address", Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator.NodeAddress))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                            ])
                            self.autonomous_system_number = None

                            self.node_address = Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator.NodeAddress()
                            self.node_address.parent = self
                            self._children_name_map["node_address"] = "node-address"
                            self._segment_path = lambda: "originator"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator, ['autonomous_system_number'], name, value)


                        class NodeAddress(_Entity_):
                            """
                            Originator node address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator.NodeAddress, self).__init__()

                                self.yang_name = "node-address"
                                self.yang_parent_name = "originator"
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
                                self._segment_path = lambda: "node-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator.NodeAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator.NodeAddress']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath.Originator']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.CandidatePath']['meta_info']


                class SegmentList(_Entity_):
                    """
                    Segment lists
                    
                    .. attribute:: stats
                    
                    	Forwarding stats of the segment list
                    	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Stats>`
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Name of the segment list, if any
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: paths
                    
                    	Segment list paths
                    	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList, self).__init__()

                        self.yang_name = "segment-list"
                        self.yang_parent_name = "active-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("stats", ("stats", Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Stats)), ("paths", ("paths", Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.stats = Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"

                        self.paths = YList(self)
                        self._segment_path = lambda: "segment-list"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList, ['name'], name, value)


                    class Stats(_Entity_):
                        """
                        Forwarding stats of the segment list
                        
                        .. attribute:: packets
                        
                        	Number of packets forwarded
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: bytes
                        
                        	Number of bytes forwarded
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Stats, self).__init__()

                            self.yang_name = "stats"
                            self.yang_parent_name = "segment-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                            ])
                            self.packets = None
                            self.bytes = None
                            self._segment_path = lambda: "stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Stats, ['packets', 'bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Stats']['meta_info']


                    class Paths(_Entity_):
                        """
                        Segment list paths
                        
                        .. attribute:: stats
                        
                        	Forwarding stats of the path
                        	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths.Stats>`
                        
                        	**config**\: False
                        
                        .. attribute:: outgoing_interface
                        
                        	Outgoing interface handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: next_hop_ipv4
                        
                        	IPv4 Next Hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: next_hop_table_id
                        
                        	Table ID for nexthop address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_protected
                        
                        	Is this path protected ?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_pure_bkup
                        
                        	Is this path a pure backup ?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_lfa_or_ecmp_backup
                        
                        	Whether the path is LFA or ECMP backup
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: load_metric
                        
                        	Path's load metric for load balancing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: path_id
                        
                        	path Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: bkup_path_id
                        
                        	Backup path Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: label_stack
                        
                        	Path outgoing labels
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "segment-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stats", ("stats", Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths.Stats))])
                            self._leafs = OrderedDict([
                                ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                                ('next_hop_ipv4', (YLeaf(YType.str, 'next-hop-ipv4'), ['str'])),
                                ('next_hop_table_id', (YLeaf(YType.uint32, 'next-hop-table-id'), ['int'])),
                                ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                ('is_pure_bkup', (YLeaf(YType.boolean, 'is-pure-bkup'), ['bool'])),
                                ('is_lfa_or_ecmp_backup', (YLeaf(YType.boolean, 'is-lfa-or-ecmp-backup'), ['bool'])),
                                ('load_metric', (YLeaf(YType.uint32, 'load-metric'), ['int'])),
                                ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                                ('bkup_path_id', (YLeaf(YType.uint8, 'bkup-path-id'), ['int'])),
                                ('label_stack', (YLeafList(YType.uint32, 'label-stack'), ['int'])),
                            ])
                            self.outgoing_interface = None
                            self.next_hop_ipv4 = None
                            self.next_hop_table_id = None
                            self.is_protected = None
                            self.is_pure_bkup = None
                            self.is_lfa_or_ecmp_backup = None
                            self.load_metric = None
                            self.path_id = None
                            self.bkup_path_id = None
                            self.label_stack = []

                            self.stats = Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths.Stats()
                            self.stats.parent = self
                            self._children_name_map["stats"] = "stats"
                            self._segment_path = lambda: "paths"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths, ['outgoing_interface', 'next_hop_ipv4', 'next_hop_table_id', 'is_protected', 'is_pure_bkup', 'is_lfa_or_ecmp_backup', 'load_metric', 'path_id', 'bkup_path_id', 'label_stack'], name, value)


                        class Stats(_Entity_):
                            """
                            Forwarding stats of the path
                            
                            .. attribute:: packets
                            
                            	Number of packets forwarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Number of bytes forwarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths.Stats, self).__init__()

                                self.yang_name = "stats"
                                self.yang_parent_name = "paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths.Stats, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths.Stats']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList.Paths']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp.SegmentList']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ActiveLsp']['meta_info']


            class ReoptimizedLsp(_Entity_):
                """
                Reoptimized LSP information
                
                .. attribute:: candidate_path
                
                	Candidate path associated with this LSP
                	**type**\:  :py:class:`CandidatePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath>`
                
                	**config**\: False
                
                .. attribute:: local_label
                
                	Local label of the LSP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: segment_list
                
                	Segment lists
                	**type**\: list of  		 :py:class:`SegmentList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp, self).__init__()

                    self.yang_name = "reoptimized-lsp"
                    self.yang_parent_name = "policy-forwarding"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("candidate-path", ("candidate_path", Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath)), ("segment-list", ("segment_list", Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList))])
                    self._leafs = OrderedDict([
                        ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                    ])
                    self.local_label = None

                    self.candidate_path = Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath()
                    self.candidate_path.parent = self
                    self._children_name_map["candidate_path"] = "candidate-path"

                    self.segment_list = YList(self)
                    self._segment_path = lambda: "reoptimized-lsp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp, ['local_label'], name, value)


                class CandidatePath(_Entity_):
                    """
                    Candidate path associated with this LSP
                    
                    .. attribute:: originator
                    
                    	Candidate path originator
                    	**type**\:  :py:class:`Originator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator>`
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Name of the candidate path, if any
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: preference
                    
                    	Candidate path preference
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: protocol_originator
                    
                    	Candidate path protocol origin
                    	**type**\:  :py:class:`XtcPolicyCpathProtoOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcPolicyCpathProtoOrigin>`
                    
                    	**config**\: False
                    
                    .. attribute:: discriminator
                    
                    	Candidate path discriminator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath, self).__init__()

                        self.yang_name = "candidate-path"
                        self.yang_parent_name = "reoptimized-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("originator", ("originator", Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('preference', (YLeaf(YType.uint32, 'preference'), ['int'])),
                            ('protocol_originator', (YLeaf(YType.enumeration, 'protocol-originator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcPolicyCpathProtoOrigin', '')])),
                            ('discriminator', (YLeaf(YType.uint32, 'discriminator'), ['int'])),
                        ])
                        self.name = None
                        self.preference = None
                        self.protocol_originator = None
                        self.discriminator = None

                        self.originator = Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator()
                        self.originator.parent = self
                        self._children_name_map["originator"] = "originator"
                        self._segment_path = lambda: "candidate-path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath, ['name', 'preference', 'protocol_originator', 'discriminator'], name, value)


                    class Originator(_Entity_):
                        """
                        Candidate path originator
                        
                        .. attribute:: node_address
                        
                        	Originator node address
                        	**type**\:  :py:class:`NodeAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator.NodeAddress>`
                        
                        	**config**\: False
                        
                        .. attribute:: autonomous_system_number
                        
                        	Originator Autonomous System Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator, self).__init__()

                            self.yang_name = "originator"
                            self.yang_parent_name = "candidate-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("node-address", ("node_address", Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator.NodeAddress))])
                            self._leafs = OrderedDict([
                                ('autonomous_system_number', (YLeaf(YType.uint32, 'autonomous-system-number'), ['int'])),
                            ])
                            self.autonomous_system_number = None

                            self.node_address = Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator.NodeAddress()
                            self.node_address.parent = self
                            self._children_name_map["node_address"] = "node-address"
                            self._segment_path = lambda: "originator"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator, ['autonomous_system_number'], name, value)


                        class NodeAddress(_Entity_):
                            """
                            Originator node address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator.NodeAddress, self).__init__()

                                self.yang_name = "node-address"
                                self.yang_parent_name = "originator"
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
                                self._segment_path = lambda: "node-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator.NodeAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator.NodeAddress']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath.Originator']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.CandidatePath']['meta_info']


                class SegmentList(_Entity_):
                    """
                    Segment lists
                    
                    .. attribute:: stats
                    
                    	Forwarding stats of the segment list
                    	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Stats>`
                    
                    	**config**\: False
                    
                    .. attribute:: name
                    
                    	Name of the segment list, if any
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: paths
                    
                    	Segment list paths
                    	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList, self).__init__()

                        self.yang_name = "segment-list"
                        self.yang_parent_name = "reoptimized-lsp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("stats", ("stats", Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Stats)), ("paths", ("paths", Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.stats = Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Stats()
                        self.stats.parent = self
                        self._children_name_map["stats"] = "stats"

                        self.paths = YList(self)
                        self._segment_path = lambda: "segment-list"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList, ['name'], name, value)


                    class Stats(_Entity_):
                        """
                        Forwarding stats of the segment list
                        
                        .. attribute:: packets
                        
                        	Number of packets forwarded
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: bytes
                        
                        	Number of bytes forwarded
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Stats, self).__init__()

                            self.yang_name = "stats"
                            self.yang_parent_name = "segment-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                            ])
                            self.packets = None
                            self.bytes = None
                            self._segment_path = lambda: "stats"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Stats, ['packets', 'bytes'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Stats']['meta_info']


                    class Paths(_Entity_):
                        """
                        Segment list paths
                        
                        .. attribute:: stats
                        
                        	Forwarding stats of the path
                        	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths.Stats>`
                        
                        	**config**\: False
                        
                        .. attribute:: outgoing_interface
                        
                        	Outgoing interface handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: next_hop_ipv4
                        
                        	IPv4 Next Hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: next_hop_table_id
                        
                        	Table ID for nexthop address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_protected
                        
                        	Is this path protected ?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_pure_bkup
                        
                        	Is this path a pure backup ?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: is_lfa_or_ecmp_backup
                        
                        	Whether the path is LFA or ECMP backup
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: load_metric
                        
                        	Path's load metric for load balancing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: path_id
                        
                        	path Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: bkup_path_id
                        
                        	Backup path Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: label_stack
                        
                        	Path outgoing labels
                        	**type**\: list of int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "segment-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("stats", ("stats", Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths.Stats))])
                            self._leafs = OrderedDict([
                                ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                                ('next_hop_ipv4', (YLeaf(YType.str, 'next-hop-ipv4'), ['str'])),
                                ('next_hop_table_id', (YLeaf(YType.uint32, 'next-hop-table-id'), ['int'])),
                                ('is_protected', (YLeaf(YType.boolean, 'is-protected'), ['bool'])),
                                ('is_pure_bkup', (YLeaf(YType.boolean, 'is-pure-bkup'), ['bool'])),
                                ('is_lfa_or_ecmp_backup', (YLeaf(YType.boolean, 'is-lfa-or-ecmp-backup'), ['bool'])),
                                ('load_metric', (YLeaf(YType.uint32, 'load-metric'), ['int'])),
                                ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                                ('bkup_path_id', (YLeaf(YType.uint8, 'bkup-path-id'), ['int'])),
                                ('label_stack', (YLeafList(YType.uint32, 'label-stack'), ['int'])),
                            ])
                            self.outgoing_interface = None
                            self.next_hop_ipv4 = None
                            self.next_hop_table_id = None
                            self.is_protected = None
                            self.is_pure_bkup = None
                            self.is_lfa_or_ecmp_backup = None
                            self.load_metric = None
                            self.path_id = None
                            self.bkup_path_id = None
                            self.label_stack = []

                            self.stats = Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths.Stats()
                            self.stats.parent = self
                            self._children_name_map["stats"] = "stats"
                            self._segment_path = lambda: "paths"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths, ['outgoing_interface', 'next_hop_ipv4', 'next_hop_table_id', 'is_protected', 'is_pure_bkup', 'is_lfa_or_ecmp_backup', 'load_metric', 'path_id', 'bkup_path_id', 'label_stack'], name, value)


                        class Stats(_Entity_):
                            """
                            Forwarding stats of the path
                            
                            .. attribute:: packets
                            
                            	Number of packets forwarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            .. attribute:: bytes
                            
                            	Number of bytes forwarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**config**\: False
                            
                            	**units**\: byte
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths.Stats, self).__init__()

                                self.yang_name = "stats"
                                self.yang_parent_name = "paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('packets', (YLeaf(YType.uint64, 'packets'), ['int'])),
                                    ('bytes', (YLeaf(YType.uint64, 'bytes'), ['int'])),
                                ])
                                self.packets = None
                                self.bytes = None
                                self._segment_path = lambda: "stats"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths.Stats, ['packets', 'bytes'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths.Stats']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList.Paths']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp.SegmentList']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding.ReoptimizedLsp']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Xtc.PolicyForwardings.PolicyForwarding']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.PolicyForwardings']['meta_info']


    class PolicySummary(_Entity_):
        """
        Summary of all policies
        
        .. attribute:: total_policy_count
        
        	Total number of policies
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: up_policy_count
        
        	Total number of policies that are operationally up
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: down_policy_count
        
        	Total number of policies that are operationally down
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: total_candidate_path_count
        
        	Total number of candidate paths
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: active_candidate_path_count
        
        	Total number of candidate paths that are active
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: inactive_candidate_path_count
        
        	Total number of candidate paths that are inactive
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: total_lsp_count
        
        	Total number of LSPs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: active_lsp_count
        
        	Total number of active LSPs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: reoptimized_lsp_count
        
        	Total number of reoptimized LSPs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cleanup_lsp_count
        
        	Total number of cleanup LSPs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: oor_lsp_count
        
        	Total number of LSPs in OOR state
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Xtc.PolicySummary, self).__init__()

            self.yang_name = "policy-summary"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('total_policy_count', (YLeaf(YType.uint32, 'total-policy-count'), ['int'])),
                ('up_policy_count', (YLeaf(YType.uint32, 'up-policy-count'), ['int'])),
                ('down_policy_count', (YLeaf(YType.uint32, 'down-policy-count'), ['int'])),
                ('total_candidate_path_count', (YLeaf(YType.uint32, 'total-candidate-path-count'), ['int'])),
                ('active_candidate_path_count', (YLeaf(YType.uint32, 'active-candidate-path-count'), ['int'])),
                ('inactive_candidate_path_count', (YLeaf(YType.uint32, 'inactive-candidate-path-count'), ['int'])),
                ('total_lsp_count', (YLeaf(YType.uint32, 'total-lsp-count'), ['int'])),
                ('active_lsp_count', (YLeaf(YType.uint32, 'active-lsp-count'), ['int'])),
                ('reoptimized_lsp_count', (YLeaf(YType.uint32, 'reoptimized-lsp-count'), ['int'])),
                ('cleanup_lsp_count', (YLeaf(YType.uint32, 'cleanup-lsp-count'), ['int'])),
                ('oor_lsp_count', (YLeaf(YType.uint32, 'oor-lsp-count'), ['int'])),
            ])
            self.total_policy_count = None
            self.up_policy_count = None
            self.down_policy_count = None
            self.total_candidate_path_count = None
            self.active_candidate_path_count = None
            self.inactive_candidate_path_count = None
            self.total_lsp_count = None
            self.active_lsp_count = None
            self.reoptimized_lsp_count = None
            self.cleanup_lsp_count = None
            self.oor_lsp_count = None
            self._segment_path = lambda: "policy-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.PolicySummary, ['total_policy_count', 'up_policy_count', 'down_policy_count', 'total_candidate_path_count', 'active_candidate_path_count', 'inactive_candidate_path_count', 'total_lsp_count', 'active_lsp_count', 'reoptimized_lsp_count', 'cleanup_lsp_count', 'oor_lsp_count'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.PolicySummary']['meta_info']


    class OnDemandColors(_Entity_):
        """
        On\-Demand Color database in XTC Agent
        
        .. attribute:: on_demand_color
        
        	On Demand Color information
        	**type**\: list of  		 :py:class:`OnDemandColor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.OnDemandColors.OnDemandColor>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class OnDemandColor(_Entity_):
            """
            On Demand Color information
            
            .. attribute:: color  (key)
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: disjoint_path_info
            
            	Disjoint path information
            	**type**\:  :py:class:`DisjointPathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.OnDemandColors.OnDemandColor.DisjointPathInfo>`
            
            	**config**\: False
            
            .. attribute:: color_xr
            
            	Color
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: absolute_margin
            
            	Absolute Metric Margin
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: relative_margin
            
            	 Relative Metric Margin
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: maximum_sid_depth
            
            	Maximum SID Depth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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
                    ('absolute_margin', (YLeaf(YType.uint32, 'absolute-margin'), ['int'])),
                    ('relative_margin', (YLeaf(YType.uint32, 'relative-margin'), ['int'])),
                    ('maximum_sid_depth', (YLeaf(YType.uint32, 'maximum-sid-depth'), ['int'])),
                ])
                self.color = None
                self.color_xr = None
                self.absolute_margin = None
                self.relative_margin = None
                self.maximum_sid_depth = None

                self.disjoint_path_info = Xtc.OnDemandColors.OnDemandColor.DisjointPathInfo()
                self.disjoint_path_info.parent = self
                self._children_name_map["disjoint_path_info"] = "disjoint-path-info"
                self._segment_path = lambda: "on-demand-color" + "[color='" + str(self.color) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/on-demand-colors/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.OnDemandColors.OnDemandColor, ['color', 'color_xr', 'absolute_margin', 'relative_margin', 'maximum_sid_depth'], name, value)


            class DisjointPathInfo(_Entity_):
                """
                Disjoint path information
                
                .. attribute:: disjointness_type
                
                	Disjointness type
                	**type**\:  :py:class:`XtcDisjointness <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcDisjointness>`
                
                	**config**\: False
                
                .. attribute:: group_id
                
                	Group ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sub_id
                
                	Sub ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.OnDemandColors.OnDemandColor.DisjointPathInfo']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Xtc.OnDemandColors.OnDemandColor']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.OnDemandColors']['meta_info']


    class Controller(_Entity_):
        """
        Controller information
        
        .. attribute:: policy_requests
        
        	Table containing policy requests
        	**type**\:  :py:class:`PolicyRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class PolicyRequests(_Entity_):
            """
            Table containing policy requests
            
            .. attribute:: policy_request
            
            	Policy request information
            	**type**\: list of  		 :py:class:`PolicyRequest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class PolicyRequest(_Entity_):
                """
                Policy request information
                
                .. attribute:: source_address  (key)
                
                	Source Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: end_point_type  (key)
                
                	Endpoint Address Type
                	**type**\:  :py:class:`XtcAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAddressFamily>`
                
                	**config**\: False
                
                .. attribute:: end_point_address  (key)
                
                	Endpoint Address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: color  (key)
                
                	Color
                	**type**\: int
                
                	**range:** 1..4294967295
                
                	**config**\: False
                
                .. attribute:: route_distinguisher  (key)
                
                	Route Distinguisher
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: end_point
                
                	End point
                	**type**\:  :py:class:`EndPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.EndPoint>`
                
                	**config**\: False
                
                .. attribute:: source_address_xr
                
                	Source address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: binding_sid
                
                	Binding SID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: preference
                
                	Preference
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: color_xr
                
                	Color
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: route_distinguisher_xr
                
                	Route distinguisher
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: creation_time
                
                	Creation time of the request in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: second
                
                .. attribute:: last_updated_time
                
                	Last updated time of the request in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: second
                
                .. attribute:: segment_list
                
                	Segment lists
                	**type**\: list of  		 :py:class:`SegmentList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.Controller.PolicyRequests.PolicyRequest, self).__init__()

                    self.yang_name = "policy-request"
                    self.yang_parent_name = "policy-requests"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['source_address','end_point_type','end_point_address','color','route_distinguisher']
                    self._child_classes = OrderedDict([("end-point", ("end_point", Xtc.Controller.PolicyRequests.PolicyRequest.EndPoint)), ("segment-list", ("segment_list", Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList))])
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

                    self.segment_list = YList(self)
                    self._segment_path = lambda: "policy-request" + "[source-address='" + str(self.source_address) + "']" + "[end-point-type='" + str(self.end_point_type) + "']" + "[end-point-address='" + str(self.end_point_address) + "']" + "[color='" + str(self.color) + "']" + "[route-distinguisher='" + str(self.route_distinguisher) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/controller/policy-requests/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest, ['source_address', 'end_point_type', 'end_point_address', 'color', 'route_distinguisher', 'source_address_xr', 'binding_sid', 'preference', 'color_xr', 'route_distinguisher_xr', 'creation_time', 'last_updated_time'], name, value)


                class EndPoint(_Entity_):
                    """
                    End point
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Controller.PolicyRequests.PolicyRequest.EndPoint']['meta_info']


                class SegmentList(_Entity_):
                    """
                    Segment lists
                    
                    .. attribute:: name
                    
                    	Explicit segment list name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: type
                    
                    	Segment list type
                    	**type**\:  :py:class:`XtcPolicyPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcPolicyPath>`
                    
                    	**config**\: False
                    
                    .. attribute:: active
                    
                    	Whether the segment list is active (used)
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: weight
                    
                    	Weight of the segment list
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: metric_type
                    
                    	Metric type of the segment list
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: metric_value
                    
                    	Accumulated metric of the segment list
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: is_valid
                    
                    	True if path is valid
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: pce_based_path
                    
                    	True if the path is to be computed by PCE
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: pce_address
                    
                    	Address of the PCE computed the path
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: error
                    
                    	Error (for display only)
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: hops
                    
                    	SR hop list
                    	**type**\: list of  		 :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList, self).__init__()

                        self.yang_name = "segment-list"
                        self.yang_parent_name = "policy-request"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hops", ("hops", Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcPolicyPath', '')])),
                            ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
                            ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                            ('metric_type', (YLeaf(YType.uint8, 'metric-type'), ['int'])),
                            ('metric_value', (YLeaf(YType.uint64, 'metric-value'), ['int'])),
                            ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                            ('pce_based_path', (YLeaf(YType.boolean, 'pce-based-path'), ['bool'])),
                            ('pce_address', (YLeaf(YType.str, 'pce-address'), ['str'])),
                            ('error', (YLeaf(YType.str, 'error'), ['str'])),
                        ])
                        self.name = None
                        self.type = None
                        self.active = None
                        self.weight = None
                        self.metric_type = None
                        self.metric_value = None
                        self.is_valid = None
                        self.pce_based_path = None
                        self.pce_address = None
                        self.error = None

                        self.hops = YList(self)
                        self._segment_path = lambda: "segment-list"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList, ['name', 'type', 'active', 'weight', 'metric_type', 'metric_value', 'is_valid', 'pce_based_path', 'pce_address', 'error'], name, value)


                    class Hops(_Entity_):
                        """
                        SR hop list
                        
                        .. attribute:: sid
                        
                        	SID value
                        	**type**\:  :py:class:`Sid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.Sid>`
                        
                        	**config**\: False
                        
                        .. attribute:: local_address
                        
                        	Local address
                        	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.LocalAddress>`
                        
                        	**config**\: False
                        
                        .. attribute:: remote_address
                        
                        	Remote address
                        	**type**\:  :py:class:`RemoteAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.RemoteAddress>`
                        
                        	**config**\: False
                        
                        .. attribute:: sid_type
                        
                        	SID type
                        	**type**\:  :py:class:`XtcSrSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSrSid>`
                        
                        	**config**\: False
                        
                        .. attribute:: algorithm
                        
                        	Algorithim
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops, self).__init__()

                            self.yang_name = "hops"
                            self.yang_parent_name = "segment-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sid", ("sid", Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.Sid)), ("local-address", ("local_address", Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.LocalAddress)), ("remote-address", ("remote_address", Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.RemoteAddress))])
                            self._leafs = OrderedDict([
                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcSrSid', '')])),
                                ('algorithm', (YLeaf(YType.uint8, 'algorithm'), ['int'])),
                            ])
                            self.sid_type = None
                            self.algorithm = None

                            self.sid = Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.Sid()
                            self.sid.parent = self
                            self._children_name_map["sid"] = "sid"

                            self.local_address = Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.LocalAddress()
                            self.local_address.parent = self
                            self._children_name_map["local_address"] = "local-address"

                            self.remote_address = Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.RemoteAddress()
                            self.remote_address.parent = self
                            self._children_name_map["remote_address"] = "remote-address"
                            self._segment_path = lambda: "hops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops, ['sid_type', 'algorithm'], name, value)


                        class Sid(_Entity_):
                            """
                            SID value
                            
                            .. attribute:: sid_type
                            
                            	SIDType
                            	**type**\:  :py:class:`XtcSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid>`
                            
                            	**config**\: False
                            
                            .. attribute:: label
                            
                            	MPLS label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.Sid, self).__init__()

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
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.Sid, ['sid_type', 'label', 'ipv6'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.Sid']['meta_info']


                        class LocalAddress(_Entity_):
                            """
                            Local address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.LocalAddress, self).__init__()

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
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.LocalAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.LocalAddress']['meta_info']


                        class RemoteAddress(_Entity_):
                            """
                            Remote address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                            
                            	**config**\: False
                            
                            .. attribute:: ipv4
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: ipv6
                            
                            	IPv6 address type
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.RemoteAddress, self).__init__()

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
                                self._perform_setattr(Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.RemoteAddress, ['af_name', 'ipv4', 'ipv6'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops.RemoteAddress']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList.Hops']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.Controller.PolicyRequests.PolicyRequest.SegmentList']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.Controller.PolicyRequests.PolicyRequest']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Xtc.Controller.PolicyRequests']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.Controller']['meta_info']


    class TopologyNodes(_Entity_):
        """
        Node database in XTC Agent
        
        .. attribute:: topology_node
        
        	Node information
        	**type**\: list of  		 :py:class:`TopologyNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class TopologyNode(_Entity_):
            """
            Node information
            
            .. attribute:: node_identifier  (key)
            
            	Node Identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:  :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier>`
            
            	**config**\: False
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: overload
            
            	Node Overload Bit
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: prefix_sid
            
            	Prefix SIDs
            	**type**\: list of  		 :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.PrefixSid>`
            
            	**config**\: False
            
            .. attribute:: ipv4_link
            
            	IPv4 Link information
            	**type**\: list of  		 :py:class:`Ipv4Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link>`
            
            	**config**\: False
            
            .. attribute:: ipv6_link
            
            	IPv6 Link information
            	**type**\: list of  		 :py:class:`Ipv6Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class NodeProtocolIdentifier(_Entity_):
                """
                Node protocol identifier
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class IgpInformation(_Entity_):
                    """
                    IGP information
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    	**config**\: False
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Igp(_Entity_):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        	**config**\: False
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        	**config**\: False
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        	**config**\: False
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Isis(_Entity_):
                            """
                            ISIS information
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                        class Ospf(_Entity_):
                            """
                            OSPF information
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(_Entity_):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier.IgpInformation']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.NodeProtocolIdentifier']['meta_info']


            class PrefixSid(_Entity_):
                """
                Prefix SIDs
                
                .. attribute:: sid_prefix
                
                	Prefix
                	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.PrefixSid.SidPrefix>`
                
                	**config**\: False
                
                .. attribute:: sid_type
                
                	SID Type
                	**type**\:  :py:class:`XtcSid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid1>`
                
                	**config**\: False
                
                .. attribute:: algorithm
                
                	Prefix\-SID algorithm number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: mpls_label
                
                	MPLS Label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class SidPrefix(_Entity_):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.PrefixSid.SidPrefix']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.PrefixSid']['meta_info']


            class Ipv4Link(_Entity_):
                """
                IPv4 Link information
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:  :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation>`
                
                	**config**\: False
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:  :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier>`
                
                	**config**\: False
                
                .. attribute:: performance_metrics
                
                	Performance metrics
                	**type**\:  :py:class:`PerformanceMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics>`
                
                	**config**\: False
                
                .. attribute:: local_ipv4_address
                
                	Local IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: remote_ipv4_address
                
                	Remote IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: administrative_groups
                
                	Link admin\-groups
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: extended_administrative_group
                
                	Link Extended admin\-groups
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: srlgs
                
                	SRLG Values
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of  		 :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.TopologyNodes.TopologyNode.Ipv4Link, self).__init__()

                    self.yang_name = "ipv4-link"
                    self.yang_parent_name = "topology-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-igp-information", ("local_igp_information", Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation)), ("remote-node-protocol-identifier", ("remote_node_protocol_identifier", Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier)), ("performance-metrics", ("performance_metrics", Xtc.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics)), ("adjacency-sid", ("adjacency_sid", Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid))])
                    self._leafs = OrderedDict([
                        ('local_ipv4_address', (YLeaf(YType.str, 'local-ipv4-address'), ['str'])),
                        ('remote_ipv4_address', (YLeaf(YType.str, 'remote-ipv4-address'), ['str'])),
                        ('igp_metric', (YLeaf(YType.uint32, 'igp-metric'), ['int'])),
                        ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                        ('maximum_link_bandwidth', (YLeaf(YType.uint64, 'maximum-link-bandwidth'), ['int'])),
                        ('max_reservable_bandwidth', (YLeaf(YType.uint64, 'max-reservable-bandwidth'), ['int'])),
                        ('administrative_groups', (YLeaf(YType.uint32, 'administrative-groups'), ['int'])),
                        ('extended_administrative_group', (YLeafList(YType.uint32, 'extended-administrative-group'), ['int'])),
                        ('srlgs', (YLeafList(YType.uint32, 'srlgs'), ['int'])),
                    ])
                    self.local_ipv4_address = None
                    self.remote_ipv4_address = None
                    self.igp_metric = None
                    self.te_metric = None
                    self.maximum_link_bandwidth = None
                    self.max_reservable_bandwidth = None
                    self.administrative_groups = None
                    self.extended_administrative_group = []
                    self.srlgs = []

                    self.local_igp_information = Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation()
                    self.local_igp_information.parent = self
                    self._children_name_map["local_igp_information"] = "local-igp-information"

                    self.remote_node_protocol_identifier = Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier()
                    self.remote_node_protocol_identifier.parent = self
                    self._children_name_map["remote_node_protocol_identifier"] = "remote-node-protocol-identifier"

                    self.performance_metrics = Xtc.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics()
                    self.performance_metrics.parent = self
                    self._children_name_map["performance_metrics"] = "performance-metrics"

                    self.adjacency_sid = YList(self)
                    self._segment_path = lambda: "ipv4-link"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link, ['local_ipv4_address', 'remote_ipv4_address', 'igp_metric', 'te_metric', 'maximum_link_bandwidth', 'max_reservable_bandwidth', 'administrative_groups', 'extended_administrative_group', 'srlgs'], name, value)


                class LocalIgpInformation(_Entity_):
                    """
                    Local node IGP information
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp>`
                    
                    	**config**\: False
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Igp(_Entity_):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis>`
                        
                        	**config**\: False
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf>`
                        
                        	**config**\: False
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp>`
                        
                        	**config**\: False
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Isis(_Entity_):
                            """
                            ISIS information
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Isis']['meta_info']


                        class Ospf(_Entity_):
                            """
                            OSPF information
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(_Entity_):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp.Bgp']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation.Igp']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.LocalIgpInformation']['meta_info']


                class RemoteNodeProtocolIdentifier(_Entity_):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class IgpInformation(_Entity_):
                        """
                        IGP information
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        	**config**\: False
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Igp(_Entity_):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            	**config**\: False
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            	**config**\: False
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            	**config**\: False
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class Isis(_Entity_):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2019-09-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                            class Ospf(_Entity_):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2019-09-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                            class Bgp(_Entity_):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2019-09-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.RemoteNodeProtocolIdentifier']['meta_info']


                class PerformanceMetrics(_Entity_):
                    """
                    Performance metrics
                    
                    .. attribute:: unidirectional_minimum_delay_microseconds
                    
                    	Min delay in microseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: microsecond
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics, self).__init__()

                        self.yang_name = "performance-metrics"
                        self.yang_parent_name = "ipv4-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('unidirectional_minimum_delay_microseconds', (YLeaf(YType.uint32, 'unidirectional-minimum-delay-microseconds'), ['int'])),
                        ])
                        self.unidirectional_minimum_delay_microseconds = None
                        self._segment_path = lambda: "performance-metrics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics, ['unidirectional_minimum_delay_microseconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.PerformanceMetrics']['meta_info']


                class AdjacencySid(_Entity_):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix>`
                    
                    	**config**\: False
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`XtcSid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid1>`
                    
                    	**config**\: False
                    
                    .. attribute:: algorithm
                    
                    	Prefix\-SID algorithm number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class SidPrefix(_Entity_):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid.SidPrefix']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link.AdjacencySid']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv4Link']['meta_info']


            class Ipv6Link(_Entity_):
                """
                IPv6 Link information
                
                .. attribute:: local_igp_information
                
                	Local node IGP information
                	**type**\:  :py:class:`LocalIgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation>`
                
                	**config**\: False
                
                .. attribute:: remote_node_protocol_identifier
                
                	Remote node protocol identifier
                	**type**\:  :py:class:`RemoteNodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier>`
                
                	**config**\: False
                
                .. attribute:: local_ipv6_address
                
                	Local IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: remote_ipv6_address
                
                	Remote IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: igp_metric
                
                	IGP Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: te_metric
                
                	TE Metric
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: maximum_link_bandwidth
                
                	Max link bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: max_reservable_bandwidth
                
                	Max Reservable bandwidth
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: adjacency_sid
                
                	Adjacency SIDs
                	**type**\: list of  		 :py:class:`AdjacencySid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class LocalIgpInformation(_Entity_):
                    """
                    Local node IGP information
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp>`
                    
                    	**config**\: False
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Igp(_Entity_):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis>`
                        
                        	**config**\: False
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf>`
                        
                        	**config**\: False
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp>`
                        
                        	**config**\: False
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Isis(_Entity_):
                            """
                            ISIS information
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Isis']['meta_info']


                        class Ospf(_Entity_):
                            """
                            OSPF information
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(_Entity_):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp.Bgp']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation.Igp']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.LocalIgpInformation']['meta_info']


                class RemoteNodeProtocolIdentifier(_Entity_):
                    """
                    Remote node protocol identifier
                    
                    .. attribute:: node_name
                    
                    	Node Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_bgp_router_id_set
                    
                    	True if IPv4 BGP router ID is set
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4_bgp_router_id
                    
                    	IPv4 TE router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4te_router_id_set
                    
                    	True if IPv4 TE router ID is set
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4te_router_id
                    
                    	IPv4 BGP router ID
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: igp_information
                    
                    	IGP information
                    	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class IgpInformation(_Entity_):
                        """
                        IGP information
                        
                        .. attribute:: igp
                        
                        	IGP\-specific information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp>`
                        
                        	**config**\: False
                        
                        .. attribute:: domain_identifier
                        
                        	Domain identifier
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Igp(_Entity_):
                            """
                            IGP\-specific information
                            
                            .. attribute:: isis
                            
                            	ISIS information
                            	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                            
                            	**config**\: False
                            
                            .. attribute:: ospf
                            
                            	OSPF information
                            	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                            
                            	**config**\: False
                            
                            .. attribute:: bgp
                            
                            	BGP information
                            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                            
                            	**config**\: False
                            
                            .. attribute:: igp_id
                            
                            	IGP ID
                            	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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


                            class Isis(_Entity_):
                                """
                                ISIS information
                                
                                .. attribute:: system_id
                                
                                	ISIS system ID
                                	**type**\: str
                                
                                	**config**\: False
                                
                                .. attribute:: level
                                
                                	ISIS level
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2019-09-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                            class Ospf(_Entity_):
                                """
                                OSPF information
                                
                                .. attribute:: router_id
                                
                                	OSPF router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                .. attribute:: area
                                
                                	OSPF area
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2019-09-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                            class Bgp(_Entity_):
                                """
                                BGP information
                                
                                .. attribute:: router_id
                                
                                	BGP router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'infra-xtc-agent-oper'
                                _revision = '2019-09-09'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
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

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier.IgpInformation']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.RemoteNodeProtocolIdentifier']['meta_info']


                class AdjacencySid(_Entity_):
                    """
                    Adjacency SIDs
                    
                    .. attribute:: sid_prefix
                    
                    	Prefix
                    	**type**\:  :py:class:`SidPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix>`
                    
                    	**config**\: False
                    
                    .. attribute:: sid_type
                    
                    	SID Type
                    	**type**\:  :py:class:`XtcSid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcSid1>`
                    
                    	**config**\: False
                    
                    .. attribute:: algorithm
                    
                    	Prefix\-SID algorithm number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: mpls_label
                    
                    	MPLS Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class SidPrefix(_Entity_):
                        """
                        Prefix
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                        
                        	**config**\: False
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid.SidPrefix']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link.AdjacencySid']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.TopologyNodes.TopologyNode.Ipv6Link']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Xtc.TopologyNodes.TopologyNode']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.TopologyNodes']['meta_info']


    class TopologySummaries(_Entity_):
        """
        Node summary table
        
        .. attribute:: topology_summary
        
        	Node summary database
        	**type**\: list of  		 :py:class:`TopologySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologySummaries.TopologySummary>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Xtc.TopologySummaries, self).__init__()

            self.yang_name = "topology-summaries"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("topology-summary", ("topology_summary", Xtc.TopologySummaries.TopologySummary))])
            self._leafs = OrderedDict()

            self.topology_summary = YList(self)
            self._segment_path = lambda: "topology-summaries"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.TopologySummaries, [], name, value)


        class TopologySummary(_Entity_):
            """
            Node summary database
            
            .. attribute:: af
            
            	Only show data related to the specified address family
            	**type**\:  :py:class:`XtcAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAddressFamily>`
            
            	**config**\: False
            
            .. attribute:: protocol
            
            	Match nodes from the specified IGP protocol
            	**type**\:  :py:class:`XtcigpProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcigpProtocol>`
            
            	**config**\: False
            
            .. attribute:: topology_ready_summary
            
            	Topology ready summary
            	**type**\:  :py:class:`TopologyReadySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologySummaries.TopologySummary.TopologyReadySummary>`
            
            	**config**\: False
            
            .. attribute:: nodes
            
            	Number of nodes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: prefixes
            
            	Number of prefixes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: prefix_sids
            
            	Number of prefix SIDs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: links
            
            	Number of links
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: adjacency_sids
            
            	Number of adjacency SIDs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Xtc.TopologySummaries.TopologySummary, self).__init__()

                self.yang_name = "topology-summary"
                self.yang_parent_name = "topology-summaries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("topology-ready-summary", ("topology_ready_summary", Xtc.TopologySummaries.TopologySummary.TopologyReadySummary))])
                self._leafs = OrderedDict([
                    ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcAddressFamily', '')])),
                    ('protocol', (YLeaf(YType.enumeration, 'protocol'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'XtcigpProtocol', '')])),
                    ('nodes', (YLeaf(YType.uint32, 'nodes'), ['int'])),
                    ('prefixes', (YLeaf(YType.uint32, 'prefixes'), ['int'])),
                    ('prefix_sids', (YLeaf(YType.uint32, 'prefix-sids'), ['int'])),
                    ('links', (YLeaf(YType.uint32, 'links'), ['int'])),
                    ('adjacency_sids', (YLeaf(YType.uint32, 'adjacency-sids'), ['int'])),
                ])
                self.af = None
                self.protocol = None
                self.nodes = None
                self.prefixes = None
                self.prefix_sids = None
                self.links = None
                self.adjacency_sids = None

                self.topology_ready_summary = Xtc.TopologySummaries.TopologySummary.TopologyReadySummary()
                self.topology_ready_summary.parent = self
                self._children_name_map["topology_ready_summary"] = "topology-ready-summary"
                self._segment_path = lambda: "topology-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/topology-summaries/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Xtc.TopologySummaries.TopologySummary, ['af', 'protocol', 'nodes', 'prefixes', 'prefix_sids', 'links', 'adjacency_sids'], name, value)


            class TopologyReadySummary(_Entity_):
                """
                Topology ready summary
                
                .. attribute:: timer
                
                	Topology readiness timer
                	**type**\:  :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.TopologySummaries.TopologySummary.TopologyReadySummary.Timer>`
                
                	**config**\: False
                
                .. attribute:: ready
                
                	Topology readiness
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ha_case
                
                	Last HA case
                	**type**\:  :py:class:`CmnHaCase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.CmnHaCase>`
                
                	**config**\: False
                
                .. attribute:: timer_value
                
                	Topology ready timer value selected at start
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: pcep_allowed
                
                	Whether PCEP is allowed
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Xtc.TopologySummaries.TopologySummary.TopologyReadySummary, self).__init__()

                    self.yang_name = "topology-ready-summary"
                    self.yang_parent_name = "topology-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("timer", ("timer", Xtc.TopologySummaries.TopologySummary.TopologyReadySummary.Timer))])
                    self._leafs = OrderedDict([
                        ('ready', (YLeaf(YType.boolean, 'ready'), ['bool'])),
                        ('ha_case', (YLeaf(YType.enumeration, 'ha-case'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper', 'CmnHaCase', '')])),
                        ('timer_value', (YLeaf(YType.uint32, 'timer-value'), ['int'])),
                        ('pcep_allowed', (YLeaf(YType.boolean, 'pcep-allowed'), ['bool'])),
                    ])
                    self.ready = None
                    self.ha_case = None
                    self.timer_value = None
                    self.pcep_allowed = None

                    self.timer = Xtc.TopologySummaries.TopologySummary.TopologyReadySummary.Timer()
                    self.timer.parent = self
                    self._children_name_map["timer"] = "timer"
                    self._segment_path = lambda: "topology-ready-summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/topology-summaries/topology-summary/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Xtc.TopologySummaries.TopologySummary.TopologyReadySummary, ['ready', 'ha_case', 'timer_value', 'pcep_allowed'], name, value)


                class Timer(_Entity_):
                    """
                    Topology readiness timer
                    
                    .. attribute:: running
                    
                    	Whether the timer is running
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: remaining_seconds
                    
                    	Number of remaining seconds
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: remaining_nano_seconds
                    
                    	Number of remaining nanoseconds
                    	**type**\: int
                    
                    	**range:** \-9223372036854775808..9223372036854775807
                    
                    	**config**\: False
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Xtc.TopologySummaries.TopologySummary.TopologyReadySummary.Timer, self).__init__()

                        self.yang_name = "timer"
                        self.yang_parent_name = "topology-ready-summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('running', (YLeaf(YType.boolean, 'running'), ['bool'])),
                            ('remaining_seconds', (YLeaf(YType.int64, 'remaining-seconds'), ['int'])),
                            ('remaining_nano_seconds', (YLeaf(YType.int64, 'remaining-nano-seconds'), ['int'])),
                        ])
                        self.running = None
                        self.remaining_seconds = None
                        self.remaining_nano_seconds = None
                        self._segment_path = lambda: "timer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/topology-summaries/topology-summary/topology-ready-summary/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Xtc.TopologySummaries.TopologySummary.TopologyReadySummary.Timer, ['running', 'remaining_seconds', 'remaining_nano_seconds'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.TopologySummaries.TopologySummary.TopologyReadySummary.Timer']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.TopologySummaries.TopologySummary.TopologyReadySummary']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Xtc.TopologySummaries.TopologySummary']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.TopologySummaries']['meta_info']


    class PrefixInfos(_Entity_):
        """
        Prefixes database in XTC Agent
        
        .. attribute:: prefix_info
        
        	Prefix information
        	**type**\: list of  		 :py:class:`PrefixInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class PrefixInfo(_Entity_):
            """
            Prefix information
            
            .. attribute:: node_identifier  (key)
            
            	Node ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: node_protocol_identifier
            
            	Node protocol identifier
            	**type**\:  :py:class:`NodeProtocolIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier>`
            
            	**config**\: False
            
            .. attribute:: node_identifier_xr
            
            	Node identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: address
            
            	Prefix address
            	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.Address>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-xtc-agent-oper'
            _revision = '2019-09-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
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


            class NodeProtocolIdentifier(_Entity_):
                """
                Node protocol identifier
                
                .. attribute:: node_name
                
                	Node Name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: ipv4_bgp_router_id_set
                
                	True if IPv4 BGP router ID is set
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ipv4_bgp_router_id
                
                	IPv4 TE router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: ipv4te_router_id_set
                
                	True if IPv4 TE router ID is set
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ipv4te_router_id
                
                	IPv4 BGP router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: igp_information
                
                	IGP information
                	**type**\: list of  		 :py:class:`IgpInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class IgpInformation(_Entity_):
                    """
                    IGP information
                    
                    .. attribute:: igp
                    
                    	IGP\-specific information
                    	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp>`
                    
                    	**config**\: False
                    
                    .. attribute:: domain_identifier
                    
                    	Domain identifier
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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


                    class Igp(_Entity_):
                        """
                        IGP\-specific information
                        
                        .. attribute:: isis
                        
                        	ISIS information
                        	**type**\:  :py:class:`Isis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis>`
                        
                        	**config**\: False
                        
                        .. attribute:: ospf
                        
                        	OSPF information
                        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf>`
                        
                        	**config**\: False
                        
                        .. attribute:: bgp
                        
                        	BGP information
                        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp>`
                        
                        	**config**\: False
                        
                        .. attribute:: igp_id
                        
                        	IGP ID
                        	**type**\:  :py:class:`XtcIgpInfoId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcIgpInfoId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-xtc-agent-oper'
                        _revision = '2019-09-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
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


                        class Isis(_Entity_):
                            """
                            ISIS information
                            
                            .. attribute:: system_id
                            
                            	ISIS system ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: level
                            
                            	ISIS level
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Isis']['meta_info']


                        class Ospf(_Entity_):
                            """
                            OSPF information
                            
                            .. attribute:: router_id
                            
                            	OSPF router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            .. attribute:: area
                            
                            	OSPF area
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Ospf']['meta_info']


                        class Bgp(_Entity_):
                            """
                            BGP information
                            
                            .. attribute:: router_id
                            
                            	BGP router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'infra-xtc-agent-oper'
                            _revision = '2019-09-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
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

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                                return meta._meta_table['Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp.Bgp']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                            return meta._meta_table['Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation.Igp']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier.IgpInformation']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.PrefixInfos.PrefixInfo.NodeProtocolIdentifier']['meta_info']


            class Address(_Entity_):
                """
                Prefix address
                
                .. attribute:: ip_address
                
                	Prefix IP address
                	**type**\:  :py:class:`IpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.Xtc.PrefixInfos.PrefixInfo.Address.IpAddress>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-xtc-agent-oper'
                _revision = '2019-09-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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


                class IpAddress(_Entity_):
                    """
                    Prefix IP address
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`XtcAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_agent_oper.XtcAfId>`
                    
                    	**config**\: False
                    
                    .. attribute:: ipv4
                    
                    	IPv4 address type
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ipv6
                    
                    	IPv6 address type
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-xtc-agent-oper'
                    _revision = '2019-09-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
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

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                        return meta._meta_table['Xtc.PrefixInfos.PrefixInfo.Address.IpAddress']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                    return meta._meta_table['Xtc.PrefixInfos.PrefixInfo.Address']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
                return meta._meta_table['Xtc.PrefixInfos.PrefixInfo']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.PrefixInfos']['meta_info']


    class InterfaceSummary(_Entity_):
        """
        Summary of all interfaces
        
        .. attribute:: interface_count
        
        	Number of interfaces
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: interface_operational_up_count
        
        	Number of interfaces that are operationally up
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: interface_operational_down_count
        
        	Number of interfaces that are operationally down
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-xtc-agent-oper'
        _revision = '2019-09-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Xtc.InterfaceSummary, self).__init__()

            self.yang_name = "interface-summary"
            self.yang_parent_name = "xtc"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                ('interface_operational_up_count', (YLeaf(YType.uint32, 'interface-operational-up-count'), ['int'])),
                ('interface_operational_down_count', (YLeaf(YType.uint32, 'interface-operational-down-count'), ['int'])),
            ])
            self.interface_count = None
            self.interface_operational_up_count = None
            self.interface_operational_down_count = None
            self._segment_path = lambda: "interface-summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-xtc-agent-oper:xtc/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Xtc.InterfaceSummary, ['interface_count', 'interface_operational_up_count', 'interface_operational_down_count'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
            return meta._meta_table['Xtc.InterfaceSummary']['meta_info']

    def clone_ptr(self):
        self._top_entity = Xtc()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_xtc_agent_oper as meta
        return meta._meta_table['Xtc']['meta_info']


